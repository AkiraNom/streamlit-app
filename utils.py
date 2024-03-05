import base64
import datetime
import pandas as pd
import streamlit as st

def read_image(path):
    """image from local file"""

    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    return data_url

# navigation button to the tesla website
def tesla_html_link():
    return st.markdown('''
            <a href="https://tesla.com" class="cta">
            <span>To web</span>
            <svg width="13px" height="10px" viewBox="0 0 13 10">
                <path d="M1,5 L11,5"></path>
                <polyline points="8 1 12 5 8 9"></polyline>
            </svg>
            </a>
            <div><br></div>
                    ''', unsafe_allow_html=True)

# get stock price through yfinance
def get_stock_price(ticker_info, period1='1y', period2='max'):

      return (ticker_info.history(period=period1),
              ticker_info.history(period=period2),
              datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# get financial and cash flow data through yfinance
def get_financial_data(ticker_info, document_type:str, period='annual'):

    if document_type == 'financial':

        if period == 'annual':
            df = ticker_info.financials
            df.columns = df.columns.year

        else:
            df = ticker_info.quarterly_financials
            col_names = [f'Q{q} {year}' for q, year in zip(df.columns.quarter, df.columns.year)]
            df.columns = col_names

    else: # cash flow data
        if period == 'annual':
            df = ticker_info.cash_flow
            df.columns = df.columns.year

        else:
            df = ticker_info.quarterly_cashflow
            col_names = [f'Q{q} {year}' for q, year in zip(df.columns.quarter, df.columns.year)]
            df.columns = col_names

    return df

def subset_cash_flow_data(df):
  #Extract variable used in analysis
  prefixes = ['Cash Flow','Free Cash']
  vars_cat = [var for var in df.index if var.startswith(tuple(prefixes))]

  #subset a dataset
  df = df.loc[vars_cat, :]

  # shorten the index name
  df.rename(index=lambda x: x.replace('Cash Flow From Continuing ' ,'').replace('Activities',''), inplace=True)

  return df

def subset_financial_data(df):
    # extract variables from financial data for later analysis
    vars_cat = ['Total Revenue', 'Net Income Continuous Operations']

      #subset a dataset
    df = df.loc[vars_cat, :]

    # rename index
    df.rename(index=lambda x: x.replace('Net Income Continuous Operations' ,'Earnings').replace('Total',''), inplace=True)

    return df

# get the latest news through yfinance
# @st.cache_data
def get_financial_news(ticker_info):

    return ticker_info.news


def add_scroll_button(navigation_target: str):
    return st.markdown(f'''
                    <div class="custom-button">
            <a target="_self" href="{navigation_target}">
                <button>
                    <i class="fas fa-chevron-down"></i>
                </button>
            </a>
            <br>
        </div>
            ''', unsafe_allow_html=True)


