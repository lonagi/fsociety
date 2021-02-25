jupyter contrib nbextension install --user
jupyter nbextension enable freeze/main
jupyter nbextension enable scroll_down/main
jupyter nbextension enable varInspector/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable toggle_all_line_numbers/main
jupyter nbextension enable scratchpad/main
cp ./notebook.json ~/.jupyter/nbconfig/
cp ./tree.json ~/.jupyter/nbconfig/
cp ./common.json ~/.jupyter/nbconfig/
cp ./jupconfig.py ~/
echo "Jupyter change theme to dark-green"
pip3 install jupyterthemes
jt -t monokai -f fira -fs 13 -nf ptsans -nfs 11 -N -kl -cursw 5 -cursc r -cellw 95% -T
exit 0