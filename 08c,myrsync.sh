#!/bin/bash

#`#--dry-run` --update 
# --progress --stats

opt=' -v  '


#088 not phys to virt Dr anymore because vibo clock, etc
#089
#08c entire beta



echo 'phys to virt ========================================'

########luckybackup

####rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/beta/JUPYTER/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/JUPYTER/

####rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/beta/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/

####rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/

###rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/ martin@127.0.0.1:/home/martin/grdr20/

rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Downloads/RSYNC/ martin@127.0.0.1:/home/martin/Downloads/RSYNCrem/

echo 'virt to phys ========================================'


rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/Downloads/RSYNCrem/ /home/martin/Downloads/RSYNC/


echo 'virt to phys ========================================'


##rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/JUPYTER/   /home/martin/Dropbox/grdr20/PyMartinCA/beta/JUPYTER/
rsync -h  $opt    -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/   /home/martin/Dropbox/grdr20/PyMartinCA/beta/

##echo 'virt to phys ========================================'
##rsync $opt -h  -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/testOfRules/   /home/martin/Dropbox/grdr20/PyMartinCA/beta/testOfRules/


echo 'virt to phys ========================================'

sshport=2223 ;  rsync  `#--dry-run`  --backup --backup-dir=$HOME/Documents/rsync.bak/  $opt   -h  -r -tgo -p --update --files-from=$HOME/Dropbox/git...ls-files  --protect-args   -e "ssh -p $sshport" martin@127.0.0.1:/home/martin/  ~/Dropbox/$sshport/

