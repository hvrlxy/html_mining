import requests
from bs4 import BeautifulSoup

def get_html(link: str):
    html_text = requests.get(link).text
    return html_text

def get_tree(html_text: str):
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

