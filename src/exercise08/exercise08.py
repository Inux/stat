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


diff = pd.Series([-7,-16,-3,2,-1,-10,-11,2,-8])

################################################
#Aufgabe 8.3

#H0 = Die Messgeräte messen das Gleich
#Alternativ Hypothese -> Messgerät B misst grössere Werte Wie Messgerät A (uD < u0)

st.probplot(diff, plot=plt)

#Verwerfungsbereich
st.t.ppf([0.025, 0.975], loc=0, df=diff.count()-1, scale=diff.std()/np.sqrt(diff.count()))

#Alternativehypothese
st.t.ppf(0.05, loc=0, df=diff.count()-1, scale=diff.std()/np.sqrt(diff.count()))

# Verwerfungsbereich Alternativhypothese: -unendlich, -3.84
st.t.cdf(x=-5.78, df=diff.count()-1, loc=0, scale=diff.std()/np.sqrt(diff.count()))


################################################
#Aufgabe 8.4

#H0 = Es gibt keine Unterschiede 
#Alternative Hypothese = Es gibt unterschiede zwischen den Kieferlängen

jackals = pd.read_table(r"/Users/inux/Projects/HSLU/stat/src/exercise08/jackals.txt", sep= " ")
st.ttest_ind(jackals["M"], jackals["W"], equal_var=False)

new = jackals["M"] - jackals["W"]
new.describe()

st.t.cdf(x=new.mean(), df=9, loc=0, scale=new.std()/np.sqrt(10))

st.t.ppf(q=0.05, df=9, loc=0, scale=new.std()/np.sqrt(10))

1 - st.t.cdf(x=new.mean(), df=9, loc=0, scale=new.std()/np.sqrt(10))

#
st.mannwhitneyu(jackals["M"], jackals["W"], alternative="two-sided")

st.wilcoxon(new, correction=False)


################################################
#Aufgabe 8.5

zurich = pd.Series([16.6, 12.7, 14, 53.3, 117, 62.6, 27.6])
basel = pd.Series([10.4,8.91,11.7,29.9,46.3,25,29.4])

diff = zurich - basel
diff

st.probplot(diff, plot=plt)

#A
diff.describe()
diff.mean()
diff.std()

#B ungepaart, verschiedene lokalitäten, zeiten, messgeräte (Wie ein Gruppe und Kontrollgruppe)

#C 
#H0: Zürich und Basel konsumieren gleich viel MDMA
#Alternative Hypothese: In Zürich wird mehr MDMA konsumiert als in Basel

#Verwerfungsbereich
st.ttest_ind(zurich, basel, equal_var=False)

#0.22/2 ist grösser als 0.05 deshalb wird Nullhypothese beibehalten! (0.05 kommt von 1-0.95)