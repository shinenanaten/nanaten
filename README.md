# 🎨 ホームページ制作君 (Homepage Builder Tool)

AIを活用して、参考URLやHTMLソースからおしゃれなホームページを自動生成するツールです。

## ✨ 特徴

- 🌐 **参考URL入力**: 既存のWebサイトを参考にしたデザイン生成
- 📝 **HTMLソース入力**: 既存のHTMLを改善・最適化
- 🎯 **カスタム要望**: デザインや機能についての詳細な要望を指定可能
- 🤖 **AI搭載**: Claude 3.5 Sonnetを使用した高品質な生成
- 📱 **レスポンシブ**: モバイルフレンドリーなデザインを自動生成
- 🎨 **モダンデザイン**: 最新のWebデザイントレンドに対応
- 💾 **即座にダウンロード**: 生成されたHTMLをすぐにダウンロード可能

## 🚀 セットアップ

### 必要要件

- Python 3.8以上
- Anthropic API Key

### インストール手順

1. リポジトリをクローン
```bash
git clone <repository-url>
cd nanaten
```

2. 仮想環境を作成（推奨）
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存パッケージをインストール
```bash
pip install -r requirements.txt
```

4. 環境変数を設定
```bash
cp .env.example .env
```

`.env`ファイルを編集して、Anthropic API Keyを設定:
```
ANTHROPIC_API_KEY=your_api_key_here
```

5. アプリケーションを起動
```bash
python app.py
```

6. ブラウザで開く
```
http://localhost:5000
```

## 📖 使い方

### 基本的な使い方

1. **参考URLを入力**（オプション）
   - デザインの参考にしたいWebサイトのURLを入力

2. **HTMLソースを入力**（オプション）
   - 改善したい既存のHTMLコードを貼り付け

3. **追加の要望を入力**（オプション）
   - 例: 「ダークモード対応」「アニメーション多め」「ミニマルなデザイン」

4. **「ホームページを生成」ボタンをクリック**
   - AIが自動的におしゃれなホームページを生成

5. **結果を確認**
   - プレビュータブで視覚的に確認
   - HTMLコードタブでソースコードを確認
   - 「HTMLをダウンロード」ボタンでファイルを保存

### 使用例

#### 例1: 参考URLのみ
```
参考URL: https://www.apple.com
追加の要望: シンプルでミニマルなデザイン
```

#### 例2: HTMLソースのみ
```html
HTMLソース:
<!DOCTYPE html>
<html>
<head><title>My Site</title></head>
<body>
  <h1>Welcome</h1>
  <p>This is my website</p>
</body>
</html>

追加の要望: モダンでカラフルなデザインに変更
```

#### 例3: 両方を組み合わせ
```
参考URL: https://www.stripe.com
HTMLソース: [既存のHTML]
追加の要望: グラデーションを多用したデザイン
```

## 🏗️ プロジェクト構造

```
nanaten/
├── app.py                 # Flaskアプリケーション（バックエンド）
├── requirements.txt       # Python依存パッケージ
├── .env                   # 環境変数（gitignore対象）
├── .env.example          # 環境変数のサンプル
├── templates/
│   └── index.html        # フロントエンドUI
├── static/               # 静的ファイル（将来的に使用）
└── README.md             # このファイル
```

## 🔧 API エンドポイント

### `POST /api/fetch-url`
参考URLからHTMLコンテンツを取得

**リクエスト:**
```json
{
  "url": "https://example.com"
}
```

**レスポンス:**
```json
{
  "success": true,
  "html": "...",
  "text": "..."
}
```

### `POST /api/generate`
ホームページを生成

**リクエスト:**
```json
{
  "referenceHtml": "...",
  "sourceHtml": "...",
  "requirements": "..."
}
```

**レスポンス:**
```json
{
  "success": true,
  "html": "<!DOCTYPE html>..."
}
```

## 🛠️ カスタマイズ

### プロンプトのカスタマイズ
`app.py`の`build_generation_prompt`関数を編集することで、AI生成のスタイルを調整できます。

### UIのカスタマイズ
`templates/index.html`のスタイルセクションを編集することで、見た目を変更できます。

## 🐛 トラブルシューティング

### API Keyエラー
```
Error: Anthropic API Key is not set
```
→ `.env`ファイルに正しいAPI Keyが設定されているか確認

### URLフェッチエラー
```
Failed to fetch URL
```
→ URLが正しいか、アクセス可能なサイトか確認

### ポートが使用中
```
Address already in use
```
→ `.env`のPORT番号を変更するか、既存のプロセスを終了

## 📝 ライセンス

MIT License

## 🤝 コントリビューション

プルリクエストを歓迎します！

## 📧 お問い合わせ

問題が発生した場合は、Issueを作成してください。

---

Made with ❤️ using Claude AI
