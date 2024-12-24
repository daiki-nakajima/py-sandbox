import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# 環境変数ファイルをロード
load_dotenv()
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# キーベースの認証を使用して Azure OpenAI クライアントを初期化する
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# チャット プロンプトを準備する
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "test"
            }
        ]
    }
]

# 音声認識が有効になっている場合は音声結果を含める
messages = chat_prompt

# 入力候補を生成する
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.1,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())
