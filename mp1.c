#include <string>
#include <iostream>
#include <sys/types.h> 
#include <sys/socket.h>

int main(char* message, char* ip_addr)
{
  if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) { 
    perror("cannot create socket"); return 0; 
  }
  
}
