from src import *


sample_html = 'https://www.traillink.com/stateactivity/mn-running-trails/'

web_data = webmine(
    url_path=sample_html,
    source_code=None
)

web_data.print_all_df()
