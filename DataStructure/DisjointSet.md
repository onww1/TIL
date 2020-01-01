# Disjoint Set

## Union



## Find





## Friend - Enemy Disjoint Set

다음과 같은 두가지의 연산을 요구하는 문제가 존재한다.

1. $S_i$와 $S_j$는 서로 같은 팀이다.
2. $S_i$와 $S_j$는 서로 다른 팀이다.

팀은 총 2개가 존재한다.

즉, A와 B가 같은 팀이고, B와 C가 같은 팀이라면 A와 C는 같은 팀이어야 한다.
또한 A와 B가 다른 팀이고 B와 C가 다른 팀이라면 A와 C는 같은 팀이어야 하며,
A와 B가 같은 팀이고, B와 C가 다른 팀이라면 A와 C는 다른 팀이어야 한다.

이런 관계가 주어졌을 때, 모순된 연산이 존재하는 지 판별해야 하는 문제이다.

예를 들어,
1 A B
1 B C
2 A C
라는 연산이 존재한다면, ABC는 서로 같은 팀이지만, AC는 다른팀이어야 하므로, 모순이 된다.

서로 같은 팀으로 이어주는 연산은 disjoint-set을 이용해서 쉽게 해결할 수 있다.
서로 다른 팀으로 만드는 연산은 어떻게 해야할까?

A와 반드시 달라야 하는 가상의 사람을 원수라고 하자.
2 A C 라는 연산이 주어졌을 때, A를 C의 원수와 같은 팀으로 만들고
C를 A의 원수와 같은 팀으로 만들어주자.

마찬가지로, 1 A C라는 연산이 주어진다면, A를 C와 같은 팀으로 만들고,
A의 원수와 C의 원수를 같은 팀으로 만들어주자.

이때 모순된 결과가 주어졌는지는 어떻게 판별할까?
$S_1$, $S_2$, ..., $S_n$ 의 모든 원소를 확인해서 Si와 Si의 원수가 같은 팀이라면, 모순된 결과라고 생각할 수 있다.

이는 다음과 같은 간단한 코드로 처리할 수 있다.

```c++
int p[2 * n]; // i의 가상의 원수는 i + n

int find(int a) {
	if (p[a] == a) return a;
	return p[a] = find(p[a]);
}

void merge(int a, int b) {
	a = find(a); b = find(b);
	if (a == b) return;
	p[b] = a;
}

void make_team(int a, int b) {
	merge(a, b);
	merge(a + n, b + n);
}

void make_enemy(int a, int b) {
	merge(a, b + n);
	merge(a + n, b);
}

bool is_true(){
	for(int i = 0; i < n; i++)
		if(find(i) == find(i + n)) return 0;
	return 1;
}
```