# SPH Particle Simulation - Sorting Algorithm Implementations

This project contains implementations of various sorting algorithms for the Smooth Particle Hydrodynamics (SPH) simulation, focusing on Bitonic Sort, Counting Sort, Merge Sort, and Bucket Sort. Different parallelization techniques are applied to experiment and analyze the performance.

## File List

- `particle_simulation_bitonic_sort_cuda.cu`: Bitonic Sort simulation program implemented with CUDA parallelization.
- `particle_simulation_counting_sort_pthread.cpp`: Counting Sort simulation program implemented with Pthreads parallelization.
- `particle_simulation_counting_sort_openmp.cpp`: Counting Sort simulation program implemented with OpenMP parallelization.
- `particle_simulation_counting_sort_cuda.cu`: Counting Sort simulation program implemented with CUDA parallelization.

## Instructions

### Environment Setup

To run the programs, set up the appropriate environment for the required parallelization technique:

- **CUDA**: Install the NVIDIA CUDA Toolkit and configure the environment variables.
- **Pthreads**: Ensure that your C++ compiler supports the pthread library.
- **OpenMP**: Ensure that your compiler supports OpenMP (e.g., GCC, Clang).

### Modify Number of Particles

To change the number of particles, open the relevant file (e.g., `particle_simulation_counting_sort_pthread.cpp`) and modify the `num_particles` variable to set the desired number of particles (e.g., 10K, 100K, 1M, etc.).

### Compile and Run

To compile and run the programs, follow these steps based on the file type:

- **CUDA Program**: Use `nvcc` to compile, for example:
    ```bash
    nvcc particle_simulation_bitonic_sort_cuda.cu -o bitonic_sort_cuda
    ./bitonic_sort_cuda
    ```

- **Pthreads Program**: Use a C++ compiler to compile, for example:
    ```bash
    g++ particle_simulation_counting_sort_pthread.cpp -o counting_sort_pthread -lpthread
    ./counting_sort_pthread
    ```

- **OpenMP Program**: Use a compiler that supports OpenMP, for example:
    ```bash
    g++ particle_simulation_counting_sort_openmp.cpp -o counting_sort_openmp -fopenmp
    ./counting_sort_openmp
    ```

### Result Analysis

- Modify the `num_particles` value to test the performance with different particle counts.
- Collect performance data such as execution time for comparison and analysis.

### Notes

- CUDA programs require a compatible NVIDIA GPU to execute.
- Ensure that the appropriate tools and libraries are installed in the environment for successful compilation and execution.
