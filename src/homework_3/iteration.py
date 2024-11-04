import random
import numpy as np

x=0.25
y=0.25
gamma=0.9

T_a0=[[0,0,0,0],
    [0,1-x,0,x],
    [1-y,0,0,y],
    [1,0,0,0]]
T_a1=[[0,1,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
T_a2=[[0,0,1,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    
T = np.array([T_a0, T_a1, T_a2])

R=[0,0,1,10] #reward

def update_V(s,v,action):
  max_value = 0
  for a in range(T.shape[0]):
    temp = 0
    for dest in range(len(R)):
      temp+=T[a,s,dest]*v[dest]
    if temp>max_value:
      max_value=temp
      action[s]=a # update the action
  return R[s]+gamma*max_value
  
action=[1,0,0,0] # initial action
max_iter=400 # max iteration
V=np.array([0.0,0.0,0,0]) # initial value
V_new=V.copy() # new state value
print("initial action",action)
print("initial status",V_new)
while True:
  for s in range(len(R)):
    V_new[s]=update_V(s,V,action) # update the status
  diff = np.sqrt(np.sum((V_new - V) ** 2))
  if diff<0.0001:
    break
  else:
    V=V_new.copy()

print("final difference:",diff)
print("optimal action:",action)
print("optimal status:",V_new)
