d = {
    'Codingal': int(input("Enter a number for the key named 'Codingal' (range 1 to 10): ")), 
    'is': int(input("Enter a number for the key named 'is' (range 1 to 10): ")),
    'the': int(input("Enter a number for the key named 'the' (range 1 to 10): ")),
    'best': int(input("Enter a number for the key named 'best' (range 1 to 10): ")),
    'tutor': int(input("Enter a number for the key named 'tutor' (range 1 to 10): ")),
    'for': int(input("Enter a number for the key named 'for' (range 1 to 10): ")),
    'Coding': int(input("Enter a number for the key named 'Coding' (range 1 to 10): "))
}

value = int(input('Enter the value that you want to find the occurrence of: '))

# Check if all numbers entered are within the range 1 to 10 (inclusive)
# Using d[key] to safely access the dictionary values
if all(1 <= v <= 10 for v in d.values()):
    frequency = list(d.values()).count(value)
    print('Frequency of', value, 'is:', frequency)
else:
    print('Some values entered are outside the valid range (1 to 10).')