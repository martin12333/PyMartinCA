from __future__ import print_function

from scipy.ndimage import filters
import time

from pylab import *
import matplotlib.pyplot as plt

print(ndbmin* ndbmax* ndsmin* ndsmax)

print(ns*(1-pskip)*ndbmin* ndbmax* ndsmin* ndsmax)

#matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")

#matplotlib.rc("image",interpolation="nearest")


plt.ion()
#plt.ioff()


#img_plot = plt.imshow(a)
#plt.show(block=False)


####plt.matshow())
##plt.figure()
#### wrong: extent=(xlo, xhi, ylo, yhi) ) 
##, interpolation="nearest")
##, cmap = plt.cm.gray)



OR = logical_or
AND = logical_and

id1=-1

plotysum=zeros( (niter,1) )

for j in xrange(ns):


    for dbmax in range(ndbmax):

        bmax=bmax0+dbmax

        for dsmax in range(ndsmax):

            smax=smax0+dsmax


            for dbmin in range(ndbmin):

                bmin=bmin0+dbmin

                for dsmin in range(ndsmin):

                    smin=smin0+dsmin


                    if   rand()<pskip  or  bmax<bmin or (smax+1) < smin: continue #####not break
                    
                    
                    
                    id1+=1
                    
                    
                    
                    

                    p=0.5#0.3#0.5 #0.25 #0.16
                    
                    a = zeros( ( h, w ), dtype=bool) 
                    a[ h0 : h0+h2 , w0 : w0+w2 ] = (rand( h2, w2 )<p) 
                    
                    #a=(rand( h, w )<p) 


                    
                    afade = 0.1 * a
                    ##averyold = a #########??
                    averyold = 0 
                    aold360=0
                    aold420=0
                    aold840=0
                    
                    
                    
                    plotx=zeros( (niter,1) )
                    ploty=zeros( (niter,1) )
                    plotz=zeros( (niter,1) )
                    
                    dam51=0
                    
                    
                    
                    
                    iper=0
                    
                    ahistory=[0]*int(3+niter/12)
                    assert step1==12
                    
                    
                    settleTime=2e9


                    for i in xrange(1,niter):

                        n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  
                        n=n41.round()   
                        birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
                        survi = AND(  n>=smin,  AND( n<=smax, a )  )
                        a =  OR( birth , survi )  

                        #as51=(0.0+a).sum()
                        am51=(0.0+a).mean()

                        ######settleTime=i

                        plotx[i]=i
                        ploty[i]=am51 #as51



                        if (i % 12)==0:
                            ahistory[i/12] =a

                        
                        
                        if (i % 24)==0:
                            aslower=ahistory[i/24]
                            if (a==aslower).all() :
                                #print(' ',i,id1)
                                if iper==0:
                                    settleTime=i/2
                                    iper=i
                                else:
                                    print(' i-iper',i-iper,id1)
                                    break
                            




                        if (i % step1)==0:

                            if bfade:
                                afade = q*a + (1-q)*afade
                                asho=afade
                            else:
                                asho=0+a
                                
                            ada51= logical_xor(a, averyold)  
                            averyold =a 


                            olddam51=dam51
                            dam51=ada51.mean()
                            
                            plotz[i]=dam51

                            if dam51 == 0 :
                                settleTime=i
                                #print('dam51==0',id1)
                                break
                            
                            
                            
                            
                            
                            
                            
                            
                            ##adaimage = transpose( ( ( asho)))
                            ##b = array(255*clip(adaimage,0,1),'B')

                            ###imshow(asho)
                            #show()


                            #img_plot.set_data(asho)
                            #plt.draw()


                            ##time.sleep(sleep1)
                            
                            
                        if (i % 360)==0:
                            if (a==aold360).all():
                                print(' p360:',i,iper,id1)
                                #print(i,am51,dam51,bmin,bmax,smin,smax)
                                settleTime=i-360
                                break
                            aold360=a

                        if (i % 840)==0:
                            if (a==aold840).all():
                                print(' p840:',i,iper,id1)
                                #print(i,am51,dam51,bmin,bmax,smin,smax)
                                settleTime=i-840
                                break
                            aold840=a


                        #250#175: #0.200 
                        if i ==100 and am51 >0.320:
                            break

                        if i ==200 and am51 >0.300:
                            break



                        if i ==300 and am51 >0.290:
                            break




                        if i ==500 and am51 >0.270:
                            break




                        if i ==700 and am51 >0.240:
                            break


                        if (i % step2)==0:
                            sam51='{:.3f}'.format(am51)
                            sdam51='{:.3f}'.format(dam51)
                            #print( i, sam51, sdam51)
                            
                            #if am51 >0.250:#175: #0.200 :
                                #break #################250


                    dam51=olddam51
                    
                    if i<settleTime:
                        settleTime=i
                        
                    sam51='{:.3f}'.format(am51)
                    sdam51='{:.3f}'.format(dam51)
                    #if dam51>0.005 and dam51<0.150 and am51>0.005 and am51<0.150:
                    #if dam51>0.001 and dam51<0.150 and am51>0.001 and am51<0.150:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and settleTime>70:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and settleTime>150:
                    #if dam51>0.001 and dam51<0.150 and am51>0.000 and am51<0.150 and settleTime>450:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and settleTime>450:
                    #if  am51>0.000 and am51<0.175 and settleTime>400:
                    if  dam51<0.150 and am51>0.000 and am51<0.175 and settleTime>200:#50:#500:#1000:#400:#600: #1200:
                        print('pmc11',settleTime,sam51,sdam51,'ltl',r,bmin,bmax,smin,smax,w,w2,id1)
                        #plot(ploty[:settleTime],'x')
                        #plot(ploty,'x-')
                       
                    
                    
                    if am51<0.999:#500:#100: #500: #0.200 :
                        plot(ploty[:settleTime],'x')
                        #plot(ploty,'x-')
                        ##plot(plotz,'x')
                        ##plot( ploty[niter0:], plotz[niter0:],'x')
                    
                    
                    
                    
                    ##plotysum += ploty
                    
                    
                    
                    
