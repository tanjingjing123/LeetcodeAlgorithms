def angleClock(hour, minutes):
    one_min_angle = 6
    one_hour_angle = 30

    minutes_angle = one_min_angle * minutes
    hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

    diff = abs(hour_angle - minutes_angle)
    return min(diff, 360 - diff)

hour = 3
minutes = 15
print(angleClock(hour, minutes))