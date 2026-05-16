from flask import Flask, request, jsonify

app = Flask(name)

# المتغير ده اللي هنخزن فيه أمر البوت اللي جاي من ريبليت
bot_command = "لا يوجد أوامر حالياً"

@app.route('/')
def home():
    return f"السيرفر يعمل بنجاح! الأمر الحالي للبوت هو: {bot_command}"

# الرابط ده اللي ريبليت هيبعت عليه الكود أو التحديثات بالذكاء الاصطناعي
@app.route('/update_bot', methods=['POST'])
def update_bot():
    global bot_command
    data = request.get_json()
    if data and 'command' in data:
        bot_command = data['command']
        return jsonify({"status": "success", "message": "تم استقبال تحديث البوت بنجاح!"}), 200
    return jsonify({"status": "error", "message": "بيانات غير صالحة"}), 400

if name == "main":
    app.run(host='0.0.0.0', port=8080)
