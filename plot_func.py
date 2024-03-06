
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

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
        height=700,
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

def plot_bar_chart(df, title, y_axis_title, categoryorder='total descending',barmode='group'):

    color_discrete_sequence = ['#7E909A', '#A5D8DD', '#0091D5','#1C4E80']

    fig = px.bar(df, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(title = f'<b>{title}</b>',
                      xaxis = dict(tickfont = dict(size=16),
                                  tickangle=45,
                                  categoryorder=categoryorder),
                      yaxis = dict(title = y_axis_title,
                                   tickfont = dict(size=16),
                                   showgrid=True,
                                   gridwidth=1,
                                   gridcolor='grey'),
                      font = dict(size=17),
                      legend = dict(font = dict(size=16)),
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      barmode=barmode)

    return fig

def plot_scatter(df, title):

    colors = ['rgba(204, 204, 204, 0.95)', 'rgba(98,98,226,0.5)']

    fig =px.scatter(df,
                    color_discrete_sequence=colors
                    )

    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))
    fig.update_layout(xaxis_type='category')
    fig.update_layout(title= f'<b>{title}<b>',
                    xaxis=dict(tickfont = dict(size=16),
                                tickangle=45,
                                showgrid=False,
                                zeroline=True,
                                ),
                    yaxis = dict(tickfont = dict(size=16),
                                    showgrid=True,
                                    gridwidth=1,
                                    gridcolor='grey'),
                    yaxis_tickprefix = '$',
                    font = dict(size=17),
                    legend = dict(font = dict(size=16)),
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)',)

    return fig


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

    note = f'Source:<a href="https://www.sec.gov/"">The SEC</a>  Data: <a href=link>{report_name}</a>'
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


