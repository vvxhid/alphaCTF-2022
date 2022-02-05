#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 64 
#define FLAG_LENGTH 57

void disable_buffering(void);
void win();

int main(int argc, char*argv[]) {

  disable_buffering();

  char buff[20];
  
  printf("Enter your name here: ");
  scanf("%s", buff);
  
  return 0; 
}

void disable_buffering (void){

  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

}

void win() {

  char buffer[BUFFER_SIZE];
  memset(buffer, 0, BUFFER_SIZE);

  FILE *flagFd = fopen("flag.txt", "r");

  if (flagFd == NULL) {

    printf("Error: opening flag file failed");
    exit(0);
  }

  fgets(buffer, FLAG_LENGTH + 1, flagFd);
  fclose(flagFd);
  write(1, buffer, strlen(buffer));


}