/**
 * @file main.c
 * @author Luna, Lihué Leandro
 * @author Bonino, Francisco Ignacio
 * @brief Programa en C para el primer trabajo práctico de
 *        Sistemas de Computación.
 * @version 0.1
 * @since 2022-03-18
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <ctype.h>

void mult(int a, int b, int *result) __attribute__((cdecl));

int main(int argc, char *argv[])
{
    char msg[] = "Esta es la parte de C.\n";

    write(0, msg, strlen(msg));

    system("rm -f result.txt");
    system("touch result.txt");

    int file = open("result.txt", O_WRONLY);
    int result = 0;
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    fprintf(stdout, "\nVoy a multiplicar %d por %d\n", a, b);

    mult(a, b, &result);

    char buff[1000];

    sprintf(buff, "%d", result);

    write(file, buff, strlen(buff));
}