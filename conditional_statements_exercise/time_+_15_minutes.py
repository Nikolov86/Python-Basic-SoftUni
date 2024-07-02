hours = int(input())
minutes = int(input())

new_hours = (hours + (minutes + 15) // 60) % 24
new_minutes = (minutes + 15) % 60

if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
   print(f"{new_hours}:{new_minutes}")


