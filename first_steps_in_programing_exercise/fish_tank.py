length_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percent = float(input())

volume_of_aquarium = length_in_centimeters * width_in_centimeters * height_in_centimeters
volume_of_litters = volume_of_aquarium * 0.001
recalc_percent = percent / 100

NEED_LITTERS = volume_of_litters * (1 - recalc_percent)


print(NEED_LITTERS)