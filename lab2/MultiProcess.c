#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void ChildTask(){
	printf("Salam, saya anak tau\n");
}

void ParentTask(){
	printf("dan saya adalah bapaknya");
}

int main(void){
	pid_t pid = fork();

	if(pid == 0){
		ChildTask();
		exit(EXIT_SUCCESS);
	}

	else if(pid>0){
		wait(NULL);
		ParentTask();
	}

	else{
		printf("unable to create child process");
	}

	return EXIT_SUCCESS;
}
