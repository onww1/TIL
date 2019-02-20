# 이항계수 (Binomial Coefficient)
#### 이항계수 (nCr) mod p 계산

1. $O(n^2)$
* [파스칼 삼각형](https://ko.wikipedia.org/wiki/파스칼의_삼각형)을 이용하여 구하는 방법.
* 이 방법은 나눗셈을 하지 않으므로 안정적인 방법이다.
* 하지만 비효율적이다.



2. $O(n log p)$
* [페르마의 소정리](https://ko.wikipedia.org/wiki/페르마의_소정리)에 의하여 $a^{(p-1)} \equiv 1~(mod~p)$이며, 이를 응용하면 $a^{(p-2)} \equiv a^{-1}~(mod~p)$임을 알 수 있다. 이때 factorial의 값은 전처리를 해둔다.



3. $O(n + logp)$
* 앞선 방법에서 factorial의 inverse의 값도 $(n-1)!^{-1} \equiv n\times(n!)^{-1}$의 관계를 이용하여 전처리해둔다.



4. $O(n)$
* 정수 `i`에 대한 역원을 동적계획법으로 계산하는 방법
* `inv(1) = 1`
* `inv(i) = -(p / i) * inv(p % i)`



5. $O((n + p)logn)$
* `n`과 `p`가 작다면 소인수분해를 통해서 해결 가능하다.



6. $O(p)$
* **lucas theorem**을 이용하는 방법이다.

> 출처 : http://koosaga.com/63