/**
 *	Splay Tree
 *	(reference : https://cubelover.tistory.com/10)
 *	
 *	Insert, Delete, Search : amortized O(logN)
 *	
 *	Splay 연산을 이용한 구간에 대한 쿼리가 자유롭고,
 *	AVL Tree나 Red-Black Tree와 같은 다른 BBST보다 구현이 단순한 편.
 *
 *	Splay Tree는 쿼리로 들어온 노드에 대해 
 *	splay 연산을 행해서 amortized O(log N) 시간에 동작하는 자료구조.
 *
 *	splay 연산은 임의의 노드 x를 루트로 만드는 연산.
 *	( Rotate(x) 함수를 이용하여 x를 x의 부모 위치로 올림. )
 *
 *	1. x가 루트이면, 루트를 만드는 데 성공했으므로 종료한다.
 *	2. x의 부모 p가 루트이면, Rotate(x)를 행하고 종료한다. (Zig Step)
 *	3. x의 조부모를 g라고 하면, 다음 두 가지 경우가 있다.
 *	3-1. g -> p의 방향과 p -> x의 방향이 같은 경우, Rotate(p) 이후 Rotate(x)를 행한다. (Zig-Zig Step)
 *	3-2. g -> p의 방향과 p -> x의 방향이 다른 경우, Rotate(x)를 두 번 행한다. (Zig-Zag Step)
 *	4. 1로 돌아가서 루트가 될 때까지 반복한다.
 */

#if 0
/**
 *	가장 기본이 되는 노드 구조체
 *
 *	l : left_child
 *	r : right_child
 *	p : parent
 *	key : data
 */
struct node {
	node *l, *r, *p;
	int key;
} *tree;

/* Rotate */
void Rotate(node *x) {
	node *p = x->p;
	node *b;
	if (x == p->l) {
		p->l = b = x.r;
		x.r = p;
	} else {
		p->r = b = x.l;
		x.l = p;
	}
	x->p = p->p;
	p->p = x;
	if (b) b->p = p;
	(x->p ? p == x->p->l ? x->p->l : x->p->r : tree) = x;
}

/* Splay 연산 */
void Splay(node *x) {
	while (x->p) {
		node *p = x->p;
		node *g = p->p;
		if (g) Rotate((x == p->l) == (p == g->l) ? p : x);
		Rotate(x);
	}
}

/* Insert */
void Insert(int key) {
	node *p = tree, **pp;
	if (!p) {
		node *x = new node;
		tree = x;
		x->l = x->r = x->p = NULL;
		x->key = key;
		return;
	}
	while (1) {
		if (key == p->key) return;
		if (key < p->key) {
			if (!p->l) {
				pp = &p->l;
				break;
			}
			p = p->l;
		} else {
			if (!p->r) {
				pp = &p->R;
				break;
			}
			p = p->r;
		}
		node *x = new node;
		*pp = x;
		x->l = x->r = NULL;
		x->p = p;
		x->key = key;
		Splay(x);
	}
}

/* Find */
bool Find(int key) {
	node *p = tree;
	if (!p) return false;
	while (p) {
		if (p->key == key) break;
		if (p->key > key) {
			if (!p->l) break;
			p = p->l;
		} else {
			if (!p->r) break;
			p = p->r;
		}
	}
	Splay(p);
	return key == p->key;
}

/* Delete */
void Delete(int key) {
	if (!Find(key)) return;
	node *p = tree;
	if (p->l) {
		if (p->r) {
			tree = p->l;
			tree->p = NULL;
			node *x = tree;
			while (x->r) x = x->r;
			x->r = p->r;
			p->r->p = x;
			Splay(x);
			delete p;
			return;
		}
		tree = p->l;
		tree->p = NULL;
		delete p;
		return;
	}
	if (p->r) {
		tree = p->r;
		tree->p = NULL;
		delete p;
		return;
	}	
	delete p;
	tree = NULL;
}
#endif

#if 1
/**
 *	Splay Tree를 이용한 Kth Element
 */
struct node {
	node *l, *r, *p;
	int cnt, key;
} *tree;

void Update(node *x) {
	x->cnt = 1;
	if (x->l) x->cnt += x->l->cnt;
	if (x->r) x->cnt += x->r->cnt;
}

void Rotate(node *x) {
	node *p = x->p;
	node *b;
	if (x == p->l) {
		p->l = b = x->r;
		x->r = p;
	} else {
		p->r = b = x->l;
		x->l = p;
	}
	x->p = p->p;
	p->p = x;
	if (b) b->p = p;
	(x->p ? x->p->l == p ? x->p->l : x->p->r : tree) = x;
	Update(p);
	Update(x);
}

void Splay(node *x) {
	while (x->p) {
		node *p = x->p;
		node *g = p->p;
		if (g) Rotate((x == p->l) == (p == g->l) ? p : x);
		Rotate(x);
	}
}

void Find_Kth(int k) {
	node *x = tree;
	while (1) {
		while (x->l && x->l->cnt > k) x = x->l;
		if (x->l) k -= x->l->cnt;
		if (!k--) break;
		x = x->r;
	}
	Splay(x);
}

void Insert(int key) {
	node *p = tree, **pp;
	if (!p) {
		node *x = new node;
		x->l = x->r = x->p = NULL;
		x->key = key;
		x->cnt = 1;
		return;
	}
	while (1) {
		if (key <= p->key) {
			if (!p->l) {
				pp = &p->l;
				break;
			}
			p = p->l;
		} else {
			if (!p->r) {
				pp = &p->r;
				break;
			}
			p = p->r;
		}
	}
	node *x = new node;
	*pp = x;
	x->l = x->r = NULL;
	x->p = p;
	x->key = key;
	Splay(x);
}

#endif