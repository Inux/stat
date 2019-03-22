#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:40:02 2018

@author: mirkobirbaumer
"""

# Einführung Aufgabe 1.1

from pandas import Series,DataFrame
import pandas as pd
data = pd.read_csv(".../child.csv",sep=",",index_col=0)

data.head()
data.describe()
data.mean()
data.median()
data.index
"China" in data.index
"Netherlands" in data.index
data.columns
drunk = data.sort_values(by="Drunkenness", ascending=False)
drunk["Drunkenness"]
drunk["Drunkenness"].head()

# Befehle Deskriptive Statistik

# Mittelwert
from pandas import Series
import pandas as pd
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03,80.03, 80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
methodeA.mean()

# Varianze und Standardabweichung
methodeA.var()
methodeA.std()

# Median

methodeA.median()
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97,80.03, 79.95, 79.97])
methodeB.median()

# Quantile

methodeA.quantile(q=.25, interpolation="midpoint")
methodeA.quantile(q=.75, interpolation="midpoint")

# Quartilsdifferenz
q75, q25 = methodeA.quantile(q = [.75, .25], interpolation="midpoint")
iqr = q75 - q25
iqr

## Quantilen

noten = Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4,3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])
noten.quantile(q = np.linspace(.2,1,5), interpolation="midpoint")

# Histogramm : Absolute Häufigkeit

import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03,80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03,79.95, 79.97])
methodeA.plot(kind="hist", edgecolor="black")
plt.title("Histogramm von Methode A")
plt.xlabel("methodeA")
plt.ylabel("Haeufigkeit")
plt.show()

# Histogramm : Relative Häufigkeit (Dichte)

import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03,80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03,79.95, 79.97])
methodeA.plot(kind="hist", edgecolor="black", normed=True)
plt.title("Histogramm von Methode A")
plt.xlabel("methodeA")
plt.ylabel("Haeufigkeit")
plt.show()

# Einführung Aufgabe 1.5

from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

geysir = pd.read_table("../geysir.dat", sep=" ", index_col=0)
geysir.head()
plt.subplot(221)
geysir["Zeitspanne"].plot(kind="hist", edgecolor="black")
plt.xlabel("10 Klassen")

plt.subplot(222)
geysir["Zeitspanne"].plot(kind="hist", 
                          bins=20,
                          edgecolor="black")
plt.xlabel("20 Klassen")

plt.subplot(223)
geysir["Zeitspanne"].plot(kind="hist", 
                          bins=np.arange(41,107,11), 
                          edgecolor="black")
plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")

plt.show()