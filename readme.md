# 🤖 AI-Powered Invoice OCR API
### نظام ذكي لاستخراج بيانات الفواتير وأتمتتها بالذكاء الاصطناعي

[English](#english-description) | [الوصف باللغة العربية](#الوصف-باللغة-العربية)

---

## الوصف باللغة العربية

هذا المشروع عبارة عن سيرفر (API) متكامل مبني باستخدام إطار العمل **Flask**، مصمم لاستقبال صور الفواتير واستخراج البيانات الحساسة منها ديناميكيًا بدقة عالية عبر تقنيات الذكاء الاصطناعي (Vision LLMs). يقوم النظام بتحويل النصوص غير المنظمة داخل الصور إلى بيانات مهيكلة (Structured JSON) ثم جدولتها وحفظها تلقائيًا داخل ملف Excel مركزي لتقليل الأخطاء البشرية وتوفير سياق محاسبي منظم.

### 🚀 المميزات الرئيسية:
- **المعالجة بالذكاء الاصطناعي (AI Vision):** الاعتماد على نماذج الرؤية المتقدمة عبر **OpenRouter (Llama 3.2 Vision)** لقراءة تفاصيل الفاتورة بدقة (الاسم، التاريخ، المجموع، المنتجات) مهما اختلف تصميم الفاتورة.
- **تأكيد هيكلة البيانات (Data Validation):** استخدام مكتبة **Pydantic** لفرض تصميم صارم (Schema) على مخرجات الذكاء الاصطناعي لضمان عدم وجود بيانات ناقصة أو عشوائية.
- **التنظيم والجدولة التلقائية:** معالجة البيانات المستخرجة وتسطيحها (Flattening) عبر مكتبة **Pandas** لحفظ المنتجات المتعددة داخل نفس الفاتورة بشكل منسق تلقائيًا في ملف Excel مخصص (`invoices_vault.xlsx`).
- **إدارة الملفات المؤقتة:** نظام حماية يقوم بحفظ الصور مؤقتًا لمعالجتها ثم حذفها فورًا من السيرفر لضمان الأمان وعدم استهلاك المساحة.

### 🛠️ التقنيات المستخدمة (Tech Stack):
- **Python / Flask** (لبناء السيرفر والتحكم المنطقي بالخلفية).
- **OpenRouter API / OpenAI SDK** (للاستخراج الذكي والمعالجة السياقية للفواتير).
- **Pydantic** (لبناء الـ Schema وتأكيد صحة هيكل البيانات المستخرجة).
- **Pandas & OpenPyXL** (لمعالجة البيانات وتصديرها وجدولتها في ملفات Excel).

---

## English Description

This project is a production-ready, production-grade **AI-Powered Invoice OCR API** built with **Flask**. It allows users to upload invoice or receipt images, leverages advanced Vision Large Language Models (LLMs) to accurately extract key financial data point-by-point, and automatically structures and appends them into a centralized Excel spreadsheet—eliminating manual data entry and human error.

### 🚀 Key Features:
- **AI-Driven Vision Extraction:** Utilizes advanced vision models via **OpenRouter (Llama 3.2 Vision)** to dynamically parse and interpret complex text layouts from invoice images.
- **Strict Schema Enforcement:** Employs **Pydantic** structures to guarantee that the AI output strictly adheres to a predefined contract (Invoice Number, Vendor, Date, Line Items, and Total).
- **Automated Excel Flattening:** Uses **Pandas** to break down multi-item invoices into clean, linear rows, appending them seamlessly into an active Excel sheet (`invoices_vault.xlsx`).
- **Secure File Lifecycle:** Automatically flushes temporary uploaded images immediately after AI completion to preserve server state and privacy.

### 🛠️ Tech Stack:
- **Python / Flask** (Core backend routing and microservice architecture).
- **OpenRouter API** (Vision AI Orchestration using OpenAI-compatible SDK).
- **Pydantic** (Data modeling and strict structural validation).
- **Pandas & OpenPyXL** (Data manipulation, dataframe structures, and Excel generation).

---

## 🔌 API Endpoints (توثيق الـ API)

### 1. Health Check
* **Endpoint:** `GET /`
* **Response:**
```json
{
  "status": "success",
  "message": "Welcome to your Invoice OCR API server!"
}

### 2. Process Invoice
* **Endpoint:** `POST /process-invoice`
* **Content-Type:** `multipart/form-data`
* **Payload:** `image` (The invoice image file: png, jpg, jpeg)
* **Response Example:**
```json
{
  "status": "success",
  "message": "Data extracted and saved to Excel successfully!",
  "data": {
    "invoice_number": "INV-2026-089",
    "vendor_name": "Tech Solutions Ltd",
    "date": "2026-05-22",
    "items": [
      {
        "description": "Cloud Hosting Service",
        "quantity": 1,
        "price": 75.50
      },
      {
        "description": "SSL Certificate",
        "quantity": 2,
        "price": 15.00
      }
    ],
    "total_amount": 105.50
  }
}

💻 Getting Started (طريقة التشغيل المحلي)
1. Clone the repository / تحميل المشروع
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install dependencies / تثبيت المكتبات المطلوبة
Make sure you are in your virtual environment, then run:
pip install -r requirements.txt

3. Set up Environment Variables / إعداد المتغيرات السرية
Create a .env file in the root directory of the project and add your token:

Code snippet :
OPENROUTER_API_KEY=your_actual_openrouter_api_key_here

4. Run the Server / تشغيل السيرفر
python server.py

The application will start locally on http://localhost:5000. You can send a POST request to http://localhost:5000/process-invoice using Postman, Thunder Client, or cURL.
.
