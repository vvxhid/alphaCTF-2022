#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char name[32]; 
char *file_name;

void disable_buffering();
void print_username();
void set_username(); 
int get_num();
void menu();
void get_flag();

int main(int argc, char*argv[]) {

    disable_buffering();

    int option = 0;

    printf("Your name: ");
    read(0, name, 32);
    fflush(stdin);

    file_name = "/dev/urandom";

    while (1) {

        menu();
        option = get_num();

        fflush(stdin);

        switch (option) {

            case 1:

                set_username();
                break; 

            case 2:

                print_username();
                break;

            case 3:

                get_flag();
                break; 

            default:
                
                printf("Invalid choice\n");
                break;
        }
    }
}

void disable_buffering() {

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

}

int get_num() {

    unsigned int num = 0;
    int line;

    scanf("%u", &num);
    line = getchar();
    return num;

}

void menu() {

    printf("[1]- Set username\n");
    printf("[2]- Print username\n");
    printf("[3]- Get flag\n");


    printf("> ");

}

void set_username() {

    fflush(stdin);
    printf("Enter your new username: ");
    fread(name, 1, strlen(name), stdin);

}

void print_username() {

    puts(name);
}

void get_flag() {

    FILE *fd = NULL;
    char buffer[5];
    int guess = 0;

    fd = fopen(file_name, "rb");

    if (fd == NULL) {

        printf("Cannot open file \n");
        return;
    }


    fread(buffer, 1, 4, fd);

    printf("Guess: ");
    guess = get_num();

    if (guess == *(int*)buffer) {

        system("cat flag.txt");
    }

    else {

        printf("Nope!\n");
    }
}