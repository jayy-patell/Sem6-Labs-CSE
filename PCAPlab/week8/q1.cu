#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#define N 1024
__global__ void wordFreq(char *sent,char *word,int n,int *d_count)
{	
	int i = threadIdx.x;
	for(int j=0; j<n; j++) 
	{		
		if(sent[i+j]!=word[j]) return;
	}
	atomicAdd(d_count,1);
}

int main(void)
{
	char sent[N],word[100],*d_sent,*d_word;
	int count=0, *d_count;
	printf("Enter a sentence: "); fgets(sent,N,stdin);
	printf("Enter a word: "); scanf("%s",word);
	printf("Sentence: %sWord: %s\n",sent,word);
	cudaMalloc((void **)&d_sent,strlen(sent)*sizeof(char));
	cudaMalloc((void **)&d_word,strlen(word)*sizeof(char));
	cudaMalloc((void **)&d_count,sizeof(int));
	cudaMemcpy(d_sent,sent,strlen(sent)*sizeof(char),cudaMemcpyHostToDevice);
	cudaMemcpy(d_word,word,strlen(word)*sizeof(char),cudaMemcpyHostToDevice);
	cudaMemcpy(d_count,&count,sizeof(int), cudaMemcpyHostToDevice);
	wordFreq<<<1,strlen(sent)-strlen(word)>>>(d_sent,d_word,strlen(word), d_count);
	cudaMemcpy(&count,d_count,sizeof(int),cudaMemcpyDeviceToHost);
	printf("Word occurences: %d\n",count);
	cudaFree(d_sent);
	cudaFree(d_word);
	cudaFree(d_count);
	return 0;
}