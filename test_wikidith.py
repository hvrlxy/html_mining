# This is a sample Python script.
from main.parse import *
from main.traverse import *
from tabulate import tabulate
from main.extract import *
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#getting the sample html file
sample_html = 'https://wikidth.org/tim-kiem?status=5794f03dd7ced228f4419191&qs=1&y=2022&m=2&q=&start=0&so=1&tf=1&vo=2'
tree = get_tree(get_html(sample_html))

# print_children(tree)
items = tree.find_all(class_ = 'book-item')
#test the compare subtree function
# print(compare_node_structure(items[0], items[2]))

#check the contain data function
# nodes = tree.find_all(class_ = 'book-list')
# print(len(check_contain_df(nodes[0])))

#check the find all df function
list_df = traverse(tree)
print(list_df.keys())

#test extract strings function
# test_string = items[0]
# print(extract_strings(test_string))

#test convert all df function
df_dict = convert_all_df(list_df)
# print(tabulate(df_dict['book-list'], headers='keys', tablefmt='psql'))

#test convert to excel function
convert_to_excel(df_dict, './test_results/wikidth.xlsx')
