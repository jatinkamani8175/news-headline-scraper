📰 TOI News Headlines Scraper

A simple Python script that scrapes the latest headlines from the Times of India homepage.  
It fetches news from `<h2>` and `<h3>` tags and stores them in a clean, daily `.txt` file.

🧰 Tools & Requirements

| Tool           | Purpose                           |
|----------------|------------------------------------|
| Python 3.x     | Core scripting language            |
| requests       | For making HTTP requests           |
| BeautifulSoup  | To parse and extract HTML content  |
| datetime       | For timestamped filenames          |

🚀 Features

🌐 Scrapes live headlines from the TOI homepage  
🏷️ Extracts content from both `<h2>` and `<h3>` tags  
📅 Saves results to a file named like: `toi_headlines_YYYY-MM-DD.txt`  
✍️ Outputs headlines in a numbered, sorted list  
⚠️ Gracefully handles network failures and missing content  

📦 Usage

```bash
python TimeofindiaNews.py
