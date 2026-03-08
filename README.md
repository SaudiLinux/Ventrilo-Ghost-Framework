# <div align="center"><font color="#007bff">Ventrilo-Ghost Framework 🛡️💀</font></div>

<div align="center">
  <h3><b>إطار عمل متكامل لاختبار الاختراق المتقدم (v1.0.0-Alpha)</b></h3>
  <p>
    <b>Developed by:</b> <font color="blue" size="5"><b>SayerLinux</b></font><br>
    <b>Email:</b> <a mailto:href="mailto:SaudiLinux1@gmail.com"><font color="blue">mailto:SaudiLinux1@gmail.com</font></a>
  </p>
  <img src="https://img.shields.io/badge/Developer-SayerLinux-blue?style=for-the-badge&logo=linux" alt="Developer Badge">
  <img src="https://img.shields.io/badge/Maintained-Yes-green?style=for-the-badge" alt="Maintained Badge">
  <img src="https://img.shields.io/badge/Version-1.0.0--Alpha-orange?style=for-the-badge" alt="Version Badge">
</div>

---

## 🚀 نظرة عامة (Overview)

**Ventrilo-Ghost** هو إطار عمل احترافي صممه المطور **SayerLinux** لعمليات Red Teaming والاستطلاع العميق. يتميز المحرك بقدرة فائقة على تجاوز أنظمة الحماية واستغلال الثغرات بشكل آلي وذكي باستخدام تقنيات برمجة غير متزامنة (Asynchronous).

---

## 💎 المميزات العبقرية (Key Features)

- **⚡ محرك Async فائق السرعة:** فحص آلاف الصفحات في وقت قياسي باستخدام `aiohttp`.
- **🕵️ تخفي كامل (Stealth Mode):** تجاوز جدران الحماية (WAF Bypass) عبر تغيير الـ `User-Agent` وتزوير الـ `IP`.
- **🕸️ العنكبوت الذكي (Spider Engine):** زحف تلقائي داخل الروابط الداخلية للموقع واستخراج البيانات الحساسة.
- **🧨 الاستغلال التلقائي (Auto-Exploit):** حقن تلقائي لثغرات SQLi وفتح Reverse Shell للتحكم الكامل.
- **🖥️ لوحة تحكم Ghost C2:** واجهة ويب مركزية (Dashboard) لإدارة السيرفرات والضحايا بضغطة زر.

---

## 🛠️ هيكل المشروع (Project Structure)

```text
Ventrilo-Ghost-Framework/
├── core/
│   ├── scanner.py        # محرك الفحص العميق والتخفي
│   └── exploiter.py      # وحدة الاستغلال التلقائي (SQLi, LFI, RCE)
├── c2_server/
│   ├── app.py            # خادم السيطرة والتحكم (Backend)
│   └── templates/        # واجهة الويب (Dashboard UI)
├── agent/
│   └── ghost_agent.py    # العميل "الشبح" للتحكم عن بعد
├── main.py               # المحرك الرئيسي وواجهة التحكم
└── requirements.txt      # المكتبات المطلوبة للتشغيل


⚙️ التثبيت والتشغيل (Setup)

# تحميل المستودع
git clone https://github.com/SaudiLinux/Ventrilo-Ghost-Framework.git

# الدخول للمجلد
cd Ventrilo-Ghost-Framework

# تثبيت المكتبات
pip install -r requirements.txt

# تشغيل الأداة الرئيسية
python main.py
