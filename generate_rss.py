# generate_rss.py
import os
from datetime import datetime

SITE_URL = "https://caster2731.github.io/Kenmofm-567Thz--Podcast"
MP3_DIR = "episodes"

items = ""
for filename in sorted(os.listdir(MP3_DIR), reverse=True):
    if filename.endswith(".mp3"):
        filepath = f"{SITE_URL}/{MP3_DIR}/{filename}"
        title = filename.replace(".mp3", "")
        pub_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
        items += f"""<item>
  <title>{title}</title>
  <enclosure url="{filepath}" type="audio/mpeg"/>
  <pubDate>{pub_date}</pubDate>
  <guid>{filepath}</guid>
</item>
"""

rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>ケンモFMポッドキャスト</title>
  <link>{SITE_URL}</link>
  <description>スレタイ読み上げ自動配信</description>
  <language>ja</language>
  {items}
</channel>
</rss>
"""

with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss)

print("✅ rss.xml を生成しました")
