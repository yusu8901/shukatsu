import streamlit as st
import requests
import json
import os

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
    page_title="就活チャットボット",
    page_icon="🤖"
)

st.title("就活チャットボット")

# チャット履歴を表示
for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力処理
if prompt := st.chat_input("ここに入力してください"):

    # ユーザーのメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state["chat_history"].append({"role": "user", "content": prompt})

    # ユーザーが"終了"と入力した場合
    if prompt == "終了":
        # 会話を継続し、JSONデータを受け取る
        json_str = continue_conversation(st.session_state["conversation_id"], prompt)

        # 受け取ったjson文字列をPythonの辞書型に変換
        try:
            data = json.loads(json_str)  # ここでdataをdictとして格納
        except json.JSONDecodeError:
            st.error("取得したデータがJSONではありませんでした。")
            data = {}

        st.title("カスタムバー可視化例")

        # dataが想定の構造である場合のみ可視化
        if isinstance(data, dict):
            for category, items in data.items():
                st.subheader(category)
                if isinstance(items, dict):
                    for label, value in items.items():
                        # valueは0~5を想定
                        percentage = (value / 5) * 100

                        html = f"""
                        <div style="margin-bottom:20px;">
                            <!-- 上部ラベル -->
                            <div style="font-weight:bold; margin-bottom:5px; font-size:14px;">
                                {label}
                            </div>
                            <!-- 中段：左0 右5 表示 -->
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                                <span>0</span>
                                <span>5</span>
                            </div>
                            <!-- 下段：バー本体 -->
                            <div style="background-color:#e1e1e1; border-radius:10px; height:20px; width:100%; position:relative;">
                                <div style="background-color:#4c9aff; width:{percentage}%; height:100%; border-radius:10px; position:absolute; left:0;">
                                </div>
                            </div>
                        </div>
                        """

                        st.markdown(html, unsafe_allow_html=True)
        else:
            st.error("取得したdataが辞書型ではありません。")

    else:
        # "終了"以外は通常の会話継続
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
