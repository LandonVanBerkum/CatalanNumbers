def cat (N):
    row = [1]
    for i in range(1, (N+1)//2):
        curr = (row[-1] * (N - i + 1)) // i
        row.append(curr)
    return row[-1]-row[-2]
 
goal = int(input())
print(cat(2*goal - 1) % 1000000007)
