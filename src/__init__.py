from src.traverse import *
from src.extract import *
from src.parse import *

class webmine(url_path):
    def __init__(self):
        self.url_path = url_path
        self.soup_tree = get_tree(get_html(self.url_path))

    def generate_dataframes(self):
        list_df = traverse(tree)
