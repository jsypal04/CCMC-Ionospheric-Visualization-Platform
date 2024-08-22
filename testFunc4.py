import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def heatmap_sssm_plot(allphase, type, year): #remove YY if working
    TITLES=[['GloTEC ','JPL GIM ','SAMI3 ','SAMI3-RCM ','SAMI3-TIEGCM ','IRI-2016 ','IRI-2020 ',
            'WAM-IPE ','WACCM-X ','TIEGCM-Weimer ','TIEGCM-Heelis ','CTIPe ','GITM-SWMF ','PBMOD '],
              ['GIS_NCKU','IRI2016','IRI2020','SAMI3-RCM','SAMI3-TIEGCM',
               'SAMI3-ICON','WACCM-X','GITM-SWMF','TIEGCM-Weimer','TIEGCM-Heelis','WAM-IPE','CTIPe'],
              ['GIS_NCKU','IRI2016','IRI2020','SAMI3-RCM','SAMI3-TIEGCM',
               'SAMI3-ICON','WACCM-X','GITM-SWMF','TIEGCM-Weimer','TIEGCM-Heelis','WAM-IPE','CTIPe']]
    skillscore = ['nSS_RMSE','nSS_P\u03C3,diff','nSS_R','nSS_ME']
    # plot Figure 4
    PHASE=['Quiet time','Main phase','Recovery phase']
    tt = ['TEC', 'foF2', 'hmF2']
    
    fig = make_subplots(3, 1, specs=[[{}], [{}], [{}]],subplot_titles=(PHASE[0], PHASE[1], PHASE[2]), vertical_spacing=0.12, horizontal_spacing=0.02)
    #flagrow=1
    flagcol=0
    for z,c in zip(allphase,range(3)):
        
        flagcol+=1
        if c == 0:df = pd.DataFrame(z, columns=skillscore,index=TITLES[type])
        else:df = pd.DataFrame(z,columns=skillscore)
        fig.add_trace(go.Heatmap(
            z=df.iloc[::-1],
            showscale=False,
            colorscale="RdBu_r",
            text = df.iloc[::-1],
            
            texttemplate="%{text}",

            ), flagcol, 1)
        
        fig.update(layout_coloraxis_showscale=False)
        #p = df.iloc[::-1]
        

    x = np.arange(len(TITLES[type]))  # the label locations

    fig.update_xaxes(tickmode = 'array', showticklabels=True, ticktext = df.columns, ticks="outside", tickvals= x, row=1, col=1)
    fig.update_xaxes(tickmode = 'array', showticklabels=True, ticktext = df.columns, ticks="outside", tickvals= x, row=2, col=1)
    fig.update_xaxes(tickmode = 'array', showticklabels=True, ticktext = df.columns, ticks="outside", tickvals= x, row=3, col=1)
    fig.update_layout(barmode = "group", title = tt[type]+' total normalized skill score for the '+year+' storm', title_x=0.53)
    fig.update_yaxes(title='\u03A3nSS', title_standoff=0) #range=[0,5]
    fig.update_yaxes(showticklabels=False, row = 2, col = 1)
    fig.update_yaxes(showticklabels=False, row = 3, col = 1)
    fig.update_yaxes(tickmode = 'array', showticklabels=True, ticktext = TITLES[type], ticks="outside", tickvals= x)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_layout(showlegend=False, margin=dict(
        l = 160,   #left margin
        #r = 150,   #right margin
        b=20,  # bottom margin
        t=65,  # top margin
        pad=0
    ))
    return fig