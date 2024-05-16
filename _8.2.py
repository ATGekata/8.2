def shift_array(arr):
    n = len(arr)
    shifted_arr = [arr[n-1]] + arr[:n-1]
    return shifted_arr

N = int(input("Enter the number of elements N: "))

numbers = list(map(int, input().split()))

shifted_numbers = shift_array(numbers)

print("Shifted array:")
for num in shifted_numbers:
    print(num, end=" ")
