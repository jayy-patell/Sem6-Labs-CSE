#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
__global__ void matmul(int *a, int *b, int *t,int n)
{
	int r = blockIdx.y*blockDim.y+threadIdx.y;
	int c=blockIdx.x*blockDim.x + threadIdx.x;
	int q=blockDim.x*gridDim.x;
	int sum=0;
	for(int k=0; k<n; k++) sum+=a[r*n+k]*b[k*q+c];
	t[r*q+c]=sum;
}
int main(void)
{
	int *a, *b, *t, m,n,p,q;
	int *d_a,*d_b,*d_t;
	printf("m value: "); scanf("%d",&m);
	printf("n value: "); scanf("%d",&n);
	printf("p value: "); scanf("%d",&p);
	printf("q value: "); scanf("%d",&q);
	int size = sizeof(int)*m*n, size1 = sizeof(int)*p*q, size2=sizeof(int)*m*q;
	a = (int *) malloc(size);
	b = (int *) malloc(size1);
	t = (int *) malloc(size2);
	printf("Enter matrix A: ");
	for(int i=0; i<m*n; i++) scanf("%d",&a[i]);
	printf("Enter matrix B: ");
	for(int i=0; i<p*q; i++) scanf("%d",&b[i]);
	for(int i=0; i<m; i++)
	{
		for(int j=0; j<n; j++)
		{
			printf("%d ",a[i*n+j]);
		}
		printf("\n");
	}
	for(int i=0; i<p; i++)
	{
		for(int j=0; j<q; j++)
		{
			printf("%d ",b[i*q+j]);
		}
		printf("\n");
	}
	cudaMalloc((void **) &d_a,size);
	cudaMalloc((void **) &d_b,size1);
	cudaMalloc((void **) &d_t,size2);
	cudaMemcpy(d_a,a,size,cudaMemcpyHostToDevice);
	cudaMemcpy(d_b,b,size1,cudaMemcpyHostToDevice);
	dim3 block(2,2,1), grid(ceil(q/2),ceil(m/2),1);
	matmul<<<grid,block>>>(d_a,d_b,d_t,n);
	cudaMemcpy(t,d_t,size2,cudaMemcpyDeviceToHost);
	printf("Result vector:\n");
	for(int i=0; i<m; i++)
	{
		for(int j=0; j<q; j++) printf("%d ",t[i*q+j]);
		printf("\n");
	}
	cudaFree(d_a);
	cudaFree(d_t);
	return 0;	
}