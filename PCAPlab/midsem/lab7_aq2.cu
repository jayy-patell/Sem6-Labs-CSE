//Selection sort on matrix rows. Each row is sorted by one thread.

__global__ void ssortmatr(int *A, int size)
{
    int rowid = threadIdx.x;
    for(int i=0; i<size-1; i++)
    {
        int mini=i;
        for(int j=i+1; j<size; j++)
            if(A[rowid*3+mini]>A[rowid*3+j]) mini=j;
        if(mini!=i)
        {
            int temp = A[rowid*3+mini];
            A[rowid*3+mini]=A[rowid*3+i];
            A[rowid*3+i]=temp;
        }
    }
}