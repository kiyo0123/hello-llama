import ollama, json

messages = [
    # ← system ロール：モデルに「必ず日本語で答えよ」と指示
    {
        "role": "system",
        "content": (
            "あなたはフレンドリーかつプロフェッショナルな AI アシスタントです。"
            "すべての回答を日本語で返してください。"
        )
    },
    # user ロール：ふつうの入力
    {"role": "user", "content": "サッカーワールドカップの歴代優勝国と準優勝国を教えて下さい。直近10回分教えて。"}
]

response = ollama.chat(
    #model="llama3:8b",
    model="gemma3:12b",
    messages=messages,
    options={          # ← ここに推論パラメータをまとめて指定
        "temperature": 0.7,     # 数字が大きいほどランダム（既定 0.8）
        "top_p": 0.9,           # nucleus sampling。1.0 でオフ
        "top_k": 40,            # 0 でオフ。大きいほど多様
        "repeat_penalty": 1.1,  # 同じ語の繰り返し抑制 (>1.0 で有効)
        "seed": 42              # 乱数を固定して毎回同じ出力に
    }
)

print(json.dumps(response["message"]["content"], ensure_ascii=False, indent=2))
