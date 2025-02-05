"""Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the
chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
create function: solve(numheads, numlegs):"""
def solve (num_heads,num_legs):
    for chickens in range(num_heads):
        rabbits = num_heads - chickens
        if 4*rabbits + 2*chickens == num_legs:
            return rabbits,chickens
    return None

heads = 35
legs = 94
rabbits,chickens = solve(heads,legs)
print(rabbits,chickens)
#12,23
