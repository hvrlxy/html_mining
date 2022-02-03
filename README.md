# EXTRACTING DATA FROM AN HTML SOURCE CODE

This library uses html parser to identify duplicated codes from a html file, extract information from the file and convert the data into pandas dataframe or excel format. It makes use of famous library, including beautifulsoup, pandas, tabulate, ... and aims to make web scrapping easier for data scientists.

The program works well with well-formated HTML/HTML5 webpage, and examples of its usage can be found in the library. The library is still in development, and I hope to add more features and restructure the library in the near future.

## Initialization
To start the program, we will need either a url path or an html file. The program will read in the html codes and parsed them into a tree.


```
from src import *
  
sample_html = 'https://twitchtracker.com/channels/viewership'
file_path = 'test_cases/twitchdata.html'
f = open(file_path,'r')

soup_code = webmine(source_code=f)
soup_url = webmine(url_path=sample_html)
```

To get the most precise dataset, I believe downloading the html source code using chrome extension is the most effective way. Some webpages deliberately make it hard for people to crawl data from their webpage, so reading from an url path might lose a great chunch of html codes.

## Retrieving the dataframe

To retrieve all the tables and data from the webpage, we call the attribute:

```
soup = webmine(source_code=f)
soup.df_dict
```

which will return a dictionary with keys are the names of the table, and values are pandas dataframe that are ready to be used and analyzed.

## Export to excel
To export the dataframes crawled to an excel file, simply input the code

```
soup.generate_excel('excel_path')
```
This function will export the data into an excel file of our choice, with each dataframe occupied a seperate sheet.

## Examples
There are different examples available in this repo. This program works well with well-formatted html file, and was able to retrieve most of the table-based data available in a webpage.

## Drawbacks and Future Works
The program still have problem with retrieving the correct table/column names, and I am researching intensively on how to incorporate other methods into this program. The program also has problem with ill-formatted html codes, and I am working on improving accuracies in those edge cases.
