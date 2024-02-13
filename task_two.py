from collections import deque


def is_palindrome(s):

    s_formatted = ''.join(e for e in s if e.isalnum()).lower()

    queue = deque()
    for char in s_formatted:
        queue.append(char)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return f"Рядок '{s}' не є паліндромом."
    return f"Рядок '{s}' є паліндромом."


input_string = input("Введіть рядок, щоб перевірити чи він є паліндромом: ")
print(is_palindrome(input_string))