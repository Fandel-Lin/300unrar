#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	char input[8];
	FILE *read_ptr;
	read_ptr = fopen("hex.txt","r");
	
	FILE *write_ptr;
	write_ptr = fopen("ascii.png","wb");
	
	
	char x[1024];
    /* assumes no word exceeds length of 1023 */
    while (fscanf(read_ptr, " %1023s", x) == 1) {
        puts(x);
        char ret = strtol(x, NULL, 16); // atoi for hex => strtol
        printf("%c\n",ret);
        fwrite(&ret,sizeof(char)*1,1,write_ptr);
    }
	
}
