## ����� ����Ž���� ���� ���̽� ���α׷�. 
  
### �ִ°�쿣 �迭���� `x` ������, �� �ܿ��� `-1` ��ȯ 

```python
def binarySearch (arr, l, r, x): 
    # base case üũ
    if r >= l: 
        mid = l + (r - l)/2

        # ��Ұ� �߰��� �ִ°��
        if arr[mid] == x: 
            return mid 

        # ��Ұ� �߰����� ������ ���� �����迭���� ������ �� ����  
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

        # �� �ܰ�쿡 ��Ҵ� ������ �����迭���� ������ �� ����
        else: 
            return binarySearch(arr, mid+1, r, x) 

    else: 
        # ��Ұ� �迭�ȿ� �������� ����
        return -1
```