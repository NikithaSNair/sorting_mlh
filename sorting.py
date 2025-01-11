def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_sort(numbers)
print(numbers)
