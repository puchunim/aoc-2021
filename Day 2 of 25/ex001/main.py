with open("commands.txt", "r") as cmd_file:
    commands = cmd_file.read().split("\n") # Generating list of submarine commands

h_pos = 0 # Horizontal position of the submarine
depth = 0 # Depth of the submarine

for cmd_arg in commands: # For all de instructions in list
    cmd, arg = cmd_arg.split(" ") # Spliting command and arg into separate variables

    if cmd == "forward": # If the instruction is to go forward
        h_pos += int(arg) # Horizontal position is increased
    
    elif cmd == "down": # If the instruction is to go down
        depth += int(arg) # Depth is increased
    
    else: # Else (command is to go up)
        depth -= int(arg) # Depth is decreased

print(f"Horizontal position: {h_pos}")
print(f"Depth amount: {depth}")
print(f"{h_pos} x {depth} = {h_pos * depth}")
