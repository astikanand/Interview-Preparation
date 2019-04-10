def clock_angle(hours, minutes):
    h = hours%12
    m = minutes%60

    hour_hand_angle = h*30 + m*0.5
    minute_hand_angle = m*6

    angle = abs(hour_hand_angle-minute_hand_angle)

    return min(angle, 360-angle)



print("Example-1: clock_angle(9, 60)")
print(clock_angle(9, 60))

print("Example-2: clock_angle(12, 30)")
print(clock_angle(12, 30))

print("Example-3: clock_angle(3, 30)")
print(clock_angle(3, 30))
