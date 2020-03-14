# originally evolved from
#http://nbviewer.ipython.org/github/martin12333/teaching-simso/blob/master/52-largerthanlife.ipynb
#https://github.com/thearn/game-of-life/blob/master/conway.py

from pylab import *

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
###bfade, q, qqq may be related to Cc
#M1 or weighted
#smin==slo
#smax==shi
#bmin==blo
#bmax==bhi
#NM or weighted



#=============================
diam =5 #3
blo=7 #3 ##24 ##23.5 ##2.60 #70 #60 #50 ##6.5 ###7*(beta70 - d691) ##2.98 #3*beta70 #xx #3
slo=7 #3 ##31 ##30.5 ##3.35 #25 #15 #01 #2.9 #8 #7  #20 #30 #40 #50 ##6.5 ###7*(beta70 - d691) #8  ##2.98 #3*beta70 #yy - 1 #slo = 3

xlo=7 ##3 ##23 ##22.5 ##2.5 #2.9 #2.8 #2.5 #2
xhi=11 ##6 ##45 ##45.5   ##5 #3.6 #4.1 #4.2 #4.5 #5 #10
ylo=7 ##3 ##28 ##27.5 ##3 # 4.4 #4.2  #3 #3.9 #3.8
yhi=11 ##54 ##54.5 ##6 #4.3 #4.8  #6 #5.1 #5.2 #10

#=============================
h=950 #1040 #h=180 #h=730 #h=360 #w=h*2
w=h

p=0.25 #0.16
a = 1.0*(rand( h, w )<p)    

x11 = floor(linspace(xlo, xhi + 0.999, w))
y11 = floor(linspace(yhi + 0.999 , ylo, h))
##x11 = (linspace(xlo, xhi , w))
##y11 = (linspace(yhi  , ylo, h))
xx, yy = meshgrid(x11, y11)
 
bhi=xx
shi=yy

niter = 3000   
sli=0 #0.1 #0 #0.01
skipy=5 #1 #37 #5 #2

bfade = True  # False
q = 0.3 #0.1 #q = 1. / 2.
qqq=4 #8 #qqq=1.8
afade = 0.1 * a
#averyold = 0*a



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
execfile('b5backend_bLtL_pygame.py')
