import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envから環境変数を読み込む
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# LLMモデルの準備
chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7, model_name="gpt-3.5-turbo")

# 専門家の定義
experts = {
    "料理の専門家": "あなたは料理の専門家です。家庭で作れる美味しいレシピを提案してください。",
    "金融の専門家": "あなたは金融の専門家です。投資や節約に関するアドバイスを提供してください。"
}

# Streamlit UI
st.title("専門家LLMアプリ")
st.markdown("このアプリでは、選択した専門家としてLLMが回答します。質問を入力してください。")

# ラジオボタンで専門家を選択
selected_expert = st.radio("専門家を選択してください", list(experts.keys()))

# ユーザーからの質問入力
user_input = st.text_input("質問を入力してください")

# 応答取得用関数
def get_response(expert_prompt, user_input):
    messages = [
        SystemMessage(content=expert_prompt),
        HumanMessage(content=user_input)
    ]
    return chat(messages).content

# 入力があれば処理
if user_input:
    system_prompt = experts[selected_expert]
    response = get_response(system_prompt, user_input)
    st.markdown("### 回答")
    st.write(response)
