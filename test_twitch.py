from src import *

sample_html = 'https://twitchtracker.com/channels/viewership'
file_path = 'test_cases/twitchdata.html'
f = open(file_path,'r')

soup = webmine(source_code=f)
soup.generate_excel('test_results/twitchdata.xlsx')
