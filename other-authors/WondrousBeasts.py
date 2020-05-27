# WondrousBeasts.py
# painfully slow Larger than Life rule simulator
# (pretty much only works for patterns with reliably limited bounding boxes..)

import golly as g

g.addlayer()
g.new("WondrousBeasts")
g.putcells(g.parse("""32b4o$30b7o$29b10o$28b12o$28b13o$27b3o5b6o$5b3o19b3o5b6o$3b7o17b3o5b6o
$2b9o16b3o5b6o$b12o15b3o2b8o$b13o14b12o$5o3b6o15b10o$2o7b5o16b7o$2o7b
5o18b3o$3o5b6o$3o2b9o$b3ob8o$2b10o$3b7o$4b5o!"""))

if g.numstates()>2: g.exit("Please switch to a two-state rule.")

while 1:
  rmin=g.getrect()
  r=[rmin[0]-5,rmin[1]-5,rmin[2]+10,rmin[3]+10]
  newlist=[]
  for j in range(r[1],r[1]+r[3]):
    for i in range(r[0],r[0]+r[2]):     
      count=0
      for y in range(-7,8):
        for x in range(-7,8):
          count+=g.getcell(i+x,j+y)
      # for now, just hard-code the Wondrous Beasts rule
      #   (we'll generalize later)
      #     (and speed things up a lot)
      #  rule = R7,C0,M1,S65..114,B65..95,NM
      if g.getcell(i,j)==1:
        if count<65 or count>114: newlist+=[i,j,0]
      else:
        if count>=65 and count<=95: newlist+=[i,j,1]
  if len(newlist)%2==0: newlist+=[0]
  g.putcells(newlist,0,0,1,0,0,1,"copy") # use copy mode so the state-0 cells overwrite state-1 cells
  g.setgen("+1")
  g.update()
