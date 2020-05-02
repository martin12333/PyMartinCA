from pylab import *
import numpy as np

#parameters are described at PARAMETERS.txt

r=2

diam = 2*r + 1

bmin0=7; bmax0=11; smin0=7; smax0=10
bmin0=7; bmax0=8; smin0=6; smax0=10
#bmin0=6; bmax0=6; smin0=6; smax0=6
#bmin0=5; bmax0=6; smin0=5; smax0=6
#bmin0=4; bmax0=5; smin0=4; smax0=5

ndbmin=1; ndbmax=1; ndsmin=1; ndsmax=1
#ndbmin=3; ndbmax=1; ndsmin=3; ndsmax=1
#ndbmin=2; ndbmax=3; ndsmin=2; ndsmax=3
#ndbmin=3; ndbmax=4; ndsmin=3; ndsmax=4
#ndbmin=2; ndbmax=6; ndsmin=2; ndsmax=5
#ndbmin=3; ndbmax=6; ndsmin=3; ndsmax=5
#ndbmin=5; ndbmax=8; ndsmin=5; ndsmax=8
pskip=0


#

#xhi=xlo+dx52
#yhi=ylo + dy52

#=============================

w=320#256##320#240#320 ##64*diam #256 #1850 #2000 #2250 #1800
h=w #256 #1300 #1400 #950

w0=40#64#128
h0=40#64#128

w2=240#128#16#25#16
h2=240#128#16#25#16
#


np.random.seed()      


#=============================

###x11 = floor(linspace(xlo, xhi + 0.999, w))
###y11 = floor(linspace(yhi + 0.999 , ylo, h))
#x11 = (linspace(xlo, xhi , w))
#y11 = (linspace(yhi  , ylo, h))
#xx, yy = meshgrid(x11, y11)
 
#

ns=9#5#7#20#30#1 #7#10 #3



#3000#1600 #550 #300#150# 600 #300 #400 #200 #1000 #3000   
niter =1700#900#300#150 #plot
niter0=niter-50
#sleep1=    0 #0.3      #0.1 #0 #0.01
step1=12#60##12 #4 #20 #8 #15 #5 #1 #37 #2
step2=60*3#*2 #120 #1

bfade = False#True  # False
q = 0.1#0.9 #0.8#0.7 #0.3 #0.1 
###qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8

#




#execfile('backend_LtL_imshow.py')
#execfile('backend_LtL_pygame.py')
#execfile('backend-LtL-pop-plot-sanity-check.py')

execfile('backend-LtL-pop-plot.py' )
#execfile('backend-LtL-automated.py' )



