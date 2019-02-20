# KMP Algorithm

## Failure Function (실패함수)

```C++
/* KMP Algorithm - Make Failure Function */

// P : Pattern
// F : Failure function
// main : 순차적으로 Pattern을 지나가는 index
// sub : failure function에 저장될 값을 탐색하는 index

int sub = 0;
for (int main = 1; main < Pattern_length; ++main) {
    // sub가 0보다 크면서, 현재 main과 sub가 일치하지 않으면 이전으로 돌아감.
    while (sub > 0 && P[main] != P[sub]) 
        sub = F[sub - 1];
    
    // main과 sub의 글자가 같으면 sub의 값을 올려주고 저장.
    // 이 부분 다음에서부터 탐색을 하면 된다는 의미
    if (P[main] == P[sub])
        F[main] = ++sub;
}
```



## Matching (매칭)

```c++
/* KMP Algorithm - Matching */

// P : Pattern
// T : Text
// F : Failure Function
// main : Text를 처음부터 순차적으로 지나가는 index
// sub : Pattern의 Failure Function에 따라 이동하는 index

int sub = 0;
for (int main = 0; main < Text_length; ++main) {
    
    // sub가 0보다 크면서 현재 Text와 Pattern이 일치하지 않으면 sub를 앞으로 이동
    while (sub > 0 && T[main] != P[sub]) 
        sub = F[sub - 1];
    
    // Text와 Pattern의 글자가 일치할 때,
    if (T[main] == P[sub]) {
        
        // Pattern이 모두 일치했다면
        if (sub == Pattern_length - 1) {
            /* ... 무언가 처리를 한다. */
            sub = F[sub]; // 이전의 다른 것도 있을 수 있으니 이전으로 돌린다.
        }
        else sub++; // 마지막이 아니라면 다음 패턴을 확인해야 하므로 sub를 올린다.
    }
}
```

