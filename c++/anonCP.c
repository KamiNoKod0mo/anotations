#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>

//system
#include <stdlib.h>


void initS(int argc, char *argv[]);

int main(int argc, char *argv[]){
    initS(argc,argv);

    return 0;
}

void initS(int argc, char *argv[]){
    int meusocket;
    int conecta;
    int porta;
    //char *ip = argv[1];
    
    /* printf("Digite o ip: ");
    fgets(ip,11,stdin);
    printf("Digite Porta: ");
    scanf("%i",&porta); */

    //printf("%i, %s",porta,ip);
    char comando[100];
    sprintf(comando, "ping -c 1 %s", argv[1]);
    system(comando);

    
    struct hostent *site = gethostbyname(argv[1]);
    printf("IP: %s\n",inet_ntoa(*((struct in_addr *)site->h_addr)));
    char *ip = inet_ntoa(*((struct in_addr *)site->h_addr));


    struct sockaddr_in alvo;
    //IPv4,Conexão orientada, protocolo
    //cat /etc/services
    
    meusocket = socket(AF_INET,SOCK_STREAM,0);
    alvo.sin_family = AF_INET;
    alvo.sin_port = htons(atoi(argv[2]));
    alvo.sin_addr.s_addr = inet_addr(ip);

    conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof alvo);

    if(conecta ==0){
        printf("Porta Aberta \n");
        close(meusocket);
        close(conecta);
    }else{
        printf("Porta Fechada \n");
    }
}
//gcc -save-temps
//ldd ...