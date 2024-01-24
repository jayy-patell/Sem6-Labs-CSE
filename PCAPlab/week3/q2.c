#include<mpi.h>
#include<stdio.h>

int main(int argc, char* argv[]){
	int rank,size,N,M,A[10],B[10],ans[10],avg=0,i,final_ans=0;

	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(rank==0){
		N=size;
		printf("Enter M: ");
		scanf("%d",&M);

		for(i=0;i<N*M;i++){
			scanf("%d", &A[i]);
		}
	}
	MPI_Bcast(&M,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Bcast(&N,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scatter(A,M,MPI_INT,B,M,MPI_INT,0,MPI_COMM_WORLD);
	printf("I have recieved ");
	for(i=0;i<M;i++) printf("%d ",B[i]);
	printf(" in process %d\n",rank);

	for(i=0;i<M;i++){
		avg+=B[i];
	}
	avg/=M;

	MPI_Gather(&avg,1,MPI_INT,ans,1,MPI_INT,0,MPI_COMM_WORLD);

	if(rank==0){
		printf("the result gathered in the root: ");
		for(i=0;i<N;i++)
			final_ans += ans[i];
		final_ans/=N;
		printf("The avg of all process is %d\n",final_ans);
	}

	MPI_Finalize();
	return 0;
}