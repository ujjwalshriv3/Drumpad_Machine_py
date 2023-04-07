## ���̽� map() �Լ�

##### map() �Լ��� �־��� iterable (���, Ʃ�� ��)�� �� �׸� �־��� �Լ��� ������ �� ��� list�� ��ȯ�մϴ�.


#### ����

```python
map(fun, iter)
```

#### �Ű������� :

```
fun : �־��� iterable�� �� ��Ҹ� map�� �����ϴ� �Լ��Դϴ�.
iter : ���ε� iterable�Դϴ�.
```


## ����

Ʃ�ÿ��� �� �ܾ��� ���̸� ����Ͻʽÿ�:
 
```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(list(x))
```

#### ���

[5, 6, 6]