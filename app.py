import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components
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

st.empty()
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

df_cash_flow_yr = (utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='annual')
                   .pipe(utils.subset_cash_flow_data)
                   )
df_cash_flow_q = (utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='quarterly')
                  .pipe(utils.subset_cash_flow_data)
                  )
df_financial_yr = (utils.get_financial_data(TICKER_INFO, document_type='financial', period='annual')
                   .pipe(utils.subset_financial_data)
                   )
df_financial_q = (utils.get_financial_data(TICKER_INFO, document_type='financial', period='quarterly')
                  .pipe(utils.subset_financial_data)
                  )

# plot cash flow graph
fig_cash_flow_yr = plot_func.plot_bar_chart(df=df_cash_flow_yr,
                                            title='Cash Flow',
                                            y_axis_title='Balance ($)')

fig_cash_flow_q = plot_func.plot_bar_chart(df=df_cash_flow_q,
                                           title='Cash Flow',
                                           y_axis_title='Balance ($)',
                                           categoryorder='category ascending'
                                           )

#plot earnings and revenue graph
fig_financial_yr = plot_func.plot_scatter(df_financial_yr,
                                          title = 'Revenue & Earnings')

fig_financial_q = plot_func.plot_scatter(df_financial_q,
                                         title = 'Revenue & Earnings')

tab1, tab2 = st.tabs(["Annual", "Quarterly"])

st.empty()
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        #### Cash Flow, annual
        st.empty()
        st.plotly_chart(fig_cash_flow_yr, theme=None, use_container_width=True)

    with col2:
        #### Revenue & Earnings, annual
        st.empty()
        st.plotly_chart(fig_financial_yr, theme=None, use_container_width=True)

with tab2:

    col1, col2 = st.columns(2)

    with col1:
        #### Cash Flow, quartely
        st.empty()
        st.plotly_chart(fig_cash_flow_q, theme=None, use_container_width=True)

    with col2:
        #### Revenue & Earnings, quartely
        st.empty()
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
st.empty()
st.plotly_chart(plot_func.plot_sankey_diagram(df,link, report_name),use_container_width=True)

utils.add_scroll_button('#header-4')

#############################
# Header 4
st.header('Tesla EV sales', anchor='header-4', divider='blue')

path_model_data = './data/EV_sales_by_model.csv'
df_model = utils.get_sales_data(path_model_data)

fig_model = plot_func.plot_bar_chart(df=df_model,
                                     title = 'EV models',
                                     y_axis_title='Vehicle delivery',
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     )

path_country_data = './data/EV_sales_by_country.csv'
df_country = utils.get_sales_data(path_country_data)

fig_country = plot_func.plot_bar_chart(df=df_country,
                                     title = 'EV sales by country',
                                     y_axis_title='Vehicle delivery',
                                     color_discrete_sequence = ['#1C4E80','#0091D5','#7E909A'],
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     )
tab1, tab2 = st.tabs(['Model','Country'])

st.empty()
with tab1:
    col1, col2 = st.columns((2,1))

    with col1:
        st.empty()
        st.plotly_chart(fig_model, theme=None, use_container_width=True)
    with col2:

        st.markdown('''<div class='model_title'>
                    <h3>Tesla Model Y</h3>
                    ''', unsafe_allow_html=True)
        utils.image_slideshow()



with tab2:
    col1, col2 = st.columns((2,1))

    with col1:
        st.empty()
        st.plotly_chart(fig_country, theme=None, use_container_width=True)
    with col2:

        st.markdown(f'''<div class="market-description">
                    <br>
                    <br>
                    <h3>Increasing Sales in <span>China</span></h3>
                        <p>
                            Since 2020, Tesla’s sales in China have been strong
                            after its introduction from the Shanghai Gigafactory.
                            <span>China</span> represents a large portion of global
                            sales underlying an important market for Tesla.
                    </p>
                    <br>
                    </div>
                    ''', unsafe_allow_html=True)

utils.add_scroll_button('#header-5')

#############################
# Header 5
st.header('Other EV companies', anchor='header-5', divider='blue')

path_share_data = './data/EV_share.csv'
df_share_subset = (utils.get_sales_data(path_share_data)
                   .pipe(utils.subset_EV_company))

# df_share_subset = utils.subset_EV_company(df_share)

fig_share= plot_func.plot_bar_chart(df=df_share_subset,
                                     title = 'TOP 5 EV companies',
                                     y_axis_title='Vehicle delivery',
                                     color_discrete_sequence = ['#1C4E80', '#0091D5', '#A5D8DD', '#7E909A', '#BEC7CC'],
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     )

col1, col2 = st.columns((2,1))

st.empty()
with col1:
    st.empty()
    st.plotly_chart(fig_share, theme=None, use_container_width=True)

with col2:
    st.markdown(f'''<div class="share-description">
            <br>
            <br>
            <br>
            <br>
            <h3> <span>Tesla</span> leading the EV market</h3>
                <p> In the fourth quater of 2023, Tesla accounts for about 56% of all battery EV sales in US,
                showing the strong share in the market.
            </p>
            <br>
            </div>
            ''', unsafe_allow_html=True)

utils.add_scroll_button('#header-6')


#############################
# Header 6
st.header('Investment on Charging Station across US', anchor='header-6', divider='blue')

path_station = './data/charge_station.json'
df_station = (pd.read_json(path_station)
              .pipe(utils.pre_processing_station_data)
              .pipe(utils.subset_station_data)
              .pipe(utils.count_station_per_state)
              .pipe(utils.deal_missing_year)
              .pipe(utils.calc_cumulative_sum)
              )
df_station = (df_station.assign(category=df_station.apply(utils.set_sataion_cat, axis=1))
              .pipe(utils.add_category_to_timeframe)
              )

fig_station = plot_func.plot_choropleth(df_station)

col1, col2 = st.columns((2,1))

with col1:

    st.plotly_chart(fig_station, theme=None, use_container_width=True)

with col2:

    st.markdown(f'''<div class="station-description">
        <br>
        <br>
        <br>
        <br>
        <h3> <span>Tesla</span> Expandng the Supercharger Station</h3>
            <p> Tesla is investing to expand electric vehicle charging
            infrastructure in the US
        </p>
        <br>
        </div>
        ''', unsafe_allow_html=True)

# utils.add_scroll_button('#header-')

#############################
# Header
# st.header('', anchor='header-', divider='blue')

# utils.add_scroll_button('#header-')
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
