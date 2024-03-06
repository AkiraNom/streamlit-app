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
            # pre-processing data structure, data type
            df = pre_processing_annual_data(df)

        else:
            df = ticker_info.quarterly_financials
            # pre-processing data structure, data type
            df = pre_processing_quarterly_data(df)

    else: # cash flow data
        if period == 'annual':
            df = ticker_info.cash_flow
            # pre-processing data structure, data type
            df = pre_processing_annual_data(df)

        else:
            df = ticker_info.quarterly_cashflow
            # pre-processing data structure, data type
            df = pre_processing_quarterly_data(df)

    return df

def pre_processing_annual_data(df):

    df.columns.name = 'Period'
    df = df.transpose()
    df = df.reset_index()
    df['Period']=df['Period'].dt.year.astype(str)
    df=df.set_index('Period')
    df = df.iloc[::-1]

    return df

def pre_processing_quarterly_data(df):

    df.columns.name = 'Period'
    df = df.transpose()
    df = df.reset_index()
    df['Period']=df['Period'].dt.to_period('Q').astype(str).str.replace('Q',' Q')
    df=df.set_index('Period')
    df = df.iloc[::-1]

    return df


def subset_cash_flow_data(df):
  #Extract variable used in analysis
  prefixes = ['Cash Flow','Free Cash']
  vars_cat = [var for var in df.columns if var.startswith(tuple(prefixes))]

  #subset a dataset
  df = df.loc[:,vars_cat]

  # shorten the index name
  df.rename(columns=lambda x: x.replace('Cash Flow From Continuing ' ,'').replace('Activities',''), inplace=True)

  # set data type as int
  df = df.astype('Int64')

  return df

def subset_financial_data(df):
    # extract variables from financial data for later analysis
    vars_cat = ['Total Revenue', 'Net Income Continuous Operations']

      #subset a dataset
    df = df.loc[:,vars_cat]

    # rename index
    df.rename(columns=lambda x: x.replace('Net Income Continuous Operations' ,'Earnings').replace('Total',''), inplace=True)

    # set data type as int
    df = df.astype('Int64')

    return df

# get sales data
def get_sales_data(file_path):

    return pd.read_csv(file_path)

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

# navigate to the top
def add_top_button(navigation_target: str):
    return st.markdown(f'''
                    <div class="custom-button">
            <a target="_self" href="{navigation_target}">
                <button>
                    <i class="fas fa-chevron-up"></i>
                </button>
            </a>
            <br>
        </div>
            ''', unsafe_allow_html=True)
