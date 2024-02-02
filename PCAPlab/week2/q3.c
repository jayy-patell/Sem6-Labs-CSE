#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int rank, size, x, i;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int arr[size - 1];
    MPI_Status status;
    if(rank == 0){
        printf("Enter %d integers: ", size - 1);
        for(i = 0; i < size - 1; i++)
            scanf("%d", &arr[i]);
        int buffer_size = MPI_BSEND_OVERHEAD + sizeof(int)*size-1;
        char *buffer = (char*)malloc(buffer_size);
        MPI_Buffer_attach(buffer, buffer_size);
        for(i = 0; i < size - 1; i++)
            MPI_Bsend(&arr[i], 1, MPI_INT, i+1, i+1, MPI_COMM_WORLD);
        MPI_Buffer_detach(&buffer, &buffer_size);
    }
    else{
        MPI_Recv(&x, 1, MPI_INT, 0, rank, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        if (rank % 2)
            printf("Rank: %d, Number Recieved: %d, Cube: %d\n", rank, x, x * x * x);
        else
        printf("Rank: %d, Number Recieved: %d, Square: %d\n", rank, x, x * x);
    }
    MPI_Finalize();
    return 0;
}