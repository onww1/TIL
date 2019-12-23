code



```c++
const int S = 2002, E = 2003;
struct dinic {
	struct edge {
		int v, op, c;
	};
	int lv[E + 1], lst[E + 1];
	queue<int> q;
	vector<edge> edg[E + 1];
	void addEdge(int a, int b, int f) {
		edg[a].push_back({ b,(int)edg[b].size(),f });
		edg[b].push_back({ a,(int)edg[a].size() - 1,0 });
	}
	bool bfs() {
		memset(lv, -1, sizeof(lv));
		q.push(S);
		lv[S] = 0;
		while (!q.empty()) {
			int cur = q.front();
			q.pop();
			for (edge &i : edg[cur]) {
				if (lv[i.v] == -1 && i.c > 0) {
					lv[i.v] = lv[cur] + 1;
					q.push(i.v);
				}
			}
		}
		return lv[E] != -1;
	}
	int dfs(int cur, int flow) {
		if (cur == E) return flow;
		int sz = edg[cur].size();
		for (int &k = lst[cur]; k < sz; k++) {
			edge &i = edg[cur][k];
			if (lv[i.v] == lv[cur] + 1 && i.c > 0) {
				int df = dfs(i.v, min(flow, i.c));
				if (df) {
					i.c -= df;
					edg[i.v][i.op].c += df;
					return df;
				}
			}
		}
		return 0;
	}
	int getAns() {
		int ans = 0;
		while (bfs()) {
			memset(lst, 0, sizeof(lst));
			while (true) {
				int ret = dfs(S, INF);
				if (!ret) break;
				ans += ret;
			}
		}
		return ans;
	}
} mf;
```

