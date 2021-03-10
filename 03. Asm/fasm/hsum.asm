; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt
; 65894359865h + 7643970823 - 8745645332 
        
org 100h
jmp begin

A dd 94359865h, 658h
B dd 3970823h, 764h
C dd 45645332h, 87h
S dd ?, ? 

begin:
lea si, A
lea bx, B
lea di, C
lea bp, S

mov cx, 8

sum:
mov al, [si]
adc al, [bx]
sub al, [di]
mov [bp], al

inc si
inc di
inc bx
inc bp  

loop sum


ret




