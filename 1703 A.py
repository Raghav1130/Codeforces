#1703 A
a = ["yes","YES","yES","YeS","YEs","yeS","Yes","yEs"]

testcase = int(input())

for i in range(testcase):

    word = input()
    if len(word)==3:
        if word in a:
            print("YES")
        else:
            print("NO")