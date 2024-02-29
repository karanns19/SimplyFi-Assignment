def convert_to_indian_currency(num):
    num_str = str(num)  # Convert the integer to a string
    length = len(num_str)  # Find the length of the string
    commas_needed = (length - 1) // 2 # Determine the number of commas needed
    
    if length % 2 != 0: # If the length is not divisible by 2, adjust commas_needed
        commas_needed -= 1

    result = num_str[:length % 2 or 1] # Initialize the result string with the first character(s)

    for i in range(commas_needed): # Loop to add commas and remaining characters
        result += ',' + num_str[length % 2 + i * 2: length % 2 + (i + 1) * 2]

    return result


# Test cases
inputs = [504678, 123456789, 9876543210]
for num in inputs:
    print(f"Input: {num}, Output: {convert_to_indian_currency(num)}")
