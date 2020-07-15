    1  setopt -?
    2  setopt --help
    3  setopt 
    4  setopt >zsh.setopt
    5  # ted .zsh_hi je jiny sor
    6  guguyuyututut
    7  echo guguyuyututut
    8  sfjfjdsfkds
    9  history
   10  which sh
   11  ls -l /bin/sh
   12  #dash
   13  pip list
   14  pip --help
   15  pip --verbose
   16  pip --verbose install
   17  pip help install
   18  pip --verbose
   19  pip download jupyterlab
   20  sudo pip install jupyterlab --system
   21  sudo --help
   22  ###sudo pip install jupyterlab --system
   23  sudo -H pip install jupyterlab --system
   24  jupyter lab
   25  linuxfromscratch.org/version-check.sh
   26  pwd
   27  git init
   28  git remote add origin https://github.com/actes/newbie-attempts--dotfiles-at-s18.git
   29  git pull -v
   30  git push -u origin master
   31  ll
   32  git pull 
   33  git pull origin master
   34  ll
   35  history
   36  git add .zsh_history
   37  git commit -m 'update'
   38  git push -u origin master
   39  echo ==== http://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html 
   40  echo '==== http://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html \n'
   41  history
   42  sudo apt-get install bison m4 makeinfo
   43  sudo apt-get install bison m4 texinfo
   44  sudo mv -v /bin/sh /bin/sh.be4-lfs
   45  sudo ln -sv /bin/bash /bin/sh
   46  history
   47  linuxfromscratch.org/version-check.sh
   48  export LFS=/mnt/lfs
   49  sudo mkdir -pv $LFS 
   50  ls /mnt
   51  ls $LFS
   52  mc
   53  echo export LFS=/mnt/lfs 
   54  history
   55  echo cp -v  --backup=numbered  --update    --target-directory ~  ~/.bashrc
   56  mkdir ~/backu
   57  cp -v  --backup=numbered  --update    --target-directory ~/backu  ~/.bashrc
   58  history
   59  echo export LFS=/mnt/lfs >>~/.bashrc
   60  cp -v  --backup=numbered  --update    --target-directory ~/backu  ~/.bashrc
   61  tail ~/.bashrc
   62  git add .zsh_history
   63  git commit -m 'update'
   64  git push -u origin master
   65  git add
   66  git add --help
   67  git status
   68  git commit --help
   69  git add --dry-run .*hist*
   70  git add  .*hist*
   71  git add --dry-run .*zsh*
   72  git add --dry-run .gitconfig
   73  git add  .gitconfig
   74  git add  .zshrc
   75  git show
   76  git add  .zshrc.pre-oh-my-zsh
   77  git add  .zsh_history
   78  git commit --help
   79  git commit --dry-run -a
   80  git commit --dry-run -a -m update
   81  git add  .zsh_history
   82  git commit  -a -m update
   83  git push -u origin master
   84  set|grep marti
   85  set|grep --count  marti
   86  set|grep --count  lfs
   87  set|grep lfs
   88  history
   89  fc
   90  history
   91  fc
   92  history
   93  sudo
   94  sudo --help
   95  sudo --shell
   96  history
   97  sudo --shell
   98  ls -l .*his*
   99  sudo --login
  100  sudo --shell
  101  ls -l .*his*
  102  sudo --set-home
  103  sudo bash
  104  ls -l .*his*
  105  sudo --set-home 
  106  sudo --shell  --set-home 
  107  #sudo --shell  --set-home bash
  108  ls -l .*his*
  109  sudo --shell  --set-home bash
  110  sudo  --set-home bash
  111  ls -l .*his*
  112  ls -la
  113  history
  114  man sudo
  115  sudo --shell  --set-home 
  116  ls -l .*his*
  117  history
  118  sudo sh -c 'echo sf'
  119  sudo sh -c 'echo sf >>1'
  120  ll
  121  history
  122  sudo cat /root/.bashrc
  123  sudo cat /root/.bashrc | tee 2
  124  ll
  125  history
  126  sudo cat /root/.bashrc | tee root.bashrc
  127  history
  128  cp -v  --backup=numbered  --update    --target-directory ~/backu  ~/root.bashrc
  129  echo export LFS=/mnt/lfs >>~/root.bashrc\n
  130  cp -v  --backup=numbered  --update    --target-directory ~/backu  ~/root.bashrc
  131  history
  132  history|grep git
  133  git commit  -a -m update
  134  git status
  135  history|grep git
  136  git push -u origin master
  137  history
  138  sudo --shell  --set-home 
  139  history|grep /sh
  140  sudo cp -iv /root/.bashrc    /root/.bashrc.be4-lfs
  141  echo sudo sh -c ' cat /home/martin/root.bashrc  >root.bashrc.aftr-lfs  '
  142  sudo sh -c ' cat /home/martin/root.bashrc   '
  143  sudo sh -c ' cat /home/martin/root.bashrc  >root.bashrc.aftr-lfs  '
  144  history
  145  echo fsfsudo cp -iv /root/.bashrc    /root/.bashrc.be4-lfs
  146  sudo sh -c ' cat /home/martin/root.bashrc  >/root/.bashrc.aftr-lfs  '
  147  sudo ll /root 
  148  sudo ls -la /root 
  149  ll
  150  sudo ls -la /root 
  151  sudo cp -iv /root/.bashrc.aftr-lfs    /root/.bashrc
  152  sudo ls -la /root 
  153  history
  154  history|grep git
  155  git commit  -a -m update ;  git push -u origin master
  156  tail ~/root.bashrc
  157  git commit  -a -m update ;  git push -u origin master
  158  history|grep sud
  159  sudo --shell  --set-home 
  160  sudo --login
  161  sudo -i
  162  sudo -H
  163  sudo -H bash
  164  echo $_
  165  ls
  166  echo $_
  167  history
  168  git commit  -a -m update ;  git push -u origin master
  169  sudo mkdir -v $LFS/sources\n
  170  sudo chmod -v a+w $LFS/sources #
  171  cat >wget-list <<EOF\nhttp://ftp.gnu.org/gnu/coreutils/coreutils-8.31.tar.xz\nEOF
  172  history
  173  cat wget-list
  174  wget --input-file=wget-list --continue --directory-prefix=$LFS/sources
  175  sudo mkdir -v $LFS/sources      $LFS/tools\n\n
  176  echo ln -sv $LFS/tools /\n
  177  ln --help
  178  sudo ln -sv $LFS/tools /\n
  179  chmod -v a+wt $LFS/sources
  180  sudo chmod -v a+wt $LFS/sources
  181  sudo chown -v martin:martin $LFS/tools
  182  sudo chown -v martin:martin $LFS/sources
  183  umask
  184  history
  185  wget  --continue --directory-prefix=$LFS/sources http://ftp.gnu.org/gnu/binutils/binutils-2.32.tar.xz
  186  mc
  187  cd linuxfromscratch.org
  188  ll
  189  cd
  190  git add .bashrc
  191  git commit  -a -m update ;  git push -u origin master
  192  sudo adduser lfs
  193  sudo --help
  194  sudo --user=lfs
  195  sudo --user=lfs -i
  196  history
  197  sudo chown -v lfs:lfs $LFS/sources
  198  sudo chown -v lfs:lfs $LFS/tools
  199  sudo --user=lfs -i
  200  wget  --continue --directory-prefix=$LFS/sources http://ftp.gnu.org/gnu/binutils/binutils-2.32.tar.xz
  201  sudo --user=lfs -i
  202  cd linuxfromscratch.org
  203  cat >>lfs-histo <<EOF\nlfs@s18:/mnt/lfs/sources$ history \n    1  ll\n    2  mv .bashrc 1.bashr\n    3  cat > ~/.bashrc << "EOF"\n    4  set +h\n    5  umask 022\n    6  LFS=/mnt/lfs\n    7  LC_ALL=POSIX\n    8  LFS_TGT=$(uname -m)-lfs-linux-gnu\n    9  PATH=/tools/bin:/bin:/usr/bin\n   10  export LFS LC_ALL LFS_TGT PATH\n   11  EOF\n   12  set|less\n   13  mc\n   14  mc\n   15  cd /mnt/lfs/sources/\n   16  ll\n   17  ls -l\n   18  xz\n   19  xz binutils-2.32.tar.xz\n   20  xz --decompress binutils-2.32.tar.xz\n   21  ls -l\n   22  tar xvf binutils-2.32.tar.xz\n   23  ls -l\n   24  rm binutils-2.32.tar \n   25  tar xvf binutils-2.32.tar.xz\n   26  ls -l\n   27  cd /mnt/lfs/sources/\n   28  tar xvf binutils-2.32.tar.xz\n   29  history \nEOF
  204  hist
  205  history
  206  git commit  -a -m update ;  git push -u origin master
  207  cd /mnt/lfs/sources/
  208  pwd
  209  ll
  210  mkdir -v build
  211  cd       build\n
  212  cd
  213  cd /mnt/lfs/sources/
  214  cd binutils-2.32
  215  mkdir -v build
  216  ls -ld .
  217  ls -ld ..
  218  cd ../..
  219  ll
  220  wget  --continue --directory-prefix=$LFS/sources https://www.kernel.org/pub/linux/kernel/v5.x/linux-5.2.8.tar.xz
  221  cd
  222  cd linuxfromscratch.org
  223  cp -vi ~/../lfs/.bash_history ~/linuxfromscratch.org
  224  cp -vi ~/../lfs/.bashrc ~/linuxfromscratch.org
  225  ll  ~/../lfs/
  226  ls -la  ~/../lfs/
  227  ls -la
  228  git add .bash_history .bashrc version-check.sh 
  229  git commit  -a -m update ;  git push -u origin master
  230  history | grep echo
  231  sudo mkdir -pv $LFS/{dev,proc,sys,run}
  232  sudo mknod -m 600 $LFS/dev/console c 5 1
  233  sudo mknod -m 666 $LFS/dev/null c 1 3
  234  sudo mount -v --bind /dev $LFS/dev
  235  sudo mount -vt devpts devpts $LFS/dev/pts -o gid=5,mode=620
  236  sudo mount -vt proc proc $LFS/proc
  237  sudo mount -vt sysfs sysfs $LFS/sys
  238  sudo mount -vt tmpfs tmpfs $LFS/run
  239  if [ -h $LFS/dev/shm ]; then\n  mkdir -pv $LFS/$(readlink $LFS/dev/shm)\nfi
  240  [ -h $LFS/dev/shm ]
  241  echo [ -h $LFS/dev/shm ]
  242  echo [[ -h $LFS/dev/shm ]]
  243  test  -h $LFS/dev/shm
  244  if [ -h $LFS/dev/shm ]; then\n echo mkdir -pv $LFS/$(readlink $LFS/dev/shm)\nfi
  245  echo '==== http://clfs.org/view/clfs-embedded/x86/introduction/hostreqs.html '
  246  mkdir clfs.org
  247  cd clfs.org
  248  cat > version-check.sh << "EOF"\n#!/bin/bash\n\n# Simple script to list version numbers of critical development tools\nset -e\nbash --version | head -n1 | cut -d" " -f2-4\necho -n "Binutils: "; ld --version | head -n1 | cut -d" " -f3-\nbzip2 --version 2>&1 < /dev/null | head -n1 | cut -d" " -f1,6-\necho -n "Coreutils: "; chown --version | head -n1 | cut -d")" -f2\ndiff --version | head -n1\nfind --version | head -n1\ngawk --version | head -n1\ngcc --version | head -n1\nldd $(which ${SHELL}) | grep libc.so | cut -d ' ' -f 3 | ${SHELL} | head -n 1 \\n| cut -d ' ' -f 1-10\ngrep --version | head -n1\ngzip --version | head -n1\nm4 --version | head -n1\nmake --version | head -n1\necho "#include <ncurses.h>" | gcc -E - > /dev/null\npatch --version | head -n1\nsed --version | head -n1\nsudo -V | head -n1\ntar --version | head -n1\nmakeinfo --version | head -n1\n\nEOF
  249  cat version-check.sh
  250  bash version-check.sh
  251  sudo apt-get install ncurses
  252  sudo apt-get install curses
  253  apt-cache search ncurses
  254  sudo apt-get install libncurses5
  255  sudo apt-get install libncurses5-dev
  256  cat > version-check.sh << "EOF"\n#!/bin/bash\n\n# Simple script to list version numbers of critical development tools\n###set -e\nbash --version | head -n1 | cut -d" " -f2-4\necho -n "Binutils: "; ld --version | head -n1 | cut -d" " -f3-\nbzip2 --version 2>&1 < /dev/null | head -n1 | cut -d" " -f1,6-\necho -n "Coreutils: "; chown --version | head -n1 | cut -d")" -f2\ndiff --version | head -n1\nfind --version | head -n1\ngawk --version | head -n1\ngcc --version | head -n1\nldd $(which ${SHELL}) | grep libc.so | cut -d ' ' -f 3 | ${SHELL} | head -n 1 \\n| cut -d ' ' -f 1-10\ngrep --version | head -n1\ngzip --version | head -n1\nm4 --version | head -n1\nmake --version | head -n1\necho "#include <ncurses.h>" | gcc -E - > /dev/null\npatch --version | head -n1\nsed --version | head -n1\nsudo -V | head -n1\ntar --version | head -n1\nmakeinfo --version | head -n1\n\nEOF
  257  bash version-check.sh
  258  ll
  259  add version-check.sh
  260  git add version-check.sh
  261  git commit  -a -m update ;  git push -u origin master
  262  sudo mkdir -p /mnt/clfs
  263  export CLFS=/mnt/clfs
  264  sudo chmod 777 ${CLFS}
  265  mkdir -v ${CLFS}/sources
  266  sudo groupadd clfs
  267  sudo useradd -s /bin/bash -g clfs -m -k /dev/null clfs
  268  sudo passwd clfs
  269  sudo chown -Rv clfs ${CLFS}
  270  cd $CLFS
  271  wget  --continue --directory-prefix=$CLFS/sources http://www.kernel.org/pub/linux/kernel/v4.x/linux-4.9.22.tar.xz
  272  ll
  273  cd sources
  274  ll
  275  history | grep tar
  276  wget  --continue --directory-prefix=$CLFS/sources http://ftp.gnu.org/gnu/binutils/binutils-2.27.tar.bz2
  277  cd
  278  history | grep ..
  279  history | grep '..'
  280  history | grep -F '..'
  281  history | grep '[.][.]'
  282  cp -vi ~/../clfs/.bashrc ~/clfs.org
  283  cp -vi ~/../clfs/.bash_history ~/clfs.org
  284  cp -vi ~/../clfs/.bash_profile ~/clfs.org
  285  cd ~/clfs.org
  286  git add .bash_history .bash_profile .bashrc
  287  git commit  -a -m update ;  git push -u origin master
  288  mc
  289  wget  --continue --directory-prefix=$CLFS/sources http://gcc.gnu.org/pub/gcc/releases/gcc-6.2.0/gcc-6.2.0.tar.bz2
  290  wget  --continue --directory-prefix=$CLFS/sources http://ftp.gnu.org/gnu/gmp/gmp-6.1.1.tar.bz2
  291  wget  --continue --directory-prefix=$CLFS/sources http://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz
  292  wget  --continue --directory-prefix=$CLFS/sources http://ftp.gnu.org/gnu/mpfr/mpfr-3.1.4.tar.bz2
  293  cp -vi ~/../clfs/.bash_history ~/clfs.org
  294  git commit  -a -m update ;  git push -u origin master
  295  cp -vi ~/../clfs/.bash_history ~/clfs.org
  296  cd
  297  git commit  -a -m update ;  git push -u origin master
  298  echo '==== https://github.com/ivandavidov/minimal '
  299  sudo apt install wget make gawk gcc bc bison flex xorriso libelf-dev libssl-dev
  300  cd minimal-linux-script
  301  ll
  302  ./minimal.sh
  303  mc
  304  echo sudo apt install qemu
  305  apt search qemu-system
  306  apt search qemu-system-x86
  307  apt show qemu-system-x86
  308  apt show qemu-system
  309  sudo apt install qemu-system-x86
  310  mc
  311  cd minimal-linux-script
  312  ./qemu64.sh
  313  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso -boot d 
  314  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso 
  315  cd minimal-linux-script
  316  qemu-system-x86_64 
  317  qemu-system-x86_64 -?
  318  qemu-system-x86_64 --help
  319  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso -boot d -vga none 
  320  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso -boot d  -nographic 
  321  sudo apt install qemu-kvm 
  322  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso -boot d  -nographic 
  323  cd minimal-linux-script
  324  qemu-system-x86_64 -m 128M -cdrom minimal_linux_live.iso -boot d  -nographic 
  325  mc
  326  cd landley.net--aboriginal
  327  tar xvf system-image-i586.tar.gz
  328  mc
  329  ll
  330  cd system-image-i586
  331  ./run-emulator.sh
  332  cd landley.net--aboriginal
  333  cd system-image-i586
  334  mc
  335  cat myrun-emulator.sh
  336  qemu-system-i386  -serial mon:stdio     -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  337  qemu-system-i386 -curses  -serial mon:stdio     -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  338  cd landley.net--aboriginal
  339  cd system-image-i586
  340  qemu-system-i386 -curses  -serial mon:stdio     -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  341  qemu-system-i386   -serial mon:stdio     -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  342  qemu-system-i386        -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  343  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  344  qemu-system-i386   -serial mon:stdio   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  345  qemu-system-i386 -curses  -serial mon:stdio     -cpu pentium -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  346  qemu-system-i386 -curses  -serial mon:stdio    -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  347  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=i586 $KERNEL_EXTRA" $QEMU_EXTRA 
  348  history
  349  cd ..
  350  tar xvf system-image-i486.tar.gz
  351  cd system-image-i486
  352  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA 
  353  git commit  -a -m update ;  git push -u origin master
  354  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA 
  355  qemu -cpu help
  356  qemu-system-i386 -cpu help
  357  history
  358  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA -cpu pentium
  359  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA -cpu 586
  360  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA -cpu 486
  361  env
  362  env -i
  363  env -i sh
  364  cd busybox-rh
  365  ll
  366  bunzip2 rh-9-shrike.img.bz2
  367  history | grep qemu
  368  \tcd
  369  cd busybox-rh
  370  ll
  371  qemu-system-i386 rh-9-shrike.img
  372  qemu-system-i386 rh-9-shrike.img -nographic
  373  history | grep qemu
  374  qemu-system-i386 rh-9-shrike.img -nographic -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA
  375  \tmc
  376  git add .config/mc/ini
  377  git commit  -a -m update ;  git push -u origin master
  378  mc
  379  git commit  -a -m update ;  git push -u origin master
  380  git commit  -a 
  381  git status
  382  git show
  383  git push -u origin master
  384  git clone https://api.glitch.com/git/pika-web-example
  385  mc
  386  npm i json5
  387  mc
  388  cd browser-require-attempts
  389  npm init
  390  npm i json5
  391  mc
  392  git add package.json
  393  git add package-lock.json
  394  git show
  395  git status
  396  cd ..
  397  git status
  398  git commit  -a -m update ;  git push -u origin master
  399  mc
  400  cd browser-require-attempts
  401  history
  402  npm i json5 --save
  403  mc
  404  tac ~/.node_repl_history  ;    node
  405  git status
  406  git commit  -a -m update ;  git push -u origin master
  407  mc
  408  npm i --global serve
  409  mc
  410  npm i  serve
  411  npm i  @pika/web
  412  cd browser-require-attempts
  413  npm i  @pika/web --save-dev
  414  mc
  415  npm ls
  416  npm ls -g
  417  history
  418  tac ~/.node_repl_history  ;    node
  419  cat >>index.js
  420  mc
  421  pika
  422  npx @pika/web
  423  mc
  424  git add index.html index.js script.js
  425  git commit  -a -m update ;  git push -u origin master
  426  cd browser-require-attempts
  427  history
  428  npx serve
  429  cd browser-require-attempts
  430  npx serve
  431  npx --help
  432  npx serve &
  433  cat index.js
  434  cat script.js
  435  cat index.js >>script.js
  436  mc
  437  git commit  -a -m update ;  git push -u origin master
  438  yarn
  439  mc
  440  cd
  441  which yarn
  442  yarn global add serve
  443  mc
  444  history
  445  sudo npm i --global serve
  446  cd browser-require-attempts
  447  serve &
  448  ./node_modules/.bin/mkdirp --help
  449  mkdirp --help
  450  yarn mkdirp --help
  451  history
  452  npx serve &
  453  ./node_modules/.bin/mkdirp --help
  454  history
  455  yarn mkdirp --help
  456  cd browser-require-attempts
  457  yarn mkdirp --help
  458  time yarn mkdirp --help
  459  time ./node_modules/.bin/mkdirp --help
  460  npm bin
  461  cd
  462  npm bin
  463  cd browser-require-attempts
  464  npm run mkdirp --help
  465  npm run-script mkdirp --help
  466  git commit  -a -m update ;  git push -u origin master
  467  ./node_modules/.bin/pika --help
  468  ./node_modules/.bin/pika-web --help
  469  mc
  470  cd
  471  history
  472  cd mkdirp-p
  473  #npm i mkdirp --save
  474  npm init
  475  npm i mkdirp --save
  476  npm ls
  477  cd ..
  478  cd browser-require-attempts
  479  npm ls
  480  mc
  481  cd
  482  history
  483  cd browserfs-p
  484  npm init
  485  npm i browserfs --save
  486  npm ls
  487  ./node_modules/.bin/pika-web --help
  488  ~/node_modules/.bin/pika-web --help
  489  ~/node_modules/.bin/pika-web 
  490  mc
  491  cd ~/mkdirp-p
  492  ~/node_modules/.bin/pika-web 
  493  mc
  494  cd ~/browser-require-attempts
  495  ~/node_modules/.bin/pika-web 
  496  mc
  497  cd
  498  sudo npm install --global rollup
  499  cd browser-require-attempts
  500  rollup
  501  rollup main.js --format iife --name "myBundle" --file bundle.js
  502  ll
  503  cat index.js
  504  rollup index.js --format iife --name "myBundle" --file bundle.js
  505  mc
  506  rollup index.js --format iife --name "myBundle" --file bundle-iife.js
  507  cat bundle-iife.js
  508  rollup index.js --format amd --name "myBundle" --file bundle-amd.js
  509  rollup index.js --format umd --name "myBundle" --file bundle-umd.js
  510  rollup index.js --format esm --name "myBundle" --file bundle-esm.js
  511  rollup index.js --format cjs --name "myBundle" --file bundle-cjs.js
  512  mc
  513  fil=script.js
  514  rollup $fil --format iife --name "myBundle" --file bundle-iife.js
  515  mc
  516  rollup $fil  --format cjs --name "myBundle" --file bundle-cjs.js
  517  #rollup $fil  --format cjs --name "myBundle" --file bundle-cjs.js
  518  rollup $fil  --format amd --name "myBundle" --file bundle-amd.js
  519  rollup $fil  --format umd --name "myBundle" --file bundle-umd.js
  520  rollup $fil  --format esm --name "myBundle" --file bundle-esm.js
  521  mc
  522  cd roll-1
  523  tac ~/.node_repl_history  ;    node
  524  mc
  525  history
  526  cd ..
  527  fil=a3script.js
  528  rollup $fil --format iife --name "myBundle" --file bundle-iife.js
  529  mc
  530  rollup $fil --format iife --name "myBundle" --file bundle-iife.js
  531  mc
  532  rollup $fil --format iife --name "myBundle" --file bundle-iife.js
  533  mc
  534  #rollup $fil  --format cjs --name "myBundle" --file bundle-cjs.js
  535  rollup $fil  --format cjs --name "myBundle" --file bundle-cjs.js
  536  rollup index.js --format amd --name "myBundle" --file bundle-amd.js
  537  rollup $fil --format amd --name "myBundle" --file bundle-amd.js
  538  rollup $fil --format umd --name "myBundle" --file bundle-umd.js
  539  mc
  540  git commit  -a -m update ;  git push -u origin master
  541  npx help --config
  542  npx --help --config
  543  man npx
  544  rollup
  545  cd
  546  git clone https://github.com/streamich/memfs-webpack
  547  cd memfs-webpack
  548  npm install
  549  ls -l  /snap/bin/node
  550  npm ls |less
  551  npm ls --help
  552  npm  --help ls
  553  man npm
  554  npm ls --depth 1
  555  npm ls --depth 0
  556  npm ls --depth 1
  557  npm ls --depth 2
  558  mc
  559  cd memfs-webpack
  560  npm run start
  561  mc
  562  cd memfs-webpack
  563  mc
  564  ps 
  565  ps -u martin
  566  ps -ef|grep ser
  567  ps -ef|grep npm
  568  ps -ef|grep web
  569  pstree
  570  cd git-pokusy
  571  openssl -?
  572  openssl --help
  573  openssl zlib -d -in 0f15d3ae14a52ebd82da4181e44a7320747de9
  574  openssl help
  575  openssl help|grep zlib
  576  openssl help 2>&1|grep zlib
  577  openssl help 2>&1|grep cf
  578  openssl help 2>&1|grep cfb
  579  openssl help 2>&1|grep zl
  580  openssl help 2>&1|grep z
  581  openssl help 2>&1|grep l
  582  openssl help 2>&1|grep li
  583  openssl  enc -z -none -d   -in 0f15d3ae14a52ebd82da4181e44a7320747de9
  584  python
  585  sudo apt install qpdf
  586  sudo apt install --help
  587  sudo apt install qpdf
  588  man apt
  589  man apt-get
  590  sudo apt-get install --fix-broken --reinstall qpdf
  591  git commit  -a -m update ;  git push -u origin master
  592  zlib-flate -uncompress < FILE
  593  cd git-pokusy
  594  zlib-flate -uncompress <0f15d3ae14a52ebd82da4181e44a7320747de9
  595  zlib-flate -uncompress <15a956202b368a158ca812f419cc971c0fe7be
  596  for i in * ; do ; echo $i; done
  597  for i in * ; do ; zlib-flate -uncompress <$i  ; done
  598  for i in * ; do ; zlib-flate -uncompress <$i  ; done |less
  599  git commit  -a -m update ;  git push -u origin master
  600  history
  601  mc
  602  fish
  603  history
  604  history|less
  605  journalctl -b
  606  journalctl -b|grep cloud
  607  dmesg|grep cloud
  608  journalctl -b|grep -i cloud
  609  journalctl -b|grep -i --context=2   cloud
  610  mc
  611  pwd
  612  ll m*
  613  mkdir mn
  614  sudo mount /dev/sr0 $HOME/mn
  615  mc
  616  history
  617  mc
  618  less /run/cloud-init/ds-identify.log
  619  mc
  620  less /run/cloud-init/ds-identify.log
  621  less /var/log/cloud-init.log
  622  less /var/log/cloud-init-output.log
  623  echo '============https://www.cyberciti.biz/faq/unix-linux-chroot-command-examples-usage-syntax/'
  624  J=$HOME/jail
  625  mkdir -p $J
  626  mkdir -p $J/{bin,lib64,lib}
  627  cd $J
  628  cp -v /bin/{bash,ls} $J/bin
  629  ldd /bin/bash
  630  cp -v /lib64/libtinfo.so.5 /lib64/libdl.so.2 /lib64/libc.so.6 /lib64/ld-linux-x86-64.so.2 $J/lib64/
  631  cp -v /lib/x86_64-linux-gnu/libtinfo.so.5 /lib64/libdl.so.2 /lib64/libc.so.6 /lib64/ld-linux-x86-64.so.2 $J/lib64/
  632  cp -v /lib/x86_64-linux-gnu/libdl.so.2 /lib64/libc.so.6  $J/lib64/
  633  cp -v /lib/x86_64-linux-gnu/libc.so.6  $J/lib64/
  634  sudo chroot $J /bin/bash
  635  set
  636  env
  637  env|grep -i ld
  638  env|grep -i lib
  639  history
  640  mkdir -p $J/{bin,lib64,lib,lib/x86_64-linux-gnu}
  641  ldd /bin/bash
  642  cp -v /lib/x86_64-linux-gnu/libtinfo.so.5  $J/lib/x86_64-linux-gnu
  643  cp -v /lib/x86_64-linux-gnu/libdl.so.2  $J/lib/x86_64-linux-gnu
  644  cp -v /lib/x86_64-linux-gnu/libc.so.6  $J/lib/x86_64-linux-gnu
  645  du -a 
  646  sudo chroot $J /bin/bash
  647  history
  648  du -a 
  649  git commit  -a -m 'chroot' ;  git push -u origin master
  650  mc
  651  git commit  -a -m 'sudoers.d' ;  git push -u origin master
  652  mkdir -p downloads/ububase
  653  cd  downloads/ububase
  654  wget http://cdimage.ubuntu.com/ubuntu-base/releases/bionic/release/ubuntu-base-18.04.3-base-amd64.tar.gz
  655  sha256sum ubuntu-base-18.04.3-base-amd64.tar.gz
  656  sudo apt install schroot
  657  gzip -d ubuntu-base-18.04.3-base-amd64.tar.gz
  658  history
  659  tar xvf ubuntu-base-18.04.3-base-amd64.tar
  660  cat /etc/resolv.conf
  661  l
  662  du -m
  663  l
  664  history
  665  sudo chroot . /bin/bash
  666  ll
  667  l
  668  history
  669  mc
  670  sudo apt update
  671  sudo apt install apt-transport-https ca-certificates curl software-properties-common
  672  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  673  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
  674  sudo apt update
  675  apt-cache policy docker-ce
  676  sudo apt install docker-ce
  677  echo '====' https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
  678  sudo systemctl status docker
  679  history
  680  git checkout -b violet
  681  history|less
  682  git commit  -a -m 'ububase,docker' ;  git push -u origin violet
  683  sudo usermod -aG docker ${USER}
  684  su - ${USER}
  685  id -nG
  686  docker
  687  docker version
  688  docker
  689  docker info
  690  du -m /var/lib/docker
  691  sudo du -m /var/lib/docker
  692  df -m
  693  df -m >>df-m
  694  cat df-m
  695  history
  696  docker run hello-world\n
  697  docker pull ubuntu:18.04
  698  docker images
  699  docker run -it ubuntu
  700  docker images
  701  docker ps
  702  docker ps -a
  703  history
  704  docker ps -a
  705  docker start goofy_stonebraker
  706  docker ps
  707  docker
  708  docker stop goofy_stonebraker
  709  docker ps
  710  docker start --help
  711  docker run --help
  712  history
  713  docker run -it ubuntu
  714  docker ps
  715  docker ps -a
  716  docker image ls 
  717  docker image history 
  718  docker system df
  719  docker system 
  720  docker system info
  721  history qemu
  722  history |grep qemu
  723  history |grep -i abori
  724  history |less
  725  mc
  726  history |grep -i hist_
  727  history |grep -i hist
  728  HIST_STAMPS=dd.mm.yyyy
  729  history |grep -i hist
  730  set
  731  set|grep -i hist
  732  export HIST_STAMPS=dd.mm.yyyy
  733  HIST_STAMPS=dd.mm.yyyy history
  734  mc
  735  history |grep -i hist
  736  history 
  737  history |less
  738  qemu --version
  739  qemu-system-i386 --version
  740  mc
  741  history
  742  history |grep emu
  743  history |grep emu|less
  744  cd openwrt
  745  qemu-system-i386   -nographic -no-reboot -kernel linux -initrd rootfs.cpio.gz -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA 
  746  qemu-system-i386   -nographic -no-reboot    -hda openwrt-18.06.5-x86-legacy-combined-ext4.img              -append "panic=1 console=ttyS0 HOST=jmenoooi586 $KERNEL_EXTRA" $QEMU_EXTRA 
  747  qemu-system-i386   -nographic -no-reboot    -hda openwrt-18.06.5-x86-legacy-combined-ext4.img        $QEMU_EXTRA 
  748  echo         $QEMU_EXTRA 
  749  history
  750  qemu-system-i386 --help
  751  qemu-system-i386 --help|less
  752  qemu-system-i386 -machine help
  753  qemu-system-i386 --help|less
  754  qemu-system-i386   -nographic -no-reboot  -m 128 -net none  openwrt-18.06.5-x86-legacy-combined-ext4.img        $QEMU_EXTRA 
  755  history
  756  qemu-system-i386 --help|grep -i nat
  757  qemu-system-i386 -nic model=help
  758  qemu-system-i386  -net -nic model=help
  759  qemu-system-i386 -nic user,model=help
  760  qemu-system-i386 -netdev model=help
  761  qemu-system-i386 -netdev id=a1,model=help
  762  qemu-system-i386   -net nic,model=?
  763  qemu-system-i386   -net nic,model='?'
  764  history
  765  qemu-system-i386   -nographic -no-reboot  -m 128   openwrt-18.06.5-x86-legacy-combined-ext4.img        $QEMU_EXTRA 
  766  cd openwrt
  767  qemu-system-i386   -nographic -no-reboot  -m 128   openwrt-18.06.5-x86-legacy-combined-ext4.img        $QEMU_EXTRA 
  768  qemu-system-i386   -nographic   -m 128   openwrt-18.06.5-x86-legacy-combined-ext4.img        $QEMU_EXTRA 
  769  mc
  770  cd mi
  771  cd 
  772  cd minimal-linux-script
  773  make busybox install
  774  cd busybox-1.30.1
  775  make busybox install
  776  mc
  777  cd
  778  history|grep docke
  779  docker run -it busybox
  780  apt install  --simulate busybox-static
  781  apt install  --simulate busybox-initramfs
  782  apt download busybox-static
  783  mc
  784  cd apt-download
  785  ar x busybox-static_1%3a1.27.2-2ubuntu3.2_amd64.deb
  786  mc
  787  history
  788  apt download busybox-initramfs
  789  mc
  790  man dpkg-deb 
  791  gzip --keep -d data.tar.xz
  792  l
  793  tar xvf data.tar.xz
  794  mc
  795  xz --keep -d data.tar.xz
  796  l
  797  mc
  798  history
  799  history|less
  800  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install /initmy
  801  mc
  802  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install /initmy
  803  man chroot
  804  cd  ~/minimal-linux-script/busybox-1.30.1/_install   && sudo chroot . ./initmy
  805  cd  ~/minimal-linux-script/busybox-1.30.1/_install   && sudo chroot . initmy
  806  mc
  807  history
  808  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 /initmy
  809  ps -ef
  810  mc
  811  history
  812  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 /initmy
  813  mc
  814  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 /initmy
  815  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 initmy
  816  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 /initmy
  817  history
  818  mc
  819  sudo chroot ~/apt-download/ /bin/busybox
  820  sudo chroot ~/apt-download/ /bin/busybox -i
  821  sudo chroot ~/apt-download/ /bin/busybox busybox
  822  sudo chroot ~/apt-download/ /bin/busybox ls /
  823  sudo chroot ~/apt-download/ /bin/busybox sh
  824  sudo chroot ~/apt-download/ /bin/busybox du -x /
  825  sudo chroot ~/minimal-linux-script/busybox-1.30.1/_install.1 /initmy
  826  mc
  827  cd minimal-linux-script/mycopy
  828  ll
  829  grep -i ext4 .config
  830  grep -i 9p .config
  831  mc
  832  cd ..
  833  mc
  834  history
  835  history|grep kern
  836  history|grep tar
  837  cd minimal-linux-script
  838  tar xvf kernel.tar.xz  -C kernel
  839  mkdir kernel
  840  cd kernel
  841  tar xvf ../kernel.tar.xz  
  842  make defconfig\n
  843  l
  844  cd linux-5.0.2
  845  make defconfig\n
  846  make help
  847  make menuconfig
  848  mc
  849  cd ..
  850  cd -
  851  pwd
  852  rm -rf *
  853  df -m
  854  mc
  855  cd
  856  history|grep docke
  857  docker run -it ubuntu
  858  history|grep chroo
  859  mc
  860  sudo chroot ~/downloads/ububase
  861  mc
  862  sudo chroot ~/downloads/ububase
  863  docker info
  864  mc
  865  lsinitramfs --h
  866  lsinitramfs -l
  867  cd downloads
  868  lsinitramfs -l
  869  lsinitramfs initrd.img-4.15.0-74-generic
  870  file `which lsinitramfs`
  871  cat  `which lsinitramfs`
  872  unmkinitramfs --h
  873  unmkinitramfs -v initrd.img-4.15.0-74-generic ini
  874  mc
  875  lsmod|grep e10
  876  lsmod|less
  877  lsmod|grep -i net
  878  history
  879  mc
  880  lspci
  881  lspci |grep 100
  882  cat /proc/pci
  883  lspci |grep -i net
  884  mc
  885  find /proc -name '*pci*'
  886  find /proc -name '*pci*' 2>2
  887  mc
  888  od initrd.img-4.15.0-72-generic.txt|less
  889  hexdump initrd.img-4.15.0-72-generic.txt|less
  890  xxd  initrd.img-4.15.0-72-generic.txt|less
  891  less  initrd.img-4.15.0-72-generic.txt
  892  mc
  893  ifconfig -a
  894  ls -l /dev/ttyS0
  895  mc
  896  history
  897  sudo chroot ~/downloads/ububase
  898  man dpkg
  899  mc
  900  cd downloads
  901  grep ackag status
  902  grep ^Packag status
  903  grep ^Packag status|wc
  904  grep ^Packag status >89
  905  grep -E '^Packag|^Prior' status 
  906  grep -E '^Packag|^Prior' status >prior
  907  mc
  908  grep -E '^Prior' status |sort|uniq -c
  909  history |tail -n 30
  910  dpkg-query --h
  911  dpkg-query --help
  912  man dpkg-query
  913  dpkg-query --showformat='${Package}\t${Version}\n' --show
  914  dpkg-query --showformat='${Package}\t${Priority}\n' --show
  915  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep requir
  916  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep requir|wc
  917  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep importan|wc
  918  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep standar|wc
  919  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep optiona|wc
  920  history |tail -n 30
  921  sudo chroot ~/downloads/ububase
  922  dpkg-query --showformat='${Package}\t${Priority}\n' --show|grep requir >requi
  923  mc
  924  sort requi >s
  925  cd downloads
  926  sort requi >s
  927  comm --h
  928  comm -23 ../s s
  929  comm -13 ../s s
  930  comm -23 ../s s >comm-23
  931  history |tail -n 30
  932  comm -23 ../s s
  933  mc
  934  history|grep jupy
  935  jupyter lab
  936  jupyter lab --h
  937  jupyter lab --no-browser
  938  history
  939  mawk '/^Architecture: / { arch = $2; } /^Package: / { package = $2; } /^Priority: required/ { print package " (" arch ")"; }' < /var/lib/dpkg/status
  940  mawk '/^Architecture: / { arch = $2; } /^Package: / { package = $2; } /^Priority: required/ { print package; }' < /var/lib/dpkg/status
  941  history
  942  find -name '*.ipyn*'
  943  history
  944  grep ssenti < /var/lib/dpkg/status
  945  history|tail
  946  echo mawk ' /^Package: / { package = $2; }              /^Package: / { package = $2; }              /^Priority: required/ { print package; }' < /var/lib/dpkg/status
  947  echo mawk ' /^Package: / { package = $2; }   /^Priority: required/   { p= $2; }       /^Essential: yes/   { print package p ; }' < /var/lib/dpkg/status\n
  948  mawk ' /^Package: / { package = $2; }   /^Priority: required/   { p= $2; }       /^Essential: yes/   { print package p ; }' < /var/lib/dpkg/status\n
  949  mawk ' /^Package: / { package = $2; }   /^Priority: required/   { p= $2; }       /^Essential: yes/   { print package " " p ; }' < /var/lib/dpkg/status\n
  950  mawk ' /^Package: / { package = $2; }   /^Priority: required/   { p= $2; }       /^Essential: yes/   { print package " " p ; }' < /var/lib/dpkg/status|wc\n
  951  mawk ' /^Package: / { package = $2; }   /^Priority: required/   { p= $2; }       /^Essential: yes/   { print package " " p ; }' < ~/downloads/ububase/var/lib/dpkg/status|wc\n
  952  history|tail
  953  socat
  954  tty
  955  ps l
  956  stty -a
  957  (sleep 5; echo hello, world) &
  958  mc
  959  newgrp tty
  960  sudo -i
  961  sudo less -f /dev/vcs1
  962  mkdir pipes
  963  cd pipes
  964  mknod --he
  965  man mknod
  966  mknod p oin
  967  man mknod
  968  mknod oin p
  969  ll
  970  mknod oout p
  971  ll
  972  tr a b <oout >oin &
  973  echo abbds >oout
  974  cat oin
  975  tr a b <oout >oin &
  976  echo abbds >oout &
  977  cat oin
  978  tr a b <oout >oin &
  979  echo abbds >oout &
  980  cat oin &
  981  tr a b <oout >oin &
  982  (echo abbds; echo aaa) >oout 
  983  cat oin &
  984  history|grep dock
  985  docker run -it ubuntu
  986  sudo apt-get --no-act install sysvinit-utils
  987  sudo apt-get --no-act install 
  988  git commit  -a -m 'hist' ;  git push -u origin violet
  989  ping 10.0.2.2
  990  apt-cache search qemu
  991  dpkg --h
  992  dpkg --help
  993  dpkg --listfiles qemu-system-common
  994  dpkg --listfiles qemu-system-common qemu-block-extra:amd64
  995  dpkg --listfiles qemu-system-common qemu-block-extra:amd64|grep -i 9p
  996  dpkg --listfiles qemu-system-common qemu-block-extra:amd64   qemu-kvm qemu-system-x86 qemu-utils                    |grep -i 9p
  997  find / -name '*9p*' 
  998  find / -name '*9p*' 2>2
  999  find / -name '*9p*.ko' 2>2
 1000  history
 1001  dpkg --listfiles linux-modules-4.15.0-72-generic
 1002  dpkg --listfiles linux-modules-4.15.0-72-generic|grep 9p
 1003  history
 1004  sudo mkdir -p /mnt/ram
 1005  sudo mount -vt  ramfs ramfs /mnt/ram/
 1006  free -m
 1007  cd /mnt/ram
 1008  sudo mkdir -p /mnt/ram/w
 1009  sudo chown -Rv martin:martin /mnt/ram/w
 1010  mc
 1011  history
 1012  free -m
 1013  cd
 1014  free -m |tee -a free-m
 1015  cd /mnt/ram/w
 1016  ll
 1017  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh --help
 1018  ll
 1019  chmod u+x poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh
 1020  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh --help
 1021  mkdir p
 1022  echo ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh -d p -S -R
 1023  history
 1024  sudo mount -vt  ramfs ramfs /mnt/ram/
 1025  sudo mkdir -p /mnt/ram/w
 1026  sudo chown -Rv martin:martin /mnt/ram/w
 1027  free -m |tee -a free-m
 1028  history
 1029  free -m |tee -a free-m
 1030  cd /mnt/ram/w
 1031  chmod u+x poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh
 1032  mkdir p
 1033  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh --help
 1034  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh -d p -S -R -D -l
 1035  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh -d p -S -R -D -l|less
 1036  ./poky-glibc-x86_64-core-image-sato-core2-32-qemux86-toolchain-3.0.1.sh -d p -S -R -D -l >list
 1037  free -m |tee -a free-m
 1038  mc
 1039  sudo apt install zstd 
 1040  mc
 1041  cd arch-i486
 1042  unzstd --keep linux-5.4.13.arch1-1.0-i486.pkg.tar.zst
 1043  mc
 1044  sudo apt install binwalk 
 1045  cd archis
 1046  ll
 1047  binwalk bzImage
 1048  ll
 1049  history
 1050  binwalk --extract  bzImage
 1051  mc
 1052  binwalk --extract  _bzImage.extracted/3E80
 1053  mc
 1054  ll
 1055  binwalk --extract  vmlinuz-linux
 1056  binwalk --extract  _vmlinuz-linux.extracted/4708
 1057  binwalk --extract  bzimage
 1058  binwalk --extract  _bzimage.extracted/3E62
 1059  binwalk --extract bzImage.hum
 1060  binwalk --extract _bzImage.hum.extracted/3E80
 1061  mc
 1062  ll
 1063  mc
 1064  history|grep qem
 1065  qemu-system-i386   -nographic   -m 128   openwrt-18.06.5-x86-legacy-combined-ext4.img 
 1066  qemu-system-i386   -nographic   -m 128  openwrt/openwrt-18.06.5-x86-legacy-combined-ext4.img 
 1067  qemu-system-i386   -nographic   -m 128   -cdrom iso/linux3.iso 
 1068  qemu-system-i386   -nographic   -m 128   -cdrom iso/linux4.iso
 1069  history
 1070  history|grep qem|grep ini
 1071  history|grep qem|grep initr
 1072  qemu-system-i386   -nographic   -m 128   -kernel arch-v86/vmlinuz-linux -initrd arch-v86/initramfs-linux.img -append "ignore_loglevel"
 1073  qemu-system-i386   -nographic   -m 128   -kernel arch-v86/vmlinuz-linux -initrd arch-v86/initramfs-linux.img -append "ignore_loglevel console=ttyS0"
 1074  qemu-system-i386   -nographic   -m 128   -kernel arch-v86/vmlinuz-linux -initrd arch-v86/initramfs-linux-fallback.img -append "ignore_loglevel console=ttyS0"
 1075  qemu-system-i386   -nographic   -m 128   -kernel arch-v86/vmlinuz-linux -initrd arch-v86/initramfs-linux-fallback.img -append "ignore_loglevel console=ttyS0" -hda openwrt/openwrt-18.06.5-x86-legacy-combined-ext4.img
 1076  qemu-system-i386   -nographic   -m 128   -kernel arch-v86/vmlinuz-linux -initrd arch-v86/initramfs-linux-fallback.img -append "ignore_loglevel console=ttyS0 root=/dev/hda1  " -hda openwrt/openwrt-18.06.5-x86-legacy-combined-ext4.img
 1077  history
 1078  qemu -boot d 
 1079  history
 1080  qemu-system-i386   -nographic   -m 128   -cdrom iso/linux4.iso -boot d   -hda openwrt/openwrt-18.06.5-x86-legacy-combined-ext4.img
 1081  ls
 1082  mc
 1083  history
 1084  qemu-system-i386   -nographic   -m 128  openwrt/openwrt-18.06.5-x86-legacy-combined-ext4.img 
 1085  qemu-system-i386   -nographic   -m 128   -cdrom iso/linux3.iso 
 1086  qemu-system-i386   -nographic   -m 128   -cdrom iso/linux4.iso
 1087  history|grep was
 1088  history|grep dock
 1089  sudo systemctl status docker
 1090  docker info
 1091  du -m /var/lib/docker
 1092  sudo du -m /var/lib/docker
 1093  history|grep dock
 1094  docker images
 1095  docker ps -a
 1096  docker image ls
 1097  docker image history
 1098  docker system df
 1099  docker system
 1100  docker system info
 1101  docker pull wasienv/wasienv
 1102  sudo du -m --threshold=10m /var/lib/docker
 1103  sudo du -m --threshold=2m /var/lib/docker
 1104  sudo -i mc  /var/lib/docker
 1105  docker system df
 1106  docker image ls
 1107  docker ps -a
 1108  mkdir adocker
 1109  cd adocker
 1110  mount
 1111  mount >0.m
 1112  df -m
 1113  df -m >0.df
 1114  history
 1115  docker system df
 1116  docker system df >0.d.s.df
 1117  sudo du -ms  /var/lib/docker
 1118  sudo du -ms  /var/lib/docker |tee >0.du-ms
 1119  l
 1120  cat *
 1121  history|grep dock
 1122  docker run -it wasienv
 1123  docker run -it wasienv/wasienv
 1124  cd adocker
 1125  history
 1126  l
 1127  mount >1.m
 1128  df -m >1.df
 1129  docker system df >1.d.s.df
 1130  sudo du -ms  /var/lib/docker |tee >1.du-ms
 1131  history
 1132  cd adocker
 1133  diff 0.df 1.df
 1134  diff 0.d.s.df 1.d.s.df
 1135  diff 0.du-ms 1.du-ms
 1136  sudo du -ms  /var/lib/docker |tee >2.du-ms
 1137  diff 0.du-ms 2.du-ms
 1138  docker system df >2.d.s.df
 1139  diff 0.d.s.df 2.d.s.df
 1140  diff 0.m 1.m
 1141  docker run -it wasienv/wasienv
 1142  sudo -i mc  /var/lib/docker
 1143  apt show dive
 1144  wget https://github.com/wagoodman/dive/releases/download/v0.9.1/dive_0.9.1_linux_amd64.deb\n
 1145  sudo apt install ./dive_0.9.1_linux_amd64.deb
 1146  dive
 1147  dive --h
 1148  docker image ls
 1149  dive wasienv
 1150  dive wasienv/wasienv
 1151  dive --h
 1152  docker ps -a
 1153  dive focused_feistel
 1154  dive wasienv/wasienv
 1155  docker run --rm -it -v \\n/var/run/docker.sock:/var/run/docker.sock \\n-v /yourpath:/.config/jesseduffield/lazydocker \\nlazyteam/lazydocker
 1156  history
 1157  sudo du -ms  /var/lib/docker |tee >3.du-ms
 1158  sudo du -ms  /var/lib/docker |tee 3.du-ms
 1159  sudo du -ms  /var/lib/docker |tee 4.du-ms
 1160  docker run --rm -it -v \\n/var/run/docker.sock:/var/run/docker.sock \\n-v /yourpath:/.config/jesseduffield/lazydocker \\nlazyteam/lazydocker
 1161  pwd
 1162  mc
 1163  cd adocker
 1164  sudo du -msx  /var/lib/docker |tee 5.du-msx
 1165  docker run --rm -it -v \\n/var/run/docker.sock:/var/run/docker.sock \\n-v /yourpath:/.config/jesseduffield/lazydocker \\nlazyteam/lazydocker
 1166  sudo -i mc  /var/lib/docker
 1167  cd adocker
 1168  history|grep dock
 1169  sudo du -m --threshold=10m /var/lib/docker
 1170  sudo du -m --threshold=10m /var/lib/docker|grep tmp
 1171  sudo -i mc  /var/lib/docker
 1172  sudo du -m --threshold=10m /var/lib/docker
 1173  bash -x
 1174  bash -x >bash-x
 1175  l
 1176  bash -x 2>bash-x
 1177  l
 1178  mc
 1179  bash -x -i 2>bash-x
 1180  l
 1181  mc
 1182  bash -v
 1183  history
 1184  bash -v -i 2>bash-v-i
 1185  mc
 1186  l
 1187  set|grep -i hist
 1188  less /etc/profile
 1189  mc
 1190  cd
 1191  ls .profile
 1192  cat .profile
 1193  mc
 1194  cat .bashrc|grep -i pat
 1195  cd adocker
 1196  l
 1197  history
 1198  zsh -v -i 2>zsh-v-i
 1199  zsh -x -i 2>zsh-x-i
 1200  mc
 1201  grep -i hist zsh-v-i
 1202  grep -i hist zsh-x-i
 1203  grep HIST zsh-x-i
 1204  grep HIST zsh-v-i
 1205  grep HIST zsh-x-i
 1206  set|grep -i hist
 1207  history
 1208  grep HIST zsh-v-i
 1209  cd adocker
 1210  grep HIST zsh-v-i
 1211  grep HIST zsh-x-i
 1212  mc
 1213  history
 1214  set|grep -i hist
 1215  cd
 1216  echo git clone --depth=1 https://github.com/martin12333/bash-it.git ~/.bash_it
 1217  history
 1218  cd adocker
 1219  l
 1220  mkdir bash-it
 1221  cd bash-it
 1222  l
 1223  history
 1224  bash -v -i 2>bash-v-i
 1225  bash -x -i 2>bash-x-i
 1226  grep HIST bash-x-i
 1227  grep HIST bash-v-i
 1228  mc
 1229  history
 1230  set|grep -i hist
 1231  mc
 1232  setopt 
 1233  setopt |grep his
 1234  apt search fzf
 1235  apt show fzf
 1236  ls -l /dev/ttyS0
 1237  cat .zshrc|grep bind
 1238  cd adocker
 1239  grep bind bash-it/bash-v-i
 1240  grep bind bash-it/bash-x-i
 1241  grep bind zsh-v-i
 1242  grep bind zsh-x
 1243  grep bind zsh-x-i
 1244  grep bindk zsh-x-i
 1245  grep ' bindk' zsh-x-i
 1246  grep ' bindk' zsh-x-i|grep his
 1247  history
 1248  cd adocker
 1249  cd bash-it
 1250  bash -x -i 2>bash-x-i-his
 1251  bash -v -i 2>bash-v-i-hi
 1252  cd ..
 1253  grep bind bash-it/bash-x-i-his
 1254  grep bind bash-it/bash-v-i-hi
 1255  mc
 1256  history|grep opt
 1257  setopt
 1258  omz_history
 1259  echo $terminfo
 1260  46R62;9;c
 1261  echo $terminfo >fdfgfd
 1262  mc
 1263  history
 1264  grep ' bindk' zsh-x-i|grep his
 1265  cd adocker
 1266  grep ' bindk' zsh-x-i|grep his
 1267  cat -v
 1268  git commit  -a -m 'hist' ;  git push -u origin violet
 1269  history
 1270  ll
 1271  ls -la
 1272  mc
 1273  setopt
 1274  setopt |grep his
 1275  set|grep -i hist
 1276  mc
 1277  alias
 1278  history
 1279  cd ~/grdr20/PyMartinCA/beta/JUPYTER/output
 1280  awk '$7<1.6 && $12>250' <fromcsv-g3ltl-r2.rules.csv | awk '{print( $13, $14, $15, $12, $7)}'
 1281  awk '$12>250' <fromcsv-g3ltl-r2.rules.csv | awk '{print( $13, $14, $15, $12, $7)}'
 1282  awk '$12>50' <fromcsv-g3ltl-r2.rules.csv | awk '{print( $13, $14, $15, $12, $7)}'
 1283  awk '$7<1.6 && $12>250' <fromcsv-g3ltl-r2.rules.csv | awk '{print( $13, $14, $15, $12, $7)}'
 1284  awk '$12>250' <fromcsv-g3ltl-r2.rules.csv | awk '{print( $13, $14, $15, $12, $7)}'
