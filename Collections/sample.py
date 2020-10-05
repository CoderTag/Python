import sys

print(sys.argv)

if sys.argv[1] == "add":
    print(f'={int(sys.argv[2]) + int(sys.argv[3])}')