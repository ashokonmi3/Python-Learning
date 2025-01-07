import multiprocessing
import threading
import time

# Function to compute the sum of squares of a large range of numbers


# def compute_sum_of_squares(start, end):
#     total = 0
#     for i in range(start, end):
#         total += i * i
#     return total

# # Function to run the task using multiple threads


# def run_with_threads():
#     threads = []
#     start_time = time.time()

#     # Create multiple threads to run the compute_sum_of_squares function
#     for i in range(4):  # 4 threads
#         thread = threading.Thread(
#             target=compute_sum_of_squares, args=(i * 250000, (i + 1) * 250000))
#         threads.append(thread)
#         thread.start()

#     # Wait for all threads to finish
#     for thread in threads:
#         thread.join()

#     print(
#         f"Time taken with multithreading: {time.time() - start_time:.4f} seconds")


# if __name__ == "__main__":
#     run_with_threads()
# ==============================

# Function to compute the sum of squares of a large range of numbers

def compute_sum_of_squares(start, end):
    total = 0
    for i in range(start, end):
        total += i * i
    return total

# Function to run the task using multiple processes


def run_with_multiprocessing():
    processes = []
    start_time = time.time()

    # Create a pool of 4 processes to run the compute_sum_of_squares function
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(compute_sum_of_squares, [(
            i * 250000, (i + 1) * 250000) for i in range(4)])

    print(
        f"Time taken with multiprocessing: {time.time() - start_time:.4f} seconds")


if __name__ == "__main__":
    run_with_multiprocessing()
