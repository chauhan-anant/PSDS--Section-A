#To find the maximum number of pairs of characters that can be formed from a given string,we can use a frequency dictionary to count the occurrences of each character. Then, we can calculate how many pairs can be formed by taking the integer division of each character's count by 2 and summing these values.
A = int(input("Enter number of test cases: "))
for _ in range(A):
    s = input("Enter the string: ")
    reccure = {}
    for ch in s:
        reccure[ch] = reccure.get(ch, 0) + 1
    ans = 0
    for count in reccure.values():
        ans += count // 2
    print(ans)