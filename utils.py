import base64
import datetime
import pandas as pd
import streamlit as st

import yfinance

def read_image(path):
    """image from local file"""

    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    return data_url


# get stock price through yfinance
def get_stock_price(ticker_info, period1='1y', period2='max'):
# obtain last 2 years stock price for plot
# other valid period option: “1d”, “5d”, “1mo”,
#“3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”
      return (ticker_info.history(period=period1),
              ticker_info.history(period=period2),
              datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# get cash flow data through yfinance
def get_cash_flow_data(ticker_info):

    cash_flow_yr = ticker_info.cash_flow
    cash_flow_yr.columns = cash_flow_yr.columns.year

    cash_flow_q = ticker_info.quarterly_cashflow
    col_names = [f'Q{q} {year}' for q, year in zip(cash_flow_q.columns.quarter, cash_flow_q.columns.year)]
    cash_flow_q.columns = col_names

    return cash_flow_yr, cash_flow_q

# get financial data through yfinance
def get_financial_data(ticker_info):

    financial_yr = ticker_info.financials
    financial_yr.columns = financial_yr.columns.year

    financial_q = ticker_info.quarterly_financials
    col_names = [f'Q{q} {year}' for q, year in zip(financial_q.columns.quarter, financial_q.columns.year)]
    financial_q.columns = col_names

    return financial_yr, financial_q


### css for custom-button
st.markdown('''    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha384-..." crossorigin="anonymous">
        <style>
            .custom-button a {
                margin: 0;
                padding: 0;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                text-decoration: none;
            }

            .custom-button button {
                background-color: transparent;
                border: none;
                cursor: pointer;
                font-size: 16px;
                display: inline-block;
            }

            .custom-button button i {
                font-size: 50px;
                margin-right: 8px;
            }

            .custom-button button:hover {
                color: orange;
            }
        </style>

    <div class="custom-button">
        <a target="_self" href="#header-1">
            <button>
                <i class="fas fa-chevron-down"></i>
            </button>
        </a>
    </div>''', unsafe_allow_html=True)



def add_scroll_button(navigation_target: str):
    return st.markdown(f'''
                    <div class="custom-button">
            <a target="_self" href="{navigation_target}">
                <button>
                    <i class="fas fa-chevron-down"></i>
                </button>
            </a>
        </div>
            ''', unsafe_allow_html=True)
