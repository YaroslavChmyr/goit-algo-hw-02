from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    request = random.randint(1, 1000)
    queue.put(request)
    print(f"Заявка {request} додана до черги.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request} оброблена.")
    else:
        print("Черга порожня. Немає заявок для обробки.")

while True:
    requests_amount = random.randint(1, 10)
    for _ in range(requests_amount):
        generate_request()
        time.sleep(random.uniform(0.5, 1.0))
    for _ in range(requests_amount):
        process_request()
        time.sleep(random.uniform(0.5, 1.0))
    user_input = input("Натисніть Enter, щоб продовжити, або 'q' та Enter, щоб вийти: ")
    if user_input.strip().lower() == 'q':
        print("Гарного дня!")
        break