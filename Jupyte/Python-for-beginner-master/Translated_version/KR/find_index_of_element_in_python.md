# ���̽㿡�� ��� ����� index�� ã�°�?

 `index()` �޼ҵ带 ����Ͽ� ����� index�� ã�� �� �ֽ��ϴ�. �� �޼ҵ�� list���� ����� ù ��° �߻��� ��ȯ�մϴ�. �������� ������ ������ ��ȯ�մϴ�.

## ���� 1

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('bar')
```

- ���:

```sh
1
```

## ���� 2

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('foo')
```

- ���:

```sh
0
```

## ���� 3

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('thing')
```

- ���:

```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'thing' is not in list
```
