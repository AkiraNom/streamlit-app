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

# TICKER = 'TSLA'
# TICKER_INFO = yf.Ticker(TICKER)

# stock_price_1yr, stock_price_max, current_time = utils.get_stock_price(TICKER_INFO, period1='1y', period2='max')

# tab1, tab2 = st.tabs(['Default', 'Colorblind friendly']
# with tab1:

#     st.plotly_chart(plot_func.plot_candle_chart(stock_price_1yr,
#                                                 stock_price_max,
#                                                 current_time,
#                                                 colorblind=False),
#                     use_container_width=True)

# with tab2:

#     st.plotly_chart(plot_func.plot_candle_chart(stock_price_1yr,
#                                                 stock_price_max,
#                                                 current_time,
#                                                 colorblind=True),
#                     use_container_width=True)


# utils.add_scroll_button('#header-2')

#########################################
# Header 2
st.header('Financials', anchor='header-2', divider='blue')

# df_cash_flow_yr = (utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='annual')
#                    .pipe(utils.subset_cash_flow_data)
#                    )
# df_cash_flow_q = (utils.get_financial_data(TICKER_INFO, document_type='cash flow', period='quarterly')
#                   .pipe(utils.subset_cash_flow_data)
#                   )
# df_financial_yr = (utils.get_financial_data(TICKER_INFO, document_type='financial', period='annual')
#                    .pipe(utils.subset_financial_data)
#                    )
# df_financial_q = (utils.get_financial_data(TICKER_INFO, document_type='financial', period='quarterly')
#                   .pipe(utils.subset_financial_data)
#                   )

# # plot cash flow graph
# fig_cash_flow_yr = plot_func.plot_bar_chart(df=df_cash_flow_yr,
#                                             title='Cash Flow',
#                                             y_axis_title='Balance ($)',
#                                             data_source = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a></b>')

# fig_cash_flow_q = plot_func.plot_bar_chart(df=df_cash_flow_q,
#                                            title='Cash Flow',
#                                            y_axis_title='Balance ($)',
#                                            categoryorder='category ascending',
#                                            data_source = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a></b>'
#                                            )

# #plot earnings and revenue graph
# fig_financial_yr = plot_func.plot_scatter(df_financial_yr,
#                                           title = 'Revenue & Earnings',
#                                           data_source = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a></b>')

# fig_financial_q = plot_func.plot_scatter(df_financial_q,
#                                          title = 'Revenue & Earnings',
#                                          data_source = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a></b>')

# tab1, tab2 = st.tabs(["Annual", "Quarterly"])


# with tab1:
#     col1, col2 = st.columns(2)

#     with col1:
#         #### Cash Flow, annual
#         st.plotly_chart(fig_cash_flow_yr, theme=None, use_container_width=True)

#     with col2:
#         #### Revenue & Earnings, annual
#         st.plotly_chart(fig_financial_yr, theme=None, use_container_width=True)

# with tab2:

#     col1, col2 = st.columns(2)

#     with col1:
#         #### Cash Flow, quartely
#         st.plotly_chart(fig_cash_flow_q, theme=None, use_container_width=True)

#     with col2:
#         #### Revenue & Earnings, quartely
#         st.plotly_chart(fig_financial_q, theme=None, use_container_width=True)

# ## css for font size in the tab
# css = '''
# <style>
#     .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
#     font-size:1.5rem;
#     }
# </style>
# '''

# st.markdown(css, unsafe_allow_html=True)

utils.add_scroll_button('#header-3')

##############################
# Header 3
st.header('Visualize Income Statement', anchor='header-3', divider='blue')

df, link, report_name = sankey_data.tesla_sankey_data()

col1, col2 = st.columns((2,1))
with col1:

    st.plotly_chart(plot_func.plot_sankey_diagram(df,link, report_name),use_container_width=True)

with col2:
    st.markdown(f'''<div>
            <br>
            <br>
            <br>
            <h3 style='color:orange;'>Sankey Diagram</h3>
                <p class="sankey-description">
                    Sankey diagram presents an overview of the main money flows through business and
                    how the money is earned and used in each sector.
                </p>
            <br>
            </div>
            ''', unsafe_allow_html=True)
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
                                     data_source='<b>Source: <a href="https://www.visualcapitalist.com/charted-teslas-global-sales-by-model-and-year-2016-2023/">Visual Capitalist</a></b>'
                                     )

path_country_data = './data/EV_sales_by_country.csv'
df_country = utils.get_sales_data(path_country_data)

fig_country = plot_func.plot_bar_chart(df=df_country,
                                     title = 'EV sales by country',
                                     y_axis_title='Vehicle delivery',
                                     color_discrete_sequence = ['#1C4E80','#0091D5','#7E909A'],
                                     categoryorder='total ascending',
                                     barmode='relative',
                                     data_source='<b>Source: <a href="https://ir.tesla.com/sec-filings">Tesla SEC filings</a></b>'
                                     )
tab1, tab2 = st.tabs(['Model','Country'])
with tab1:
    col1, col2 = st.columns((2,1))

    with col1:
        st.plotly_chart(fig_model, theme=None, use_container_width=True)
    with col2:

        st.markdown('''<div class='model_title'>
                    <h4>Tesla Model Y</h4>
                    ''', unsafe_allow_html=True)
        utils.image_slideshow()



with tab2:
    col1, col2 = st.columns((2,1))

    with col1:
        st.plotly_chart(fig_country, theme=None, use_container_width=True)
    with col2:

        st.markdown(f'''<div>
                    <br>
                    <br>
                    <br>
                    <h3>Increasing Sales in <span style='color:orange;'>China</span></h3>
                        <p class="market-description">
                            Since 2020, Tesla&apos;s sales in China have been strong
                            after its introduction from the Shanghai Gigafactory.
                            <span style='color:orange;'>China</span> represents a large portion of global
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
                                     data_source='<b>Source: <a href="https://www.coxautoinc.com/market-insights/q4-2023-ev-sales/">Cox Automotive</a></b>'
                                     )

col1, col2 = st.columns((2,1))
with col1:
    st.plotly_chart(fig_share, theme=None, use_container_width=True)

with col2:
    st.markdown(f'''<div>
            <br>
            <br>
            <br>
            <br>
            <h3> <span style='color:orange;'>Tesla</span> leading the EV market</h3>
                <p  class="share-description"> In the fourth quater of 2023, Tesla accounts for
                about <span style='color:orange; font-weight:bold'>56%</span> of all battery EV sales in US,
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
df_station = (utils.load_station_data(path_station)
              .pipe(utils.pre_processing_station_data)
              .pipe(utils.subset_station_data)
              .pipe(utils.count_station_per_state)
              .pipe(utils.deal_missing_year)
              .pipe(utils.calc_cumulative_sum)
              )
df_station = (df_station.assign(category=df_station.apply(utils.set_sataion_cat, axis=1))
              .pipe(utils.add_category_to_timeframe)
              )

fig_station = plot_func.plot_choropleth(df_station,
                                        data_source='<b>Source: <a href="https://supercharge.info/data">Supercharge.info</a></b>')

col1, col2 = st.columns((2,1))

with col1:

    st.plotly_chart(fig_station, theme=None, use_container_width=True)

with col2:

    st.markdown(f'''<div>
        <br>
        <br>
        <br>
        <br>
        <h3> <span style='color:orange;'>Tesla</span> Expandng the Supercharger Station</h3>
            <p class="station-description"> Tesla is investing to expand EV charging
            infrastructure in the US. Furthermore, it expandes supercharger station to all EV (non-Tesla) cars
            to strength the EV charging network.
        </p>
        <br>
        </div>
        ''', unsafe_allow_html=True)

utils.add_top_button('#top-header')
st.markdown('''<div class="top-button"><a href="#top-header">Back to Top</a> </div>''',
            unsafe_allow_html=True)

###########################
# Layout-sidebar: displays the headers


with st.sidebar:

    st.markdown('''
                <div class="section-list">
                <h2>Table of Contents</h2>
                <a href="#top-header"><span>&#127970;</span>Company description</a> <br>
                <a href="#header-1"><span>&#x1f4c8;</span> Strock Price</a><br>
                <a href="#header-2"><span>&#x1f4b5;</span>Financial Statement</a><br>
                <a href="#header-3"><span>&#x1f4b5;</span>Visuzalise Income Statement</a><br>
                <a href="#header-4"><span>&#128664;</span>Tesla EV Sales</a><br>
                <a href="#header-5"><span>&#127970;</span>Other EV companies</a><br>
                <a href="#header-6"><span>&#9981;</span>Charging Station Map in US</a><br>
                <a href="#top-header"><span>&#10067; </span>FAQ</a> <br>
                <a href="#top-header"><span>&#x2709; </span>Contact</a> <br>
                <a href="#top-header"><span>&#128394; </span>About</a> <br>

                </div>
    ''', unsafe_allow_html=True)


    st.markdown("---")
    st.markdown('''
                <h2>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="20"></a>
                </h2>
        ''',
        unsafe_allow_html=True
    )
st.markdown('''    <style>
        .container {
            height: 10vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container p {
            color: orange;
            margin: 3px
        }


        .container a i::before {
            text-decoration: none;
            font-size: 24px;
            color: #ffffff;
            transition: all 0.3s linear;
            margin-left: 10px;
            margin-right 10px;
        }

        .container a:hover i {
            transform: scale(1.5);
        }

        .youtube:hover i::before {
            color: red;
        }
        .instagram:hover i::before {
            color: #e11d74;
        }
        .linkedin:hover i::before {
            color: #04009a;
        }
    </style>''', unsafe_allow_html=True
    )
with st.sidebar:
    st.markdown('''<div class="container">
            <p>Follow : </p>
            <a class="link linkedin" href="https://www.linkedin.com/company/">
                <i class="fab fa-linkedin-in"></i>
            </a>
            <a class="link instagram" href="https://www.instagram.com/">
                <i class="fab fa-instagram"></i>
            </a>
            <a class="link youtube" href="https://www.youtube.com/">
                <i class="fab fa-youtube"></i>
            </a>
        </div>''', unsafe_allow_html=True)
