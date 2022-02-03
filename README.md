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

One noticable example of the use of this program is retrieving the information from this url: https://money.cnn.com/data/markets. The code for the below program can be found in the file test_stock.py

```
from src import *

sample_html = 'https://money.cnn.com/data/markets'

web_data = webmine(
    url_path=sample_html,
    source_code=None
)

web_data.print_all_df()
```

The program was able to print out all the tables available on the webpage, with some trouble finding the correct columns/tables' names;
```
three-equal-columnswsod
+----+---------------+----------------------+-----------------+------------------------+
|    | ticker-name   | ticker-name-change   | ticker-points   |   ticker-points-change |
|----+---------------+----------------------+-----------------+------------------------|
|  0 | Dow           | -0.75%               | 35,362.70       |                -266.63 |
|  1 | Nasdaq        | -2.21%               | 14,098.39       |                -319.15 |
|  2 | S&P           | -1.39%               | 4,525.76        |                 -63.62 |
|  3 | Dow           | -0.75%               | 35,362.70       |                -266.63 |
+----+---------------+----------------------+-----------------+------------------------+
module-bodywsodmost-popular-stocks
+----+----------------------------+-----------+-----------+
|    | column                     | column1   | column2   |
|----+----------------------------+-----------+-----------|
|  0 | Twitter Inc                | 34.43     | -5.70%    |
|  1 | Ford Motor Co              | 20.15     | -2.33%    |
|  2 | Chipotle Mexican Grill Inc | 1,443.97  | -2.73%    |
|  3 | Exxon Mobil Corp           | 79.33     | -1.60%    |
|  4 | Visa Inc                   | 231.85    | -1.52%    |
|  5 | Twitter Inc                | 34.43     | -5.70%    |
+----+----------------------------+-----------+-----------+
module-bodywsodgainers
+----+---------------------------+-----------+----------+
|    | column                    | column1   |   hidden |
|----+---------------------------+-----------+----------|
|  0 | FedEx Corp                | +6.10%    |        0 |
|  1 | Occidental Petroleum Corp | +5.56%    |        0 |
|  2 | Dollar General Corp       | +5.02%    |        0 |
|  3 | Best Buy Co Inc           | +4.24%    |        0 |
|  4 | Marathon Oil Corp         | +3.18%    |        0 |
|  5 | FedEx Corp                | +6.10%    |        0 |
+----+---------------------------+-----------+----------+
module-bodywsodlosers
+----+-----------------------+-----------+----------+
|    | column                | column1   |   hidden |
|----+-----------------------+-----------+----------|
|  0 | Xylem Inc             | -10.53%   |        0 |
|  1 | Salesforce.Com Inc    | -6.24%    |        0 |
|  2 | Twitter Inc           | -6.04%    |        0 |
|  3 | Epam Systems Inc      | -5.23%    |        0 |
|  4 | Lincoln National Corp | -5.16%    |        0 |
|  5 | Xylem Inc             | -10.53%   |        0 |
+----+-----------------------+-----------+----------+
module-bodywsodcurrencies
+----+-----------------+-----------+
|    | column          | column1   |
|----+-----------------+-----------|
|  0 | British Pound   | $1.36     |
|  1 | Japanese Yen    | ¥0.01     |
|  2 | Canadian Dollar | $0.79     |
|  3 | Chinese Yuan    | ¥0.16     |
|  4 | Euro            | $1.13     |
+----+-----------------+-----------+
```

## Drawbacks and Future Works
The program still have problem with retrieving the correct table/column names, and I am researching intensively on how to incorporate other methods into this program. The program also has problem with ill-formatted html codes, and I am working on improving accuracies in those edge cases.
