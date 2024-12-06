import streamlit as st
import requests
import json

# Difyのchat-messagesエンドポイント
API_URL = "https://api.dify.ai/v1/chat-messages"

# DifyのSecret Keyを設定
API_KEY = "app-hGAM3olRZwsGWGmBEvgNlMZM"

# リクエスト共通ヘッダー
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

# セッション状態の初期化
if "conversation_id" not in st.session_state:
    st.session_state["conversation_id"] = None
    st.session_state["chat_history"] = []

# 新規会話を開始する関数
def start_conversation(query: str, inputs: dict = {}):
    data = {
        "inputs": inputs,
        "query": query,
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "user-123"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        resp_json = response.json()
        return resp_json.get("conversation_id", None), resp_json.get("answer", "")
    else:
        st.error(f"Error: {response.text}")
        return None, None

# 会話を継続する関数
def continue_conversation(conversation_id: str, query: str):
    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "conversation_id": conversation_id,
        "user": "user-123"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        resp_json = response.json()
        return resp_json.get("answer", "")
    else:
        st.error(f"Error: {response.text}")
        return ""

# Streamlitのページ設定
st.set_page_config(
    page_title="Chat with Dify Bot",
    page_icon="🤖"
)

st.title("Chat with Dify Bot")

# チャット履歴を表示
for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力処理
if prompt := st.chat_input("ここに入力してください"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state["chat_history"].append({"role": "user", "content": prompt})

    if st.session_state["conversation_id"] is None:
        # 新規会話開始
        conversation_id, response = start_conversation(prompt)
        if conversation_id:
            st.session_state["conversation_id"] = conversation_id
    else:
        # 会話を継続
        response = continue_conversation(st.session_state["conversation_id"], prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state["chat_history"].append({"role": "assistant", "content": response})
