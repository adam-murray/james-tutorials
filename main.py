import requests 

from bs4 import BeautifulSoup

PAGE_URL = "http://www.example.com"

def fetch_page(url: str):
    return requests.get(url)

def fetch_file(file_path: str):
    pass

def process_json():
    pass

def process_page(page):
    soup = BeautifulSoup(page.content)
    return soup.find("title").string

def main():
    title = process_json()
    print(title)

if __name__ == "__main__":
    main()
 