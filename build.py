import datetime

# 1. 現在の日時を取得
now = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M")

# 2. 記事データ（Pythonのリストと辞書）
posts = [
    {"title": "VS CodeとPythonでサイト作成開始！", "body": "PythonスクリプトからHTMLを自動生成する仕組みを作りました。"},
    {"title": "GitHub Pagesの公開テスト", "body": "完全無料で自分のサイトを持てるようになりました。"},
]

# 3. 記事データをHTMLパーツに変換
posts_html = ""
for post in posts:
    posts_html += f"""
    <article class="post">
      <h2>{post['title']}</h2>
      <p>{post['body']}</p>
    </article>
    """

# 4. 全体のHTMLを組み立てる
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>omiyajunkieのホームページ</title>
  <style>
    body {{ font-family: sans-serif; max-width: 760px; margin: 40px auto; padding: 0 20px; background: #f4f6f8; color: #333; }}
    header {{ background: #1d4ed8; color: #fff; padding: 24px; border-radius: 12px; margin-bottom: 24px; }}
    .post {{ background: #fff; padding: 20px; border-radius: 10px; margin-bottom: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }}
    footer {{ text-align: center; color: #666; font-size: 0.9em; margin-top: 32px; }}
  </style>
</head>
<body>
  <header>
    <h1>omiyajunkie's Website</h1>
    <p>Pythonで生成したホームページ</p>
  </header>
  <main>
    {posts_html}
  </main>
  <footer>
    最終更新：{now}
  </footer>
</body>
</html>
"""

import os

# 5. build.py と同じフォルダ（homepageの中）に index.html を書き出す
output_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html の生成が完了しました！")