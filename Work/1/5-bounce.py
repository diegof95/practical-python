# bounce.py
#
# Exercise 1.5

height = 100
bouncing = 3/5

print("""A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5 the height it fell.\nTable showing the height of the first 10 bounces:""")

i = 0
while i < 10:
    new_height = round(height * bouncing, 4)
    print('Bounce ', i, ':', new_height)
    height = new_height
    i += 1