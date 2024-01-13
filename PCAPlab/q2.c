#include "mpi.h"
#include <stdio.h>
#include<string.h>

int main(int argc, char* argv[]) {
	int rank,size,x;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status st;
	if(rank==0){
		int nums[5];
		printf("Enter a values in master process: ");
		//we can scanf only in one specific process area
		for(int i=0;i<5;i++){
			scanf("%d", &nums[i]);
			//MPI_Send(&nums[i],1,MPI_INT,i+1,123,MPI_COMM_WORLD);
		}
		for(int i=0;i<5;i++){
			MPI_Send(&nums[i],1,MPI_INT,i+1,123,MPI_COMM_WORLD);
			// printf("%d", nums[i]);
		}
		//printf("I have sent %d from process 0\n", nums[i]);
	}else{
		int x;
		MPI_Recv(&x,1,MPI_INT,0,123,MPI_COMM_WORLD,&st);
		printf("I have recieved %d in process %d\n", x,rank);
	}
	MPI_Finalize();
	return 0;
}