from main.traverse import *
from main.extract import *
from main.parse import *
from tabulate import tabulate


url = 'https://www.traillink.com/stateactivity/mn-running-trails/'
soup = get_tree(get_html(url))

list_df = traverse(soup)
df_dict = convert_all_df(list_df)

convert_to_excel(df_dict, './test_results/trails.xlsx')
