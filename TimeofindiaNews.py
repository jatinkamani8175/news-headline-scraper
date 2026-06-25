import requests
from bs4 import BeautifulSoup
from datetime import datetime

html_text = requests.get("https://timesofindia.indiatimes.com/").text

soup = BeautifulSoup(html_text,'lxml')
news_headline = soup.find_all('div',class_ = 'Kt6Pm style_change T5Q6J')

news_paragraph = soup.find_all('p',class_ = "hEoJ3")

# for headline, paragraph in zip(news_headline[1:], news_paragraph):
#     print("Headline:", headline.text)
#     print("Paragraph:", paragraph.text)
#     print()


news = datetime.now().strftime("TOI_News_%Y-%m-%d_%H-%M-%S.txt")

with open(news, "w", encoding="utf-8") as file:
    file.write(f"TOI News Scraped on {datetime.now()}\n")
    file.write("=" * 80 + "\n\n")

    for headline, paragraph in zip(news_headline[1:], news_paragraph):
        file.write(f"Headline: {headline.text}.\n")
        file.write(f"Paragraph: {paragraph.text}\n")
        file.write("-" * (len(paragraph.text)+11) + "\n")
