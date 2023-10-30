from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

# OpenAIのモデルに対応するトークナイザを取得
enc = tiktoken.encoding_for_model("gpt-4")

@app.route('/count_tokens', methods=['POST'])
def count_tokens():
    print(request.json)
    if not request.json:
        return jsonify({"error": "JSON body expected"}), 400

    text = request.json.get('text')
    if text is None:
        return jsonify({"error": "Key 'text' not found in the request body"}), 400
    
    # トークンのエンコードとその数を取得
    encoded_tokens = enc.encode(text)
    tokens_count = len(encoded_tokens)
    
    return jsonify({"tokens": tokens_count})

@app.route('/')
def home():
    return "Hello, this is the home page!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

