#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void){
	for(int i=i; i<13; i++){
		pid_t pid = fork();

		if(pid==0){
			printf("Child process => PPID=%d, PID=%d\n", getppid(), getpid());
			exit(0);
		}

		else{
			printf("Parent process => PID=%d\n", getpid());
			wait(NULL);
			printf("Child process is finished. \n");
		}
	}

	return EXIT_SUCCESS;
}
