```C
#include <stdio.h>  

int magic = 0 ;  

int main(){  
        char buf[0x100];  
	setvbuf(stdout,0,2,0);  
	puts("Please crax me !");  
	printf("Give me magic :");  
	read(0,buf,0x100);  
	printf(buf);  
	if(magic == 0xda){  
	        system("cat /home/craxme/flag");  
	}else if(magic == 0xfaceb00c){  
	        system("cat /home/craxme/craxflag");  
	}else{  
	        puts("You need be a phd");  
	}  
}
```  
For the source code above, we can use **cr4ck.py** to change magic to 0xda; **craxme2.py** to change magic to 0xfaceb00c; in the end, we can use **craxme3.py** to get the shell!  
  
```C
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void read_input(char *buf,unsigned int size){
    int ret ;
    ret = __read_chk(0,buf,size,size);
    if(ret <= 0){
        puts("read error");
        _exit(1);
    }
    if(buf[ret-1] == '\n')
        buf[ret-1] = '\x00';
}

char buf[0x10];

int main(){
	setvbuf(stdin,0,_IONBF,0);
	setvbuf(stdout,0,_IONBF,0);
	setvbuf(stderr,0,_IONBF,0);
	for(unsigned int i = 4 ; i >= 0 ; i--){
		printf("Input:");
		read_input(buf,0x10);
		printf(buf);
		puts("");
		close(i);
	}
}
```  
For the source code above, the write-up will be in the fun.py.

