#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
_global_ void odd(int *A, int size)
{
    int gtid = threadIdx.x;
    if(gtid%2!=0 && ((gtid+1) < size))
    {
        if(A[gtid]>A[gtid+1])
        {
            int temp = A[gtid];
            A[gtid] =A[gtid+1];
            A[gtid+1] = temp;
        }
    }
}
_global_ void even(int *A, int size)
{
    int gtid = threadIdx.x;
    if(gtid%2==0 && ((gtid+1) < size))
    {
        if(A[gtid]>A[gtid+1])
        {
            int temp = A[gtid];
            A[gtid] =A[gtid+1];
            A[gtid+1] = temp;
        }
    }
}
int main()
{
    int size=8;
    int A[size]={23,45,76,12,98,34,9,25};
    int *dA;
    cudaMalloc((void **)&dA,sizeof(int)*size);
    cudaMemcpy(dA, A, sizeof(int)*size, cudaMemcpyHostToDevice);
    for(int i=0; i<size/2; i++)
    {
        odd<<<1,size>>>(dA,size);
        even<<<1,size>>>(dA,size);
    }
    cudaMemcpy(A,dA,sizeof(int)*size,cudaMemcpyDeviceToHost);
    for(int i=0; i<size; i++)
    {
        printf("%d ",A[i]);
    }
    cudaFree(dA);
    return 0;
}