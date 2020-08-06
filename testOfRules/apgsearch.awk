BEGIN {
xs=0;xp=0;xq=0;y=0;z=0;
}

/@ROOT/ {root=$2; }

/@RULE/ {rule=$2; }

/@NUM_SOUPS/ {NUM_SOUPS=$2}
/@NUM_OBJECTS/ {NUM_OBJECTS=$2}

/^xs/ {xs++}
/^xp/ {xp++}
/^xq/ {xq++}
/^y/ {y++}
/^z/ {z++}

END{print  "@RULE",rule, "@ROOT",root , "NUM_SOUPS",NUM_SOUPS, "NUM_OBJECTS", NUM_OBJECTS, "xs",xs, "xp", xp, "xq", xq, "y",y,"z",z }
