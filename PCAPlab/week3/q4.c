#include "mpi.h"
#include<stdio.h>

int main(int argc, char *argv[])
{
    int rank,size,i;
    char *s1, *s2, r1[10],r2[20];
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Barrier(MPI_COMM_WORLD);
    double st = MPI_Wtime();

    if(rank==0)
    {
        s1="string";
        s2="length";
        for(i=0;i<20;i++)
            r2[i]='\0';
    }

    MPI_Scatter(s1,1,MPI_CHAR,r1,1,MPI_CHAR,0,MPI_COMM_WORLD);
    MPI_Scatter(s2,1,MPI_CHAR,&r1[1],1,MPI_CHAR,0,MPI_COMM_WORLD);
    
    MPI_Gather(r1,2,MPI_CHAR,r2,2,MPI_CHAR,0,MPI_COMM_WORLD);

    if(rank ==0 )
    {
        s1=s1+3;
        s2=s2+3;
    }

    MPI_Scatter(s1,1,MPI_CHAR,r1,1,MPI_CHAR,0,MPI_COMM_WORLD);
    MPI_Scatter(s2,1,MPI_CHAR,&r1[1],1,MPI_CHAR,0,MPI_COMM_WORLD);
    
    MPI_Gather(r1,2,MPI_CHAR,&r2[6],2,MPI_CHAR,0,MPI_COMM_WORLD);

    if(rank == 0 )
        puts(r2);
    double et = MPI_Wtime();
    printf("The time taken is %lf\n",et-st);

    MPI_Finalize();
    return 0;
}