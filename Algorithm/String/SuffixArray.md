# Suffix Array (접미사 배열; SA)

## Suffix Array 구하기 1 : STL sort 

```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

/**
 *	MAX : 배열 사이즈의 최댓값
 *	T : 1, 2, 4, 8, ... 식으로 커지는 변수
 *	Length : 배열의 길이
 *	SuffixArray : 접미사 배열을 담는 배열
 *	group : 접미사의 그룹을 저장하는 배열
 *	temp_group : 계산 과정에서 임시 저장하는 배열
**/
const int MAX = 500050;
int T, Length, SuffixArray[MAX], group[MAX], temp_group[MAX];
char S[MAX];

// 비교 함수
bool compare(int x, int y) {
    // x와 y의 group이 같으면 T만큼 인덱스를 증가시켰을 때의 group으로 비교.
    if (group[x] == group[y]) return group[x + T] < group[y + T];
    
    // x와 y의 group이 다르면 그 값을 비교.
    return group[x] < group[y];
}

void makeSuffixArray() {
    // SuffixArray의 첫 글자 비교를 위한 전처리
    for (int i = 0; i < Length; ++i) {
        SuffixArray[i] = i;
        group[i] = S[i] - 'a';
    }
    
    while (T <= Length) {
        // 비교 과정에서 -1은 절대적으로 작은 값이므로 barrier의 역할
        g[Length] = -1; 
        
        // 그룹에 의한 정렬
        sort(SuffixArray, SuffixArray + Length, compare);
        
        // 새로운 그룹을 설정
        temp_group[SuffixArray[0]] = 0;
        for (int i = 1; i < Length; ++i) {
            // 다른 그룹일 때, 다음 그룹 번호로 지정
            if (compare(SuffixArray[i - 1], SuffixArray[i]))
                temp_group[SuffixArray[i]] = temp_group[SuffixArray[i - 1]] + 1;

            // 같은 그룹일 때, 같은 그룹 번호로 지정
            else temp_group[SuffixArray[i]] = temp_group[SuffixArray[i - 1]];
        }
        
        // temp_group 배열에 있는 그룹 정보를 group 배열로 이동
        for (int i = 0; i < Length; ++i)
            group[i] = temp_group[i];
        
        // T의 값을 2배만큼 증가
        T <<= 1;
    }
}
```





## Suffix Array 구하기 2 : Counting Sort

```C++
#include <cstdio>
#include <cstring>

const int MAX = 500050;
int Length, count[MAX], group[MAX], temp_group[MAX];
char S[MAX];

void countingSort(const int *temp_group, const int *group, int *SuffixArray, int Length, int range) {
    // counting sort를 하기 전에 먼저 초기화.
    for (int i = 0; i <= range; ++i) 
        count[i] = 0;
    
    // temp_group에 있는 값들을 인덱스로 하여 group에 있는 값을 count
    for (int i = 0; i < Length; ++i)
        count[group[temp_group[i]]]++;
    
    // counting sort를 위하여 누적합 계산
    for (int i = 1; i <= range; ++i)
        count[i] += count[i - 1];
    
    // 누적합을 이용하여 SuffixArray에 정렬
    for (int i = Length; i--; SuffixArray[--count[group[temp_group[i]]]] = temp_group[i]);
}

void makeSuffixArray(const char *S, int *SuffixArray, int Length) {
    int i, j, k;
    
    // 첫 글자로 정렬을 하기 위한 전처리
    for (i = 0; i < Length; ++i) {
        group[i] = A[i] - 'a' + 1;
        temp_group[i] = i;
    }
    
    // 첫 글자를 기준으로 counting sort
    countingSort(temp_group, group, SuffixArray, Length, 26);
    
    // i : 1, 2, 4, 8, ... 과 같이 증가하는 변수
    for (i = k = 1; i < Length && k < Length; i <<= 1) {
        for (k = 0; k < i; ++k)
            temp_group[k] = k - i + Length;
        for (j = 0; j < Length; ++j)
            if (SuffixArray[j] >= i)
                temp_group[k++] = SuffixArray[j] - i;
        
        countingSort(temp_group, group, SuffixArray, Length, k);
        
        temp_group[SuffixArray[0]] = k = 1;
        for (j = 1; j < Length; ++j) {
            if (group[SuffixArray[j]] != group[SuffixArray[j - 1]] ||
               	group[SuffixArray[j] + i] != group[SuffixArray[j - 1] + i])
                ++k;
            temp_group[SuffixArray[j]] = k;
        }
        for (j = 0; j < Length; ++j) group[j] = temp_group[j];
    }
}
```

