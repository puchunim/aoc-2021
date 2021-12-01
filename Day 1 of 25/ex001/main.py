with open("depths.txt", "r") as depths: # Opening the depths.txt file
    med = [int(d) for d in depths.read().split("\n")] # Creating the medition list

tmp = med[0] # Temp. value
print(f"{tmp} (N/a - no previous measurement)") # Initial value

total_depth = 0 # Total count of depth higher than the previous ones
for depth in med[1:]: # For depth in depth values (ignoring the first)
    if depth < tmp: # If the act. depth is lower than temporary value
        print(f"{depth} (decreased)")
    
    elif depth > tmp: # If the act. depth is higher than temporary value
        print(f"{depth} (increased)")
        total_depth += 1 # The counter is increased
    
    else: # Else (both values are equal)
        print(f"{depth} (no change)")

    tmp = depth # The temporary variable always will be updated

print(f"{total_depth} depths are higher than the previous one")
# Output: 1624