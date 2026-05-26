s = input("Enter a string: ")
result = ""

for char in s:
    found = False
    
    for r in result:
        if char == r:
            found = True
            break
    
    if not found:
        result = result + char

print("After removing duplicates:", result)