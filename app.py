import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import yfinance as yf

st.set_page_config(
    page_title='Tesla Analysis App',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={'About': '''Add description here'''}
)

import css
import plot_func
import sankey_data
import utils


##############################
# main page layout

# company logo
logo_path = R"./images/Tesla_logo.png"
logo = utils.read_image(logo_path)

st.header('', anchor='top-header')
# st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

st.markdown(
    f'<img src="data:image/gif;base64,{logo}" alt="logo tesla" width="60" height="500" class="logo">',
    unsafe_allow_html=True,
)

st.markdown(f'''<div class="top-page">
                <p>
                    Tesla.Inc was founded in San Carlos, California in 2003 by <i> Martin Eberhard </i>
                    and <i>Marc Tarpenning </i> and currently led by <span><i> Elon Musk</i></span>.
                    In 2021, he decided to move its headquater for the company to Austin, Texas.
                    Tesla designs, manufactures and sells electric vehicles, stationary battery energy storage devices
                    from home to grid-scale, solar panels and solar shingles, and related products and services
            </p>
            <br>
            </div>
            ''', unsafe_allow_html=True)

utils.tesla_html_link()

utils.add_scroll_button('#header-1')

###########################################################
# header 1
st.header('Stock price', anchor='header-1', divider='blue')

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


utils.add_scroll_button('#header-2')

#########################################
# Header 2
st.header('Financials', anchor='header-2', divider='blue')

df_cash_flow_yr = utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='annual')
df_cash_flow_q = utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='quarterly')
df_financial_yr = utils.get_financial_data(TICKER_INFO, document_type='financial', period='annual')
df_financial_q = utils.get_financial_data(TICKER_INFO, document_type='financial', period='quarterly')

#Extract variable for cash flow bar plot
df_cash_flow_yr_subset = utils.subset_cash_flow_data(df_cash_flow_yr)
df_cash_flow_q_subset = utils.subset_cash_flow_data(df_cash_flow_q)

# plot cash flow graph
fig_cash_flow_yr = plot_func.plot_bar_chart(df=df_cash_flow_yr_subset,
                                            title='Cash Flow',
                                            y_axis_title='Balance ($)')

fig_cash_flow_q = plot_func.plot_bar_chart(df=df_cash_flow_q_subset,
                                           title='Cash Flow',
                                           y_axis_title='Balance ($)',
                                           categoryorder='category ascending'
                                           )

# variables for earnigns and Revenue
df_financial_yr_subset = utils.subset_financial_data(df_financial_yr)
df_financial_q_subset = utils.subset_financial_data(df_financial_q)

#plot earnings and revenue graph
fig_financial_yr = plot_func.plot_scatter(df_financial_yr_subset,
                                          title = 'Revenue & Earnings')

fig_financial_q = plot_func.plot_scatter(df_financial_q_subset,
                                         title = 'Revenue & Earnings')

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

## css for font size in the tab
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

utils.add_scroll_button('#header-3')

##############################
# Header 3
st.header('Visualize Income Statement', anchor='header-3', divider='blue')

df, link, report_name = sankey_data.tesla_sankey_data()
st.plotly_chart(plot_func.plot_sankey_diagram(df,link, report_name),use_container_width=True)

utils.add_scroll_button('#header-4')

#############################
# Header 4
st.header('Tesla EV sales', anchor='header-4', divider='blue')

df_model = utils.get_sales_data('./data/EV_sales_by_model.csv')
df_model = df_model.set_index('Date')

fig_model = plot_func.plot_bar_chart(df=df_model,
                                     title = 'EV models',
                                     y_axis_title='Vehicle delivery',
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     )



df_country = utils.get_sales_data('./data/EV_sales_by_country.csv')
df_country = df_country.set_index('Date')

fig_country = plot_func.plot_bar_chart(df=df_country,
                                     title = 'EV sales by country',
                                     y_axis_title='Vehicle delivery',
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     )
tab1, tab2 = st.tabs(['Model','Country'])

with tab1:
    col1, col2 = st.columns((2,1))

    with col1:
        st.plotly_chart(fig_model, theme=None, use_container_width=True)
    with col2:
        st.markdown('add description')

with tab2:
    col1, col2 = st.columns((2,1))

    with col1:
        st.plotly_chart(fig_country, theme=None, use_container_width=True)
    with col2:
        st.markdown('add description')






#############################
# Header 5

utils.add_top_button('#top-header')

###########################
# Layout-sidebar: displays the headers

## FIX the sidebar
# 1. Title : table of contents, center alighnment
# 2. list the header link, left alighnment
# 3.link or add an icon of streamlit, twitter, instagram etc



# st.sidebar.markdown('''<div class="sidebar">
# # Sections
# <p>
# [Company Description](#Top) <br>
# :sparkles:[Stock Price](#header-1)<br>
# [Financial Statement](#header-2) <br>
# [Visualize Income Statement](#header-3) <br>
# </p>
# </div>
# ''', unsafe_allow_html=True)

# st.markdown("""
# <style>
#     [data-testid=stSidebar] {
#         text-align: left
#     }
# </style>
# """, unsafe_allow_html=True)

# st.sidebar.header('Table of Contents')
# st.sidebar.markdown('''
#     [Company Description](#Top)''', unsafe_allow_html=True)
