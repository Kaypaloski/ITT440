#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

int main(){
        int client_fd, valread;
        struct sockaddr_in server_addr;

        client_fd = socket(AF_INET, SOCK_STREAM, 0);
        if (client_fd==0){
                perror("socket failed");
                exit (EXIT_FAILURE);
        }

        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons(8334);

        if(inet_pton(AF_INET, "192.168.149.130", &server_addr.sin_addr) <= 0){
                perror("Invalid address/ Address not supported");
                exit(EXIT_FAILURE);
        }

        if(connect(client_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0){
                perror("Conecction Failed");
                exit(EXIT_FAILURE);
        }

        int received_number;

        valread = read(client_fd, &received_number, sizeof(received_number));
        if(valread == 0){
                printf("Connection closed by the server.\n");
        }
        else{
                printf("Received random number from the server : %d\n", received_number);
        }

        close(client_fd);
        return 0;
}
