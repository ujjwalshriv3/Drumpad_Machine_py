# ���̽㿡���� ��������

## ����

���������� �迭�� �ּ� n�� �ݺ��ϰ�(n�� ������ �迭����� ��) �����׸��� �� ���� ���Ͽ� ������ �߸��Ȱ�� ��ü�Ѵ�.

__Worst Case ���⵵: n^2^__

## �ڵ�

```python
# ������ List
L = [5, 3, 2, 1, 6]

def bubble_sort(List):
	COMPLETED = False
	while not COMPLETED:
		COMPLETED = True
		for i in range(len(L) - 1):
			if List[i] > List[i+1]:
				COMPLETED = False
				List[i], List[i+1] = List[i+1], List[i]
	return List

print(bubble_sort(L))
```