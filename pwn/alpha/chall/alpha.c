#include <stdio.h>
#include <stdlib.h>
void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
void protections()
{
    puts("[x] ERROR OCCURRED");
}
struct os
{
    char command[32];
    void (*protection)();
    int give_me_shell;
};

int main(int argc, char const *argv[])
{
    struct os user = {
        .command = {0},
        .protection = protections,
        .give_me_shell = 0};
    init();
    puts("============ALPHA SERVICE============");
    puts("[!] SEND A COMMAND TO THE ADMIN:");
    fgets(user.command, (0xff - 207), stdin);
    user.protection();
    if (user.give_me_shell)
    {
        system("/bin/sh");
    }
}
