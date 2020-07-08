@color 2

:loop
arp -s 192.168.1.254 xx-xx-xx-xx-xx-xx
ipconfig /flushdns
timeout /t 10
goto loop

FOR /L %%G IN (1,1,10) DO echo %%G ping -n 1 -w 1000 192.168.254.254 >nul

@pause