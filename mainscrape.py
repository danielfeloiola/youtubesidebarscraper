from advanced_link_crawler import download
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = input('url: ')
    page = download(url)
    
    print(page)
