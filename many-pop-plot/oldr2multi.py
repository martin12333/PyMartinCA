from pylab import *
import numpy as np

#parameters are described at PARAMETERS.txt

r=2

bmin=7; smin=6
xlo=8; dx52=0.9;  ylo=10; dy52=0.9

bmin=7; smin=7
xlo=8; dx52=3.9;  ylo=10; dy52=0.9

#

xhi=xlo+dx52
yhi=ylo + dy52

#=============================

w=256*4# 256
h=256 #

w0=128
h0=128

w2=25+256*3#16
h2=25#16

#

np.random.seed()      


#=============================

###x11 = floor(linspace(xlo, xhi + 0.999, w))
###y11 = floor(linspace(yhi + 0.999 , ylo, h))
x11 = (linspace(xlo, xhi , w))
y11 = (linspace(yhi  , ylo, h))
xx, yy = meshgrid(x11, y11)
 
bmax=xx
smax=yy

#

ns=7#10 #3

niter = 300 #400 #200 #1000 #3000   
sleep1=    0 #0.3      #0.1 #0 #0.01
step1=50 #4 #20 #8 #15 #5 #1 #37 #2
step2=50#60 #120 #1

bfade = False#True  # False
q = 0.1#0.9 #0.8#0.7 #0.3 #0.1 
###qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8

#


diam = 2*r + 1


#execfile('backend_LtL_imshow.py')
#execfile('backend_LtL_pygame.py')
#execfile('backend-LtL-pop-plot.py' )
execfile('backend-LtL-pop-plot-sanity-check.py')



