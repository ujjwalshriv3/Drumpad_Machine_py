# ���̽㿡�� list�� �����ϴ¹�.

list�� = �����ڷ� ����� �� �ֽ��ϴ�. ���� ���:

```python
old_list = [1, 2, 3]
new_list = old_list
```

�� ������� list�� �����ϴ°ſ� ������ ���� ����� new_list�� �����ϴ� ���, old_list���� �����ȴٴ� ���Դϴ�.

# ����

```python
old_list = [1, 2, 3]
new_list = old_list

# list�� ��� �߰�
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )
```

����� ���α׷��� ���� ��, ����� �Ʒ��� ���� ���Դϴ�:

```bash
Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']
```

�׷���, ���� ����� ���� list�� �������� �ʰ� �� list�� ������ �ϴ°� �ʿ��� ��, copy()�޼ҵ带 ����� �� �ֽ��ϴ�. �̰� ���� ������ �Ҹ��ϴ�.

copy()�޼ҵ��� ������ �Ʒ��� �����ϴ�:

```python
new_list = list.copy()
```

# ����

```python
# ���� list
list = ['cat', 0, 6.7]

# list �����ϱ�
new_list = list.copy()

# ���ο� list�� ��� �߰��ϱ�
new_list.append('dog')

# ���ο� list�� �� list ����ϱ�
print('Old List: ', list)
print('New List: ', new_list)
```

����� ���α׷��� ���� ��, ����� �Ʒ��� ���� ���Դϴ�:

```python
Old List: ['cat', 0, 6.7]
New List: ['cat', 0, 6.7, 'dog']
```