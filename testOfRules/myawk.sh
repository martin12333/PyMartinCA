grep r2 output/random$1.csv |awk '$7<1.4 && $12>300 && ($5/$9)<20 {print $0,"Pw2ratio",$5/$9,"htratio",$12/$3} '|tr -s ' ' ','|tee awk-random$1.csv|nl

