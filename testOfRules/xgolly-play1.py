#program version 010
#from __future__ import print_function
from __future__ import division

################ tunable parameters

w2=1600#800#200#500#400#200#100#50#1000#256#128#16#25
h2=30#w2#16
#maxtime=4*unit1 #*2
maxtime=w2#*2 #*4#*2
halftime=maxtime//2
##niter =wt#600#500#400#300#6##1000#500###800 # #1500
hthreshold=800#400:#200:#100:

step1=12 #4 #20 #8 #15 #5 #1 #37 #2
#step2=120#12#60 #120 #1


import golly as g

from glife import rect
#import glife

#print dir(g)
#print 'sfds'

####rulestr='r2b7t9s7t10'
rulestr='B2cek3cky4cektwz5qr6ckn7/S01c2aen3-eir4-aiqz5-acy6e'

g.new("my-play1")
g.setrule(rulestr)

#######print g.__dict__

#blinker = g.parse("3o!")

p=0.5 #0.3#0.5 #0.25 #0.16
##a[ h0 : h0+h2 , w0 : w0+w2 ] = (rand( h2, w2 )<p) 
##p1[0:h2, 0:w2] = p
g.select([0,0,w2,h2])
g.randfill(int(100*p))

#print blinker	

#g.putcells(blinker, 6, -40, 1, 0, 0, 1, "xor")

bbox = rect( g.getrect() )

print bbox
