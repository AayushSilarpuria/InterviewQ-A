# input : "AAAAERCCEETTTAA"
# Output: "A4E1R1C2E2T3A2"

my_string = "AAAAERCCEETTTAA"
current_char = my_string[0]
current_count = 1
output_str = ""

for i in range(1, len(my_string)):
    if my_string[i] == current_char:
        current_count += 1
    else:
        output_str += current_char + str(current_count)
        current_char = my_string[i]
        current_count = 1

output_str += current_char + str(current_count)
print(output_str) # prints "A4E1R1C2E2T3A2"

