testcase = int(input()) 
problems_solved_count = 0

for _ in range(testcase):

    opinions = list(map(int, input().split()))
    if sum(opinions) >= 2:
        problems_solved_count += 1

print(problems_solved_count)