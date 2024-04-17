#include<cuda.h>
_global_ void replaceElements(int *mat,int *B,int m,int n){
  int rid=blockIdx.y*blockDim.y+threadIdx.y;
  int cid=blockIdx.x*blockDim.x+threadIdx.x;
  if(rid<m&&cid<n){
    if(rid==cid)
      B[rid*n+cid]=0;
    else if(rid>cid){
      int sd=0;
      int temp=mat[rid*n+cid];
      while(temp>0){
        sd+=(temp%10);
        temp/=10;
      }
      B[rid*n+cid]=sd;
    }
    else{
      int fact=1;
      int num=mat[rid*n+cid];
      while(num>0){
        fact*=num;
        num--;
      }
      B[rid*n+cid]=fact;
    }
  }
}
int main(){
  int *A,*B,m,n;
  int *d_A,*d_B;
  printf("Enter dimensions: ");
  scanf("%d%d",&m,&n);
  printf("Enter the elements: ");
  A=(int*)malloc(m*n*sizeof(int));
  B=(int*)malloc(m*n*sizeof(int));
  for(int i=0;i<m*n;i++)
    scanf("%d",&A[i]);
  printf("A:-");
  for(int i=0;i<m*n;i++){
    if(i%n==0)
      printf("\n%d ",A[i]);
    else
      printf("%d ",A[i]);
  }
  printf("\nB:-");
  cudaMalloc((void**)&d_A,m*n*sizeof(int));
  cudaMalloc((void**)&d_B,m*n*sizeof(int));
  cudaMemcpy(d_A,A,m*n*sizeof(int),cudaMemcpyHostToDevice);
  dim3 grid(ceil(n/32.0),ceil(m/32.0),1);
  dim3 block(32,32,1);
  replaceElements<<<grid,block>>>(d_A,d_B,m,n);
  cudaMemcpy(B,d_B,m*n*sizeof(int),cudaMemcpyDeviceToHost);
  for(int i=0;i<m*n;i++){
    if(i%n==0)
      printf("\n%d ",B[i]);
    else
      printf("%d ",B[i]);
  }
  printf("\n");
  cudaFree(d_A);
  cudaFree(d_B);
  return 0;
}