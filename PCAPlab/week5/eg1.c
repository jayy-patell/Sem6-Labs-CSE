#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// OpenCL includes
#include <CL/cl.h>

#define MAX_SOURCE_SIZE 1000

int main() {
    int n; 
	const char *programSource = "__kernel void vecmul(__global int *A, __global int *B, __global int *C) {
	  int idx = get_global_id(0); C[idx] =A[idx] * B[idx];}";

	 
	 puts(programSource); 
	int *A = NULL; 
	int *B = NULL; 
	int *C = NULL; // Output array

	fprintf(stdout,"ENTER NUMBER ELEMENTS IN THE VECTOR\n");
	scanf("%d",&n);
	size_t datasize=(n*sizeof(int));
	printf("size is datasize%d\n",datasize);
	size_t source_size=strlen(programSource);
	A=(int *)malloc(sizeof(int)*n);
	B=(int *)malloc(sizeof(int)*n);
	C=(int *)malloc(sizeof(int)*n);

	printf("enter the data for A\n");
	for(int i=0;i<n;i++)
		scanf("%d",&A[i]);
	printf("enter the data for B\n");
	for(int i=0;i<n;i++)
		scanf("%d",&B[i]);

	
	// Use this to check the output of each API call
	cl_int status;


	// STEP 1: Discover and initialize the platforms

	cl_uint numPlatforms = 0;
	cl_platform_id *platforms = NULL;
	// Use clGetPlatformIDs() to retrieve the number of platforms
	status = clGetPlatformIDs(0, NULL, &numPlatforms);
	printf("%d platform success %d ",status,numPlatforms); 
	// Allocate enough space for each platform

	platforms = (cl_platform_id*)malloc(numPlatforms*sizeof(cl_platform_id));

	// Fill in platforms with clGetPlatformIDs()
	status = clGetPlatformIDs(numPlatforms, platforms, NULL);

	char pform_vendor[40];
	clGetPlatformInfo(platforms[0], CL_PLATFORM_NAME, sizeof(pform_vendor),
	&pform_vendor, NULL);
	printf(" the vendor %s",pform_vendor);


	// STEP 2: Discover and initialize the devices

	cl_uint numDevices = 0;
	cl_device_id *devices = NULL;
	// Use clGetDeviceIDs() to retrieve the number of // devices present
	status=clGetDeviceIDs(platforms[0],CL_DEVICE_TYPE_GPU,0,NULL,&numDevices);
	// Allocate enough space for each device
	devices = (cl_device_id*)malloc(numDevices*sizeof(cl_device_id));
	// Fill in devices with clGetDeviceIDs()
	status = clGetDeviceIDs(platforms[0],CL_DEVICE_TYPE_GPU,numDevices,devices,NULL);
	printf("%d Device success %d ",status,numDevices); 
	char name_data[100];
	int err = clGetDeviceInfo(devices[0], CL_DEVICE_NAME,sizeof(name_data), name_data, NULL);
	printf(" the device name %s",name_data);


	// STEP 3: Create a context

	cl_context context = NULL;
	// Create a context using clCreateContext() and
	// associate it with the devices
	context = clCreateContext(NULL,numDevices,devices,NULL,NULL,&status);
	printf("%d context success %d ",status,numDevices); 


	// STEP 4: Create a command queue

	cl_command_queue cmdQueue,cmdQueue1;
	// Create a command queue using clCreateCommandQueue(),
	// and associate it with the device you want to execute on
	cmdQueue = clCreateCommandQueue(context, devices[0], 0, &status);
	printf("%d CQ success %d ",status,numDevices); 


	// STEP 5: Create device buffers

	cl_mem bufferA; // Input array on the device
	cl_mem bufferB;
	cl_mem bufferC;

	// Use clCreateBuffer() to create a buffer object (d_A)
	// that will contain the data from the host array A
	bufferA = clCreateBuffer(context,CL_MEM_READ_ONLY,datasize,NULL,&status);
	bufferB = clCreateBuffer(context,CL_MEM_READ_ONLY,datasize,NULL,&status);
	// Use clCreateBuffer() to create a buffer object (d_C)
	// with enough space to hold the output data
	bufferC = clCreateBuffer(context,CL_MEM_WRITE_ONLY,datasize,NULL,&status);


	// STEP 6: Write host data to device buffers

	// Use clEnqueueWriteBuffer() to write input array A to
	// the device buffer bufferA
	status = clEnqueueWriteBuffer(cmdQueue,bufferA,CL_TRUE,0,datasize,A,0,NULL,NULL);

	status = clEnqueueWriteBuffer(cmdQueue,bufferB,CL_TRUE,0,datasize,B,0,NULL,NULL);


	// STEP 7: Create and compile the program

	// Create a program using clCreateProgramWithSource()
	cl_program program = clCreateProgramWithSource(context,1,(const char**)&programSource,(const size_t *)&source_size,&status);

	// Build (compile) the program for the devices with
	// clBuildProgram()
	status = clBuildProgram(program,numDevices,devices,NULL,NULL,NULL);


	// STEP 8: Create the kernel

	cl_kernel kernel = NULL;

	// Use clCreateKernel() to create a kernel from the
	// vector addition function (named "vecadd")
	kernel = clCreateKernel(program, "vecmul", &status);

	printf("kernel created %d ",status);


	// STEP 9: Set the kernel arguments

	// Associate the input and output buffers with the kernel
	// using clSetKernelArg()
	status = clSetKernelArg(kernel,0,sizeof(cl_mem),&bufferA);
	status = clSetKernelArg(kernel,1,sizeof(cl_mem),&bufferB);
	status |= clSetKernelArg(kernel,2,sizeof(cl_mem),&bufferC);


	// STEP 9: Set the kernel arguments

	// Associate the input and output buffers with the kernel
	// using clSetKernelArg()


	// STEP 10: Configure the work-item structure

	// Define an index space (global work size) of work
	// items for
	// execution. A workgroup size (local work size) is not
	// required,
	// but can be used.
	size_t globalWorkSize[3];
	// There are elements work-items
	globalWorkSize[0] = n;


	// STEP 11: Enqueue the kernel for execution

	// Execute the kernel by using
	// clEnqueueNDRangeKernel().
	// globalWorkSize is the 1D dimension of the
	// work-items
	status = clEnqueueNDRangeKernel(cmdQueue,kernel,1,NULL,globalWorkSize,NULL,0,NULL,NULL);


	// STEP 12: Read the output buffer back to the host

	// Use clEnqueueReadBuffer() to read the OpenCL output
	// buffer (bufferC)
	// to the host output array (C)
	clEnqueueReadBuffer(
		cmdQueue,
		bufferC,
		CL_TRUE,
		0,
		datasize,
		C,
		0,
		NULL,
		NULL);


	printf("the array add is  \n");
	for(int i=0;i<n;i++)
	printf("%d ",C[i]);


	// STEP 13: Release OpenCL resources

	// Free OpenCL resources
	clReleaseKernel(kernel);

	clReleaseProgram(program);
	clReleaseCommandQueue(cmdQueue);

	clReleaseMemObject(bufferA);
	clReleaseMemObject(bufferB);
	clReleaseMemObject(bufferC);
	clReleaseContext(context);

	// Free host resources
	free(A);
	free(B);
	free(C);
	free(platforms);
	free(devices);
}
