# from multiprocessing import Process, Queue

# def square_numbers(numbers, result_queue):
#     squared_numbers = [x ** 2 for x in numbers]
#     result_queue.put(squared_numbers)

# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5]
#     result_queue = Queue()

#     # 각 프로세스가 독립적으로 실행되며, 서로 다른 작업을 수행
#     num_of_processes = 3
#     processes = [Process(target=square_numbers, args=(data, result_queue)) for _ in range(num_of_processes)]

#     for process in processes:
#         process.start()

#     for process in processes:
#         process.join()

#     # 결과를 큐에서 수집
#     results = [result_queue.get() for _ in processes]

#     print("Results:", results)





# from multiprocessing import Process
# import time

# def print_numbers(n):
#     for i in range(1, n+1):
#         print(f"Number: {i}")
#         time.sleep(1)

# if __name__ == "__main__":
#     process1 = Process(target=print_numbers, args=(5,))
#     process2 = Process(target=print_numbers, args=(3,))

#     process1.start()  # 첫 번째 프로세스 시작
#     process2.start()  # 두 번째 프로세스 시작

#     process1.join()   # 첫 번째 프로세스 완료 대기
#     process2.join()   # 두 번째 프로세스 완료 대기

#     print("All processes are complete.")




# from multiprocessing import Process

# def print_continent(name="아시아"):
#     print(f"대륙의 이름은: {name}")

# if __name__ == "__main__":
#     # 기본 프로세스
#     default_process = Process(target=print_continent)
#     default_process.start()
#     print(f"Default Process PID: {default_process.pid}")

#     # 추가 프로세스 생성
#     continents = ["아메리카", "유럽", "아프리카"]
#     processes = [Process(target=print_continent, args=(continent,)) for continent in continents]

#     for process in processes:
#         process.start()
#         print(f"Started Process PID: {process.pid}")

#     # 모든 프로세스가 완료되기를 기다림
#     default_process.join()
#     for process in processes:
#         process.join()