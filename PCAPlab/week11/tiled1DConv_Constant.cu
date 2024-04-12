#include <stdio.h>
#include <stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

__constant__ int ks=3;
__constant__ int k[3];

__global__ void oneDconv(int *a,int *r, int as)
{	
	int gtid = blockIdx.x*blockDim.x+threadIdx.x;
	int h = ks/2;
	if (gtid<as) 
	{
		int result = 0, i, ii;
		for(i=0; i<ks; i++)
		{
			ii=gtid-h+i;
			if(ii>=0 && ii<as) result+=a[ii]*k[i];
		}
		r[gtid]=result;
	}
}
int main(void) {
	int a[10]={1,2,3,4,5,6,7,8,9,10},mask[3]={1,2,1},r[10];
	int as=10,ks=3,size1=as*sizeof(int);
	int *da,*dr;
	cudaMalloc((void **)&da,size1);
	cudaMalloc((void **)&dr,size1);
	cudaMemcpy(da,a,size1,cudaMemcpyHostToDevice);
	cudaMemcpyToSymbol(k,mask,sizeof(int)*ks);
	oneDconv<<<1,10>>>(da,dr,as);
	cudaMemcpy(r,dr,size1,cudaMemcpyDeviceToHost);
	for(int i=0; i<as; i++) printf("%d ",r[i]);
	cudaFree(da);
	cudaFree(dr);
	return 0;
}	