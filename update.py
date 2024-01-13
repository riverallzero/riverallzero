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
### | About
**🎓 Jeonbuk National University** | computer science & digital agriculture

<a href="mailto:kallzero1008@jbnu.ac.kr">
  <img alt="gmail" src="https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white"/>
</a>
<a href="https://www.linkedin.com/in/riverallzero/">
  <img alt="linkedin" src="https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white"/>
</a>
<a href="https://riverallzero.tistory.com/">
  <img alt="tistory" src="https://img.shields.io/badge/Tistory-000000.svg?style=for-the-badge&logo=Tistory&logoColor=white"/>
</a>

### | Blog Post</h3>



"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
