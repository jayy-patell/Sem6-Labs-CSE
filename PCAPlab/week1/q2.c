#include<stdio.h>
#include"mpi.h"

int main(int argc, char* argv[]){
	int rank,size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	if(rank%2==0){
		printf("my rank is %d so HELLO\n",rank);
	}else{
		printf("my rank is %d so WORLD\n",rank);
	}
	MPI_Finalize();
	return 0;
}