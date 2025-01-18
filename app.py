import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from flask import Flask, render_template, request, jsonify, send_from_directory
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from io import BytesIO
import os

# 使用 Hugging Face Hub 上的在线模型
model_name = "charent/ChatLM-mini-Chinese"  # 在线模型标识符

# 加载分词器和模型
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)

# 设置模型为评估模式
model.eval()

# 生成响应函数
def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(inputs.shape, dtype=torch.long)
    output = model.generate(inputs, 
                            attention_mask=attention_mask, 
                            max_length=256,  
                            num_return_sequences=1, 
                            no_repeat_ngram_size=2, 
                            top_p=0.8, 
                            temperature=1.0, 
                            do_sample=True, 
                            num_beams=1,          
                            length_penalty=1.0)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# 初始化 Flask 应用
app = Flask(__name__)

# 设置 favicon.ico 路由
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

# 语音识别函数
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="zh-CN")  # 使用Google的中文识别
        print("你说的是：", text)
        return text
    except sr.UnknownValueError:
        return "抱歉，我没有听清楚。"
    except sr.RequestError:
        return "无法连接到语音识别服务。"

# 语音合成函数 (使用 pyttsx3)
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 设置语速
    engine.setProperty('volume', 1)  # 设置音量
    engine.say(text)
    engine.runAndWait()

# 或者使用 gTTS 将文本转为语音文件（这里返回的是字节流）
def speak_text_gtts(text):
    tts = gTTS(text=text, lang='zh')
    audio_stream = BytesIO()
    tts.save(audio_stream)
    audio_stream.seek(0)  # Rewind to the beginning of the audio stream
    return audio_stream

# 首页路由，渲染网页
@app.route('/')
def home():
    return render_template('index.html')

# 与AI聊天的接口
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = generate_response(user_input)
    return jsonify({'response': response})

# 语音识别接口
@app.route('/voice-recognition', methods=['GET'])
def voice_recognition():
    text = recognize_speech()  # 调用语音识别
    response = generate_response(text)  # AI生成响应
    return jsonify({'response': response})

# 语音合成接口
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    user_input = request.form['message']
    audio_stream = speak_text_gtts(user_input)  # 使用 gTTS 生成语音
    return jsonify({'audio': audio_stream.getvalue()})

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
