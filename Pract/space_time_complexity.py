myRange = 1000000

# timeEfficiency = [r*r for r in range(myRange)]
# print(timeEfficiency)


spaceEfficiency = (r*r for r in range(myRange))
print(spaceEfficiency)
for val in spaceEfficiency:
    print(val, end=" ")
    
# Run it as $ /usr/bin/time -f "Memory used (kB): %M\nUser time (seconds): %U" python3  space_time_complexity.py

