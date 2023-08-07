money = 0
num_shoes = int(input())
shoe_sizes = [int(i) for i in input().split()]
num_customers = int(input())
for i in range(num_customers):
    inp = [int(i) for i in input().split()]
    if inp[0] in shoe_sizes:
        money += inp[1]
        shoe_sizes.remove(inp[0])
print(money)
