# python-Fibonacci
## 피보나치 수열
###### for문을 이용하여 피보나치 수열을 구하고 거기서 몇 초 정도 걸리는지 궁금해서 구해보았다.(함수 사용 X) , 두번쨰는 함수도 사용하여 보았다.
```python
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
```
###### 이 코드의 결과값은 아래에 이미지와 같다.
![결과값](https://user-images.githubusercontent.com/106458316/182027327-9276bcaa-06c7-4cb5-9f93-1dc0ceaa9438.png)

### 2. 함수 사용해서 작성해보기
```python
