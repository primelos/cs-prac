def truckTour(petrolpumps):
    tank = 0
    start = 0
    current = 0

    while start < len(petrolpumps):
        tank += petrolpumps[current][0]
        tank -= petrolpumps[current][1]

        if tank >= 0:
            current = (current + 1) % len(petrolpumps)
            if current == start:
                return start
        else:
            start = current + 1
            current = start
            tank = 0

# Input(stdin)
# 3
# 1 5
# 10 3
# 3 4

# answer = index  => 1