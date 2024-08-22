import numpy as np
import plotly.graph_objects as go
from scipy import stats
import plotly.express as px
from plotly.subplots import make_subplots
from dash import html

def model_comparison_plot(TEC1, TEC2, TITLES,comp, z):

    y = (TEC2.flatten())[np.logical_not(np.isnan(TEC2.flatten()))]
    x = (TEC1.flatten())[np.logical_not(np.isnan(TEC1.flatten()))]
    fig = make_subplots(cols = 1, rows = 1)

    while len(y) != len(x):
        if len(y)>len(x):
            y = np.delete(y, -1)
        if len(x) > len(y):
            x = np.delete(x, -1)
    x1 =  np.array_split(x, 3)
    y1 =  np.array_split(y, 3)
    for i in range(3):
        x = x1[i]
        y = y1[i]
        a, b = np.polyfit(x, y, 1)
        if i == 0: 
            fig = go.Figure(data=(go.Scatter(
                x=x,
                y=y,
                mode='markers',
                marker=dict(color= z[0],
                        colorscale='Viridis', size=14, colorbar=dict(thickness=20, title='Prob. Distr.'))), go.Scatter(x=(np.arange((np.min(x)-5), (np.max(x)+5))), y=(a*np.arange((np.min(x)-5), (np.max(x)+5))+b))))
        else:
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='markers',
                visible = "legendonly",
                marker=dict(color= z[i], 
                        colorscale='Viridis', size=14, colorbar=dict(thickness=20, title='Prob. Distr.'))))
            fig.add_trace(go.Scatter(x=(np.arange((np.min(x)-5), (np.max(x)+5))), y=(a*np.arange((np.min(x)-5), (np.max(x)+5))+b), visible = "legendonly",))

    fig.update_traces(marker=dict(size=4), line={'width': 4, 'color': 'black'})
    fig.update_layout(coloraxis_colorbar_title_text = 'Probability Distribution')
    fig.update_yaxes(title=TITLES[comp], showline=True, linewidth=2, linecolor='black', mirror=True, title_standoff = 4)
    fig.update_xaxes(title_text=TITLES[0],  showline=True, linewidth=2, linecolor='black', mirror=True)


    buttons=list([
        dict(args=[{'visible': [True, True, False, False, False, False]}, 
                   {'title':TITLES[comp]+'Quiet'}], label="Quiet", method="update"),
        dict(args=[{'visible': [False, False, True, True, False, False]}, 
                   {'title':TITLES[comp]+'Main'}], label="Main", method="update"),
        dict(args=[{'visible': [False, False, False, False, True, True]}, 
                   { 'title':TITLES[comp]+'Recovery'}], label="Recovery", method="update")
    ])

    fig.update_layout(showlegend=False, title = TITLES[comp]+'Quiet', title_x=0.5,
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"l": 10, "t": 10},
                showactive=True,
                x=-0.15,
                xanchor="left",
                y=1.3, 
                yanchor="top"
                )])

    return fig

#model_comparison_plot(pic, pic2,'GloTEC ', dataz)
