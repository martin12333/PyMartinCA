cd ~/apgmera
pwd 
echo
  time ./apgluxe -L 1 -t 1  --rule "$2"  -n 2000 #1000

cd ~/apgmera
pwd 

mv -i -v --target-directory=oldlog/ log.*.txt

#cd ~
#cd grdr20/PyMartinCA/beta/testOfRules/

