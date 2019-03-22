import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr = np.array([2, 1, 4, 5, -8])
print("\nArray:")
print(arr)
arr = arr*3
print(arr)
arr = arr*arr
print(arr)

temp_luz = Series(
    [1, 5, 9, 15, 20, 25, 25],
    index=("jan", "feb", "mar", "apr", "mai", "jun", "jul")
)

print("\nSeries:")
print(temp_luz)

print("\nSeries Index:")
print(temp_luz["mar"])

temp = DataFrame({
    "Luzern": ([1, 5, 9, 15, 20, 25, 25]),
    "Basel":  ([3, 4, 12, 16, 18, 23, 32]),
    "Zuerich": ([8, 6, 10, 17, 23, 22, 24])},
    index=["jan", "feb", "mar", "apr", "mai", "jun", "jul"]
)

print("\nDataFrame:")
print(temp)

print("\nColumns:")
print(temp.columns)

print("\nMean:")
print(temp.mean())
