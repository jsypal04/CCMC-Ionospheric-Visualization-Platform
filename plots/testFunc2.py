import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def rcpm_plot(Alldata, year, observ_type):
    """
    Root-mean squared error, Correlation Coefficient, Standard Deviation, and Mean Error plot. Returns a plotly figure data type.
        Alldata: Data as formatted in data.py
        year: The year of the storm as an integer
        desired_g: A number denoting the desired graph. 1 for RMSE, 2 for P\u03C3, 3 for CC, 4 for ME.
    """
    PHASE=['Quiet time','Main phase','Recovery phase']
    TITLES=[['Madrigal ','GloTEC ','JPL GIM ','SAMI3 ','SAMI3-RCM ','SAMI3-TIEGCM ','IRI-2016 ','IRI-2020 ',
            'WAM-IPE ','WACCM-X ','TIEGCM-Weimer ','TIEGCM-Heelis ','CTIPe ','GITM-SWMF ','PBMOD '],
              ['GIS_NCKU','IRI2016','IRI2020','SAMI3-RCM','SAMI3-TIEGCM',
               'SAMI3-ICON','WACCM-X','GITM-SWMF','TIEGCM-Weimer','TIEGCM-Heelis','WAM-IPE','CTIPe']]
    x = np.arange(len(TITLES[0]))
    if observ_type == 1:
        format = [[0,10],[-5,5],[0,1.2],[-5,5], "foF2"]
        titles = TITLES[1]
    elif observ_type == 2:
        format = [[0,200],[-50,100],[0,1],[-100,100], "hmF2"]
        titles = TITLES[1]
    else:
        format = [[0, 30], [-15, 15], [0, 1.2], [-25, 25], "TEC"]
        titles = TITLES[0]
        x = np.arange(len(titles))

    fig = make_subplots(1, 3, specs=[[{'colspan': 3}, None, None]])
    # metrics score bar 
    p = Alldata
    np.round(p[0][:, 0], 2)
    fig.add_trace(go.Bar(x=x, y=np.round(Alldata[0][:, 0], 2), name=PHASE[0],marker_color='steelblue'))
    fig.add_trace(go.Bar(x=x, y=np.round(Alldata[0][:,1],2), name=PHASE[1],marker_color='orange'))
    fig.add_trace(go.Bar(x=x, y=np.round(Alldata[0][:,2], 2), name=PHASE[2],marker_color='green'))#Take out the ,1,1 because its only one graph
    fig.update_yaxes(title='RMSE (TECu)', range=format[0])#range=[0,30]
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_layout(title = format[4] + " scores for the " + str(year) + " storm",title_x=0.5, barmode="group", margin=dict(
        b=40,  # bottom margin
        t=80,  # top margin
        pad=1
    ))#taken out: , xaxis_tickangle=-70
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white', tickmode = 'array', showticklabels=True, ticktext =titles, ticks="outside", tickvals= x)
    print("RCPM Almost done\n")

    # Buttons is a list that updates what is displayed on the y-axis only. It changes
    buttons=list([
    dict(args=[{'y':[np.round(p[0][:, 0], 2),np.round(p[0][:, 1], 2), np.round(p[0][:, 2], 2)]},{'yaxis.range':format[0],'yaxis2.range':format[0],'yaxis3.range':format[0], 'yaxis.title.text':'RMSE (TECu)', 'yaxis2.title.text':'RMSE (TECu)', 'yaxis3.title.text':'RMSE (TECu)'}], label="RMSE", method="update"),
    dict(args=[{'y':[np.round(p[1][:, 0], 2),np.round(p[1][:, 1], 2), np.round(p[1][:, 2], 2)]},{'yaxis.range':format[1], 'yaxis2.range':format[1],'yaxis3.range':format[1],  'yaxis.title.text':'P\u03C3,diff (TECu)', 'yaxis2.title.text':'P\u03C3,diff (TECu)', 'yaxis3.title.text':'P\u03C3,diff (TECu)'}], label="P\u03C3", method="update"),
    dict(args=[{'y':[np.round(p[2][:, 0], 2),np.round(p[2][:, 1], 2), np.round(p[2][:, 2], 2)]},{'yaxis.range':format[2], 'yaxis2.range':format[2], 'yaxis3.range':format[2], 'yaxis.title.text':'Correlation Coefficient (R)', 'yaxis2.title.text':'Correlation Coefficient (R)', 'yaxis3.title.text':'Correlation Coefficient (R)'}], label="Corr. Coeff.", method="update"),
    dict(args=[{'y':[np.round(p[3][:, 0], 2),np.round(p[3][:, 1], 2), np.round(p[3][:, 2], 2)]},{'yaxis.range':format[3], 'yaxis2.range':format[3], 'yaxis3.range':format[3], 'yaxis.title.text':'ME (TECu)', 'yaxis2.title.text':'ME (TECu)', 'yaxis3.title.text':'ME (TECu)'}], label="ME", method="update"),
    ])

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"l": 10, "t": 10},
                showactive=True,
                x=-0.25,
                xanchor="left",
                y=1.3,#LOWER THIS TO FIX. it was 1.5, now is 1, havent tested.
                yanchor="top"
            ),
        ]
    )
    return fig
    #fig.show()