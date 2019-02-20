# 2-Dimension Fenwick Tree 

# (2차원 펜윅 트리; BIT)



## Fenwick Tree란?

- Segment Tree의 **변형**

- Segment Tree의 **Memory를 더 절약**하기 위해 만든 방법



## Fenwick Tree의 핵심

- **구간 합** 대신 **부분 합**만을 빠르게 계산할 수 있는 자료구조를 만들어도 구간합을 계산할 수 있다. 
  - **부분 합** : `0 ~ k ` 의 합 
  - **구간 합** : ` a ~ b` 의 합



## Fenwick Tree 동작 방식

![ModelOfFenwickTree](/Users/sewon/Study/TIL/images/Algorithm/ModelOfFenwickTree.png)

- **Fenwick Tree Sum**

  ex) `5 ~ 15` 구간의 합 구하기

  - `1 ~ 8` + `9 ~ 12` + `13 ~ 14` + `15` - `1 ~ 4` = `5 ~ 15`
  - 비트 방식 : `1000` + `1100` + `1110` + `1111` - `0100`
    ​                 `1111` > `1110` > `1100` > `1000` (가장 오른쪽 `1`이  `0`으로 바뀜)



- **Fenwick Tree Update**

  ex) `7`을 업데이트

  - `7`, `1 ~ 8`, `1 ~ 16` 업데이트
  - 비트 방식 : `111`, `1000`, `10000` (가장 오른쪽 `1`에 `1`을 더해준다.)



## Source Code

```C++
class FenwickTree2D {
public:
    int size;
    vector< vector<long long> > data;
    
    FenwickTree2D(int _N) {
        size = _N;
        data = vector< vector<long long> >(size + 1, vector<long long>(size + 1));
    }
    
    void update(int x, int y, int val) {
        long long diff = val - sum(x, y, x, y);
        int yy;
        while (x <= size) {
            yy = y;
            while (yy <= size) {
                data[x][yy] += diff;
                yy += (yy & -yy);
            }
            x += (x & -x);
        }
    }
    
    long long sum(int x, int y) {
        long long ret = 0;
        int yy;
        while (x > 0) {
            yy = y;
            while (yy > 0) {
                ret += data[x][yy];
                yy -= (yy & -yy);
            }
            x -= (x & -x);
        }
        return ret;
    }
    
    inline long long sum(int x1, int y1, int x2, int y2) {
        return sum(x2, y2) - sum(x1 - 1, y2) - sum(x2, y1 - 1) + sum(x1 - 1, y1 - 1);
    }
};
```





> #### 출처 
>
> - https://www.crocus.co.kr/666?category=150836
>
> - https://github.com/greeksharifa/ps_code/blob/master/library/fenwick_tree_2D_BIT.h