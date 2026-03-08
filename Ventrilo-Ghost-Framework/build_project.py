import os
import shutil
import zipfile

# بيانات المشروع والمطور
project_name = "Ventrilo-Ghost-Framework"
dev_name = "SayerLinux"
dev_email = "mailto:SaudiLinux1@gmail.com"

def create_master_project():
    # 1. تحديد المسار (سطح المكتب)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    base_path = os.path.join(desktop, project_name)

    if os.path.exists(base_path):
        shutil.rmtree(base_path) # مسح المجلد القديم إذا وجد

    # 2. إنشاء الهيكل التنظيمي
    folders = ['', 'core', 'c2_server', 'c2_server/templates', 'agent']
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # 3. محتويات الملفات (بما فيها اسمك وإيميلك الملون)
    files = {
        "requirements.txt": "requests
aiohttp
beautifulsoup4
flask
colorama",
        
        "README.md": f"""# <div align="center"><font color="#007bff">Ventrilo-Ghost Framework 🛡️💀</font></div>

<div align="center">
<h3><b>إطار عمل متكامل لاختبار الاختراق المتقدم (v2.0)</b></h3>
<p>
<b>Developed by:</b> <font color="blue" size="5"><b>{dev_name}</b></font><br>
<b>Email:</b> <a href="mailto:{dev_email}"><font color="blue">{dev_email}</font></a>
</p>
</div>

---
## 🚀 نظرة عامة
إطار عمل احترافي صممه المطور **{dev_name}** لعمليات Red Teaming والاستطلاع العميق وتجاوز الحماية.""",

        "core/scanner.py": "import asyncio
import aiohttp
# [Async Scanner Logic Built by SayerLinux]
print('Scanner Engine Ready...')",
        
        "c2_server/app.py": "from flask import Flask, render_template
app = Flask(__name__)
# [C2 Control Logic Built by SayerLinux]
if __name__ == '__main__': app.run(port=5000)",

        "agent/ghost_agent.py": "import requests
# [Ghost Agent Persistence Logic]
print('Agent Active... Waiting for Command')"
    }

    # 4. كتابة الملفات
    for filename, content in files.items():
        with open(os.path.join(base_path, filename), "w", encoding="utf-8") as f:
            f.write(content)

    # 5. ضغط المجلد بالكامل في ملف ZIP
    zip_path = os.path.join(desktop, f"{project_name}.zip")
    shutil.make_archive(base_path, 'zip', base_path)

    print(f"
{'='*60}")
    print(f"[🌟] مبروك يا {dev_name}! تمت العملية بنجاح عبقري.")
    print(f"[📁] المجلد موجود على سطح المكتب: {base_path}")
    print(f"[📦] الملف المضغوط جاهز للرفع: {project_name}.zip")
    print(f"{'='*60}")

if __name__ == "__main__":
    create_master_project()