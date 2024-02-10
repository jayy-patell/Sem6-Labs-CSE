#include <stdio.h>
#include<time.h>
#include <CL/cl.h>
#include<string.h>
#include<stdlib.h>

// Max source size of the kernel string
#define MAX_SOURCE_SIZE (0x100000)

int main()
{
    char str[200];
    char *res;
    int n,i;
    
//Initialize the input string
    printf("Input String:\n");
    gets(str);
    int len= strlen(str);
    printf("Enter n:\n");
    scanf("%d",&n);

    res = malloc(sizeof(char)*len*n);
   
    
// Load the kernel source code into the array source_str
    FILE *fp;
    char *source_str;
    size_t source_size;
    fp = fopen("q1_kernel.cl", "r");
    if (!fp)
    {
        fprintf(stderr, "Failed to load kernel.\n");
        getchar();
        exit(1);
    }
    source_str = (char*)malloc(MAX_SOURCE_SIZE);
    source_size = fread( source_str, 1, MAX_SOURCE_SIZE, fp);
    fclose( fp );

// Use this to check the output of each API call
    cl_int status;

// STEP-1: Get platform and device info
    cl_platform_id platform_id = NULL;
    cl_device_id device_id = NULL;
    cl_uint ret_num_devices;
    cl_uint ret_num_platforms;

    status = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
    status = clGetDeviceIDs( platform_id, CL_DEVICE_TYPE_GPU, 1,&device_id,&ret_num_devices);

// Create an OpenCL context
    cl_context context = clCreateContext( NULL, 1, &device_id, NULL, NULL, &status);

// Create a command queue
    cl_command_queue command_queue = clCreateCommandQueue(context,device_id, CL_QUEUE_PROFILING_ENABLE, &status);

// Create memory buffers on the device for input and output string  
    cl_mem s_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY,len*sizeof(char), NULL, &status);
    cl_mem res_mem_obj = clCreateBuffer(context, CL_MEM_WRITE_ONLY,len*sizeof(char)*n, NULL, &status);

// Copy the input string into respective memory buffer
    status = clEnqueueWriteBuffer(command_queue, s_mem_obj, CL_TRUE, 0,len *sizeof(char), str, 0, NULL, NULL);

// Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1,(const char**)&source_str, (const size_t *)&source_size, &status);

// Build the program
    printf("Host error code: %d\n",status);
    status = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);
    printf("Kernel error code: %d\n",status);

// Create the OpenCL kernel
    cl_kernel kernel = clCreateKernel(program, "strCpy", &status);

// Set the arguments of the kernel
    status = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&s_mem_obj);
    status = clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&res_mem_obj);
    status = clSetKernelArg(kernel,2,sizeof(int),&len);

// Set the global work size as string length
    size_t global_item_size = n; // Process the entire lists
    size_t local_item_size = 1;

//Execute the OpenCL kernel for entire string in parallel on the device
    cl_event event;
    status = clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL,&global_item_size, &local_item_size, 0, NULL,NULL);
    //kernel execution must be finished before calculating time
    status = clFinish(command_queue);

// Read the result in memory buffer on the device to the local variable res
    status = clEnqueueReadBuffer(command_queue, res_mem_obj, CL_TRUE, 0,len*sizeof(char)*n,res, 0, NULL, NULL);
    
//Display result
    res[len*n]='\0';
    printf("\nResultant concatenated string :%s\n",res);
    

//Cleanup
    status = clReleaseKernel(kernel);
    status = clReleaseProgram(program);
    status = clReleaseMemObject(s_mem_obj);
    status = clReleaseMemObject(res_mem_obj);
    status = clReleaseCommandQueue(command_queue);
    status = clReleaseContext(context);
    free(status);

    getchar(); 

    return 0;
}