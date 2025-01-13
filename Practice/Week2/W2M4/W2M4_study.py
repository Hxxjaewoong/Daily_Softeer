from multiprocessing import Process, Queue, current_process
import time

def worker(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait() # 작업 검색..?
        except Exception:
            break
        else: # 각 프로세스는 현재 실행 중인 작업을 인쇄하고 완료 메시지를 tasks_that_are_done에 추가
            print(f"{task} is being executed by {current_process().name}")
            time.sleep(0.5) # 작업 실행 시간을 시뮬레이션
            tasks_that_are_done.put(f"{task} is done by {current_process().name}")

def main():
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    
    for task_no in range(10):
        task = f"Task no {task_no}"
        print(task)
        tasks_to_accomplish.put(task)

    processes = []
    for i in range(2):
        process = Process(target=worker, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join() # 모든 프로세스가 작업을 완료하고 동기화되는지 확인하는 부분
        
    print("\nTask Completion Results:")
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())  # 모든 프로세스가 완료된 후 tasks_that_are_done에 저장된 완료 메시지를 인쇄하는 부분
    
if __name__ == "__main__":
    main()