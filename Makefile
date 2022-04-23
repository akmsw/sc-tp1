# Authors: Luna, Lihué Leandro; Bonino, Francisco Ignacio.
# Version: 0.2
# Since: 2022-03-18

CC = gcc
CFLAGS = -m32

#En caso de ejecutar el make sin argumento, se ejecuta el target 'calc'
all: calc

calc: main.o asm_io multiplicar
	$(CC) $(CFLAGS) -o calc $< asm_io.o multiplicar.o -lm

main.o: main.c
	$(CC) $(CFLAGS) -c $<

asm_io: asm_io.asm
	nasm -f elf -d ELF_TYPE $<

multiplicar: multiplicar.asm
	nasm -f elf $<

clean:
	rm *.o calc result.txt