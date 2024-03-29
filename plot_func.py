import datetime
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

# def plot_candle_chart(fig, df_1yr, df_max, current_time, colorblind=False):
def plot_candle_chart(fig, df, name, current_time,colorblind=False):

    if name == '1M':
        visible = True
    else:
        visible = False

    # Add Traces
    fig.add_trace(
        go.Candlestick(x=df.index,
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'],
                        name=f'Candle_{name}',
                        visible = visible,
                        ),
                        )

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
                    dict(label="<b>1M</b>",
                        method="update",
                        args=[ {"visible": [True,False,False,False,False]}],
                        ),
                    dict(label="<b>3M</b>",
                        method="update",
                        args=[ {"visible": [False, True,False,False,False]}],
                        ),
                    dict(label="<b>1Y</b>",
                        method="update",
                        args=[ {"visible": [False, False,True,False,False]}],
                        ),
                    dict(label="<b>3Y</b>",
                        method="update",
                        args=[ {"visible": [False, False,False,True,False]}],
                        ),
                    dict(label="<b>MAX</b>",
                        method="update",
                        args=[{"visible": [False, False,False,False,True]}]
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
            font=dict(color='black',size=17),
            xref='x domain',
            x=0.27,
            yref='y domain',
            y=1.18,
            )

    # footer
    data_source = f'<b>Source: <a href="https://www.yahoofinance.com/">Yahoo! Finance </a> Time : {current_time}</b>'

    fig.add_annotation(
            showarrow=False,
            text=data_source,
            font=dict(color='black',size=15),
            xref='x domain',
            x=0.0,
            yref='y domain',
            y=-0.4
            )

    return fig

def change_candlestick_color(fig):

    for i in range(len(fig.data)):
        fig.data[i].increasing.line.color='steelblue'
        fig.data[i].decreasing.line.color='darkorange'

    return fig

def plot_bar_chart(df, title, y_axis_title, color_discrete_sequence = ['#7E909A', '#A5D8DD', '#0091D5','#1C4E80'], categoryorder='total descending',barmode='group', data_source=False):

    fig = px.bar(df, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(title = f'<b>{title}</b>',
                      xaxis = dict(title='',
                                   tickfont = dict(size=16),
                                   tickangle=45,
                                   categoryorder=categoryorder),
                      yaxis = dict(title = y_axis_title,
                                   tickfont = dict(size=16),
                                   showgrid=True,
                                   gridwidth=1,
                                   gridcolor='grey'),
                      font = dict(size=17),
                      legend = dict(title_text = '',
                                    font = dict(size=16)),
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      barmode=barmode,
                      margin=dict(b=100))

    if data_source !=False:
        fig.add_annotation(
            showarrow=False,
            text=data_source,
            font=dict(color='black',size=15),
            xref='x domain',
            x=0.0,
            yref='y domain',
            y=-0.3
            )


    return fig

def plot_scatter(df, title, color_discrete_sequence = ['rgba(204, 204, 204, 0.95)', 'rgba(98,98,226,0.5)'], data_source=False):

    fig =px.scatter(df, color_discrete_sequence=color_discrete_sequence)

    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))
    fig.update_layout(xaxis_type='category')
    fig.update_layout(title= f'<b>{title}<b>',
                      xaxis=dict(title='',
                                 tickfont = dict(size=16),
                                 tickangle=45,
                                 showgrid=False,
                                 zeroline=True
                                ),
                      yaxis = dict(title='',
                                   tickfont = dict(size=16),
                                   showgrid=True,
                                   gridwidth=1,
                                   gridcolor='grey'),
                      yaxis_tickprefix = '$',
                      font = dict(size=17),
                      legend = dict(title_text ='',
                                  font = dict(size=16)),
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      margin=(dict(b=100)))

    if data_source !=False:
        fig.add_annotation(
                showarrow=False,
                text=data_source,
                font=dict(color='black',size=15),
                xref='x domain',
                x=0.0,
                yref='y domain',
                y=-0.3
                )

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
    font_size=11,
    )

    data_source='<b>Source: <a href="https://ir.tesla.com/sec-filings">Tesla SEC filings</a></b>'

    fig.add_annotation(
        showarrow=False,
        text=data_source,
        font=dict(color='black',size=14),
        xref='x domain',
        x=0.0,
        yref='y domain',
        y=-0.25
        )

    return fig

def plot_choropleth(df, data_source):

    fig = px.choropleth(df,
                        locations='state',
                        locationmode='USA-states',
                        color="category",
                        color_discrete_map={
                            '0': '#fffcfc',
                            '1 - 20' : '#fff0f0',
                            '21 - 40' : '#ffdbdb',
                            '41 - 60' : '#ffbaba',
                            '61 - 80' : '#ff9e9e',
                            '81 - 100' : '#ff7373',
                            '101 - 150' : '#ff4d4d',
                            '151 and higher' : '#ff0d0d'
                            },
                        category_orders={
                        'category' : [
                            '0',
                            '1 - 20',
                            '21 - 40',
                            '41 - 60',
                            '61 - 80',
                            '81 - 100',
                            '101 - 150',
                            '151 and higher'
                        ]
                        },
                        animation_frame='Year',
                        scope='usa',
                        basemap_visible=True,
                        title='<b>Supercharger Stations in United States</b>',
                        labels={'cum_sum' : 'Number of stations',
                                'category' : 'Category'},
                        hover_name='state',
                        hover_data={
                            'cum_sum' : True,
                            'count' : False,
                            'Year': False
                        },
                        height=600,
                        width=900,
                        )

    # Adjust map layout stylings
    fig.update_layout(
        showlegend=True,
        legend_title_text='<b>Total Number of Stations</b>',
        font=dict(size= 14, color= 'black'),
        margin={"r":0,"t":40,"l":0,"b":200},
        legend=dict(orientation='v'),
        geo_bgcolor = 'rgba(0,0,0,0)'
    )

    # Adjust map geo options
    fig.update_geos(showlakes=True, lakecolor="lightskyblue",
                    subunitcolor='black')

    if data_source !=False:
        fig.add_annotation(
                showarrow=False,
                text=data_source,
                font=dict(color='black',size=15),
                xref='x domain',
                x=0.0,
                yref='y domain',
                y=-0.5
                )

    return fig
