# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:29:52 2019

@author: User
"""


import xlrd
import numpy as np
import matplotlib.pyplot as plt

############### PART 1 #####################
#for distance matrix

location1 = ("C:/Users/User/Desktop/phyton/final/distancematrix.xls")
wb=xlrd.open_workbook(location1)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
print('number of rows='+str(sheet.nrows))
print('number of columns='+str(sheet.ncols))
i=0
a=[]
for i in range(84):
    a.append(sheet.row_values(i))
    i=i+1
    
a.pop(2)
a.pop(1)
a.pop(0)
for n in range(81):
    
    a[n].pop(1)
    a[n].pop(0)
    a[n][n]=np.nan

distances=np.asarray(a)

#for coordinates matrix
location2 = ("C:/Users/User/Desktop/phyton/final/Coordinates.xlsx")
wb=xlrd.open_workbook(location2)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
print('number of rows='+str(sheet.nrows))
print('number of columns='+str(sheet.ncols))
i=0
B=[]
for i in range(1,82):
    B.append(sheet.row_values(i))
    i=i+1

coordinates=np.asarray(B) 

############## PART 2 #####################
xa = coordinates[:,2]
ya = coordinates[:,3]
x,y=[],[]
for i in range (81):
    x.append(float(xa[i]))
    y.append(float(ya[i]))
    
route1 = list(range(5))+list(range(6,81))
np.random.shuffle(route1)
route1.insert(0,5)
route1.append(5)

    
route1l = 0
dif1=[]
for i in range(80):
    d1=route1[i+1]  
    d2=route1[i]
    difference=distances[d1][d2]
    dif1.append(difference)
    route1l=route1l+difference
print('the total distance of random route is '+str(route1l))
    
plt.plot(y,x,'.')
plt.plot(y,x)
plt.axes().set_aspect('equal')
plt.ylim(36,44)
plt.xlim(25,45)

#################### PART 3 ##############################

route2=[5]
route2l=0
for i in range(80):        
    listofdistance = list(distances[route2[-1]])
    for j in range(len(listofdistance)):
        if listofdistance.index(min(listofdistance)) in route2:
            listofdistance.remove(min(listofdistance))
    route2.append(listofdistance.index(min(listofdistance)))
    
route2.append(5)
dif2=[]

for i in range(80):
    d3=route2[i+1]  
    d4=route2[i]
    difference1=distances[d3][d4]
    dif2.append(difference1)
    route2l=route2l+difference1

print('the shortest route is equal to '+str(route2l))
    
