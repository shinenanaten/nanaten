from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import anthropic
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/fetch-url', methods=['POST'])
def fetch_url():
    """Fetch HTML content from URL"""
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant content
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()

        # Get text and HTML structure
        html_content = str(soup)
        text_content = soup.get_text(separator='\n', strip=True)

        return jsonify({
            'success': True,
            'html': html_content[:50000],  # Limit size
            'text': text_content[:10000]   # Limit size
        })

    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch URL: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate', methods=['POST'])
def generate_homepage():
    """Generate homepage using AI"""
    try:
        data = request.json
        reference_html = data.get('referenceHtml', '')
        source_html = data.get('sourceHtml', '')
        requirements = data.get('requirements', '')

        # Build prompt for Claude
        prompt = build_generation_prompt(reference_html, source_html, requirements)

        # Call Claude API
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Extract generated HTML
        generated_html = message.content[0].text

        # Clean up the response (remove markdown code blocks if present)
        if '```html' in generated_html:
            generated_html = generated_html.split('```html')[1].split('```')[0].strip()
        elif '```' in generated_html:
            generated_html = generated_html.split('```')[1].split('```')[0].strip()

        return jsonify({
            'success': True,
            'html': generated_html
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def build_generation_prompt(reference_html, source_html, requirements):
    """Build prompt for AI generation"""
    prompt = """あなたはプロのWebデザイナーです。以下の情報を基に、モダンでおしゃれなホームページのHTMLを生成してください。

要件:
- レスポンシブデザイン（モバイル対応）
- モダンなCSSデザイン（グラデーション、シャドウ、アニメーションなど）
- 使いやすいUI/UX
- アクセシビリティを考慮
- 完全なHTML（<!DOCTYPE html>から</html>まで）
- CSS は <style> タグ内に記述
- JavaScript が必要な場合は <script> タグ内に記述

"""

    if requirements:
        prompt += f"\n【ユーザーの要望】\n{requirements}\n"

    if reference_html:
        prompt += f"\n【参考URL のHTML（デザインの参考にしてください）】\n{reference_html[:3000]}\n"

    if source_html:
        prompt += f"\n【元になるHTMLソース（この内容を改善してください）】\n{source_html[:3000]}\n"

    prompt += """
生成するHTMLには以下を含めてください:
1. ヘッダー（ナビゲーション）
2. ヒーローセクション（メインビジュアル）
3. 特徴・サービス紹介セクション
4. フッター

カラースキームは調和の取れた美しい配色を選んでください。
HTMLのみを出力してください。説明文は不要です。"""

    return prompt

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
