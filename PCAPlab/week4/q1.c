#include<stdio.h>
#include<mpi.h>
#include<stdlib.h>

void ErrorHandler(int err_code) {
	if(err_code != MPI_SUCCESS){
		char err_string[BUFSIZ];
		int length_err_string, err_class;
		MPI_Error_class(err_code, &err_class);
		MPI_Error_string(err_code, err_string, &length_err_string);
		printf("error: %d %s\n", err_class, err_string);
		exit(1);
	}
}

int main(int argc, char* argv[]) {
	int rank,size,fact=1,factsum,i, err_code;
	MPI_Init(&argc,&argv);
	MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
	err_code = MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	err_code = MPI_Comm_size(MPI_COMM_WORLD, &size);

	for(i=1;i<=rank+1;i++)
		fact*=i;

	err_code = MPI_Scan(&fact,&factsum,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
	printf("for process%d: fact=%d factsum=%d\n", rank,fact,factsum);
	if(rank==size-1){
		ErrorHandler(err_code);
		printf("Sum of all the factorial = %d\n", factsum);
	}

	MPI_Finalize();
	return 0;
}