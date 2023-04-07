# QuickSort �˰���
## ���� :

���̽㿡�� [17,41,5,22,54,6,29,3,13] �������� 9���� ���� ��� �����ϱ�

1. pivot�� ã���ϴ�. pivot�� ����2�� ���ϴµ� ����� �׸��̹Ƿ� �� ���ڸ� ���ʷ� pivot�� ���մϴ�. ���� ���ڰ��� pivot�� ���ʿ� �ְ� ū ���ڰ��� pivot�� �����ʿ� �ֽ��ϴ�. pivot�� ã�� ���� 3�� �߾Ӱ��� ����մϴ�. ù��°�� (17), �߰���(54) �� ��������(13)�� �����մϴ�. ���� 17�� �� �� ���� �߾Ӱ��Դϴ�.
2. pivot ���� ù ��° ��ġ (0 ��° ��ġ)�� �̵�
3. �񱳸� �����Ͻʽÿ�. ��� ��(41)�� �����ϴ�. �׵θ����� ������츶�� ���� ���ڰ��� �׵θ������� �ٲߴϴ�. ���� pivot���� ���� ��� ���ڴ� �׵θ� ���ʿ� �ְ� pivot���� ū ���ڴ� �׵θ� �����ʿ� �ֽ��ϴ�.
4. ��谪(13)�� �ִ� ��ġ�� 17�� swap�մϴ�. ���� ���� pivot ��ȣ�� �߰��� �ֽ��ϴ�.
5. ���� ���ó�� pivot���� ���� ���ڿ� ���ؼ��� quick sort�� �����Ͻʽÿ�.
6. ���� ���ó�� pivot���� ū ���ڿ� ���ؼ��� quick sort�� �����Ͻʽÿ�.

## ��� :
. QuickSort�� ������Դϴ� (�ڽ��� ȣ���ϴ� �޼ҵ�)
. ����-���� �˰���
. ��뷮 �����ͼ�Ʈ�� �ſ� ȿ����
. ��� case�� O(n log n)�Դϴ�.
. ������ �ַ� �ǹ� ���ÿ� ���� �ٸ��ϴ�.

## �ڵ� :

### ����� input(D)�� �����Ѵ��� ��������� quick-sort2�� ȣ���մϴ�.

```python
def quick_sort(D) :
	quick_sort2(D, 0, len(D) - 1)
```

```python
### ����� �Լ�
def quick_sort2 (D, low, high):
	if low < high:    #more than one item to be sorted
		p = partition(D, low, high)     # return the pivot around which where we partitioned the list
		quick_sort2(D, low, p - 1)      # sort left partition
		quick_sort2(D, p + 1, high)     # sort right partition
```

```python
### pivot�� ���
def get_pivot(D, low, high):
	mid = (high + low) // 2
	pivot = high
	if D[low] < D[mid]:
		if D[mid] < D[high]:
			pivot = mid
	elif D[low] < D[high]:
		pivot = low
	return pivot
```

```python
### partition �Լ�
def partition(D, low, high):
	pivotIndex = get_pivot(D, low, high)
	pivotValue = D[pivotIndex]
	D[pivotIndex], D[low] = D[low], D[pivotIndex]   # swap the pivot value into the leftmost position of our list
	border = low                                    # set border to the lowest item 

	for i in range(low, high + 1):
		if D[i]  <  pivotValue:
		border += 1
		D[i], D[border] = D[border], D[i]
	D[low], D[border] = D[border], D[low]

	return (border)     # return the index for the pivot
```
