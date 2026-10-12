"""会社HP（WordPress）へ貼るHTMLを作る。

  python3 build.py inline
      画像をbase64で埋め込んだ1ファイル（dist/prod-cebu-inline.html）。そのまま貼れば動く。
  python3 build.py wp https://prod-fukuoka.jp/wp-content/uploads/2026/10/
      images/ をWordPressメディアのURLに置き換えた版（dist/prod-cebu-wp.html）。
      先に images/ の画像をメディアへアップロードし、そのフォルダURLを渡す。
"""
import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
SRC = (ROOT / "index.html").read_text(encoding="utf-8")
DIST = ROOT / "dist"


def inline() -> str:
    def to_data(m: re.Match) -> str:
        data = base64.b64encode((ROOT / "images" / m.group(1)).read_bytes()).decode()
        return f'src="data:image/jpeg;base64,{data}"'

    return re.sub(r'src="images/([^"]+)"', to_data, SRC)


def wp(base: str) -> str:
    return SRC.replace('src="images/', f'src="{base.rstrip("/")}/')


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    DIST.mkdir(exist_ok=True)
    if mode == "inline":
        out = DIST / "prod-cebu-inline.html"
        out.write_text(inline(), encoding="utf-8")
    elif mode == "wp" and len(sys.argv) > 2:
        out = DIST / "prod-cebu-wp.html"
        out.write_text(wp(sys.argv[2]), encoding="utf-8")
    else:
        sys.exit(__doc__)
    print(f"{out}  {out.stat().st_size // 1024} KB")
