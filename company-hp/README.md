# 会社HP（株式会社PROD）掲載用 セブ島スタディツアー紹介ページ

構成・原稿の根拠は `docs/company-hp/STRUCTURE.md`。

| ファイル | 用途 |
|---|---|
| `index.html` | 原本。画像は `images/` を相対参照（ブラウザで直接開いて確認できる） |
| `images/` | 最適化済みの写真22枚（長辺900〜1920px） |
| `build.py` | WordPressへ貼る版を作る |
| `dist/prod-cebu-inline.html` | 画像をbase64で埋め込んだ版（約3.7MB）。そのまま貼れば動く |

## WordPressへの貼り方

### おすすめ：画像をメディアにアップロードする（ページが軽くなる）
1. `images/` の22枚をWordPressの「メディア」へアップロードする
2. アップロード先のフォルダURL（例: `https://prod-fukuoka.jp/wp-content/uploads/2026/10/`）を確認する
3. `python3 build.py wp <フォルダURL>` を実行 → `dist/prod-cebu-wp.html` ができる
4. 固定ページに「カスタムHTML」ブロックを置き、`dist/prod-cebu-wp.html` の中身を貼る

### 手早く：画像埋め込み版をそのまま貼る
`dist/prod-cebu-inline.html` の中身を「カスタムHTML」ブロックに貼る（PRODIAページと同じ方式）。
