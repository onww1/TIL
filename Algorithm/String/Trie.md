# Trie (트라이)

```C++
#include <cstdio>
#include <cstring>

struct Trie {
    bool finish;	// 특정 단어의 마지막 글자인지 표시
    Trie *next[26]; // 알파벳 26가지에 대한 child
    
    // Constructor
    Trie() {
        finish = false;
        memset(next, 0, sizeof(next));
    }
    
    // Destructor
    ~Trie() {
        for (int i = 0; i < 26; ++i)
            if (next[i]) delete next[i];
    }
    
    // 삽입 함수
    void insert(const char *key) {
        // 현재 글자가 NULL이면 단어의 끝에 도달한 것이므로 finish!
        if (*key == 0) finish = true;
        else {
            int cur = *key - 'a';
            // 해당 글자에 대한 Trie가 없으면 동적할당
            if (next[cur] == 0) next[cur] = new Trie();
            // 다음 글자에 대하여 재귀탐색
            next[cur]->insert(key + 1);
        }
    }
    
    // 검색 함수
    Trie* find(const char *key) {
        // 현재 글자가 NULL이면 해당 단어로 끝까지 도달한 것이므로 자신을 리턴
        if (*key == 0) return this;
        int cur = *key - 'a';
        // 해당 글자에 대하여 child가 없으면 탐색 실패
        if (next[cur] == 0) return NULL;
        // 다음 글자에 대하여 재귀탐색
        return next[cur]->find(key + 1);
    }
}
```

