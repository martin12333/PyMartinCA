from pylab import *
import numpy as np

#parameters are described at PARAMETERS.txt

r=1

diam = 2*r + 1

bmin=3
bmin0=1
smin=3
smin0=1
bmax0=3#xx
#smax=4#3#yy
smax0=4#3#yy
bmin0=2; bmax0=2; smin0=2; smax0=2
bmin0=3; bmax0=3; smin0=3; smax0=4


ndbmin=3; ndbmax=3; ndsmin=3; ndsmax=3
ndbmin=3; ndbmax=7; ndsmin=3; ndsmax=1
ndbmin=3; ndbmax=7; ndsmin=3; ndsmax=7
#ndbmin=3; ndbmax=1; ndsmin=3; ndsmax=1
ndbmin=4; ndbmax=4; ndsmin=4; ndsmax=4
ndbmin=3; ndbmax=4; ndsmin=3; ndsmax=4
ndbmin=1; ndbmax=1; ndsmin=1; ndsmax=1


#

#xhi=xlo+dx52
#yhi=ylo + dy52

#=============================

w=64*diam #256 #1850 #2000 #2250 #1800
h=w #256 #1300 #1400 #950

w0=128
h0=128

w2=16#25#16
h2=16#25#16

#

np.random.seed()      


#=============================

###x11 = floor(linspace(xlo, xhi + 0.999, w))
###y11 = floor(linspace(yhi + 0.999 , ylo, h))
#x11 = (linspace(xlo, xhi , w))
#y11 = (linspace(yhi  , ylo, h))
#xx, yy = meshgrid(x11, y11)
 
#

ns=15#30#1 #7#10 #3

pskip=0


niter =4000#2400 #300#150# 600 #300 #400 #200 #1000 #3000   
niter0=niter-150
#sleep1=    0 #0.3      #0.1 #0 #0.01
step1=12 #4 #20 #8 #15 #5 #1 #37 #2
step2=60 #120 #1

bfade = False#True  # False
q = 0.1#0.9 #0.8#0.7 #0.3 #0.1 
###qqq=0.2 ###0 #0.5 #1#2 #4 #8 #1.8

#




#execfile('backend_LtL_imshow.py')
#execfile('backend_LtL_pygame.py')
#execfile('backend-LtL-pop-plot-sanity-check.py')

execfile('backend-LtL-pop-plot-only-plot.py' )
#execfile('backend-LtL-automated.py' )

