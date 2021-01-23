import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

x = st.number_input("somme déposée")


def calcul(x, tau1, tau2, R, t):
    # montant reellement depose dans le compte
    z = x*(1-tau1)
    y = z*(1+R)**t + (z*(1+R)**t - z)*(1-tau2)
    return y

def AV(x, R, t):
    z = x
    y = 0.8*z*(1+R)**t
    return y

def CAP(x, R, t):
    z = x*(1-12/100)
    y = z*(1+R)**t - (z*(1+R)**t - z)*30/100
    return y

def CAP_NL(x, R, t):
    z = x*(1-12/100)
    y = z*(1+R)**t
    return y

r = st.slider("Rendement des placements (%)", 0.0, 6.0)
R = r/100

res = {}
res['AV'] = []
res['CAP'] = []
res['CAPNL'] = []
res['Montant sauve avec AV'] =[]
res['years'] = []
for i, t in enumerate(range (0, 20)):
    res['AV'] .append(AV(x, R, t))
    res['CAP'].append(CAP(x, R, t) )
    res['CAPNL'].append(CAP_NL(x,R,t))
    res['years'].append(i)
    res['Montant sauve avec AV'].append(AV(x, R, t) - CAP(x, R, t))

df = pd.DataFrame(res)
st.write(df)
fig = px.line(df, title= 'Montant total sauve avec AV' ,x= 'years', y="Montant sauve avec AV")
st.plotly_chart(fig)

df['Montant sauve avec AV par personne'] = df['Montant sauve avec AV']/3
fig = px.line(df, title= 'Montant total sauve avec par personne' ,x= 'years', y="Montant sauve avec AV par personne")
st.plotly_chart(fig)
