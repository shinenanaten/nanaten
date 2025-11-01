# セットアップガイド

## APIキーの設定

ホームページ制作君を使用するには、Anthropic API Keyが必要です。

### 方法1: 環境変数を設定（推奨）

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
python app.py
```

### 方法2: .envファイルを使用

```bash
# .envファイルを作成
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
echo "FLASK_ENV=development" >> .env
echo "FLASK_DEBUG=True" >> .env
echo "PORT=5000" >> .env

# アプリケーションを起動
python app.py
```

### 方法3: 直接指定して起動

```bash
ANTHROPIC_API_KEY="your-api-key-here" python app.py
```

## ブラウザでアクセス

アプリケーションが起動したら、以下のいずれかのURLでアクセス:

- http://127.0.0.1:5000
- http://localhost:5000

## サンプル出力

実際の生成例を確認するには、`sample_output.html` をブラウザで開いてください。

```bash
# サンプルHTMLをブラウザで開く（例）
open sample_output.html  # macOS
xdg-open sample_output.html  # Linux
start sample_output.html  # Windows
```

## トラブルシューティング

### APIキーエラー

```
WARNING: ANTHROPIC_API_KEY is not set
```

→ 上記の方法1-3のいずれかでAPIキーを設定してください。

### ポートが使用中

```
Address already in use
```

→ ポート番号を変更してください:

```bash
PORT=5001 python app.py
```

### ブラウザからアクセスできない

Docker/リモート環境の場合:
- ポートフォワーディングを設定
- または `sample_output.html` で生成結果を確認
