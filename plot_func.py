
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

def plot_candle_chart(df_1yr, df_max, current_time, colorblind=False):

    if colorblind:
        increasing_line_color='steelblue'
        increasing_fillcolor='steelblue'
        decreasing_line_color='darkorange'
        decreasing_fillcolor='darkorange'

    else:
        increasing_line_color='green'
        increasing_fillcolor='green'
        decreasing_line_color='red'
        decreasing_fillcolor='red'

    fig = go.Figure()

    # Add Traces
    fig.add_trace(
        go.Candlestick(x=df_1yr.index,
                        open=df_1yr['Open'],
                        high=df_1yr['High'],
                        low=df_1yr['Low'],
                        close=df_1yr['Close'],
                        name='Candle_1y',
                        visible = True,
                        increasing_line_color=increasing_line_color,
                        increasing_fillcolor=increasing_fillcolor,
                        decreasing_line_color=decreasing_line_color,
                        decreasing_fillcolor=decreasing_fillcolor,
                        ),
        #   row=1, col=1,
                        )

    fig.add_trace(
        go.Candlestick(x=df_max.index,
                        open=df_max['Open'],
                        high=df_max['High'],
                        low=df_max['Low'],
                        close=df_max['Close'],
                        name='Candle_max',
                        visible = False,
                        increasing_line_color=increasing_line_color,
                        increasing_fillcolor=increasing_fillcolor,
                        decreasing_line_color=decreasing_line_color,
                        decreasing_fillcolor=decreasing_fillcolor,
                        ))

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                active=0,
                x=0.57,
                y=1.2,
                name='test',
                buttons=[
                    dict(label="<b>1Y</b>",
                        method="update",
                        args=[ {"visible": [True,False]}],

                        ),
                    dict(label="<b>MAX</b>",
                        method="update",
                        args=[{"visible": [False,True]}]
                        ),
                    ],
                font =
                    dict(
                        family='Arial',
                        color = "orange",
                        size = 14,
                        ),
                ),
            ],
        xaxis = dict(tickfont = dict(size=16)),
        yaxis = dict(tickfont = dict(size=16)),
        )

    # add button label
    source_note = '<b>Data Range: </b>'

    fig.add_annotation(
            showarrow=False,
            text=source_note,
            font=dict(color='white',size=17),
            xref='x domain',
            x=0.25,
            yref='y domain',
            y=1.16,
            )



    # footer
    source_note = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a> Time : {current_time} (UTC)</b>'

    fig.add_annotation(
            showarrow=False,
            text=source_note,
            font=dict(color='white',size=15),
            xref='x domain',
            x=0.0,
            yref='y domain',
            y=-0.8
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

    fig_yr.update_layout(title='Cash Flow',
                         xaxis=dict(tickfont = dict(size=16),
                                    tickangle=45,
                                    categoryorder='total descending'),
                         yaxis = dict(tickfont = dict(size=16),
                                      showgrid=True,
                                      gridwidth=1,
                                      gridcolor='grey'),
                         legend = dict(font = dict(size=16)),
                         plot_bgcolor='rgba(0, 0, 0, 0)',
                         paper_bgcolor='rgba(0, 0, 0, 0)',)

    fig_q.update_layout(title='Cash Flow',
                        xaxis=dict(title='Cash Flow',
                                   tickfont = dict(size=16),
                                   tickangle=45,
                                   categoryorder='total ascending'),
                        yaxis = dict(tickfont = dict(size=16),
                                      showgrid=True,
                                      gridwidth=1,
                                      gridcolor='grey'),
                         legend = dict(font = dict(size=16)),
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',)



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
        fig_yr.update_layout(title='Revenue & Earnings',
                             xaxis=dict(tickfont = dict(size=16),
                                        tickangle=45,
                                        showgrid=False,
                                        zeroline=True,
                                        categoryorder='total descending'),
                            yaxis = dict(tickfont = dict(size=16),
                                        showgrid=True,
                                        gridwidth=1,
                                        gridcolor='grey'),
                            legend = dict(font = dict(size=16)),
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',)

        fig_q.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))
        fig_q.update_layout(title='Revenue & Earnings',
                            xaxis=dict(tickfont = dict(size=16),
                                       tickangle=45,
                                       showgrid=False,
                                       zeroline=True,
                                       categoryorder='total ascending'),
                            yaxis = dict(tickfont = dict(size=16),
                                        showgrid=True,
                                        gridwidth=1,
                                        gridcolor='grey'),
                            legend = dict(font = dict(size=16)),
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',)

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
        font=dict(color='white',size=14),
        xref='x domain',
        x=0.0,
        yref='y domain',
        y=-0.25
        )

    return fig


