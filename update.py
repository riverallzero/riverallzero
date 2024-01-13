import feedparser
import os

sola_blog_rss_url = "https://riverallzero.tistory.com/rss"
rss_feed = feedparser.parse(sola_blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"


markdown_text = """## 👩🏻‍💻 Dayoung Kang
### About
- <code>🎓 Jeonbuk National University</code>
  - computer science
  - digital agriculture

### Social
- <code>🅴 [E-mail](mailto:kallzero1008@jbnu.ac.kr)</code>
- <code>🅻 [LinkedIn](https://www.linkedin.com/in/riverallzero/)</code>
- <code>🆃 [Tistory](https://riverallzero.tistory.com/)</code>

### Blog Post</h3>



"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
