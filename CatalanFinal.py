MOD = 1000000007
cat_n = 1
n_1 = int(input())+1
for n in range(1,n_1):
  cat_n = (cat_n % MOD) * ((4*n - 2) % MOD)
  #modular multiplicitive inverse of n+1 mod 10**9+7
  cat_n = (cat_n % MOD) * pow(n+1, MOD-2, MOD)  
print(cat_n%MOD)
