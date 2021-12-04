with open("binaries.txt") as bn_file: # Opening binary input
    b_numbers = bn_file.read().split("\n") # Generating binary list

gamma = "" # Initializing gamma binary
epsilon = "" # Initializing epsilon binary

for num in range(0, len(b_numbers[0])): # For all numbers in 0 -> length of first item in the list
    row = [b_num[num] for b_num in b_numbers] # Generating row list

    if row.count('0') > row.count('1'): # If the count of 0's in the row are greater than 1's
        gamma += '0' # Gamma's new character is 0
        epsilon += '1' # Epsilon's new character is 1
    
    else: # Else (count of 1's is greater)
        gamma += '1' # Gamma's new character is 1
        epsilon += '0' # Epsilon's new character is 0

dec_gamma = int(gamma, 2) # Decimal convertion of gamma
dec_epsilon = int(epsilon, 2) # Decimal convertion of epsilon

print(f"Gamma binary: {gamma} (dec: {dec_gamma})")
print(f"Epsilon binary: {epsilon} (dec: {dec_epsilon})")
print(f"{dec_gamma} x {dec_epsilon} = {dec_gamma * dec_epsilon}")