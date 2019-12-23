# Queue

```c++
template <typename T>
class Queue {
public:
	Queue(int c = 2500) {
		_head = _tail = 0;
		_capacity = c;
		_data = new T[_capacity];
	}
	~Queue() { delete []_data; }
	bool empty() { return _head == _tail; }
	int size() { return (_tail - _head + _capacity) % _capacity; }
	T front() { return _data[(_head + 1) % _capacity]; }
	T back() { return _data[_tail]; }
	void push(T item) {
		if ((_tail + 1) % _capacity == _head) {
			_capacity *= 2;
			T* tmp = new T[_capacity];
			int new_head = 0, new_tail = 0, prev_capacity = _capacity / 2;
			while (_tail != _head) {
				_head = (_head + 1) % prev_capacity;
				tmp[++new_tail] = _data[_head];
			}
			_head = new_head, _tail = new_tail;
			delete []_data;
			_data = tmp;
		}
		_tail = (_tail + 1) % _capacity;
		_data[_tail] = item;
	}
	void pop() { _head = (_head + 1) % _capacity; }
private:
	T* _data;
	int _head, _tail, _capacity;
};
```

