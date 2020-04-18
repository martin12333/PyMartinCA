from pylab import *
import numpy as np

#parameters are described at PARAMETERS.txt

r=2

bmin=7
smin=7

xlo=7; dx52=6;  ylo=8; dy52=3
xlo=7; dx52=6;  ylo=8; dy52=4
xlo=8; dx52=4;  ylo=10; dy52=4
xlo=8; dx52=4;  ylo=14; dy52=4
xlo=8; dx52=4;  ylo=18; dy52=4
xlo=8; dx52=4;  ylo=22; dy52=4
xlo=11; dx52=1;  ylo=11; dy52=14
xlo=11; dx52=1;  ylo=11; dy52=4
xlo=11; dx52=1;  ylo=15; dy52=4
xlo=11; dx52=1;  ylo=15; dy52=3
xlo=11; dx52=1;  ylo=16; dy52=10
xlo=11; dx52=1;  ylo=16; dy52=2

#

xhi=xlo+dx52
yhi=ylo + dy52

#=============================

w=1850 #2000 #2250 #1800
h=950 #1300 #1400 #950
#w=dx52*256
#h=dy52*256

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
smax=10#yy

bmax22=floor(yy) #yy.round()

#

niter = 3000 #2000#1500# 600#300 #400 #200 #1000 #3000   
sleep1=    0 #0.3      #0.1 #0 #0.01
step1=8 #4 #20 #8 #15 #5 #1 #37 #2
step2=120#60 #120 #1

bfade = True  # False
q = 0.1#0.9 #0.8#0.7 #0.3 #0.1 
###qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8

#

afade = 0.1 * a
averyold = a 

diam = 2*r + 1


#execfile('backend_LtL_imshow.py')
execfile('backend_LtL_pygame.py')
