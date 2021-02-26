pip3 install notebook==5.7.8 jupyter jupyter_contrib_nbextensions jupyterthemes
jupyter contrib nbextension install --user
jupyter nbextension enable freeze/main
jupyter nbextension enable scroll_down/main
jupyter nbextension enable varInspector/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable toggle_all_line_numbers/main
jupyter nbextension enable scratchpad/main
jupyter nbextension enable snippets/main
jupyter nbextension enable snippets_menu/main
jupyter nbextension enable livemdpreview/livemdpreview
jupyter nbextension enable hinterland/hinterland
cp ./notebook.json ~/.jupyter/nbconfig/
cp ./tree.json ~/.jupyter/nbconfig/
cp ./common.json ~/.jupyter/nbconfig/
cp ./snippets.json ~/Library/Jupyter/nbextensions/snippets/
cp ./jupconfig.py ~/
echo "Jupyter change theme to dark-green"
jt -t monokai -f fira -fs 13 -nf ptsans -nfs 11 -N -kl -cursw 5 -cursc r -cellw 95% -T
exit 0