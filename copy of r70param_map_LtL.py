# beta ver

#NOTE: the showing of images does NOT currently work when running r2paramLtL.py from SPYDER v2.2


# evolved from
#http://nbviewer.ipython.org/github/martin12333/teaching-simso/blob/master/52-largerthanlife.ipynb
#https://github.com/thearn/game-of-life/blob/master/conway.py

from pylab import *


bltl=False #True #False


#=============================
#----------------
#diam =9   
#xlo= 0
#xhi= 170
#ylo=0
#yhi=170


#----------------
diam =3 #9 #3 #3

##d03=1 #3 #1

##alpha03=0.7 #1.3




d2=diam*diam
xlo= -10.0/9.0*d2 #0
xhi= 28.0/9.0*d2
ylo=-10.0/9.0*d2
yhi=27.0/9.0*d2
#----------------
#diam =11 

#blo=34 
#slo = 34
#xlo= 40
#xhi=43
#ylo=  58
#yhi= 58

#----------------


# blo=14 #3 
# slo = 14
# diam =7 
# xlo= 17
# xhi=18
# ylo=  23
# yhi= 23
#xlo= 15
#xhi=23
#ylo=  16
#yhi= 24

#----------------
#diam =3   
#xlo= 0
#xhi= 17
#ylo=0
#yhi=17
#xlo=-1 #1 #2
#xhi=7 #5 #4
#ylo=-1 #1 #2 #3
#yhi=8 #6 #5 #6 #7 
# xlo= 3
# xhi= 3 
# ylo=4
# yhi=5  
#xlo= 1 
#xhi= 10 
#ylo=1 
#yhi=10  
#xlo= -6 
#xhi= 3 
#ylo=-5 
#yhi=4  


#----------------
#blo=7 #3 
#slo = 8  #3

#diam =5 
#xlo= 7
#xhi=11
#ylo=  10
#yhi= 11
#
#
#xlo= 7
#xhi=11
#ylo=  8
#yhi= 12
#
#xlo= 9
#xhi=9
#ylo=  11
#yhi= 11


#xlo= 10
#xhi=11
#ylo=  10
#yhi= 10



#----------------
diam =3
xlo= 2
xhi= 6
ylo=2
yhi=6

beta70=0.98 #1 #0.99 #1.0
nbeta70 = 1-beta70

#=============================

h=1040 #h=180 #h=730 #h=360 #w=h*2
w=h

p=0.25 #0.16
a = 1.0*(rand( h, w )<p)    

#x11 = floor(linspace(xlo, xhi + 0.999, w))
#y11 = floor(linspace(yhi + 0.999 , ylo, h))
x11 = (linspace(xlo, xhi + 0.999, w))
y11 = (linspace(yhi + 0.999 , ylo, h))
xx, yy = meshgrid(x11, y11)
 
blo=2.98 #3*beta70 #xx #3
bhi=xx
slo=2. #3*beta70 #yy - 1 #slo = 3
shi=yy

niter = 3000   
sli=0 #0.1 #0 #0.01
skipy=5 #1 #37 #5 #2






bfade =  False   #True  # False
q = 0.3 #0.1
#qqq=1.8
qqq=4 #8
#q = 1. / 2.
afade = 0.1 * a
#averyold = 0*a



#matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
matplotlib.rc("image",cmap="summer")
matplotlib.rc("image",interpolation="nearest")
##np.dstack()
##np.concatenate()
###(tup, axis=2)


#execfile('backend_LtL_imshow.py')
##execfile('backend_LtL_pygame.py')
execfile('backend_bLtL_pygame.py')
