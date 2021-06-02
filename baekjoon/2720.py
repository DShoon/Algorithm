# Test case t
t = int(input())

user_inputs = list()
# get user input with size t
for i in range(t):
    user_inputs.append(int(input()))

# calculate n of coins for each user input
for user_input in user_inputs:
    change = [0]*4
    change[0] = user_input // 25
    change[1] = (user_input % 25) // 10
    change[2] = ((user_input % 25) % 10) // 5
    change[3] = ((user_input % 25) % 10) % 5
    print(f"{change[0]} {change[1]} {change[2]} {change[3]}")
