# 🤖 Invoice Automation Bot (AI & OCR System)
### نظام أتمتة واستخراج بيانات الفواتير ذكي بالذكاء الاصطناعي

[English](#english-description) | [الوصف باللغة العربية](#الوصف-باللغة-العربية)

---

## الوصف باللغة العربية

هذا المشروع عبارة عن نظام أتمتة متكامل (Automation System) مصمم لقراءة الفواتير المستلمة عبر البريد الإلكتروني أو سحابة التخزين وتحديدها، ومن ثم استخراج البيانات الحساسة منها ديناميكيًا باستخدام تقنيات الذكاء الاصطناعي (AI OCR)، وحفظها وتنظيمها تلقائيًا داخل جداول بيانات رقمية لتقليل الأخطاء البشرية وتوفير ساعات العمل اليدوي.

### 🚀 المميزات الرئيسية:
- **المشغل التلقائي (Trigger):** مراقبة البريد الإلكتروني أو مجلد سحابي (Google Drive) فور وصول أي فاتورة جديدة.
- **المعالجة بالذكاء الاصطناعي:** الاعتماد على نماذج الرؤية (Vision Models) مثل Google Gemini AI / OpenAI Assistants لقراءة تفاصيل الفاتورة بدقة (الاسم، التاريخ، المجموع، الضرائب) حتى وإن اختلفت صيغتها الفنية.
- **التنظيم وحفظ البيانات:** تحويل وتحليل النص المستخرج وتصديره مباشرة إلى جداول بيانات منظمة (Google Sheets / Excel) جاهزة للمراجعة المحاسبية.
- **إدارة الأخطاء (Error Handling):** كود برمي محمي يضمن معالجة الأخطاء الشائعة (مثل مشاكل الـ Mime Type للملفات والمرفقات) بشكل تلقائي.

### 🛠️ التقنيات المستخدمة (Tech Stack):
- **Python** (للربط البرمجي السحابي وإعداد السيرفر).
- **Make.com / Integromat** (كمنظم ومنسق للعمليات السيرية - Orchestrator).
- **Google Gemini AI API / OpenAI API** (للاستخراج الذكي والمعالجة السياقية للمستندات).
- **Google Drive / Gmail** (كقنوات استقبال ومدخلات).

---

## English Description

This project is an advanced, production-ready **AI-Powered Invoice Automation & OCR System**. It automatically intercepts invoices sent via emails or uploaded to cloud storage, extracts key financial data point-by-point using Large Language Models (LLMs), and structure them neatly into spreadsheets—eliminating manual data entry and human error.

### 🚀 Key Features:
- **Automated Triggering:** Monitors active workflows (via Gmail or Google Drive Webhooks) for newly uploaded or received invoices.
- **AI-Driven Data Extraction:** Leverages vision capabilities of advanced LLMs (Google Gemini AI / OpenAI Assistants API) to accurately read and parse varying invoice structures (Total, Tax, Vendor, Line Items, Date).
- **Structured Data Export:** Converts unstructured file assets into instantly formatted rows within centralized databases (Google Sheets / Excel).
- **Robust Architecture:** Equipped with continuous error handling and input filtering (e.g., handling complex file MIME Types).

### 🛠️ Tech Stack:
- **Python** (Backend Logic & Cloud Server Orchestration).
- **Make.com** (Workflow Architecture & Webhook Event Management).
- **Google Gemini AI / OpenAI API** (Intelligent OCR & Contextual Parsing).
- **Render / Deployment Platforms** (Cloud Hosting Environment).

---

## 💻 How it Works / آلية العمل

1. **Input:** Invoice uploaded to Google Drive / Received via Email.
2. **Process:** Python Server / Make.com captures the file payload -> Passes it into the AI Module with dynamic prompt optimization.
3. **Output:** Structured calculations saved into Google Sheets instantly.
