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
diam =21 #11 #7 #5 #3

bmin=125
smin=124

xlo=100; xhi=300; ylo=100; yhi=250
xlo=130; xhi=300; ylo=130; yhi=240
#xlo=150; xhi=275; ylo=137; yhi=225
xlo=125; xhi=300; ylo=125; yhi=250

xlo=125; xhi=200; ylo=150; yhi=250
xlo=150; xhi=200; ylo=175; yhi=250
xlo=150; xhi=200; ylo=175; yhi=250

xlo=150; xhi=175; ylo=187; yhi=237

xlo=160; xhi=176; ylo=190; yhi=230
xlo=160; xhi=176; ylo=210; yhi=226

xlo=160; xhi=168; ylo=214; yhi=226

xlo=164; xhi=168; ylo=217; yhi=224
xlo=164; xhi=168; ylo=217; yhi=223
xlo=164; xhi=168; ylo=218; yhi=222

xlo=163; xhi=166; ylo=217; yhi=221
xlo=163; xhi=165; ylo=217; yhi=220

xlo=163; xhi=166; ylo=217; yhi=219
xlo=163; xhi=165; ylo=218; yhi=220
#xlo=163; xhi=165; ylo=217; yhi=219
xlo=163; xhi=165; ylo=218; yhi=220

xlo=164; dx52=2;  ylo=218; dy52=2


##xlo -= 0.2 ; dx52 += 0.4; xhi=xlo+dx52
##ylo -= 0.2 ; dy52 += 0.4; yhi=ylo + dy52

#xlo -= 0.1 ; xhi+=0.1
#ylo -= 0.1 ;  yhi+=0.1

xhi=xlo+dx52
yhi=ylo + dy52


#=============================
scr52=200
##h=scr52*dy52##*3 #40 #100 #950 #1040 #h=180 #h=730 #h=360 #w=h*2
##w=scr52*dx52*1.5
h=950 #1300 #1400 #950
w=1850 #2000 #2250 #1800


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

niter = 2000 #400 #200 #1000 #3000   
sleep1=    0 #0.3      #0.1 #0 #0.01
step1=15 #17#4 #20 #8 #5 #1 #37 #2
step2=60#60 #120

bfade = True  # False
q = 0.9 #0.8#0.7 #0.3 #0.1 #q = 1. / 2.
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
