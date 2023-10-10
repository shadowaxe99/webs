```python
import requests
from bs4 import BeautifulSoup

def get_page_load_time(url):
    response = requests.get(url)
    page_load_time = response.elapsed.total_seconds()
    return page_load_time

def get_page_size(url):
    response = requests.get(url)
    page_size = len(response.content)
    return page_size

def get_lighthouse_score(url):
    lighthouse_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}"
    response = requests.get(lighthouse_url)
    data = response.json()
    score = data["lighthouseResult"]["categories"]["performance"]["score"]
    return score

def get_gtmetrix_score(url):
    gtmetrix_url = f"https://gtmetrix.com/reports/{url}/"
    response = requests.get(gtmetrix_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    score = soup.find("div", class_="report-score-percent").text
    return score

def main():
    url = "http://localhost:8000"  # replace with your website url
    print(f"Page load time: {get_page_load_time(url)} seconds")
    print(f"Page size: {get_page_size(url)} bytes")
    print(f"Lighthouse score: {get_lighthouse_score(url)}")
    print(f"GTmetrix score: {get_gtmetrix_score(url)}")

if __name__ == "__main__":
    main()
```