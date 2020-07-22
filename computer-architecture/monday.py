# In general, the `.format` method is considered more modern than the printf `%`
# operator.
​
num = 123
​
# Printing a value as decimal
​
print(num)                     # 123
print("%d" % num)              # 123
print("{:d}".format(num))      # 123
​
# Printing a value as hex
​
print(hex(num))                # 0x7b
print("%x" % num)              # 7b
print("%X" % num)              # 7B
print("%04X" % num)            # 007B
print(f"{num:x}")      # 7b
print(f"{num:X}")      # 7B
print(f"{num:04x}")    # 007b
​
# Printing a value as binary
​
print("{num:b}".format(num))      # 1111011, format method
​
# Converting a decimal number in a string to a value
​
s = "1234"; # 1234 is 0x4d2
x = int(s); # Convert base-10 string to value
​
# Printing a value as decimal and hex
​
print(num)                     # 1234
print(f"{num:x}")      # 4d2
​
# Converting a binary number in a string to a value
​
s = "100101"   # 0b100101 is 37 is 0x25
x = int(s, 2)  # Convert base-2 string to value
​
# Printing a value as decimal and hex
​
print(num)                     # 37
print(f"{num:x}")      # 25
​
​
# Conversion Python code:
​
str = "10101010"
​
def to_decimal(num_string, base):
    digit_list = list(num_string)
    digit_list.reverse()
    value = 0
    for i in range(len(digit_list)):
        print(f"+({int(digit_list[i])} * {base ** i})")
        value += int(digit_list[i]) * (base ** i)
    return value
​
to_decimal(str, 2)



###################################
"""
CPU
    Executing instructions
    Gets them out of RAM
    Registers (like variables)
        Fixed names  R0-R7
        Fixed number of them -- 8 of them
        Fixed size -- 8 bits
​
Memory (RAM)
    A big array of bytes
    Each memory slot has an index, and a value stored at that index
    That index into memory AKA:
        pointer
        location
        address
"""
​
memory = [
    1,  # PRINT_BEEJ
    1,  # PRINT_BEEJ
    1,  # PRINT_BEEJ
    3,  # SAVE_REG R2,64  register to save in, the value save there
    2,  #          R2
    64, #             64
    4,  # PRINT_REG R2
    2,  #           R2
    2,  # HALT <-- pc
]
​
register = [0] * 8
​
pc = 0  # Program Counter, index into memory of the current instruction
        # AKA a pointer to the current instruction
​
running = True
​
while running:
    inst = memory[pc]
​
    if inst == 1:  # PRINT_BEEJ
        print("Beej")
        pc += 1
​
    elif inst == 2:  # HALT
        running = False
​
    elif inst == 3:  # SAVE_REG
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
​
        register[reg_num] = value
​
        pc += 3
​
    elif inst == 4: # PRINT_REG
        reg_num = memory[pc + 1]
        print(register[reg_num])
​
        pc += 2
​
    else:
        print(f"Unknown instruction {inst}")