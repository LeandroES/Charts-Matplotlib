import matplotlib.pyplot as plt

#Bubble Sort Python Promedio
x = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y = [0.001005268096923820,0.070356798171997000,0.294240808486938000,0.710008001327514000,1.209030199050900000,1.786536931991570000,2.590527677536000000,3.494307136535640000,4.472889423370350000,5.620229053497310000,7.113364267349220000,29.203883075714100000,71.784848356246800000,128.635452032089000000,234.156673336028000000]
plt.plot(x,y,marker='o',linestyle='-',color='g',label='Python Prom')
#Bubble Sort Python Desviación Estandar
x2 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y2 = [0.000706163,0.018768023,0.094337983,0.191807135,0.342717961,0.522313391,0.801962403,1.023337955,1.332680539,1.664917723,2.30476683,8.914997652,18.75645676,37.78050826,70.27276125]
plt.plot(x2,y2,marker='o',linestyle='--',color='g',label='Python D.E.')
#Bubble Sort C++ Promedio
x3 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y3 = [0.02006180,0.00397700,0.01733960,0.03928220,0.07544960,0.11780880,0.17646460,0.21138100,0.27841080,0.36249780,0.42957900,1.83589240,4.06290460,7.32903020,12.30111100]
plt.plot(x3,y3,marker='o',linestyle='-',color='r',label='C++ Prom')
#Bubble Sort C++ Desviación Estandar
x4 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y4 = [0.04474775,0.00023707,0.00451116,0.00720680,0.01472408,0.01937846,0.01764188,0.01127242,0.01901036,0.01862501,0.00917648,0.07176137,0.18974109,0.19250875,1.97851902]
plt.plot(x4,y4,marker='o',linestyle='--',color='r',label='C++ D.E.')
#Bubble Sort Golang Promedio
#x5 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
#y5 = [30,45,58,43,36]
#plt.plot(x5,y5,marker='o',linestyle='-',color='b',label='Golang Prom')

#Bubble Sort Golang Desviación Estandar
#x6 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
#y6 = [30,45,58,43,36]
#plt.plot(x6,y6,marker='o',linestyle='--',color='b',label='Golang D.E.')

plt.legend()
plt.xlabel('Tamaño de Array')
plt.ylabel('Segundos')
plt.title('Bubble Sort')
plt.show()

#%%
import matplotlib.pyplot as plt
#Cocktail Sort Python Promedio
x7 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y7 = [0.001594400405883790,0.130591297149658000,0.485210895538330000,1.077796792984000000,1.963001298904420000,2.954405832290640000,4.341107368469230000,6.460231256484980000,7.963523197174070000,9.993674993515000000,13.201202583312900000,49.370647430419900000,119.851104831695000000,215.081068038940000000,314.734095621109000000]
plt.plot(x7,y7,marker='o',linestyle='-',color='g',label='Python Prom')
#Cocktail Sort Python Desviación Estandar
x8 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y8 = [0.000899039,0.021324258,0.05588349,0.088059516,0.28600691,0.153434744,0.224933585,0.772569569,0.356157302,0.767029447,2.104212629,2.910185048,19.44241872,26.21571317,6.83191907]
plt.plot(x8,y8,marker='o',linestyle='--',color='g',label='Python D.E.')
#Cocktail Sort C++ Promedio
x9 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y9 = [0.000030400,0.002502000,0.010945250,0.036701750,0.078343750,0.105824500,0.095908000,0.164579750,0.180534750,0.313220250,0.312332750,1.059184500,2.430938000,3.959493750,6.053580250]
plt.plot(x9,y9,marker='o',linestyle='-',color='r',label='C++ Prom')
#Cocktail Sort C++ Desviación Estandar
x10 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
y10 = [0.000001673320053068150,0.000301023808582201000,0.002366546340837920000,0.032819773748712300000,0.071188345883180400000,0.094126365886503800000,0.019899641554560700000,0.053476660562498300000,0.044282272257078300000,0.105382002550641000000,0.061513657623734400000,0.063176640158104800000,0.081492134086671200000,0.293927887551097000000,0.149570362073897000000]
plt.plot(x10,y10,marker='o',linestyle='--',color='r',label='C++ D.E.')
#Cocktail Sort Golang Promedio
#11 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
#y11 = [30,45,58,43,36]
#plt.plot(x11,y11,marker='o',linestyle='-',color='b',label='Golang Prom')

#Cocktail Sort Golang Desviación Estandar
#x12 = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
#y12 = [30,45,58,43,36]
#plt.plot(x12,y12,marker='o',linestyle='--',color='b',label='Golang D.E.')

plt.legend()
plt.xlabel('Tamaño de Array')
plt.ylabel('Tiempo')
plt.title('Cocktail Sort')
plt.show()