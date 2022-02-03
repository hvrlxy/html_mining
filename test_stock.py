from src import *

sample_html = 'https://money.cnn.com/data/markets'

web_data = webmine(
    url_path=sample_html,
    source_code=None
)

web_data.print_all_df()
