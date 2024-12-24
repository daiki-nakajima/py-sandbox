import os

from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# 環境変数ファイルをロード
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(api_key=api_key)

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="tiiuae/falcon-7b-instruct",
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)