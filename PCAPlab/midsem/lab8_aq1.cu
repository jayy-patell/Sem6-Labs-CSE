//Q2 and Q3 done in rough notebook.

%%cu
#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <string.h>
_global_ void reverse_words(char *S,int *starts, int n)
{
    int i=threadIdx.x;
    int start=starts[i], end;
    end=starts[i+1]-2;
    printf("%d - start - %d - %c ; end - %d - %c\n",i, start,S[start],end,S[end]);
    while(start<end)
    {
        char temp=S[start];
        S[start]=S[end];
        S[end]=temp;
        start++;
        end--;
    }
}
int main()
{
    int n = 4, size=0, starts[n+1], startindex=0, *dstarts;
    char A[100], *dA;
    strcpy(A,"This is my sentence");
    puts(A);
    size=strlen(A);
    starts[startindex++]=0;
    for(int i=0; i<size; i++)
    {
        if(A[i]==' ') starts[startindex++]=i+1;
    }
    starts[startindex]=size+1;
    cudaMalloc((void **)&dA,sizeof(char)*size);
    cudaMalloc((void *)&dstarts,sizeof(int)(n+1));
    cudaMemcpy(dA, A, sizeof(char)*size, cudaMemcpyHostToDevice);
    cudaMemcpy(dstarts, starts, sizeof(int)*(n+1), cudaMemcpyHostToDevice);
    reverse_words<<<1,n>>>(dA,dstarts,size);
    cudaMemcpy(A,dA, sizeof(char)*size, cudaMemcpyDeviceToHost);
	  puts(A);
    cudaFree(dA);
    return 0;
}