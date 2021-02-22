'''
A pi estimator inspired from joma
Watch his video here https://www.youtube.com/watch?v=pvimAM_SLic
the higher the value of n the higher the pi value accuracy
'''
import random

def est_pi(n):
    pts=0
    pts_c=0
    for i in range(n):
            x=random.random()
            y=random.random()
            dist=x**2+y**2
            if dist<=1:
                pts_c+=1
            pts+=1
    print(4*pts_c/pts)

_=int(input())
est_pi(_)
