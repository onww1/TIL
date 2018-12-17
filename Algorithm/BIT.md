# Fenwick Tree 

# (펜윅 트리; Binary Indexed Tree, BIT)



## Fenwick Tree란?

* Segment Tree의 **변형**

- Segment Tree의 **Memory를 더 절약**하기 위해 만든 방법



## Fenwick Tree의 핵심

* **구간 합** 대신 **부분 합**만을 빠르게 계산할 수 있는 자료구조를 만들어도 구간합을 계산할 수 있다. 
  * **부분 합** : `0 ~ k ` 의 합 
  * **구간 합** : ` a ~ b` 의 합



## Fenwick Tree 동작 방식

![ModelOfFenwickTree](../images/Algorithm/ModelOfFenwickTree.png)

* **Fenwick Tree Sum**

  ex) `5 ~ 15` 구간의 합 구하기

  * `1 ~ 8` + `9 ~ 12` + `13 ~ 14` + `15` - `1 ~ 4` = `5 ~ 15`
  * 비트 방식 : `1000` + `1100` + `1110` + `1111` - `0100`
    ​                 `1111` > `1110` > `1100` > `1000` (가장 오른쪽 `1`이  `0`으로 바뀜)



* **Fenwick Tree Update**

  ex) `7`을 업데이트

  * `7`, `1 ~ 8`, `1 ~ 16` 업데이트
  * 비트 방식 : `111`, `1000`, `10000` (가장 오른쪽 `1`에 `1`을 더해준다.)



## Fenwick Tree 만드는 방법

1. **초기화 과정 (Initialize)** : 가장 기초 상태의 트리를 만드는 것

   ```C++
   for (int i = 1; i <= n; ++i) {
       update(tree, i, arr[i]);
   }
   ```

   * **Update**를 이용하여 **`arr`** 배열에 있는 값들을 각 **`node`**에 추가

2. **갱신 과정 (Update)** : 값을 바꿀 때 트리를 수정하는 것

   ```C++
   void update(vector<ll> &tree, int i, ll diff) {
       while (i < tree.size()) {
           tree[i] += diff;
           i += (i & -i);
       }
   }
   ```

   * **`i`** 번째 노드의 값을 바꾸고, **Fenwick Tree**의 **Update** 방식에 따라 최하위 비트 `1`에 `1`을 더해주는 과정

3. **합 과정 (Sum)**  : 주어진 부분의 합을 구하는 과정

   ```C++
   ll sum(vector<ll> &tree, int i) {
       ll answer = 0;
       while (i > 0) {
           answer += tree[i];
           i -= (i & -i);	// 최하위 비트 지우기
       }
       return answer;
   }
   ```

   * **`node 1`**부터 **`node i`**까지의 합을 구하는 과정에서 **`i`**번째 노드의 값에서부터 시작해서 최하위 비트를 지워가며 해당되는 **`node`**의 값을 더하는 과정



## Source Code

```C++
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

void update(vector<ll> &tree, int i, ll diff) {
    while (i < tree.size()) {
        tree[i] += diff;
        i += (i & -i);
    }
}

ll sum(vector<ll> &tree, int i) {
    ll answer = 0;
    while (i > 0) {
        answer += tree[i];
        i -= (i & -i);	// 최하위 비트 지우기
    }
    return answer;
}

int main(int argc, char const *argv[]) {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    
    int n;
    cin >> n;
    
    vector<ll> arr(n+1);
    vector<ll> tree(n+1, 0);
  
    // initialize
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
        update(tree, i, arr[i]);
    }
    
    return 0;
}
```



## Fenwick Tree에 대한 추가 설명

* https://www.acmicpc.net/blog/view/21 (백준 온라인 저지)





> 출처 : https://www.crocus.co.kr/666?category=150836