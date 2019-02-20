# 중국인의 나머지 정리 
# (Chinese Remainder Theorem; CRT)

* 중국인의 나머지 정리는 **연립 합동식의 유일한 해를 찾는 정리**이다.

### 개념
  중국인의 나머지 정리에 대한 개념은 [중국인의 나머지 정리 - 이해하기 쉬운 설명 (Joonas' Note)](http://joonas.tistory.com/23?category=722678)에 잘 정리되어 있다.


### Source Code
```c++
  int crt(int a, int b, int a_mod, int b_mod, int tot_mod) {
    int sum = 0LL, t1 = tot_mod / a_mod, t2 = tot_mod / b_mod;
    sum = (sum + ((long long)t1 * uclid(a_mod, t1 % a_mod) % tot_mod) * a % tot_mod) % tot_mod;
    sum = (sum + ((long long)t2 * uclid(b_mod, t2 % b_mod) % tot_mod) * b % tot_mod) % tot_mod;
    return sum;
  }
```

##### uclid 함수는 [확장 유클리드 호제법](http://joonas.tistory.com/25?category=722678)를 구현한 함수이다.



> 개념 출처 : http://joonas.tistory.com/23?category=722678
> 소스 출처 : https://blog.naver.com/rdd573/221270284083

