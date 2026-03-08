import os

# تعريف اسم المجلد الرئيسي وبيانات المطور
project_name = "Ventrilo-Ghost-Framework"
developer_name = "SayerLinux"
developer_email = "mailto:SaudiLinux1@gmail.com"

# محتويات الملفات
files_content = {
    "requirements.txt": "requests
aiohttp
beautifulsoup4
flask
colorama",
    
    "README.md": f"""# <div align="center"><font color="#007bff">Ventrilo-Ghost Framework 🛡️💀</font></div>

<div align="center">
  <h3><b>إطار عمل متكامل لاختبار الاختراق المتقدم (v2.0 - 2026)</b></h3>
  <p>
    <b>Developed by:</b> <font color="blue" size="5"><b>{developer_name}</b></font><br>
    <b>Email:</b> <a href="mailto:{developer_email}"><font color="blue">{developer_email}</font></a>
  </p>
</div>

---
## 🚀 نظرة عامة
إطار عمل احترافي صممه المطور **{developer_name}** لعمليات Red Teaming والاستطلاع العميق وتجاوز الحماية.
""",

    "core/scanner.py": """import asyncio
import aiohttp
# كود الماسح العبقري الذي طورناه...""",
    
    "c2_server/app.py": """from flask import Flask, render_template
app = Flask(__name__)
# كود لوحة التحكم C2...""",
    
    "agent/ghost_agent.py": """import requests
import os
# كود العميل الشبح للتحكم عن بعد..."""
}

def create_project():
    # الحصول على مسار سطح المكتب تلقائياً
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    base_path = os.path.join(desktop, project_name)

    # إنشاء المجلدات
    folders = ['', 'core', 'c2_server', 'c2_server/templates', 'agent']
    for folder in folders:
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"[+] تم إنشاء المجلد: {path}")

    # إنشاء الملفات وكتابة الأكواد بداخلها
    for filename, content in files_content.items():
        file_path = os.path.join(base_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            print(f"[✔] تم حفظ الملف: {filename}")

    print(f"
{'='*50}
[🌟] مبروك يا {developer_name}! المشروع جاهز الآن على سطح المكتب.
{'='*50}")

if __name__ == "__main__":
    create_project()