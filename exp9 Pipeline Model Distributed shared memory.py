import threading
import queue
import time

# Pipeline Model Implementation
def stage(stage_id, input_queue, output_queue):
    while not input_queue.empty():
        try:
            task = input_queue.get_nowait()
            print(f"Stage {stage_id} processing: {task}")
            time.sleep(1)  # Simulate task processing
            output_task = f"{task} processed in Stage {stage_id}"
            output_queue.put(output_task)
            input_queue.task_done()
        except queue.Empty:
            break

def run_pipeline_model():
    num_stages = int(input("Enter the number of stages in the pipeline: "))
    num_tasks = int(input("Enter the number of tasks: "))

    # Initialize the first queue with tasks
    current_queue = queue.Queue()
    for i in range(1, num_tasks + 1):
        current_queue.put(f"Task {i}")

    # Process tasks through each stage
    for stage_id in range(1, num_stages + 1):
        next_queue = queue.Queue()
        thread = threading.Thread(target=stage, args=(stage_id, current_queue, next_queue))
        thread.start()
        thread.join()
        current_queue = next_queue  # Move to the next stage

    # Display final processed tasks
    print("\nFinal Processed Tasks:")
    while not current_queue.empty():
        print(current_queue.get())

    print("Pipeline processing complete!")
    
if __name__ == "__main__":
    run_pipeline_model()
    
# output format:
# Enter the number of stages in the pipeline: 3
# Enter the number of tasks: 5

