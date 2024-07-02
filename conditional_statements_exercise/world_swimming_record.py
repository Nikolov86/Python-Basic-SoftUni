from math import floor

record_sec = float(input())
record_met = float(input())
time_in_sec_for_one_sec = float(input())

time_for_swim =( record_met * time_in_sec_for_one_sec)

slow_down =floor( record_met /15) * 12.5

total_time = time_for_swim + slow_down

if total_time >= record_sec:
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")

else:
    total_time < record_sec
    print(f" Yes, he succeeded! The new world record is {time_for_swim + slow_down:.2f} seconds.")

