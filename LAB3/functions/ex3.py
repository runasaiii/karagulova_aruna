def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if (2 * c) + (4 * r) == numlegs:
            return c, r
    return 0


numheads, numlegs=map(int,input().split())
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution")
