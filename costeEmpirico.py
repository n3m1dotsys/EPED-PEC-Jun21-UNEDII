################################################################################
#                                                                              #
# costeEmpirico.py                                                             #
#                                                                              #
# Author : Martín "n3m1.sys" Romera Sobrado                                    #
#                                                                              #
# Brief  : Script para realizar un analisis de los costes temporales en el     #
#          peor caso para las implementaciones de BucketQueue y                #
#          BSTPriorityQueue                                                    #
#                                                                              #
################################################################################
import sys
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
from numpy.linalg import inv
# from scipy import optimize

TESTS=["BQ_ENQ","BQ_DEQ","BST_ENQ","BST_DEQ"]

test_actual="NULL"
caso_actual="0"
dataframes={}
values=[]
d=None
i = 1

for line in sys.stdin:
    line=line.replace("\n","")
    if "ms" in line:
        line=line.replace(" ms","")
        # print("Nuevo resultado: "+line)
        values.append(int(line))
    elif "pacientes" in line:
        line=line.replace(" pacientes","")
        # print("Nuevo caso: "+line)
        if values != []:
            d['case'].append(caso_actual)
            d['var'].append(st.pstdev(values))
            d['avg'].append(st.fmean(values))
            values=[]
        caso_actual=line
    elif line in TESTS:
        # print("Nuevo Test: "+line)
        if values != []:
            d['case'].append(caso_actual)
            d['var'].append(st.pstdev(values))
            d['avg'].append(st.fmean(values))
            values=[]
        if d != None:
            df = pd.DataFrame(data=d, columns=['case', 'var', 'avg'])
            df.sort_values(by=['case'])
            dataframes[test_actual]=df
        d={'case':[],'var':[],'avg':[]}
        test_actual=line
    else:
        print("Algo falla con la linea "+line)
if values != []:
    d['case'].append(caso_actual)
    d['var'].append(st.pstdev(values))
    d['avg'].append(st.fmean(values))
    values=[]
if d != None:
    df = pd.DataFrame(data=d, columns=['case', 'var', 'avg'])
    dataframes[test_actual]=df

for k in dataframes.keys():
    print(k+": ")
    print(dataframes[k])
    # dataframes[k].plot(x="case", y="avg", yerr="var", kind='scatter')
    # plt.show()

# Resultado de BQ_ENQ
cases = dataframes["BQ_ENQ"]["case"]
avg = dataframes["BQ_ENQ"]["avg"]
cov = dataframes["BQ_ENQ"]["var"]
plt.scatter(cases,avg,marker="x")
plt.errorbar(cases,avg,cov,fmt='none',barsabove=True)
plt.title("BucketQueue enqueue() test")
plt.show()

# Resultado de BQ_DEQ
enq_res = dataframes["BQ_ENQ"]['avg']
deq_res = dataframes["BQ_DEQ"]['avg']
cases = dataframes["BQ_DEQ"]['case']
enq_var = dataframes["BQ_ENQ"]['var']
deq_var = dataframes["BQ_DEQ"]['var']
avg = np.subtract(deq_res,enq_res)
cov = np.abs(np.subtract(deq_var,enq_var))
plt.scatter(cases,avg,marker="x")
plt.errorbar(cases,avg,cov,fmt='none',barsabove=True)
plt.title("BucketQueue dequeue() test")
plt.show()

# Resultado de BQ_ENQ
cases = dataframes["BST_ENQ"]["case"]
avg = dataframes["BST_ENQ"]["avg"]
cov = dataframes["BST_ENQ"]["var"]
plt.scatter(cases,avg,marker="x")
plt.errorbar(cases,avg,cov,fmt='none',barsabove=True)
plt.title("BSTPriorityQueue enqueue() test")
plt.show()

# Resultado de BQ_DEQ
enq_res = dataframes["BST_ENQ"]['avg']
deq_res = dataframes["BST_DEQ"]['avg']
cases = dataframes["BST_DEQ"]['case']
enq_var = dataframes["BST_ENQ"]['var']
deq_var = dataframes["BST_DEQ"]['var']
avg = np.subtract(deq_res,enq_res)
cov = np.abs(np.subtract(deq_var,enq_var))
plt.scatter(cases,avg,marker="x")
plt.errorbar(cases,avg,cov,fmt='none',barsabove=True)
plt.title("BSTPriorityQueue dequeue() test")
plt.show()