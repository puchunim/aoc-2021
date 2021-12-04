# with open("binaries.txt") as bn_file: # Opening binary input
#    b_numbers = bn_file.read().split("\n") # Generating binary list

# TODO: Arrumar o código todo, ele tá com problema
b_numbers = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

ox_list = b_numbers[:] # List for the Oxygen Generator
c02_list = b_numbers[:] # List for the C02 Scrubber

for num in range(0, len(b_numbers[0])): # For all numbers in 0 -> length of first element on list
    row = [b[num] for b in b_numbers] # Generating row list

    if row.count('0') > row.count('1'): # If the count of 0's are greater than 1's
        pred_ox = '0' # Predominant number for ox_list
        pred_c02 = '1' # Predominant number for c02_list

    
    elif row.count('0') < row.count('1'): # If the count of 1's are greater than 0's
        pred_ox = '1' # Predominant number for ox_list
        pred_c02 = '1' # Predominant number for c02_list

    else: # Else (1's and 0's are equal)
        pred_ox = '1' # Predominant number is 1 for Oxygen Rating
        pred_c02 = '0' # Predominant number is 0 for C02 Scrubber Rating

    ox_list = [n for n in ox_list if n[num:].startswith(pred_ox)] # Oxygen list is updated
    c02_list = [n for n in c02_list if n[num:].startswith(pred_c02)] # C02 list is updated

print(ox_list)
print(c02_list)
