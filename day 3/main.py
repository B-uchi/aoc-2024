import re

def first_half(input):
    multiply = lambda x,y: x*y
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input)
    product_sum = sum([multiply(x,y) for x,y in [[int(z) for (z) in x[4:-1].split(",")] for x in matches]])
    return product_sum

def second_half(input):
    multiply = lambda x: x[0]*x[1]
    pattern_to_match = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern_to_match, input)
    total_product = 0
    to_multiply = True
    for command in matches:
        if command == "don't()":
            to_multiply = False
            continue
        else:
            if command == "do()":
                to_multiply = True
            elif to_multiply == True:
                total_product+= multiply(tuple([int(x) for x in command[4:-1].split(",")]))
                
                
                
    return total_product
    


with open("input.txt", "r") as file:
    full_text = ""
    lines = file.readlines()
    for line in lines:
        full_text += line
        
    

# first_result = first_half(full_text)
second_result = second_half(full_text)
print(second_result)

