# Longest Common Prefix (최장 공통 접두사; LCP)

## LCP 구하기

```C++
#include <cstdio>
#include <cstring>

int RANK[MAX];
void longestCommonPrefix(const int *SuffixArray, const char *S, int *LCP, int Length) {
    // Suffix Array 순서를 RANK 배열에 저장
    for (int i = 0; i < Length; ++i) RANK[SuffixArray[i]] = i;
    
    // LCP 구하기
    for (int i = 0, len = 0; i < Length; ++i) {
        int k = RANK[i];
        if (k > 0) {
            int j = SuffixArray[k - 1];
            while (S[j + len] == S[i + len]) len++;
            LCP[k] = len;
            if (len) len--;
        }
    }
}
```

