; Authors: Luna, Lihué Leandro; Bonino, Francisco Ignacio
; Version: 0.2
; Since: 2022-03-18

%include "asm_io.inc"

segment .data

msg1 db    "Esta es la parte de Assembly. ", 0

segment .text
        global  mult

mult:   enter   0,0             ; setup routine
        pusha
        push    ebx
        mov     eax,msg1
        call    print_string
        call    print_nl
        mov     eax,[ebp + 8]
        call    print_int
        call    print_nl
        mov     eax,[ebp + 12]
        call    print_int
        call    print_nl
        mov     eax,[ebp + 8]
        mov     ebx,[ebp + 12]
        mul     ebx
        call    print_int
        call    print_nl
        mov     ebx,[ebp + 16]
        mov     [ebx],eax
        pop     ebx
        popa
        mov     eax, 0          ; go back to C
        leave
        ret