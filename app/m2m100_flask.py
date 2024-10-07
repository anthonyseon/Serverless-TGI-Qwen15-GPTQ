
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModel, pipeline
import os
import torch

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 환경 변수에서 Hugging Face API 토큰 및 모델 ID 가져오기
token = os.getenv("HUGGINGFACE_HUB_TOKEN")
model_id = os.getenv("MODEL_ID")  # Vessl의 환경변수에 설정된 MODEL_ID 가져오기

# 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=token)
model = AutoModel.from_pretrained(model_id, use_auth_token=token)

# 텍스트 생성 파이프라인 설정
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route('/generate', methods=['POST'])
def generate():
    # JSON에서 입력 텍스트 가져오기
    data = request.get_json()
    input_text = data.get('inputs', '')

    if not input_text:
        return jsonify({"error": "Input text is required"}), 400

    # 텍스트 생성
    response = generator(input_text, max_new_tokens=512, top_k=10, top_p=0.95, temperature=0.0)
    
    # 생성된 텍스트를 JSON 형식으로 반환
    return jsonify(response)

if __name__ == '__main__':
    # Flask 애플리케이션 실행
    app.run(host='0.0.0.0', port=8000, use_reloader=False)
