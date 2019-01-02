# 뤼카의 정리 (Lucas' theorem)

* [뤼카의 정리 (Lucas' theorem)](https://ko.wikipedia.org/wiki/뤼카의_정리)는 p가 작고, n이 큰 상황에서의 조합을 구하는데에 유용한 정리이다.


### Source Code
```c++
  int lucas(int n, int k, int fac[], int inv[], int p) {
    int res = 1, t1, t2;

    while (n || k) {
      t1 = n % p, t2 = k % p;
      if (t1 < t2) return 0;
      res = res * ((fac[t1] * inv[t2] % p) * inv[t1 - t2] % p) % p;
      n /= p, k /= p;
    }
    
    return res;
  }
```

> 소스 출처 : https://blog.naver.com/rdd573/221270284083