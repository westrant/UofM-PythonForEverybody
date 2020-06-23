import bs4 as bs
import requests
import sqlite3
from sqlite3 import Error
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

## This script creates our sqlite database of financial information and stats.

DB_NAME = "stocks_data2.db"

def obtain_sp500_tickers():
    resp = requests.get(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.replace('\n', '')
        if '.' not in ticker:
            tickers.append(ticker)

    return tickers

def build_db(stocks):
    conn= sqlite3.connect(DB_NAME)
    c = conn.cursor()

    for stock in stocks:
        try:
            c.execute("CREATE TABLE IF NOT EXISTS '{}' (Date DATETIME PRIMARY KEY, Open FLOAT, High FLOAT, Low FLOAT, Close FLOAT)".format(stock))
        except Error as e:
            print("Error creating table for", stock,e)
    conn.commit()
    conn.close()

def checkTables(db,stocks):
  conn = sqlite3.connect(db)
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table';")
  print("n tables: ", cursor.fetchall())
  print("n stocks: ", len(stocks))
  conn.close()

def insertData(db,stocks):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    start, end = dt.datetime(2020, 1, 1), dt.datetime(2020, 4, 24)
    for stock in stocks:
        try:
            df = web.DataReader(stock, "yahoo", start, end)
        except:
            break
        print("===", stock, "===")
        print(df.tail(1))
        for idx, val in df.iterrows():
            try:
                c.execute(
                    "INSERT INTO '{}' (Date, Open, High, Low, Close) VALUES(:Date, :Open, :High, :Low, :Close)".format(stock),
                    {'Date':idx.strftime('%Y-%m-%d %H-%M-%S'),'Open':val['Open'],'High':val['High'],'Low':val['Low'],'Close':val['Close']})
            except Error as e:
                print("Error Inserting", stock, "Err:", e)
    print("Inserted", stock)
    conn.commit()
    conn.close()

def checkData(db, stock):
  conn = sqlite3.connect(db)
  cursor = conn.cursor()

  start_date = '2020-01-01 00-00-00'
  end_date = '2020-04-31 00-00-00'

  print("(Date, Open, High, Low, Close)")
  cursor.execute("SELECT * FROM '{}' WHERE Date BETWEEN '{}' AND '{}'".format(stock,start_date,end_date))
  rows = cursor.fetchall()

  close = []
  date = []
  count = 0
  for row in rows:
      close.append(row[4])
      date.append(row[0][5:10])

  fig, ax = plt.subplots()
  fig.suptitle(stock + " share price", fontsize=20)
  plt.plot(date, close)
  every_nth = 7
  for close, date in enumerate(ax.xaxis.get_ticklabels()):
    if close % every_nth != 0:
        date.set_visible(False)

  plt.show()

  conn.close()

if __name__ == "__main__":
    #stocks = obtain_sp500_tickers()
    #build_db(stocks)
    #insertData(DB_NAME, stocks)
    #checkTables(DB_NAME,stocks)
    checkData(DB_NAME, 'CSCO')
