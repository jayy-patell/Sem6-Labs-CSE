#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<CL/cl.h>

#define MAX_SOURCE_SIZE (0x100000)

int main(){
	int i, n;
	printf("Enter how many elements: ");
	scanf("%d",&n);

	//Initialize the input vectors
	int* A = (int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++){
		A[i]=i;
	}
	int* B = (int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++){
		B[i]=i;
	}

	//Load the kernel source code into array source_str
	FILE* fp;
	char *source_str;
	size_t soruce_size;

	fp = fopen("eg2_kernel.cl","r");
	if(!fp){
		fprintf(stderr, "Failed to laod kernel.\n");
		getchar();
		exit(1);
	}
	source_str = (char*)malloc(MAX_SOURCE_SIZE);
	source_size = fread(source_str,1,MAX_SOURCE_SIZE,fp);
	fclose(fp);

	//Get platform and device info
	cl_platform_id platform_id=NULL;
	cl_device_id device_id = NULL;
	cl_uint ret_num_devices, ret_num_platforms;

	cl_int ret = clGetPlatformIDs(1,&platfrom_id,&ret_num_platforms);
	ret = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_GPU,1,&device_id,&ret_num_devices);

	//Create an OpenCL context
	cl_context context = clCreateContext(NULL,1,&device_id,NULL,NULL,&ret);

	//Create a command queue
	cl_command_queue command_queue = clCreateCommandQueue(context,device_id,NULL,&ret);

	//Create memory buffers on the device for each vector
	cl_mem a_mem_obj = clCreateBuffer(context,CL_MEM_READ_ONLY,n*sizeof(int),NULL,&ret);
	cl_mem b_mem_obj = clCreateBuffer(context,CL_MEM_READ_ONLY,n*sizeof(int),NULL,&ret);
	cl_mem c_mem_obj = clCreateBuffer(context,CL_MEM_READ_ONLY,n*sizeof(int),NULL,&ret); 

	//Copy A & B to respective memory buffers
	ret = clEnqueueWriteBuffer(command_queue,a_mem_obj,CL_TRUE,0,n*sizeof(int),A,0,NULL,NULL);
	ret = clEnqueueWriteBuffer(command_queue,b_mem_obj,CL_TRUE,0,n*sizeof(int),B,0,NULL,NULL);

	//Create a program from the kernel source
	cl_program program = clCreateProgramWithSource(context,1,(const char**)&source_str,(const size_t)&source_size, &status);

	//Build the program
	ret = clBuildProgram()

}