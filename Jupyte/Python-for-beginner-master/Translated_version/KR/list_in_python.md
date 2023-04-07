## ���̽� Lists

List�� �ֹ� �� ���� ������ �����Դϴ�. �ߺ� ����� ����մϴ�.

���̽㿡�� list�� ���ȣ�� �ۼ��˴ϴ�.

```python
L = ["git", "github", "version_control"]
print(L)
L = [1, "github", 3.4]
print(L)
```
#### �����׸�

index��ȣ�� ����Ͽ� �׸� ������ �� �ֽ��ϴ�.

```python
L = ["git", "github", "version_control"]
print(L[1])
```
#### �׸� �ٲٱ�

index��ȣ�� �����Ͽ� ���� ������ �� �ֽ��ϴ�.

```python
L = ["git", "github", "version_control"]
L[1] = 123
print(L)
```
#### list Ž��

```python
L = ["git", "github", "version_control"]
for item in L:
  print (item)
```

#### �׸��� �����ϴ��� Ȯ��

```python
L = ["git", "github", "version_control"]
if "git" in L:
  print('Yes it exists!')
```

#### List ũ��

```python
L = ["git", "github", "version_control"]
length = len(L)
print(length)
```

#### list�� �׸� �߰��ϱ�

```python
L = ["git", "github", "version_control"]
L.append("hey")
print(L)
```

```python
L = ["git", "github", "version_control"]
L.insert(1, "hey");
print(L)
```

#### list���� �׸� �����ϱ�

remove (), �̰��� ������ �׸��� �����մϴ�

```python
L = ["git", "github", "version_control"]
L.remove("git")
print(L)
```

pop (), �̰��� ������ index �����մϴ� (�Ǵ� index�� �������� ���� ��쿣 ������ �׸�).

```python
L = ["git", "github", "version_control"]
L.pop()
print(L)
```

del, �̰��� ������ index�� �����մϴ�

```python
L = ["git", "github", "version_control"]
del L[1]
print(L)
```

del, ���� �̰��� list��ü�� ������ ���� �ֽ��ϴ�

```python
L = ["git", "github", "version_control"]
del L
print(L)     #this will cause an error because "L" no longer exists.
```

clear(), �̰��� list�� ���� �޼ҵ��Դϴ�. 

```python
L = ["git", "github", "version_control"]
L.clear()
print(L)
```

#### List() contructor

L = list(("git", "github", "digital")) # ���� ���ȣ�� ����
print(L)

| Command | Description |
| --- | --- |
| append() | Adds an element at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| reverse() | Reverse the order of list |
| sort() | Sort the list |

## ���� 1

```python
a = [5,10,15,20,25,30,35,40]

print("a[2] = ", a[2])

print("a[0:3] = ", a[0:3])

print("a[5:] = ", a[5:])
```

## ���� 2

```python
t = (5,'program', 1+3j)

print("t[1] = ", t[1])


print("t[0:3] = ", t[0:3])
```

## ���� 3

```python
a = {5,2,3,1,4}

# ������ ���� ���
print("a = ", a)

# a�� ������Ÿ��
print(type(a))
```
