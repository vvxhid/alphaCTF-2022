#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_SIZE 512 
#define MAX_ENTRIES 10

void disable_buffering();
void add_book();
void remove_book();
void read_book(); 
void menu(); 
int get_option();

//BSS variables 
char *entries[MAX_ENTRIES];
int created_entries = 0;

int main(int argc, char *argv[]) {

    disable_buffering();

    printf("Here is your leak: %p\n", printf);


    int option = 0; 

    while (1) {

        menu();
        option = get_option();

        switch(option) {

            case 1:
                add_book();
                break; 

            case 2:
                read_book(); 
                break; 

            case 3:
                remove_book();
                break; 

            case 4:
                exit(0);
                break; 

            default:

                printf("Invalid option");
                break; 
        }


    }

    return 0;
}

void disable_buffering() {

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

}
void menu() {

    puts("1- Add Book");
    puts("2- Read Book");
    puts("3- Remove book");
    puts("4- Exit");

}

int get_option() {

    
    int option; 
    int c = 0; 

    printf("Enter an option: ");

    scanf("%d", &option);

    // get rid of new line
    c = getchar();
    return option;

}

void add_book() {

    fflush(stdin);

    int c = 0;
    char size_buffer[7]; 
    int size = 0; 
    char *ptr = NULL; 
    int input_length = 0;

    // MAX_ENTRIES - 1 just to avoid a BSS overflow
    if (created_entries > MAX_ENTRIES - 1) {

        printf("Maximum books reached!\n");
        return;
    }

    
    printf("Size: ");
    fgets(size_buffer, 5, stdin);
    
    size = atoi(size_buffer);

    if (size <= 0 || size > MAX_SIZE) {

        printf("Invalid size\n");
        return;
    }

    ptr = malloc(sizeof(char) * size);

    printf("Content: ");

    input_length = read(0, ptr, size);

    // overflow of two bytes in the 'next size' field
    ptr[input_length+1] = '\0';

    entries[created_entries] = ptr;

    created_entries++;

    printf("Book added\n");

}

void read_book() {

    int index = 0;

    printf("Book index: ");
    scanf("%d", &index);

    if (index < 0 || index > MAX_ENTRIES) {

        printf("Invalid index\n");
        return;
    }

    if (entries[index] == 0) {

        printf("Nope already deleted!!\n");
        return;
    }

    printf("Content: %s\n", entries[index]);
}

void remove_book() {

    int index = 0; 

    printf("Book index: "); 
    scanf("%d", &index);

    if (index < 0 || index > MAX_ENTRIES ) {

        printf("Invalid index\n");
        return; 
    }

    free(entries[index]);
    printf("Book removed!\n");
    created_entries--;

}