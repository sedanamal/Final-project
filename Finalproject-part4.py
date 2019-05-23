# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:59:24 2019

@author: User
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt

############### PART 1 #####################
#for distance matrix

location1 = ('C:/Users/User/Desktop/phyton/final/distancematrix.xls')
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
    a[n][n]=0

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
    row_values = sheet.row_values(i)
    row_values.pop(0)
    row_values.pop(0)
    B.append(row_values)
    i=i+1

coordinates=np.asarray(B) 

# Genetic Algorithm
def get_path():
  path = list(range(81))
  np.random.shuffle(path)
  return path

def get_path_length(path):
    path = np.append(path,path[0])
    total = 0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        distance = distances[j, k]
        total = total + distance
    return total

def draw_path(path):
  path_length = get_path_length(path)
  path = np.append(path,path[0])
  x = coordinates[:,1][path]
  y = coordinates[:,0][path]
  plt.plot(x,y,'-o')
  plt.text((min(x)+max(x))/2-3,43,str(path_length)+' kilometers.',fontsize=12)
  plt.ylim(min(y)-1, max(y)+2)
  plt.axes().set_aspect('equal')
  plt.show()

def cross_over(gene1,gene2, mutation=0.06):
  x = np.random.randint(81)
  new = gene1[:x]
  remaining = []
  for i in range(81):
      if gene2[i] not in new:
          remaining.append(gene2[i])
  new = np.append(new, remaining)
    
  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,81,2)
    new[[i1,i2]] = new[[i2,i1]] 
  return new

def create_initial_population(size):
  population = []
  fitness = []
  for i in range(size):
    path = get_path()
    path_length = get_path_length(path)
    population.append(path)
    fitness.append(path_length)
  population = np.array(population)
  fitness = np.array(fitness)  
  sortedindex = np.argsort(fitness)
  pop, fit = population[sortedindex], fitness[sortedindex]
  return pop, fit

def next_generation(population):
  pop, fit = [], []
  f=int(len(population)**(0.5))
  for gene1 in population[:f]:
    for gene2 in population[:f]:   
      new_path =  cross_over(gene1,gene2,mutation=0.06)
      distance = get_path_length(new_path)
      pop.append(new_path)
      fit.append(distance)
  population = np.array(pop)
  fitness = np.array(fit)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

gen = 500             # Generation Size as Input
n_pop=500          # Population Size as Input

population, fitness  = create_initial_population(n_pop)

for i in range(gen):
    population, fitness = next_generation(population)

path = population[0]
path.tolist()
draw_path(path)
