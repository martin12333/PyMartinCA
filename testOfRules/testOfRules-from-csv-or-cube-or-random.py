#program version 402

from __future__ import print_function
from __future__ import division

##%matplotlib notebook
##%matplotlib inline
##from matplotlib import pyplot as plt

import math
import lifelib

import sys
import random

################ tunable parameters

is_from_csv=False
is_from_random=True

batch8=8#3 #4#8

################ tunable parameters

nrnd=6*8 #5#50

################ tunable parameters

r=2

bmin0=7; bmax0=7; smin0=7; smax0=10
bmin0=7; bmax0=7; smin0=7; smax0=9
bmin0=7; bmax0=7; smin0=6; smax0=9
bmin0=7; bmax0=7; smin0=5; smax0=9
bmin0=7; bmax0=7; smin0=5; smax0=8
bmin0=6; bmax0=7; smin0=5; smax0=8
bmin0=5; bmax0=7; smin0=4; smax0=8
bmin0=6; bmax0=7; smin0=4; smax0=8
bmin0=6; bmax0=7; smin0=6; smax0=8
# bmin0=7; bmax0=11; smin0=7; smax0=10
#bmin0=7; bmax0=8; smin0=6; smax0=10
#bmin0=7; bmax0=9; smin0=7; smax0=10
#bmin0=6; bmax0=6; smin0=6; smax0=6
#bmin0=5; bmax0=6; smin0=5; smax0=6
#bmin0=4; bmax0=5; smin0=4; smax0=5

# ndbs=1
ndbmin=1; ndbmax=6; ndsmin=1; ndsmax=2
ndbmin=1; ndbmax=6; ndsmin=1; ndsmax=3
ndbmin=1; ndbmax=8; ndsmin=1; ndsmax=3
ndbmin=1; ndbmax=8; ndsmin=3; ndsmax=4
ndbmin=1; ndbmax=8; ndsmin=4; ndsmax=4
ndbmin=2; ndbmax=8; ndsmin=4; ndsmax=4
ndbmin=2; ndbmax=8; ndsmin=2; ndsmax=4
ndbmin=2; ndbmax=8; ndsmin=2; ndsmax=3
# ndbmin=1; ndbmax=1; ndsmin=1; ndsmax=1
#ndbmin=3; ndbmax=1; ndsmin=3; ndsmax=1
#ndbmin=2; ndbmax=3; ndsmin=2; ndsmax=3
#ndbmin=3; ndbmax=3; ndsmin=3; ndsmax=3
#ndbmin=3; ndbmax=4; ndsmin=3; ndsmax=4
#ndbmin=2; ndbmax=6; ndsmin=2; ndsmax=5
#ndbmin=3; ndbmax=6; ndsmin=3; ndsmax=5
#ndbmin=5; ndbmax=8; ndsmin=5; ndsmax=8





################ tunable parameters







#justname='p100520'
justname='random'

justnameext=justname+'.csv'




output_strlist=[]
rulestr=None

####
input_file1='default.rules.csv'
# input_file1='borderline1.rules.csv'
input_file1='input-borderline1.rules.csv'
input_file1='input-borderline1-Copy1.rules.csv'
input_file1='input-ltl-r2-2.rules.csv'
# input_file1='input-ltl-r2-12.rules.csv'
# input_file1='input-ltl-r2-18.rules.csv'
input_file1='input-ltl-r3-01.rules.csv'
input_file1='input/aselftest317-ltl-r3-08.rules.csv'
input_file1='input/aselftest340-ltl-r3-08.rules.csv'
input_file1='input/g3ltl-r2-3.rules.csv'
# input_file1='input/input-ltl-r3-16.rules.csv'
# input_file1='input/input-ltl-r3-03-Copy1.rules.csv'
input_file1='input/'+justnameext
input_file1='lifelib-input/'+justnameext


output_file1='output-2.rules.csv'
output_file1='output-borderline1-2.rules.csv'
output_file1='output-ltl-r2-02.rules.csv'
output_file1='output/output-ltl-r3-0.rules.csv'
output_file1='output/output-ltl-r3-1.rules.csv'
output_file1='output/fromcsv-ltl-r3-2.rules.csv'
output_file1='output/fromcsv-g3ltl-r2.rules.csv'
output_file1='output/'+justnameext


#unit1=100#1250#600#1500#800#900#400#200#100#50#1000#256#128
##wt=1800##3000#2400#1800#1500#1200#900#700
w2=6000#3000#1600#800#200#500#400#200#100#50#1000#256#128#16#25
h2=30#w2#16
#maxtime=4*unit1 #*2
maxtime=w2//2#2000#w2#*2 #*4#*2
halftime=maxtime//2
##niter =wt#600#500#400#300#6##1000#500###800 # #1500
hthreshold=w2//2#1200#800#400:#200:#100:

step1=24#12 #4 #20 #8 #15 #5 #1 #37 #2
#step2=120#12#60 #120 #1


#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################


space1=' '
#rest1=space1.join(sp5[i5+2:])
rest1=''
#print(rest1)


p1=None
rulestr=None
fPPratio=None
ii1=1


def main1():
    global p1,rulestr,fPPratio,ii1

    ###################

    #plt.figure()

    ##plt.yscale('log')
    #plt.loglog()

    #plt.ion()
    ##plt.ioff()

    ###################


    with open(output_file1,'a') as f1:
        print( file=f1)


    #schema1='tag1,time_s,time11,pop_s,population,ratio_s,PPratio,log2PP,space_s,w2,h2,w,h,rule_s,rulespace,rulestr'
    schema1='tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr,x,sumpop'
    print(schema1.replace(',',' '))


###################

    sp0=None
    
    ####
    random.seed()
    ####

    if is_from_csv:
        with open(input_file1) as f0:
            input1=f0.read()

    elif is_from_random:

        for irnd in range(nrnd):

#            xb=random.getrandbits(15) & random.getrandbits(15)
            xx=random.getrandbits(15) 
            
#            xb=(random.getrandbits(15) |xx)&random.getrandbits(15)
##            xb=(random.getrandbits(15) &xx)&random.getrandbits(15)
            xb=(random.getrandbits(15) &xx)

#            xs=(random.getrandbits(15) |xx)&random.getrandbits(15)
#            xs=(random.getrandbits(15) &xx)|random.getrandbits(15)
            xs=random.getrandbits(15) & random.getrandbits(15)
            xs=random.getrandbits(15) & random.getrandbits(15)  & random.getrandbits(15)
            xs=xs|xb

            xb=xb << 4
#            xb=xb << 5
            
            
            xs=xs << 4
            
            
            #523776
            #(x)

            ##uintx2=x
            ##uintx=x>>1

            #hexstring1=format(uintx, '06x')
            #hexstring1=format(uintx, '0'+    str(r*(r+1))        +'x')

            #('03ff00')


            #rulestr='r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)
            #rulestr='g3r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)
            ##rulestr='g3r2b{:07x}s{:06x}'.format(irnd,x)
            rulestr='g3r2b{:06x}s{:06x}'.format(xb  ,xs)
            ##rulestr='g3r2b{}s{}'.format(hexstring1,x)
            rulestr='g6r2b{:06x}s{:06x}'.format(xb  ,xs)
            rulestr='r2b{:06x}s{:06x}'.format(xb  ,xs)

            rule_s='rule'
            rulespace='lifelib'


###                print(rule_s,rulespace,rulestr)
######                with open(output_file1,'a') as f1:
######                    print(rule_s,rulespace,rulestr, file=f1)

            ##output_strlist+=  [rule_s,rulespace,rulestr].join(' ')   ' '.join       '{} {} {}'
            output_strlist.append(  ' '.join([rule_s,rulespace,rulestr])   )


#######################################################
    else:

        for dbmin in range(ndbmin):

            bmin=bmin0+dbmin

        ######    

            for dsmin in range(ndsmin):

                smin=smin0+dsmin

                for dsmax in range(ndsmax):

                    smax=smax0+dsmax


                        ###########

                    for dbmax in range(ndbmax):

                        bmax=bmax0+dbmax


        #############################################################################3###################
        #############################################################################3###################
        #######



                        #rulestr='r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)
                        rulestr='g3r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)

                        rule_s='rule'
                        rulespace='lifelib'


        ###                print(rule_s,rulespace,rulestr)
        ######                with open(output_file1,'a') as f1:
        ######                    print(rule_s,rulespace,rulestr, file=f1)

                        ##output_strlist+=  [rule_s,rulespace,rulestr].join(' ')   ' '.join       '{} {} {}'
                        output_strlist.append(  ' '.join([rule_s,rulespace,rulestr])   )


    ###################

    if is_from_csv:

        sp0=input1.splitlines()

    else:

        sp0=output_strlist


    #################3



    ##

    list1=sp0
    while list1:
    #     /print len(list1)
        if len(list1)>=   batch8:
            smalllist=list1[:batch8]
            list1=list1[batch8:]
        else:
            smalllist=list1
            list1=[]
        test_8_rules(smalllist)
    
    
    return

    ###################

    #for dbs in range(-ndbs,ndbs+1):
    ##for dbs in range(-1,2):
    ##for dbmax in range(ndbmax):

        #bmin=bmin0#+dbs
        #bmax=bmax0+dbs
        #smin=smin0#+dbs
        #smax=smax0#+dbs

        #rulestr='b3s23'
        #rulestr='r2b7t12s7t10'  ## niter <2000 or too much memory ? RADEJI ZATIM NEDAVAT DO FORUM
        #rulestr='b{}s23'.format(bmax)
        ######rulestr='r1b3t{}s3t4'.format(bmax)
        ##rulestr='r2b7t12s7t10'.format(bmax)
        #rulestr='r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)
    




###################
##############
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#######


    
def test_8_rules(list8)    :
    global p1, rulestr
    ###rulestrlist=[  'r{}b{}t{}s{}t{}'.format(r,bmin,bmax,smin,smax)  for   bmax in range(bmax0, bmax0+ndbs)  ]#
    rulestrlist=[ cut_rulestr_from_str(x)   for  x in list8 ]#

    try:
        #sess = lifelib.load_rules(rulestr)
        sess = lifelib.load_rules(*rulestrlist)
        #1/0
    except:
        exc_info1=sys.exc_info()
        #print("Unexpected error:", exc_info1[0])#, exc_info1[1])
        print("error:", exc_info1[0], exc_info1[1])
        #raise
        #continue
        return
    
    ###################
 
    lt = sess.lifetree()

    for rulestr in rulestrlist:
        
        p1=lt.pattern(rule=rulestr)
        p=0.3###08#02#05 #1#2#3#4#5 
        p1[0:h2, 0:w2] = p

        ################################
        test_rule()
        ################################
        
#     /print rulestrlist

    return
    

#############################################################################3###################
    
    
def cut_rulestr_from_str(str1):
    sp5=str1.split()
    #print(sp5)
    i5=sp5.index('lifelib')
    rulestr=sp5[i5+1]
    #print(rulestr)
    
    ##space1=' '
    ##rest1=space1.join(sp5[i5+2:])
    
    ##return [rulestr,rest1]
    return rulestr


##############
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################
#######
# in p1
# out p1, fPPratio
def test_rule():
    global p1, fPPratio, ii1
    
    ###pass

    pops = []
    gens = []
    hs=[]
    ws=[]
    ys=[]
    
    #####p1 = p1[niter]

    population_niter = None
    sumpopeverygen=0
    
    ##currgen = 0
    ##for _ in range(int(niter/step2)):
    for currgen in range(0,  maxtime, step1):
        
        ####
        
        p1=p1[step1]
        
        ####
        sumpopeverygen += p1.population * step1
        
        if sumpopeverygen> 100e6:#500e6:
            break ###
        
        ####
        
        if currgen//step1 == halftime//step1:
            population=p1.population ;  population_niter = population


        pops.append(p1.population)
        gens.append(currgen)
        
        bb=p1.bounding_box
        h=1
        w=1
        if bb:
            h=bb[2]-bb[0]
            w=bb[3]-bb[1]
        hs.append(h)
        ws.append(w)
        #ys.append(p1.population/h)
        ys.append(p1.population/(1+currgen))
        
        if h> hthreshold:#400:#200:#100:
            break ###
        
            
#     !free -m

    #######################################

    #plt.plot(gens, pops)
    #plt.plot(gens, hs)
    ###plt.plot(gens, pops/hs)
#     plt.plot(gens, ys)
    #plt.show()

    
    #######################################

    #print(tag1,time_s,time11,pop_s,population,space_s,w2,h2,w,h,rule_s,rulespace,rulestr)

    #######################################

    #####p1 = p1[niter]

    #######################################

    bb=p1.bounding_box
    #print(bb)

    h=1
    w=1
    if bb:
        h=bb[2]-bb[0]
        w=bb[3]-bb[1]


    tag1='soup'
    time_s='time'
    time11=currgen  ###  maxtime
    pop_s='pop'
    population=p1.population ;  population_2niter = population
    space_s='space'
    rule_s='rule'
    rulespace='lifelib'

    ratio_s='ratio'
    ######fPPratio= population_2niter/population_niter
    #######fPPratio= population_2niter/(population_niter+1)
    fPPratio= population_2niter/(pops[currgen//step1//2]+1)
    PPratio= '{:.1f}'.format(fPPratio)
    #log2PP= '{:.1f}'.format(math.log2(fPPratio) )

    #print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,log2PP,space_s,w2,h2,w,h,rule_s,rulespace,rulestr)
    #print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr)
    #print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr,rest1)
#     print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr, 'sumpop' , sumpopeverygen,    rest1)
    
    if h>300:
        if fPPratio<1.6:
            prefix1='*'
        else:
            prefix1='@'
    else:
        if fPPratio>1.2 :
            prefix1='?'
        else:
            prefix1='.'
        
    print(prefix1,tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr, 'sumpop' , sumpopeverygen, ii1,   rest1)
        
        
    with open(output_file1,'a') as f1:
        #print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,log2PP,space_s,w2,h2,w,h,rule_s,rulespace,rulestr, file=f1)
        #print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr,  'sumpop' , sumpopeverygen,    rest1, file=f1)
        print(tag1,time_s,time11,pop_s,population,ratio_s,PPratio,space_s,w2,h2,w,h,rule_s,rulespace,rulestr,  'sumpop' , sumpopeverygen,  'i', ii1,  rest1, file=f1)
       
    ii1+=1
    
    #####################################
    ##del p1
    ##del lt
    ##del sess
    #!free -m
    
    return

#end def test_rule




##############
#############################################################################3###################
#############################################################################3###################
#############################################################################3###################

main1()
    
#!free -m

# if fPPratio < 1.5:
#     p1.viewer()
