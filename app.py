from flask import Flask, render_template, request, jsonify
from utils import extract_article_text
from gemini_api import get_gemini_analysis  # bạn cần định nghĩa riêng
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.json.get('url')
    article = extract_article_text(url)
    if not article:
        return jsonify({'error': 'Không trích xuất được nội dung từ link.'}), 400

    result = get_gemini_analysis(article)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
