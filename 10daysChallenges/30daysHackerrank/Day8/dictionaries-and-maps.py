n = int(input())
phonebook = {}

# read lines into phonebook & remove 
for i in range(n):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        lookup = str(input())

        if lookup in phonebook:
            print(''.join('%s=%r' % (lookup, phonebook[lookup])))
        else:
            print("Not found")
    except EOFError:
        break