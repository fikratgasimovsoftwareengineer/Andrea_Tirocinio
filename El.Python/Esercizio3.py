#Loop Through Numbers

def count_even_numbers(n):
    even_numbers = []
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
            count += 1
    return count, even_numbers

# Get input from the user
n = int(input("Enter a number: "))

# Call the function and get the result
count, even_numbers = count_even_numbers(n)
print(f"The count of even numbers from 1 to {n} is: {count}")
print(f"The list of even numbers from 1 to {n} is: {even_numbers}")

