%%cu

#include<stdio.h>
#include "cuda_runtime.h"
#include "device_launch_paramters.h"

_gobal_ void kernel(int *A,int *B,int n,int m)
{
    int r = threadIdx.x;
    int c = threadIdx.y;
    int rsum = 0, csum = 0;
    

    if(A[r*m+c]%2==0)
    {
        for(int i=0;i<m;i++)
        {
            rsum += A[r*m+i];
        }
        B[r*m+c] = rsum;
    }
    else
    {
        for(int i=0;i<n;i++)
        {
            csum += A[i*m+c];
        }
        B[r*m+c] = csum;
    }
}

int main()
{
    int A[12]={1,2,3,4,5,6,7,8,9,10,11,12},B[12];
    int *dA,*dB;
    cudaMalloc((void **)&dA,sizeof(int)*4*3);
    cudaMalloc((void **)&dB,sizeof(int)*4*3);
    cudaMemcpy(dA, A, sizeof(int)*4*3, cudaMemcpyHostToDevice);
    dim3 grid(1,1,1);
    dim3 block(4,3,1);
    kenrel<<<grid,block>>>(dA,dB);
    cudaMemcpy(B,dB,sizeof(int)*4*3,cudaMemcpyDeviceToHost);
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<3; j++) printf("%d ",B[i*3+j]);
        printf("\n");
    }
    cudaFree(dA);
    cudaFree(dB);
    return 0;
}