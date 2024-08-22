import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def skill_scores_sum_plot(All_nss1, YY, type):
    """
    A function to plot the summation of normalized skill scores for each model. 
    """
    TITLES=[['Madrigal ','GloTEC ','JPL GIM ','SAMI3 ','SAMI3-RCM ','SAMI3-TIEGCM ','IRI-2016 ','IRI-2020 ',
            'WAM-IPE ','WACCM-X ','TIEGCM-Weimer ','TIEGCM-Heelis ','CTIPe ','GITM-SWMF ','PBMOD '],
              ['GIS_NCKU','IRI2016','IRI2020','SAMI3-RCM','SAMI3-TIEGCM',
               'SAMI3-ICON','WACCM-X','GITM-SWMF','TIEGCM-Weimer','TIEGCM-Heelis','WAM-IPE','CTIPe'],
              ['GIS_NCKU','IRI2016','IRI2020','SAMI3-RCM','SAMI3-TIEGCM',
               'SAMI3-ICON','WACCM-X','GITM-SWMF','TIEGCM-Weimer','TIEGCM-Heelis','WAM-IPE','CTIPe']] 
    PHASE=['Quiet time','Main phase','Recovery phase']
    tt = ['TEC', 'foF2', 'hmF2']
    # plot Figure 4

    fig = make_subplots(1, 3, specs=[
            [{"colspan": 3}, None, None]])


    x = np.arange(len(TITLES[type]))  # the label locations
      # the width of the bars
    fig.add_trace(go.Bar(x=x, y=All_nss1[4][:,0],name="Quiet phase", marker_color='steelblue'), row=1, col=1)
    fig.add_trace(go.Bar(x=x, y=All_nss1[4][:,1],name="Main phase", marker_color='orange'))
    fig.add_trace(go.Bar(x=x, y=All_nss1[4][:,2],name="Recovery phase", marker_color='green'))

    fig.update_xaxes(tickmode = 'array', showticklabels=True, ticktext = TITLES[type], ticks="outside", tickvals= x)

    fig.update_yaxes(title='\u03A3nSS', range=[0,5])
    fig.update_layout(barmode = "group", title = tt[type]+' total normalized skill score for the '+YY+' storm', title_x=0.5)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    #fig.update_layout(showlegend=False)
    #fig.show()
    return fig
#dta = np.load("csmc2_tnSS_hmF2.npy")
#skill_scores_sum_plot(dta, "2021", 2)

#all these functions should be more generalized. Have foF2, hmF2, TEC be fed in, in addition to all the seperate ranges and such that make up the graph.