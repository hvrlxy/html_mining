from src.traverse import *
from src.extract import *
from src.parse import *
from tabulate import tabulate

class webmine:
    def __init__(self, url_path=None, source_code=None):
        self.url_path = url_path
        self.source_code = source_code
        if self.source_code is None and self.url_path is None:
            print('Please input source code or url path!')
        elif self.url_path is not None:
            self.soup_tree = get_tree(get_html(self.url_path))
        else:
            self.soup_tree = get_tree(self.source_code)

        self.df_dict = self.generate_dataframes()

    def generate_dataframes(self):
        list_df = traverse(self.soup_tree)
        df_dict = convert_all_df(list_df)
        return df_dict

    def print_dataframe(self, df_name, df):
        print(df_name)
        print(tabulate(df, headers='keys', tablefmt='psql'))

    def print_all_df(self):
        for df_name in self.df_dict.keys():
            self.print_dataframe(df_name, self.df_dict[df_name])

    def generate_excel(self, path_name = None):
        convert_to_excel(self.df_dict, path_name)

