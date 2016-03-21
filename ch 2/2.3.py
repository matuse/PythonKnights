import math

# 1 -

r = 5
# pi = 3.14
pi = math.pi
volume = (4.0/3.0) * pi * r ** 3

print (volume)

# 2 -

n = 60
msrp = 24.95
discount = .4
shipping = 3 + (n -1) * .75
total_cost = n * (msrp - (msrp * discount)) + shipping

print (total_cost)

# 3 -

left_house = (6*60*60) + (52*60)
easy_pace = (8*60) + 15
tempo = (7 * 60) + 12

breakfast = left_house + (1 * easy_pace) + (3 * tempo)
bt_hour = breakfast / (60*60)
bt_min = (breakfast - (bt_hour*60*60)) / 60
bt_sec = breakfast - (bt_hour*60*60) - (bt_min*60)

print (bt_hour, bt_min, bt_sec)
