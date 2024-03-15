import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title='Tesla Analysis App',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={'About': '''Add description here'''}
)

import utils
import page_sections

# main page layout

######## Top page ######################

page_sections.top_page()

utils.add_scroll_button('#header-1')

######### Header 1 #######################

st.header('Stock price', anchor='header-1', divider='blue')

TICKER = 'TSLA'
TICKER_INFO = yf.Ticker(TICKER)
page_sections.stock_price(TICKER_INFO)

utils.add_scroll_button('#header-2')

########## Header 2 ######################

st.header('Financials', anchor='header-2', divider='blue')

page_sections.financials(TICKER_INFO)

utils.add_scroll_button('#header-3')

########## Header 3 ####################
st.header('Visualize Income Statement', anchor='header-3', divider='blue')

page_sections.income_statement()
utils.add_scroll_button('#header-4')

########## Header 4 ###################

st.header('Tesla EV sales', anchor='header-4', divider='blue')

page_sections.ev_sales()

utils.add_scroll_button('#header-5')

########### Header 5 ##################

st.header('Other EV companies', anchor='header-5', divider='blue')

page_sections.ohter_ev_companies()

utils.add_scroll_button('#header-6')


########### Header 6 ##################

st.header('Investment on Charging Station across US', anchor='header-6', divider='blue')

page_sections.charge_station()

utils.add_top_button('#top-header')
st.markdown('''<div class="top-button"><a href="#top-header">Back to Top</a> </div>''',
            unsafe_allow_html=True)

########### Sidebar ################

page_sections.sidebar_contents()
