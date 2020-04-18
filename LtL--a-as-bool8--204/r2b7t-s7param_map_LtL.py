from pylab import *
import numpy as np

#parameters are described at PARAMETERS.txt

r=2

bmin=7
smin=7

xlo=7; dx52=6;  ylo=9; dy52=3

#

xhi=xlo+dx52
yhi=ylo + dy52

#=============================

w=1850 #2000 #2250 #1800
h=950 #1300 #1400 #950

#

np.random.seed()      
p=0.5 #0.25 #0.16
a = (rand( h, w )<p) 

#=============================

###x11 = floor(linspace(xlo, xhi + 0.999, w))
###y11 = floor(linspace(yhi + 0.999 , ylo, h))
x11 = (linspace(xlo, xhi , w))
y11 = (linspace(yhi  , ylo, h))
xx, yy = meshgrid(x11, y11)
 
bmax=xx
smax=yy

#

niter = 300 #400 #200 #1000 #3000   
sleep1=    0 #0.3      #0.1 #0 #0.01
step1=8 #4 #20 #8 #15 #5 #1 #37 #2
step2=60 #120 #1

bfade = True  # False
q = 0.1#0.9 #0.8#0.7 #0.3 #0.1 
###qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8

#

afade = 0.1 * a
averyold = a 

diam = 2*r + 1


#execfile('backend_LtL_imshow.py')
execfile('backend_LtL_pygame.py')
