#!/usr/bin/env python3
"""ホームページ制作君のデモスクリプト"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# サンプルHTMLソース
sample_html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Coffee Shop</title>
</head>
<body>
    <h1>Welcome to My Coffee Shop</h1>
    <p>We serve the best coffee in town!</p>
    <ul>
        <li>Espresso</li>
        <li>Cappuccino</li>
        <li>Latte</li>
    </ul>
</body>
</html>
"""

requirements = "モダンでおしゃれなカフェのウェブサイト。グラデーション、カード型デザイン、ホバーエフェクトを使用。レスポンシブ対応。"

print("=" * 60)
print("ホームページ制作君 - デモ実行中...")
print("=" * 60)
print()
print("【入力情報】")
print(f"HTMLソース: {sample_html[:100]}...")
print(f"要望: {requirements}")
print()
print("AI生成中...")
print()

try:
    # API呼び出し
    response = requests.post(
        f"{BASE_URL}/api/generate",
        json={
            "sourceHtml": sample_html,
            "requirements": requirements
        },
        timeout=60
    )

    if response.status_code == 200:
        result = response.json()
        generated_html = result.get('html', '')

        # 生成されたHTMLをファイルに保存
        output_file = '/home/user/nanaten/generated_demo.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generated_html)

        print("✅ 生成成功！")
        print()
        print(f"📄 生成されたHTMLファイル: {output_file}")
        print()
        print("=" * 60)
        print("生成されたHTMLの一部:")
        print("=" * 60)
        print(generated_html[:1000])
        print()
        print("...")
        print()
        print(f"💾 完全なHTMLは {output_file} に保存されました")

    else:
        print(f"❌ エラー: HTTP {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ エラーが発生しました: {str(e)}")
