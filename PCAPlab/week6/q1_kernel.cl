__kernel void strCpy(__global char *s,__global char *res,int len)
{
	// Get index of current work item
	int tid= get_global_id(0);

	// Do operation
	for(int i=0;i<len;i++)
		res[len*tid+i]=s[i];
}