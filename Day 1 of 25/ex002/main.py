with open("depths.txt", "r") as depths: # Opening the depths.txt file
    med = [int(d) for d in depths.read().split("\n")] # Creating the medition list

tmp = med[0] + med[1] + med[2] # Temp. value
print(f"{tmp} (N/a - no previous sum)") # Initial value

i = 1 # Index start in 1 (second item of the depth list)
total_depth = 0 # Total count of depth sum higher than the previous ones
while True: # Infinite loop
    if (i + 3) > len(med): # If the index is greater than the length of the list
        break # Loops end

    # Unnecessary but readable
    t1 = med[i] # First term of the sum
    t2 = med[i+1] # Second term of the sum
    t3 = med[i+2] # Third term of the sum

    tmp_sum = t1 + t2 + t3 # Temp. sum of terms

    if tmp_sum < tmp: # If the act. sum is lower than the temporary value
        print(f"{tmp_sum} (decreased)")
    
    elif tmp_sum > tmp: # If the act. sum is higher than the temporary value
        print(f"{tmp_sum} (increased)")
        total_depth += 1
    
    else: # Else (both values are equal)
        print(f"{tmp_sum} (no change)")

    tmp = tmp_sum # Temp. value is now equal to temp. sum
    i += 1 # Index is increased

print(f"{total_depth} sums are higher than the previous one")
# Output: 1653