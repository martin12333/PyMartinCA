import golly as g

class soup:
    def __init__(self,kmax):
        self.pop=[0]*kmax #Population of pattern
        self.dpop=[0]*kmax #Change of population wrt previous generation
        

kmax=int(g.getstring("Maximum number of generations:","2000"))
ns=int(g.getstring("Number of scans:","20000"))
alpha=soup(kmax)
k=0
g.show("Press q to stop at any point.")
for j in xrange(ns):
    g.new("Spectrum_scan_"+str(j))
    g.select([0,0,16,16]) # These two lines can be substituted to analyse different patterns
    g.randfill(30)
    temp_pop=int(g.getpop())
    alpha.pop[0]+=temp_pop
    alpha.dpop[0]=0 # IMPORTANT: Ignore first data point for FT
    for i in xrange(kmax-1):
        g.run(1)
        alpha.pop[i+1]+=int(g.getpop())
        alpha.dpop[i+1]+=int(g.getpop())-temp_pop
        temp_pop=int(g.getpop())
    try:
        g.select(g.getselrect())
        g.clear(0)
    except: pass
    event=g.getevent()
    if event.startswith("key q none"):
        ns=j
        break
File=open("geneascopy_ns_%d.txt"%ns,"w+")
File.write("Gen\tPop\tdPop\tln(dPop^2)/2\tln((Pop-minpop)+1)\tabs(dPop)\t\tNS=%d\n"%ns)
minPop=min(alpha.pop)
for m in xrange(kmax):
    File.write(str(m)+"\t"+str(alpha.pop[m])+"\t"+str(alpha.dpop[m])+"\t=ln(C%d^2)/2\t"%(m+2)+"=ln(B%d-"%(m+2)+"%d+1)\t"%minPop+"=abs(C%d)\n"%(m+2))
#
File.write("\nPop{")
for n in xrange(kmax):
    File.write("%f,"%(float(alpha.pop[n])/float(ns)))
File.write("}\n\ndPop{")
for op in xrange(kmax):
    File.write("%f,"%(float(alpha.dpop[op])/float(ns)))
File.write("}")
#
File.close()
g.exit()
