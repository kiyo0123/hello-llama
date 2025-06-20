# Llama Hello


## クイックスタート

> **前提**  
> - macOS (Apple Silicon)  
> - Homebrew が入っている  
> - Git でこのリポジトリをクローン済み

```bash
# 1. Ollama を入れてサーバを起動
brew install ollama
brew services start ollama          # または別ターミナルで `ollama serve`

# 2. Llama 3 8B モデルを取得
ollama pull llama3:8b               # 初回のみ・約 5 GB

# 3. Python 仮想環境を用意して依存をインストール
uv venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt  # ollama-python が入ります

# 4. スクリプト実行（日本語で応答が返れば成功）
python hello_llama.py


