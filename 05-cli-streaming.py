from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # 파일이 있다면, 환경변수로서 로딩
client = OpenAI()
# 라이브러리 설치 필요 : pip install --upgrade openai

stream = client.responses.create(
    model="gpt-4o",
    input="make python code for factorial",
    stream=True,
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="", flush=True)
