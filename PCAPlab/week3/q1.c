#include<mpi.h>
#include<stdio.h>

int main(int argc, char* argv[]){
	int rank,size,N,A[10],B[10],c,i,sum,res=1;

	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(rank==0){
		N=size;
		printf("Enter %d values: ",N);
		for(i=0;i<N;i++){
			scanf("%d", &A[i]);
		}
	}
	MPI_Scatter(A,1,MPI_INT,&c,1,MPI_INT,0,MPI_COMM_WORLD);
	printf("I have recieved %d in process %d\n",c,rank);

	for(i=1;i<=c;i++){
		res = res*i;
	}
	
	printf("process %d sending %d recieved %d\n", rank,res,c);
	MPI_Gather(&res,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD);

	if(rank==0){
		printf("the result gathered in the root: ");
		for(i=0;i<N;i++)
			sum+=B[i];
		printf("the sum is %d\n",sum);
	}

	MPI_Finalize();
	return 0;
}