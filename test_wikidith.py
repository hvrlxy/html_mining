# This is a sample Python script.
from src import *
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#getting the sample html file
sample_html = 'https://wikidth.org/tim-kiem?status=5794f03dd7ced228f4419191&qs=1&y=2022&m=2&q=&start=0&so=1&tf=1&vo=2'

web_data = webmine(
    url_path=sample_html,
    source_code=None
)

web_data.print_all_df()
