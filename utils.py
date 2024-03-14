import base64
import datetime
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

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
@st.cache_data
def fetch_stock_price(ticker_info, period1='1y', period2='max'):

      return (ticker_info.history(period=period1),
              ticker_info.history(period=period2),
              datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# get financial and cash flow data through yfinance
@st.cache_data
def fetch_financial_data(ticker_info, document_type:str, period='annual'):

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
    df.columns = pd.DatetimeIndex(df.columns).year.astype(str)
    df = df.transpose()
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
@st.cache_data(ttl=72000)
def read_sales_data(file_path):

    df = pd.read_csv(file_path)
    df = df.set_index('Date')

    return df

# image gallery for tesla model Y
def image_slideshow():
    '''
    The codes originate from https://discuss.streamlit.io/t/automatic-slideshow/38342
    by TomJohn
    '''
    return components.html("""
      <!DOCTYPE html>
      <html>
      <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
      * {box-sizing: border-box;}
      body {font-family: Verdana, sans-serif;}
      .mySlides {display: none;}
      img {vertical-align: middle;}

      /* Slideshow container */
      .slideshow-container {
        max-width: 1000px;
        position: relative;
        margin: auto;
      }

      /* The dots/indicators */
      .dot {
        height: 15px;
        width: 15px;
        margin: 0 2px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        transition: background-color 0.6s ease;
      }

      .active {
        background-color: #717171;
      }

      /* Fading animation */
      .fade {
        animation-name: fade;
        animation-duration: 1.5s;
      }

      @keyframes fade {
        from {opacity: .4}
        to {opacity: 1}
      }

      /* On smaller screens, decrease text size */
      @media only screen and (max-width: 300px) {
        .text {font-size: 11px}
      }
      </style>
      </head>
      <body>

      <div class="slideshow-container">

      <div class="mySlides fade">
        <img src="https://www.tesla.com/ownersmanual/images/GUID-1F2D8746-336F-4CF9-9A04-F35E960F31FE-online-en-US.png" style="width:100%; height:100%", >
      </div>

      <div class="mySlides fade">
        <img src="https://digitalassets.tesla.com/tesla-contents/image/upload/f_auto,q_auto/Model-Y-Range-Desktop-LHD.jpg" style="width:100%; height:100%">
      </div>

      <div class="mySlides fade">
        <img src="https://digitalassets.tesla.com/tesla-contents/image/upload/f_auto,q_auto/Model-Y-Cabin-Desktop-LHD.jpg" style="width:100%; height:100%">
      </div>

      </div>
      <br>

      <div style="text-align:center">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </div>

      <script>
      let slideIndex = 0;
      showSlides();

      function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        let dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}
        for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";
        dots[slideIndex-1].className += " active";
        setTimeout(showSlides, 2000); // Change image every 2 seconds
      }
      </script>

      </body>
      </html>

      """,
    height=500,
)

def subset_EV_company(df, top=5):
    # select top n companies
    sales_rank = df.iloc[-1,:].rank(ascending=False).astype(int) <= top
    df = df.loc[:, sales_rank]

    return df

@st.cache_data(ttl=72000)
def load_station_data(path_station):
  return pd.read_json(path_station)

def pre_processing_station_data(df):

    # expand dictionary data in column values
    df_address = df['address'].apply(pd.Series)
    df_gps = df['gps'].apply(pd.Series)

    # merge all data frames
    df = pd.concat([df, df_address, df_gps],axis=1)

    return df

def subset_station_data(df, country='USA', status='OPEN', otherEVs=False):

    # remove unnessary data
    cols_drop = ['locationId','name','address','gps','elevationMeters',
                'powerKilowatt','solarCanopy', 'battery',
                'statusDays', 'urlDiscuss','hours','street','city'
                ]
    df = df.drop(cols_drop, axis=1)

    # subset, within USA, open station, and tesla charger only
    df = df[df['country']== country]
    df = df[(df['status']== status)]
    df = df[df['otherEVs']== otherEVs]

    # add year info
    df.loc[:,'Year'] = pd.to_datetime(df['dateOpened']).dt.year.astype(int)

    return df

def count_station_per_state(df):
    # calculate cumulative sum
    df = df.groupby(['state','Year'])['id'].count().sort_values(ascending=True).reset_index()
    df = df.rename(columns={'id':'count'})

    return df

def deal_missing_year(df):
    # fill missing year in the dataset
    first_year = df['Year'].min()
    last_year = df['Year'].max()

    years = list(range(first_year, last_year+1))
    states = df['state'].unique().tolist()

    # create a new multiindex covering all possible state * yeaer combinations
    new_index = pd.MultiIndex.from_product([states, years], names=['state', 'Year'])

    df = df.set_index(['state', 'Year'])
    df = df.reindex(new_index, fill_value=0)
    df = df.reset_index()

    # change year type to str otherwise animation displayes float-like value
    df['Year'] = df['Year'].astype(str)

    return df

def calc_cumulative_sum(df):

    df['cum_sum'] = df.groupby(['state'])['count'].cumsum()

    return df

def set_sataion_cat(row):
  if row['cum_sum'] == 0:
      return '0'
  if row['cum_sum'] > 0 and row['cum_sum'] <= 20:
      return '1 - 20'
  if row['cum_sum'] > 20 and row['cum_sum'] <= 40:
      return '21 - 40'
  if row['cum_sum'] > 40 and row['cum_sum'] <= 60:
      return '41 - 60'
  if row['cum_sum'] > 60 and row['cum_sum'] <= 80:
      return '61 - 80'
  if row['cum_sum'] > 80 and row['cum_sum'] <= 100:
      return '81 - 100'
  if row['cum_sum'] > 100 and row['cum_sum'] <= 150:
      return '101 - 150'
  if row['cum_sum'] > 150:
      return '151 and higher'

def add_category_to_timeframe(df):
  # Adds all available categories to each time frame
  # https://plotly.com/python/animations/#current-animation-limitations-and-caveats
  catg = df['category'].unique()
  dts = df['Year'].unique()

  columns = ['Year','cum_sum','category']

  for tf in dts:
      for i in catg:
          df_append = pd.DataFrame({
              'Year' : [tf],
              'cum_sum' : 'N',
              'category' : [i]
              }, columns = columns)
          df = pd.concat([df, df_append], ignore_index=True, axis=0)

  return df


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

def local_css(path):
  with open(path) as f:
      css = f.read()

  return st.markdown(f'<style>{css}</style>',
                     unsafe_allow_html=True)
