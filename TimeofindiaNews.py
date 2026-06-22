import feedparser
from datetime import datetime


def scrape_toi_rss():
    rss_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

    try:
        # Parse RSS feed
        feed = feedparser.parse(rss_url)

        if not feed.entries:
            print("❌ No news articles found.")
            return

        # Create filename with current date
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"toi_news_{date_str}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"🗓️ TOI Top Stories - {date_str}\n")
            f.write("=" * 80 + "\n\n")

            for i, article in enumerate(feed.entries, start=1):
                headline = article.get("title", "No Headline")
                description = article.get("summary", "No Description")
                link = article.get("link", "No Link")

                f.write(f"News #{i}\n")
                f.write(f"Headline    : {headline}\n")
                f.write(f"Description : {description}\n")
                f.write(f"Link        : {link}\n")
                f.write("-" * 80 + "\n\n")

        print(f"✅ Saved {len(feed.entries)} articles to '{filename}'")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    scrape_toi_rss()