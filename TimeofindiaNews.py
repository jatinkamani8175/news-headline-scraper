import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_toi_headlines():
    url = "https://timesofindia.indiatimes.com/home/headlines"

    try:
        # Step 1: Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 2: Extract <h2> and <h3> headlines
        headlines = set()

        for tag in soup.find_all(["h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headlines.add(text)  # Set ensures uniqueness

        if not headlines:
            print("⚠️ No <h2> or <h3> headlines found.")
            return

        # Step 3: Prepare output file
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"toi_headlines_{date_str}.txt"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\n🗓️ TOI Headlines on {date_str} (h2 & h3)\n\n")
            for i, headline in enumerate(sorted(headlines), 1):
                f.write(f"{i}. {headline}\n")
            f.write("\n" + "="*60 + "\n")

        print(f"✅ Saved {len(headlines)} headlines to '{filename}'")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Execute when run directly
if __name__ == "__main__":
    scrape_toi_headlines()
