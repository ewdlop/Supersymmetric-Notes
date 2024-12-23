import requests
from bs4 import BeautifulSoup
import os

def download_link_content(url, folder):
    """
    Downloads the content of a link and saves it to a file in the specified folder.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_name = os.path.join(folder, url.replace('http://', '').replace('https://', '').replace('/', '_') + '.html')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Downloaded content from {url} to {file_name}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

def crawl_and_download(html_content, folder):
    """
    Parses HTML content, extracts all links, and downloads their content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for link in links:
        url = link['href']
        if url.startswith('http'):
            download_link_content(url, folder)

def main():
    html_file_path = 'path_to_your_html_file.html'
    download_folder = 'downloaded_content'

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    crawl_and_download(html_content, download_folder)

if __name__ == "__main__":
    main()
