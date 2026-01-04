#2009 A

testcase = int(input())

for i in range(testcase):
    a, b = map(int, input().split())
    if a<=b:
        print(b-a)