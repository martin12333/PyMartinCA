# beta ver

#NOTE: the showing of images does NOT currently work when running r2paramLtL.py from SPYDER v2.2


# evolved from
#http://nbviewer.ipython.org/github/martin12333/teaching-simso/blob/master/52-largerthanlife.ipynb
#https://github.com/thearn/game-of-life/blob/master/conway.py

from pylab import *

#=============================
diam =11 

blo=34 
slo = 34
xlo= 40
xhi=43
ylo=  58
yhi= 58

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
# diam =3   
# blo=3 
# slo = 3
# xlo= 2 
# xhi=4
# ylo=3
# yhi=7
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

#=============================

h=1040
#h=180
#h=730 
#h=360
#w=h*2
w=h

p=0.5
a = 1.0*(rand( h, w )<p)    



x11 = floor(linspace(xlo, xhi + 0.999, w))
y11 = floor(linspace(yhi + 0.999 , ylo, h))
xx, yy = meshgrid(x11, y11)

 

bhi=xx


shi=yy


niter = 3000   
sli=0.01
skipy=5 #2

bfade = False
q = 0.1
#qqq=1.8
qqq=8
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


execfile('backend_LtL_imshow.py')
#execfile('backend_LtL_pygame.py')
