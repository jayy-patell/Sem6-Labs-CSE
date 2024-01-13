#include"mpi.h"
#include<stdio.h>
#include<string.h>

void toggle(char msg1[]){
	for(int c=0;c<strlen(msg1);c++){
		if (msg1[c] >= 'A' && msg1[c] <= 'Z')
	        msg1[c] = msg1[c] + 'a' - 'A';
	    else if (msg1[c] >= 'a' && msg1[c] <= 'z')
	        msg1[c] = msg1[c] + 'A' - 'a';
	}
}

int main(int argc, char* argv[]){
	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status st;

	//process 0 is the sender
	if(rank==0){
		char msg[20];
		printf("enter the string to send: ");
		scanf("%s", msg);
		printf("%s\n", msg);
		MPI_Ssend(&msg,sizeof(msg)/sizeof(msg[0]),MPI_CHAR,1,123,MPI_COMM_WORLD);
		printf("from process %d, message has been sent\n",rank);
	}else{
		char msg1[20];
		MPI_Recv(&msg1,sizeof(msg1)/sizeof(msg1[0]),MPI_CHAR,0,123,MPI_COMM_WORLD,&st);
		printf("from process %d.. message recieved\n",rank);
		toggle(msg1);
		printf("%s\n", msg1);
	}
	MPI_Finalize();
	return 0;
}