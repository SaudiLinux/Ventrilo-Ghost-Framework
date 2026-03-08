# <div align="center"><font color="#007bff">Ventrilo-Ghost Framework 🛡️💀</font></div>

<div align="center">
  <h3><b>إطار عمل متكامل لاختبار الاختراق المتقدم (v1.1.0-Stable)</b></h3>
  <p>
    <b>Developed by:</b> <font color="blue" size="5"><b>SayerLinux</b></font><br>
    <b>Email:</b> <a mailto:href="mailto:SaudiLinux1@gmail.com"><font color="blue">mailto:SaudiLinux1@gmail.com</font></a>
  </p>
  <img src="https://img.shields.io/badge/Developer-SayerLinux-blue?style=for-the-badge&logo=linux" alt="Developer Badge">
  <img src="https://img.shields.io/badge/OS-Kali_Linux_Compatible-red?style=for-the-badge&logo=kali-linux" alt="OS Badge">
  <img src="https://img.shields.io/badge/Version-1.1.0--Stable-green?style=for-the-badge" alt="Version Badge">
</div>

---

## 🚀 نظرة عامة (Overview)

**Ventrilo-Ghost** هو إطار عمل احترافي صممه المطور **SayerLinux** لعمليات Red Teaming والاستطلاع العميق. تم تحسين هذا الإصدار (v1.1.0) ليكون متوافقاً تماماً مع بيئات **Kali Linux**، مع معالجة كافة أخطاء المسارات والترميز.

---

## 💎 المميزات العبقرية (Key Features)

- **⚡ محرك Async فائق السرعة:** فحص آلاف الصفحات في وقت قياسي باستخدام تقنية `asyncio`.
- **🛡️ Ghost Encryptor:** تشفير البيانات المستخرجة بـ AES-256 قبل إرسالها لتجاوز أنظمة المراقبة.
- **🧹 مسح الأثر (Anti-Forensics):** حذف الملفات الأصلية تلقائياً بعد تشفيرها لمنع التتبع الجنائي.
- **🕵️ تخفي كامل (Stealth Mode):** تجاوز جدران الحماية (WAF Bypass) عبر تغيير الـ `User-Agent` وتزوير الـ `IP`.
- **🖥️ لوحة تحكم Ghost C2:** واجهة ويب مركزية لإدارة السيرفرات وتنفيذ الأوامر بضغطة زر.

---

## 🛠️ هيكل المشروع (Project Structure)

```text
Ventrilo-Ghost-Framework/
├── core/
│   ├── scanner.py        # محرك الفحص العميق والتخفي
│   ├── exploiter.py      # وحدة الاستغلال (SQLi, LFI, RCE)
│   └── encryptor.py      # وحدة التشفير ومسح الأثر
├── c2_server/
│   ├── app.py            # خادم السيطرة والتحكم (Backend)
│   └── templates/        # واجهة الويب (Dashboard UI)
├── main.py               # المحرك الرئيسي (Master Controller)
└── requirements.txt      # المكتبات المطلوبة للتشغيل


⚙️ التثبيت والتشغيل في Kali Linux

# تحميل المستودع
git clone https://github.com/SaudiLinux/Ventrilo-Ghost-Framework.git
cd Ventrilo-Ghost-Framework

# تثبيت المكتبات اللازمة
pip3 install requests aiohttp beautifulsoup4 flask colorama cryptography

# تشغيل الأداة الرئيسية
python3 main.py
