# for문을 이용해서 피보나치 수열을 구하고 그 수열이 몇 초가 걸리는지 구하기 

import time
n1 , n2 = 1, 1

N = 0;

while(N<3):
    N = int(input("3 이상의 자연수를 입력하세요 : "))

start = time.time()
for i in range(3,N+1):
    n3 = n2 + n1
    n1 = n2
    n2 = n3 
end = time.time() - start # 시간 끝

print(N, " 번째 피보나치 수열의 수는 : ", n3)
print("알고리즘 동작 시간 : ", end, " sec")
