from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI
import os
import openai

app = Flask(__name__)

# 设置你的 OpenAI API 密钥
api_key = ''
openai.api_key = api_key

# 初始化 Azure OpenAI 客户端
client = AzureOpenAI(
    azure_endpoint='',
    api_key='',  
    api_version="",
)

def start_conversation(messages):
    # 发送对话请求
    response = client.chat.completions.create(
        model="",
        messages=messages,
        temperature=0.5,  # 温度参数，文本的多样性，高 -> 多样高
        top_p=0.95,  # nucleus 越高越准
        frequency_penalty=0,  # 重复性的词语
        max_tokens=4000,  # 控制你传入和输出的文本最大长度
        stop=None  # 停止词
    )
    return response.choices[0].message.content.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    ai_response = start_conversation(messages)
    return jsonify({'response': ai_response})

if __name__ == "__main__":
    app.run(debug=True)