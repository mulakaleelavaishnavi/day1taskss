s = input("Enter a string: ")

longest = ""
current = ""

for char in s:
    if char not in current:
        current = current + char
    else:
        current = char   # reset when repeated
    
    if len(current) > len(longest):
        longest = current

print("Longest substring:", longest)