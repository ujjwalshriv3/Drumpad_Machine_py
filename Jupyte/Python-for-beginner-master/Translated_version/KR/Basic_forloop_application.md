## ���ڵ� `0, 1, 2, 3, 4` ����ϱ�

```python
for x in range(5):
   print(x)
```

## `3, 4, 5` ����ϱ�

```python
for x in range(3, 6):
    print(x)
```

## `3, 5, 7` ����ϱ�

```python
for x in range(3, 8, 2):
    print(x)
```
    
## ����

- List�� ����� ��� ������ ���� ã�� ���α׷�

- ���ڵ��� List

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
```
- �հ踦 �����ϱ� ���� ����

```python
sum = 0
```

- List�� �ݺ�

```python
for val in numbers:
   sum = sum+val
```
- ���: �հ�� `48`

```python
print("�հ��", sum)
```
