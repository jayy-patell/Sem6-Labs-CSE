#include <stdio.h>
#include <stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#define TW 4
#define MW 5

//N = array, M = mask, P = result

__global__ void tiled1Dconv(int *N, int *M,int *P, int width)
{	
	int i= blockIdx.x*blockDim.x+threadIdx.x,bx=blockIdx.x, tx = threadIdx.x;
	int h = MW/2;
	__shared__ int Ns[TW + MW -1];
	int halo_left_index = (bx -1)*TW + tx;
	if (tx >= TW -h) Ns[tx - (TW -h)] = (halo_left_index < 0) ? 0 : N[halo_left_index];
	Ns[h + tx] = N[i];
	int halo_right_index = (bx + 1)*TW + tx;
	if (tx < h) Ns[h +TW + tx] = (halo_right_index > width) ?  0 : N[halo_right_index];
	for(int j=0; j<8; j++) printf("%d - %d\n",i,Ns[j]);
	__syncthreads();
	int sum=0;
	for(int j=0; j<MW; j++) sum+=Ns[tx + j] * M[j];
	P[i]=sum;
}

int main(void) {
	int width = 16;
	int N[16]={1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8},M[MW]={1,1,2,1,1},P[16];
	int *dN,*dM, *dP;
	cudaMalloc((void **)&dN,sizeof(int)*width);
	cudaMalloc((void **)&dP,sizeof(int)*width);
	cudaMalloc((void **)&dM,sizeof(int)*MW);
	cudaMemcpy(dN,N,sizeof(int)*width,cudaMemcpyHostToDevice);
	cudaMemcpy(dM,M,sizeof(int)*MW,cudaMemcpyHostToDevice);
	tiled1Dconv<<<1,TW>>>(dN,dM,dP,width);
	cudaMemcpy(P,dP,sizeof(int)*MW,cudaMemcpyDeviceToHost);
	for(int i=0; i<width; i++) printf("%d ",P[i]);
	cudaFree(dM);
	cudaFree(dN);
	cudaFree(dP);
	return 0;
}	