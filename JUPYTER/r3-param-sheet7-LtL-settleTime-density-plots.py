
r=3
am51printthres=     0.100# 0.175
settleTimeThres=200#50:#500:#1000:#400:#600: #1200:

diam = 2*r + 1


##bmin0=7; bmax0=11; smin0=7; smax0=10
##bmin0=7; bmax0=8; smin0=6; smax0=10
bmin0=14; bmax0=18; smin0=12; smax0=20
bmin0=12; bmax0=14; smin0=12; smax0=18
bmin0=12; bmax0=14; smin0=12; smax0=19
#r3b12t14s12t19		1
#r3b12t16s12t18		1
bmin0 -= 1; bmax0 -= 1; smin0 -= 1; smax0 -= 1

#bmin0=12; bmax0=12; smin0=12; smax0=12
bmin0=12; bmax0=15; smin0=12; smax0=18
bmin0 -= 1; bmax0 -= 1; smin0 -= 1; smax0 -= 1
bmin0 -= 1; bmax0 -= 1; smin0 -= 1; smax0 -= 1




pskip=0;ndbmin=1; ndbmax=1; ndsmin=1; ndsmax=1
pskip=0;ndbmin=3; ndbmax=3; ndsmin=3; ndsmax=3
##ndbmin=3; ndbmax=1; ndsmin=3; ndsmax=1
#pskip=0;ndbmin=1; ndbmax=3; ndsmin=1; ndsmax=2
##pskip=0.5; ndbmin=4; ndbmax=12; ndsmin=4; ndsmax=10
##pskip=0.95; ndbmin=6; ndbmax=12; ndsmin=6; ndsmax=10
##pskip=0.9; ndbmin=6; ndbmax=12; ndsmin=6; ndsmax=10
#pskip=0.7; ndbmin=6; ndbmax=12; ndsmin=6; ndsmax=10
#pskip=0.3; ndbmin=6; ndbmax=12; ndsmin=6; ndsmax=10
pskip=0;ndbmin=4; ndbmax=11; ndsmin=5; ndsmax=7
ndbmin += 2; ndbmax += 2; ndsmin  += 2 ; ndsmax += 2
ndbmin += 2; ndbmax += 2; ndsmin  += 2 ; ndsmax += 2

#=============================

w=64#80#64#40#32#40#64#80#128#160#256##320#240#320 ##64*diam #256 #1850 #2000 #2250 #1800
h=w #256 #1300 #1400 #950

w0=10#5#10#15#20#30#40#64#128
h0=w0#64#128

w2=w-2*w0#240#128#16#25#16
h2=w2##240#128#16#25#16
#=============================


ns=1#9#15#30#1 #7#10 #3

niter =900 #300#150# 600 #300 #400 #200 #1000 #3000   
#niter0=niter-150

