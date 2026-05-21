import os
import base64
import json
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

# 1. Define the data structure for the invoice items (Schema)
class InvoiceItem(BaseModel):
    description: str = Field(description="Name of the product or service")
    quantity: int = Field(description="Quantity ordered")
    price: float = Field(description="Unit price")

# 2. Define the main structure for the invoice
class InvoiceSchema(BaseModel):
    invoice_number: str = Field(description="The invoice or receipt number")
    vendor_name: str = Field(description="Name of the vendor or company")
    date: str = Field(description="Invoice date")
    items: List[InvoiceItem] = Field(description="List of purchased items")
    total_amount: float = Field(description="The total final amount")

# Function to convert image to Base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_invoice_data(image_path):
    # 3. Connect to OpenRouter using the standard OpenAI client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY")
    )
    
    base64_image = encode_image(image_path)
    
    print("Processing invoice for free using Llama 3.2 Vision...")
    
    # 4. Send the request to the free vision model and enforce JSON output
    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": f"Extract all data from this invoice accurately. Convert it into a clean JSON object that strictly adheres to this schema, without any extra commentary: {json.dumps(InvoiceSchema.model_json_schema())}"
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
        response_format={"type": "json_object"} # Force the model to output JSON only
    )
    
    return response.choices[0].message.content

# --- Script Execution ---
if __name__ == "__main__":
    # Make sure this matches your image name in the directory
    image_path = "test_invoice.jpg" 
    
    try:
        raw_json = extract_invoice_data(image_path)
        
        print("\n=== Data Extracted Successfully! ===")
        print(raw_json)
        
        # Convert raw JSON string into a Python Dictionary for later use
        data_dict = json.loads(raw_json)
            
    except Exception as e:
        print(f"An error occurred: {e}")