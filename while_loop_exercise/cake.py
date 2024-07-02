width = int(input())
length = int(input())

cake_size = width * length
pieces_taken = 0

command = input()

while command != "STOP":
    pieces_taken += int(command)
    if pieces_taken >= cake_size:
        break
    command = input()

if pieces_taken >= cake_size:
    print("No more cake left! You need {} pieces more.".format(pieces_taken - cake_size))
else:
    print("{} pieces are left.".format(cake_size - pieces_taken))
