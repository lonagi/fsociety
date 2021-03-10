; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt
; S = 2A + C + 2B

org 100h
jmp begin

A dw 12, 61, 9, 32, 5, 13, 37, 22, 16, 3
B dw 12, 32, 514, 23, 65, 3, 4, 8, 45, 10
C dw 11, 12, 13, 54, 34, 98, 67, 34, 9, 11
S dw ?, ?, ?, ?, ?, ?, ?, ?, ?, ?

begin:

lea si, A
lea bx, B
lea di, C
lea bp, S

mov cx, 10

sum:
mov al, [si]
add al, [si]
add al, [di]
add al, [bx]
add al, [bx]
mov [bp], al

inc si
inc di
inc bx
inc bp
inc si
inc di
inc bx
inc bp

loop sum

ret