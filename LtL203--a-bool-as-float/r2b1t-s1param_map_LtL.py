# originally evolved from
#http://nbviewer.ipython.org/github/martin12333/teaching-simso/blob/master/52-largerthanlife.ipynb
#https://github.com/thearn/game-of-life/blob/master/conway.py

from pylab import *
import numpy as np
np.random.seed()      
#print 'np.random.seed()      '

#=============================
#a standard rule notation
#https://www.conwaylife.com/wiki/Larger_than_Life
#Rr,Cc,M1,Ssmin..smax,Bbmin..bmax,Nn
#Rr specifies the range (r is from 1 to 500 in Golly and LifeViewer; 1 to 10 in MCell).
#Cc specifies the number of states (c is from 0 to 255 in Golly, LifeViewer and MCell[note 1])
#Mm specifies if the middle cell is included in the neighborhood count (m is 0 or 1).
#Ssmin..smax specifies the count limits for a state 1 cell to survive.
#Bbmin..bmax specifies the count limits for a dead cell to become a birth.
#Nn specifies the extended neighborhood type (n is M for Moore or N for von Neumann. Golly and LifeViewer also support C for Circular neighborhood)

#in legacy  source code, by Martin Novy
#diam == 2*r + 1
###parameters are described at PARAMETERS.txt
#M1 or weighted
#smin==smin
#smax==smax
#bmin==bmin
#bmax==bmax
#NM or weighted



#=============================
diam =5 #3

bmin=1#5#7#3 ##24 ##23.5 ##2.60 #70 #60 #50 ##6.5 ###7*(beta70 - d691) ##2.98 #3*beta70 #xx #3

xlo=-0.2+1#5#7####5##3 #4 #3 ##23 ##22.5 ##2.5 #2.9 #2.8 #2.5 #2
dx52=0.4+23 #2.4
xhi=xlo +dx52#5.2#6#1 #5 #6 ##45 ##45.5   ##5 #3.6 #4.1 #4.2 #4.5 #5 #10

smin=1##3 ##31 ##30.5 ##3.35 #25 #15 #01 #2.9 #8 #7  #20 #30 #40 #50 ##6.5 ###7*(beta70 - d691) #8  ##2.98 #3*beta70 #yy - 1 #smin = 3

ylo=-0.2+1#10-0.2#7##4 #3 ##28 ##27.5 ##3 # 4.4 #4.2  #3 #3.9 #3.8
dy52=0.4+23 #2.4
yhi=ylo + dy52#1.4#5##1 #4 #5 #6 ##54 ##54.5 ##6 #4.3 #4.8  #6 #5.1 #5.2 #10

#=============================
scr52=200
h=scr52*dy52##*3 #40 #100 #950 #1040 #h=180 #h=730 #h=360 #w=h*2
w=scr52*dx52
h=950
w=1800

h=int(h)
w=int(w)

p=0.50 #25 #0.16
a = 1.0*(rand( h, w )<p)    

###x11 = floor(linspace(xlo, xhi + 0.999, w))
###y11 = floor(linspace(yhi + 0.999 , ylo, h))
x11 = (linspace(xlo, xhi , w))
y11 = (linspace(yhi  , ylo, h))
xx, yy = meshgrid(x11, y11)
 
bmax=xx
smax=yy

niter = 400 #400 #200 #1000 #3000   
sleep1=    0 #0.3      #0.1 #0 #0.01
step1=8#4 #20 #8 #5 #1 #37 #2
step2=60#60 #120

bfade = True  # False
q = 0.1#0.7 #0.3 #0.1 #q = 1. / 2.
qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8
afade = 0.1 * a

averyold = 0*a



#matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")

#matplotlib.rc("image",interpolation="nearest")

###np.dstack()
###np.concatenate()
####(tup, axis=2)


#execfile('backend_LtL_imshow.py')
execfile('backend_bLtL_pygame.py')
