foodpandスクレイピングツール
====

緯度経度を指定して、飲食店の情報を取得する。

# 環境構築
```
python -m venv venv
. venv/bin/activate ※ for macOS
. venv/scripts/activate ※ for windows
pip install -r requirements.txt
```

# 実行
```
python main/main.py
```

# 構造
engine/: スクレイピング処理
main/: メイン処理
models/: データ格納用
common/: 共通関数など
const/: 固定値
logs/: ログ格納