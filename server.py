import os
import base64
import json
import pandas as pd
from flask import Flask, request, jsonify
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from werkzeug.utils import secure_filename

app = Flask(__name__)

# --- 1. AI Data Structures (Schema) ---
class InvoiceItem(BaseModel):
    description: str = Field(description="Name of the product or service")
    quantity: int = Field(description="Quantity ordered")
    price: float = Field(description="Unit price")

class InvoiceSchema(BaseModel):
    invoice_number: str = Field(description="The invoice or receipt number")
    vendor_name: str = Field(description="Name of the vendor or company")
    date: str = Field(description="Invoice date")
    items: List[InvoiceItem] = Field(description="List of purchased items")
    total_amount: float = Field(description="The total final amount")

# --- 2. Helper Functions ---
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_to_excel(data_dict):
    excel_file = "invoices_vault.xlsx"
    
    # تجهيز السطور: لو الفاتورة فيها أكثر من منتج، سنكرر البيانات الأساسية لكل منتج ليصبح الجدول منسقاً
    rows = []
    invoice_num = data_dict.get("invoice_number")
    vendor = data_dict.get("vendor_name")
    date = data_dict.get("date")
    total = data_dict.get("total_amount")
    
    for item in data_dict.get("items", []):
        rows.append({
            "Invoice Number": invoice_num,
            "Vendor Name": vendor,
            "Date": date,
            "Item Description": item.get("description"),
            "Quantity": item.get("quantity"),
            "Unit Price": item.get("price"),
            "Total Invoice Amount": total
        })
        
    new_df = pd.DataFrame(rows)
    
    # إذا كان الملف موجوداً من قبل، أضيفي البيانات الجديدة له، وإلا أنشئي ملفاً جديداً
    if os.path.exists(excel_file):
        try:
            existing_df = pd.read_excel(excel_file)
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            combined_df.to_excel(excel_file, index=False)
        except Exception:
            new_df.to_excel(excel_file, index=False)
    else:
        new_df.to_excel(excel_file, index=False)

def extract_invoice_data(image_path):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY")
    )
    
    base64_image = encode_image(image_path)
    
    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": f"Extract all data from this invoice accurately. Convert it into a clean JSON object that strictly adheres to this schema: {json.dumps(InvoiceSchema.model_json_schema())}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

# --- 3. Flask API Routes ---
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "success", "message": "Welcome to your Invoice OCR API server!"})

@app.route('/process-invoice', methods=['POST'])
def process_invoice():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No image file provided"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(os.getcwd(), filename)
        file.save(temp_path)
        
        try:
            raw_json_result = extract_invoice_data(temp_path)
            
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
            structured_data = json.loads(raw_json_result)
            
            # 🔥 حفظ البيانات تلقائياً في ملف الـ Excel هنا
            save_to_excel(structured_data)
            
            return jsonify({
                "status": "success",
                "message": "Data extracted and saved to Excel successfully!",
                "data": structured_data
            }), 200
            
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)