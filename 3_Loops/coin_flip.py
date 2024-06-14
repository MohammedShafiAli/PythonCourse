import random

head_count = 0
tail_count = 0 
for i in range(100):
    flip_result = random.randint(1,2)
    if flip_result == 1:
        head_count += 1
    else:
        tail_count += 1

print("Head count: ", head_count)
print("Tail count: ", tail_count)

input("Press any key to exit")