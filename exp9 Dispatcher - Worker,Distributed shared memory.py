import threading
import queue
import time

def worker(task_queue, worker_id):
    while not task_queue.empty():
        try:
            task = task_queue.get_nowait()
            print(f"Worker {worker_id} is processing task: {task}")
            print(f"Queue after Worker {worker_id} picked a task: {list(task_queue.queue)}")
            time.sleep(2)
            print(f"Worker {worker_id} completed task: {task}\n")
            task_queue.task_done()
        except queue.Empty:
            break

def main():
    num_workers = int(input("Enter the number of workers: "))
    num_tasks = int(input("Enter the number of tasks: "))

    task_queue = queue.Queue()
    for i in range(1, num_tasks + 1):
        task_queue.put(f"Task {i}")

    print("\nInitial Task Queue:")
    print(list(task_queue.queue))

    workers = []
    for i in range(num_workers):
        thread = threading.Thread(target=worker, args=(task_queue, i + 1))
        workers.append(thread)
        thread.start()

    for thread in workers:
        thread.join()

    print("\nFinal Task Queue (should be empty if all tasks are done):")
    print(list(task_queue.queue))
    print("All tasks are completed!")

if __name__ == "__main__":
    main()
    
# output format:
# Enter the number of workers: 3
# Enter the number of tasks: 5

