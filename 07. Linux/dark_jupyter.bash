#!/bin/bash
echo "Jupyter change theme to dark-green"
pip install jupyterthemes
jt -t monokai -f fira -fs 13 -nf ptsans -nfs 11 -N -kl -cursw 5 -cursc r -cellw 95% -T
exit 0