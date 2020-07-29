# a devel version
#program version 070

from __future__ import print_function
#from __future__ import division
import numpy as np
import re

############## INPUT DATA

# M0 ... HROT

r=None
d=None#2*r+1

input1='''
R2,C2,S9-18,B4

R2,C2,S6-9,B7-9
R2,C2,S6-9,B7-8
R2,C2,S5-9,B7-8
'''
#################
''' todo test R3 C3
6-9,12,14,17,19,20,24
7,10,16,17,18,19,20,21
6-9,12,14-15,17-21,23-24
7,11-12,14-17,19-24
34-45
33-57
'''

######## I SHOULD-NOT FORGET M0 00000000000000000000000000
''' WRONG
7-10
6-10
34-58
'''

######## 
def main1():
        for x in input1.splitlines():
                if x.strip():
                print(x)

#     for lifeviewer_rulestr_part in lifeviewer_rulestr_part_list.splitlines():
#         hexstring1=lifeviewer_rulestr_part_to_lifelib(lifeviewer_rulestr_part)
#         print(hexstring1)

    return

######## 
def lifeviewer_rulestr_part_to_lifelib(sbss):




    atable1=np.zeros( d*d , dtype=int)

    #atable1[9:19]=1

    for si in sbss.split(','):
        if '-' in si:
            si2=si.split('-')
            lo1=int(si2[0])
            hi1=int(si2[1])
        else:
            lo1=int(si)
            hi1=lo1

        atable1[lo1:hi1+1]=1

    #('[0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0]')
    #str(list(atable1))
    str(atable1)


    x=0
    for i in range(d*d):
            if atable1[i] != 0:
                    x=x|(1<<i)
                    
    #523776
    #(x)

    uintx2=x
    uintx=x>>1

    ###hexstring1=format(uintx, '06x')
    hexstring1=format(uintx, '0'+        str(r*(r+1))                +'x')

    return hexstring1
######## 

######################
main1()
