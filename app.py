import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import yfinance as yf


import plot_func
import sankey_data
import utils

# Layout-sidebar: displays the headers

st.sidebar.markdown('''
# Sections
:sparkles:[Header 1](#header-1)<br>
[Header 2](#header-2)

''', unsafe_allow_html=True)


# company logo
logo_path = R"./images/Tesla_logo.png"
logo = utils.read_image(logo_path)

st.markdown(
    f'<img src="data:image/gif;base64,{logo}" alt="logo tesla" width="100">',
    unsafe_allow_html=True,
)

# main layout

# header 1
st.header('Header 1', anchor='header-1',divider='blue')

utils.add_scroll_button('#header-2')

# header 2
st.header('Stock price', anchor='header-2', divider='blue')

TICKER = 'TSLA'
TICKER_INFO = yf.Ticker(TICKER)

stock_price_1yr, stock_price_max, current_time = utils.get_stock_price(TICKER_INFO, period1='1y', period2='max')

tab1, tab2 = st.tabs(['Default', 'Colorblind friendly'])

with tab1:
    st.plotly_chart(plot_func.plot_candle_chart(stock_price_1yr,
                                                stock_price_max,
                                                current_time,
                                                colorblind=False),
                    use_container_width=True)

with tab2:
    st.plotly_chart(plot_func.plot_candle_chart(stock_price_1yr,
                                                stock_price_max,
                                                current_time,
                                                colorblind=True),
                    use_container_width=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:18px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)


utils.add_scroll_button('#header-3')

# Header 3
st.header('Financials', anchor='header-3', divider='blue')

cash_flow_yr, cash_flow_q = utils.get_cash_flow_data(TICKER_INFO)
financial_yr, financial_q = utils.get_financial_data(TICKER_INFO)

#Extract variable for cash flow bar plot
prefixes = ['Cash Flow','Free Cash']
vars_cat = [var for var in cash_flow_yr.index if var.startswith(tuple(prefixes))]

# variables for earnigns and Revenue
vars_cat_earning_revenue = ['Net Income Continuous Operations', 'Total Revenue']
fig_cash_flow_yr, fig_cash_flow_q = plot_func.plot_bar_chart(cash_flow_yr, cash_flow_q, vars_cat)

vars_cat = ['Net Income Continuous Operations', 'Total Revenue']
fig_financial_yr, fig_financial_q = plot_func.plot_scatter(financial_yr, financial_q, vars_cat)


tab1, tab2 = st.tabs(["Annual", "Quarterly"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        #### Cash Flow, annual
        st.plotly_chart(fig_cash_flow_yr, theme=None, use_container_width=True)

    with col2:
        #### Revenue & Earnings, annual
        st.plotly_chart(fig_financial_yr, theme=None, use_container_width=True)

with tab2:

    col1, col2 = st.columns(2)

    with col1:
        #### Cash Flow, quartely
        st.plotly_chart(fig_cash_flow_q, theme=None, use_container_width=True)

    with col2:
        #### Revenue & Earnings, quartely
        st.plotly_chart(fig_financial_q, theme=None, use_container_width=True)

utils.add_scroll_button('#header-4')

st.header('Visualize Tesla Income Statement', anchor='header-4', divider='blue')

df, link, report_name = sankey_data.tesla_sankey_data()
st.plotly_chart(plot_func.plot_sankey_diagram(df,link, report_name),use_container_width=True)

st.markdown('''
                    <div class="custom-button">
            <a target="_self" href="#header-1">
                <button>
                    <i class="fas fa-chevron-down"></i>
                </button>
            </a>
        </div>
            ''', unsafe_allow_html=True)

