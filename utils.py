import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.title.string if soup.title else 'Không có tiêu đề'
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs if len(p.get_text()) > 50)

        return f"{title}\n\n{text[:4000]}"  # Giới hạn tránh prompt quá dài
    except Exception as e:
        print("Error extracting article:", e)
        return None
