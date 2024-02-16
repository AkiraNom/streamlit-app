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

# get company description through yfinance
def button_company_link():
    return st.markdown(f'''
                    <div>
            <a href="https://tesla.com" class="link-button">
                <button>
                    <i class="fas fa-chevron-right"></i>
                </button>
            </a>
        </div>
            ''', unsafe_allow_html=True)


# get stock price through yfinance
def get_stock_price(ticker_info, period1='1y', period2='max'):

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

    ''', unsafe_allow_html=True)

st.markdown('''
            <style>
            .logo {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
            }
            .top-page p{

                font-size: 20px;
                font-weight:bold;
                text-align: center;
            }
            .top-page span {
                color: orange;
            }
            </style>
            ''', unsafe_allow_html=True)


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


def test_button():
    return st.markdown('''
                       <style>
                       .main{
                           width: 80%;
                           height: 100vh;
                           display: flex;
                           justify-content: space-around;
                           align-items: center;
                           margin: 0 auto;
                        }
                    .btn {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-width:220.52px;
                        min-height: 56px;
                        font-family: calibri;
                        border: none;
                        border-radius: 100px;
                        cursor: pointer;
                        font-weight: 400;
                        text-decoration: none;
                        transition: all 0.5s linear;
                        }

                        span {
                            font-size: 30px;
                            font-weight: 700;
                            padding: 0 10px;
                        }

                        ion-icon {
                            font-size: 2em;
                            transition: all 0.5s linear;
                        }

                        .btn:hover ion-icon {
                            transform: rotate(-90deg);

                        }

                        div {
                            position: relative;
                        }

                        .yellow {
                            /* background: #0ebac5; */
                            background: none;
                            color: black;
                        }

                        .yellow::before {
                            content: "";
                            display: block;
                            width: 56px;
                            height: 100%;
                            background-color:#0ebac5;
                            position: absolute;
                            border-radius: 100px;
                            left: 1em;
                            z-index: -1;
                            transition: all 600ms ease;
                        }

                        .yellow:hover::before {
                            width: 100%;
                        }

                        .yellow:hover ion-icon {
                            transform: translateX(10px);
                        }
                    </style>


                       ''', unsafe_allow_html=True)
