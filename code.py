import time

start = time.time()

pi = '3141592653589793238462643383279'
favorites = ['314', '49', '9001', '15926535897', '14', '93238', '9323', '8462643383279', '793', '4', '159265358979', '314159']

output = '314 15926535897 9323 8462643383279' # answer = 3 (spaces needed)


# Find any numbers that fit in pi and sort them from biggest to smallest
fav_nums = []
for i in range(len(favorites)):
    if pi.find(favorites[i]) != -1:
        fav_nums.append(favorites[i])
fav_nums.sort(key=int, reverse=True)

end_while = 20  # Should be adjusted on the size of pi
index = 0
loop = 0
count = 0
spaces = -1  # Not 0 because there is no space in the beginning
nums = []
repeat_nums = []
other_nums = [] # This list can be used further to make the algorithm find more complex combinations
found = False

while not found:

    # Goes through every number in fav_nums
    for i in range(len(fav_nums)):
        
        if i == 0: repeat_nums = nums
        
        # Checks if the number fits at given index
        if pi.find(fav_nums[i], index) == index:
            nums.append(fav_nums[i])
            index += len(fav_nums[i])
            spaces+=1

        # If the next number cannot be found, removes last fit
        if loop == 3:
            other_nums.append(nums[-1])
            index -= len(fav_nums[fav_nums.index(nums[-1])])
            fav_nums.pop(fav_nums.index(nums[-1]))
            nums.pop()
            spaces-=1
            loop = 0
            break

    if repeat_nums == nums: loop+=1
    count+=1

    if index == len(pi):
        found = True
    elif count == end_while:
        print("Cannot find the number or end_while is too small")

print(nums)
print(spaces)


end = time.time()
print("\nTime elapsed: " + str(end-start))
