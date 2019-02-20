# 확장 유클리드 알고리즘
# (Extended Euclidian Algorithm)

* [확장 유클리드 알고리즘(Extended Euclidian Algorithm)](https://ko.wikipedia.org/wiki/유클리드_호제법#.ED.98.B8.EC.A0.9C.EB.B2.95.EC.9D.98_.ED.99.95.EC.9E.A5)은 유클리드 호제법을 확장한 것이다.

### 개념
  확장 유클리드 알고리즘에 대한 개념은 [확장 유클리드 알고리즘으로 나머지 연산의 곱셈 역원 구하기 (Joonas' Note)](http://joonas.tistory.com/25?category=722678)에 잘 정리되어 있다.


### Source Code
```c++
  int uclid(int r1, int r2) {
    int t, r, s, q, p = r1;
    int s1 = 1, s2 = 0;
    int t1 = 0, t2 = 1;

    while (r2) {
      q = r1 / r2;
      r = r1 - q * r2;
      r1 = r2, r2 = r;

      s = s1 - q * s2;
      s1 = s2, s2 = s;

      t = t1 - q * t2;
      t1 = t2, t2 = t;
    }

    if (t1 < 0) t1 += p;
    return t1;
  }
```

> 개념 출처 : http://joonas.tistory.com/25?category=722678
> 소스 출처 : https://blog.naver.com/rdd573/221270284083