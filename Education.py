from __future__ import annotations
from decimal import Decimal
from typing import Self
from dataclasses import dataclass
from pathlib import Path
import numpy 
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor


Apple=numpy.array([157,156,159])
n=len(Apple)

print(type(numpy.arange(n)),type(n))
model=LinearRegression().fit(numpy.arange(n).reshape((n,1)),Apple)

input_data=numpy.array([[0],
                        [1],
                        [2],
                        [3],
                        [4],
                        [5],
                        [6],
                        [100],
                        [23]])

print(model.predict(input_data),type(model),input_data.reshape((-1,1)))

X=numpy.array([ [0, "No"],
                [10, "No"],
                [60, "Yes"],
                [90, "Yes"]])
n=len(X)
print(n)

model=LogisticRegression().fit(X[:,0].astype(float).reshape(-1,1),X[:,1])

input_data=numpy.array([[2],
                        [12],
                        [13],
                        [5],
                        [35],
                        [36],
                        [40],
                        [50]])

print(model.predict(input_data),type(model),X[:,0])

a=numpy.array([range(30,41)]).reshape((-1,1))

print(a,model.predict_proba(a))

X = numpy.array([[35, 7000], [45, 6900], [70, 7100],
                [20, 2000], [25, 2200], [15, 1800]])

kmeans=KMeans(n_clusters=2).fit(X)

cc=kmeans.cluster_centers_

print(cc,type(cc),type(kmeans))

X = numpy.array([  [35, 30000], [45, 45000], [40, 50000],
                [35, 35000], [25, 32500], [40, 40000]])

KNN=KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape((-1,1)),X[:,1])

a=numpy.array([[35]])

res=KNN.predict(a)
print(type(KNN),res,type(res))

X = numpy.array(
    [[20,  11,  20,  30,  4000,  3000],
    [12,   4,   0,   0, 1000,  1500],
    [2,   0,   1,  10,   0,  1400],
    [35,   5,  10,  70,  6000,  3800],
    [30,   1,   4,  65,   0,  3900],
    [35,   1,   0,   0,   0, 100],
    [15,   1,   2,  25,   0,  3700],
    [40,   3,  -1,  60,  1000,  2000],
    [40,   1,   2,  95,   0,  1000],
    [10,   0,   0,   0,   0,  1400],
    [30,   1,   0,  50,   0,  1700],
    [1,   0,   0,  45,   0,  1762],
    [10,  32,  10,   5,   0,  2400],
    [5,  35,   4,   0, 13000,  3900],
    [8,   9,  40,  30,  1000,  2625],
    [1,   0,   1,   0,   0,  1900],
    [1,  30,  10,   0,  1000,  1900],
    [7,  16,   5,   0,   0,  3000]])

neural_net=MLPRegressor(max_iter=10000).fit(X[:,:-1],X[:,-1])

a=numpy.array([20,1,10,50,1000]).reshape(1,-1)

res=neural_net.predict(a)
print(res)