# Heavy-Light Decomposition

## Code

```c++
struct HLD {
    const int SZ = 1 << 17;
    vector <int> edges[SZ];
    int root, node_num, tree[2 * SZ], num[SZ], idx[SZ]; 
    int hld[SZ], w[SZ], depth[SZ], parent[SZ];
    SegmentTree seg;
    
    void preprocess(int node) {
        w[node] = 1;
        for (int next : edges[node]) {
            if (!w[next]) {
                parent[next] = node;
                depth[next] = depth[node] + 1;
                preprocess(next);
                w[node] += w[next];
            }
        }
    }
    
    void numbering(int node) {
        int heavy_node = -1;
        num[node] = node_num++;
        idx[num[node]] = node;
        for (int next : edges[node]) {
            if (parent[next] == node && (heavy_node == -1 || w[heavy_node] < w[next]))
                heavy_node = next;
        }
        if (heavy_node != -1) {
            hld[heavy_node] = hld[node];
            numbering(heavy_node);
        }
        for (int next : edges[node]) {
            if (parent[next] == node && next != heavy_node) {
                hld[next] = next;
                numbering(next);
            }
        }
    }
    
    void init_HLD(int n, int r) {
        root = hld[r] = parent[r] = r;
        depth[r] = node_num = 0;
        memset(w, 0, sizeof(w));
        preprocess(r);
        numbering(r);
    }
    
    int query(int a, int b) {
        int ret = 0;
        while (hld[a] != hld[b]) {
            if (depth[hld[a]] > depth[hld[b]]) {
                ret += segQuery(num[hld[a]], num[a]);
                a = parent[hld[a]];
            }
            else {
                ret += segQuery(num[hld[b]], num[b]);
                b = parent[hld[b]];
            }
        }
        if (depth[a] > depth[b]) swap(a, b);
        return ret += segQuery(num[a], num[b]);
    }
}
```

