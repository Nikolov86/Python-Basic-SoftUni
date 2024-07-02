width = int(input())
length = int(input())
height = int(input())

apartment_volume = width * length * height
total_boxes_volume = 0

command = input()

while command != "Done":
    total_boxes_volume += int(command)
    if total_boxes_volume >= apartment_volume:
        break
    command = input()

if total_boxes_volume >= apartment_volume:
    print("No more free space! You need {} Cubic meters more.".format(total_boxes_volume - apartment_volume))
else:
    print("{} Cubic meters left.".format(apartment_volume - total_boxes_volume))
