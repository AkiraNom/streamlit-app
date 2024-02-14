
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

def plot_candle_chart(df):

  # roughly 250 trading days in one year
  yr = 250

  fig = go.Figure()

  # Add Traces
  fig.add_trace(
      go.Candlestick(x=df.index[-yr:],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Candle_1y',
                    visible = True
                    ))

  fig.add_trace(
      go.Candlestick(x=df.index[-yr*2:],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Candle_2y',
                    visible = False
                    ))

  fig.add_trace(
      go.Candlestick(x=df.index[-yr*5:],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Candle_5y',
                    visible = False
                    ))

  fig.add_trace(
      go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Candle_max',
                    visible = False
                    ))



  fig.update_layout(
      updatemenus=[
          dict(
              type="buttons",
              direction="right",
              active=0,
              x=0.57,
              y=1.2,
              buttons=[
                  dict(label="1yr",
                      method="update",
                      args=[{"visible": [True,False,False,False]}],
                      ),
                  dict(label="2yr",
                      method="update",
                      args=[{"visible": [False,True,False,False]}],
                      ),
                  dict(label="5yr",
                      method="update",
                      args=[{"visible": [False,False,True,False]}],
                      ),
                  dict(label="Max",
                      method="update",
                      args=[{"visible": [False,False,False,True]}]
                      ),
                  ]
              )
          ]
      )

  return fig

def plot_bar_chart(df_yr, df_q, vars_cat, document='Cash Flow'):

  fig_yr = go.Figure()
  fig_q = go.Figure()

  for var_cat in vars_cat:
    if 'Cash Flow' in var_cat:
      name = var_cat.replace('Cash Flow From Continuing ' ,'')
      name = name.replace('Activities','')
    elif 'Total' in var_cat:
      name = var_cat.replace('Total ', '')
    else:
      name = var_cat.replace('Net Income Continuous Operations','Earnings')


    fig_yr.add_trace(go.Bar(name = name,
                            x=df_yr.columns,
                            y=df_yr.loc[var_cat,:]))

    fig_q.add_trace(go.Bar(name = name,
                            x=df_q.columns,
                            y=df_q.loc[var_cat,:]))

  fig_yr.update_layout(xaxis={'categoryorder':'total descending'})
  fig_q.update_layout(xaxis={'categoryorder':'total ascending'})

  # place the legend horizontally
  fig_yr.update_layout(legend=dict(
                                orientation="h",
                                entrywidth=100,
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1),
                        margin=dict(
                                l=50,
                                r=50,
                                b=30,
                                t=30,
                                pad=4
    ),)

  fig_q.update_layout(legend=dict(
                              orientation="h",
                              entrywidth=100,
                              yanchor="bottom",
                              y=1.02,
                              xanchor="right",
                              x=1),
                        margin=dict(
                              l=50,
                              r=50,
                              b=30,
                              t=30,
                              pad=4
    ))


  return fig_yr, fig_q

def plot_scatter(df_yr, df_q, vars_cat):

  fig_yr = go.Figure()
  fig_q = go.Figure()

  colors = ['rgba(204, 204, 204, 0.95)', 'rgba(98,98,226,0.5)']


  for var_cat, color in zip(vars_cat, colors):
    if 'Total' in var_cat:
      name = var_cat.replace('Total ', '')
    else:
      name = var_cat.replace('Net Income Continuous Operations','Earnings')

    fig_yr.add_trace(go.Scatter(name = name,
                            x=df_yr.columns,
                            y=df_yr.loc[var_cat,:],
                            marker=dict(color=color, line_color=color),
                            mode='markers'))

    fig_q.add_trace(go.Scatter(name = name,
                            x=df_q.columns,
                            y=df_q.loc[var_cat,:],
                            marker=dict(color=color, line_color=color),
                            mode='markers'))

    fig_yr.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

    fig_q.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

  return fig_yr, fig_q

def plot_sankey_diagram(df, link, report_name):

  link = dict(source = df['source'],
              target = df['target'],
              value = df['value'],
              color=df['link_colors'])

  node = dict(label = df['label'],
              x = df['x'],
              y =df['y'] ,
              color=df['colors'],
              pad=20,
              thickness=10)

  data = go.Sankey(link = link, node=node)

  # plot
  fig = go.Figure(data)
  fig.update_layout(
  title_text=report_name,
  font_family="Arial Black",
  font_color="Black",
  font_size=11,)

  note = f'Source:<a href="https://www.sec.gov/"">The SEC</a> Data: <a href=link>{report_name}</a>'
  fig.add_annotation(
      showarrow=False,
      text=note,
      font=dict(size=10),
      xref='x domain',
      x=0.0,
      yref='y domain',
      y=-0.2
      )

  return fig
