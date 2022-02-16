write_char('H');
write_char('e');
write_char('l');
write_char('l');
write_char('o');
write_char('!');
write_char('\n');
write_char('G');
write_char('i');
write_char('v');
write_char('e');
write_char(' ');
write_char('m');
write_char('e');
write_char(' ');
write_char('Y');
write_char('o');
write_char('u');
write_char('r');
write_char(' ');
write_char('F');
write_char('l');
write_char('a');
write_char('g');
write_char(':');
write_char('\n');

int flag[] = {'A', 'l', 'p', 'h', 'a', 'C', 'T', 'F', '{', 'p', 'l', '3', '4', '5', '3', '_', 'd', '0', 'n', 
'7', '_', 'h', '4', '7', '3', '_', 'm', '3', '_', 'h', 'h', 'h', 'h', 'h', '}', '\n'};

int tab[36];
int i = 0;

while(i != 36) {
    tab[i] = read_char();
    i = i + 1;
}

int a = 0;
int b = 0;
while (flag[a] == tab[b]){
    flag[a] = 0;
    a = a + 1;
    b = b + 1;
}
int mytest = 1;
while (a != 36) {
    a = 36;
    mytest = 0;
    write_char('N');
    write_char('a');
    write_char('h');
    write_char('\n');
}
while (mytest == 1) {
    write_char('C');
    write_char('o');
    write_char('r');
    write_char('r');
    write_char('e');
    write_char('c');
    write_char('t');
    write_char('!');
    write_char('\n');
    mytest = 0;
}