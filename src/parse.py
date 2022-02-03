import requests
from bs4 import BeautifulSoup

def get_html(link: str):
    '''
    given the url, get the source html code
    :param link: url link
    :return: html codes
    '''
    html_text = requests.get(link).text
    return html_text

def get_tree(html_text: str):
    '''
    given the html source code, return a parsed tree
    :param html_text: html code
    :return: soup root node
    '''
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

