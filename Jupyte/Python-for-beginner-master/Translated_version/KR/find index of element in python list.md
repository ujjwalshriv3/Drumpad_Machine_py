# ���̽� list���� index�� ��� ã��.

������ ���ؼ�, `index()` �޼ҵ�� �־��� ��Ҹ� list���� ã�� �� ��ġ�� ��ȯ�Ѵ�.

�׷���, ���� ��Ұ� �ι� �̻� �����ϸ�, `index()` �޼ҵ�� ���� ����/ù��° ��ġ�� ��ȯ�Ѵ�.

**�޸�**: ���̽㿡�� index�� `1` �� �ƴ϶�  `0` ���� �����Ѵ�.

list�� ���� `index()` �޼ҵ��� ������ ������ ����:

```python
list.index(element)
```

# `index()` �Ű�����

index �޼ҵ�� �ϳ��� ���ڸ��� �޴´�:
* **element** - �˻��� ���.

# `index()` �� ��ȯ��

 `index()` �޼ҵ�� list���� ����� index�� ��ȯ�Ѵ�.

ã�� �� ������, ��Ұ� list�ȿ� ������ ��Ÿ���� ValueError�� ����Ų��.

# ����

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# ��� 'e' �� �˻���
index = vowels.index('e')

#  'e' �� index�� ��µ�
print('e�� index:', index)

#  'i' �� ��Ұ� �˻���
index = vowels.index('i')

# ����� ù���� index�� ��µ�
print('i�� index:', index)
```

����� ���α׷��� �����ٸ�, ����� �Ƹ� �Ʒ��� �������̴�:

```bash
The index of e: 1
The index of i: 2
```