# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np


#Aufgabe 4.1 - d)

st.chi2.ppf(q=[0.05, 0.95], df=27)


#Aufgabe 4.2 
st.norm.interval(alpha=0.99, loc=160, scale=5/np.sqrt(36)) #Bekannt: Standardabweichung, Mittelwert (Erwartung)

#mit t.interval erhalten wir einen Falschen Wert, weil bei einer T-Verteilung noch mehr unter der Kurve liegt (nur nutzen,
#wenn Werte fehlen!)
st.t.interval(alpha=0.99, loc=160, scale=5/np.sqrt(36), df=35) 

#Aufgabe 3
cloud = pd.Series([18.0, 30.7, 19.8, 27.1, 22.3, 18.8, 31.8, 23.4, 21.2, 27.9, 31.9, 27.1,25.0, 24.7, 26.9, 21.8, 29.2, 34.8, 26.7, 31.6])
cloud.describe()

cloud_diff = cloud - 25 #Differenz!


st.t.cdf(x=25, df=19, loc=cloud.mean(), scale=cloud.std()/np.sqrt(20)) #t test variante 1
st.ttest_1samp(cloud_diff, popmean=0).pvalue/2 # test variante 2, popmean = 0 weil mean abgezogen (cloud_diff)


st.t.ppf(q=[0.05], loc=cloud.mean(), scale=cloud.std()/np.sqrt(20), df=19)
st.t.interval(alpha=0.9, loc=cloud.mean(), scale=cloud.std()/np.sqrt(20), df=19)

#Aufgabe 4
#H0 = u0 = uA = 55
#Ha = u0 != uA

beer = pd.Series([56, 59, 49, 51, 58, 57, 52, 57, 52, 57, 50, 57, 58, 54, 59])

st.probplot(beer, plot=plt)

#DIFF!
beer_diff = beer - 55

#Achtung! wilcoxon ist beidseitig, deswegen nehmen wir die Hälfte
st.wilcoxon(beer_diff, zero_method="wilcox", correction=False).pvalue / 2

#Binomial Test geht auch!
st.binom_test(x=(sum(n>0 for n in beer_diff)), n=15, p=0.5, alternative='less')