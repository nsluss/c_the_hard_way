#include <stdio.h>

int main(int argc, char *argv[]){
	if(argc == 3){
		printf("going to add the next two numbers.");
		for(i=0;i<argc;i++){
			printf("%d ",argv[i]);
		}
	}
}
