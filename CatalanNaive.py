nums = [1,1]
MOD = 1000000007
goal = int(input())
for i in range(2, goal+1):
  s = 0
  for k in range(1, i+1):
    left = nums[k-1] % MOD
    right = nums[i-k] % MOD
    s = (s + (left * right) % MOD) % MOD
  nums.append(s)
print(nums[-1])
