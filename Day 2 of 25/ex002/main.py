with open("commands.txt", "r") as cmd_file:
    commands = cmd_file.read().split("\n") # Generating list of submarine commands

h_pos = 0 # Horizontal position of the submarine
depth = 0 # Depth of the submarine
aim = 0 # Aim of the submarine

for cmd_arg in commands: # For all instruction in the list
    cmd, arg = cmd_arg.split(" ") # Spliting command and arg of the command

    if cmd == "forward":
        h_pos += int(arg) # Horizontal position is increased

        if aim: # If aim is not 0
            depth += int(arg) * aim # Depth is increased with the result of arg * aim

    elif cmd == "down": # If the command is go down
        aim += int(arg) # Aim is increase
    
    elif cmd == "up": # If the command is go up
        aim -= int(arg) # Aim is decreased

print(f"Aim position: {aim}")
print(f"Horizontal position: {h_pos}")
print(f"Depth amount: {depth}")
print(f"{h_pos} x {depth} = {h_pos * depth}")
