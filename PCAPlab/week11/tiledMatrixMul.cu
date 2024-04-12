#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define BW 2
#define TW 2
#define WIDTH 4

__global__ void matmul(int *a, int *b, int *t)
{
	__shared__ int MDs[TW][TW];
	__shared__ int NDs[TW][TW];
	int bx=blockIdx.x, by = blockIdx.y, tx = threadIdx.x, ty = threadIdx.y;
	int r=by*TW + ty, c = bx*TW+tx;
	int pval=0;
	for(int m=0; m<WIDTH/TW; m++)
	{
		MDs[ty][tx]=a[r*WIDTH + m*TW + tx];
		NDs[ty][tx]=b[(m*TW + ty)*WIDTH + c];
		__syncthreads();
		for(int k=0; k<TW; k++)
		{
			pval+=MDs[ty][k]*NDs[k][tx];
		}
		__syncthreads();
	}
	t[r*WIDTH + c] = pval;
}
int main(void)
{
	int *a, *b, *t;
	int *d_a,*d_b,*d_t;
	int size = sizeof(int)*WIDTH*WIDTH;
	a = (int *) malloc(size);
	b = (int *) malloc(size);
	t = (int *) malloc(size);
	printf("Enter matrix A (4x4): ");
	for(int i=0; i<WIDTH*WIDTH; i++) scanf("%d",&a[i]);
	printf("Enter matrix B: ");
	for(int i=0; i<WIDTH*WIDTH; i++) scanf("%d",&b[i]);
	cudaMalloc((void **) &d_a,size);
	cudaMalloc((void **) &d_b,size);
	cudaMalloc((void **) &d_t,size);
	cudaMemcpy(d_a,a,size,cudaMemcpyHostToDevice);
	cudaMemcpy(d_b,b,size,cudaMemcpyHostToDevice);
	int numblocks = WIDTH/BW;
	dim3 block(BW,BW,1), grid(numblocks,numblocks,1);
	matmul<<<grid,block>>>(d_a,d_b,d_t);
	cudaMemcpy(t,d_t,size,cudaMemcpyDeviceToHost);
	printf("Result vector:\n");
	for(int i=0; i<WIDTH; i++)
	{
		for(int j=0; j<WIDTH; j++) printf("%d ",t[i*WIDTH+j]);
		printf("\n");
	}
	cudaFree(d_a);
	cudaFree(d_b);
	cudaFree(d_t);
	return 0;	
}