# Segment Ʈ�� (�־��� ������ ��)

## ����

Segment Ʈ���� �⺻������ ���� �Ǵ� Segment�� �����ϴ�  ���Ǵ� ����Ʈ���Դϴ�. Segment Ʈ���� �� ���� ������ ��Ÿ���ϴ�.

## ����

Segment Ʈ���� ����Ʈ���̱� ������ ������ �����迭�� ����Ͽ� Segment Ʈ���� ��Ÿ�� �� �ֽ��ϴ�.
Segment Ʈ���� ��͸� ����Ͽ� ������ �� �ֽ��ϴ� (�ؿ��� ���� ����).
������ Segment Ʈ���� �����Դϴ�. �� ���α׷��� �־��� �迭�� ���� Segment Ʈ�� ������ �����մϴ�. ���� ���� �۾��� �����մϴ�.

## �ڵ�
```python
	tree = [-1] * 100
    arr = [1, 3, 5, 7, 9, 11]

    def buildSegmentTree(node, start, end):
        if start == end:
            tree[node] = arr[start]
        
        else:
            mid = (start + end) // 2
            buildSegmentTree(2 * node, start, mid)
            buildSegmentTree((2 * node) + 1, mid+1, end)
            tree[node] = tree[2*node] + tree[(2*node) + 1]

    def printTree(node):
        if tree[node] == -1:
            return
        
        print(tree[node],end="")
        print(', ', end="")
        printTree(node * 2)
        printTree((node * 2) + 1)

    def getSum(node, start, end, qs, qe):
        if (qe < start or end < qs):
            return 0
        if (qs <= start and qe >= end):
            return tree[node]
        mid = (start + end) // 2
        partialSum1 = getSum(2 * node, start, mid, qs, qe)
        partialSum2 = getSum((2 * node) + 1, mid + 1, end, qs, qe)
        return (partialSum1 + partialSum2)

    buildSegmentTree(1, 0, 5)

    # ��� Segment Ʈ�� ���
    printTree(1)
    print()
    # 36, 9, 4, 1, 3, 5, 27, 16, 7, 9, 11, ���

    # index 1���� 3���� �迭������ ���� �μ�  
    print("Sum of values in given range = ", getSum(1, 0, 5, 1, 3))
    # 15 ���

    # index 2���� 5���� �迭������ ���� �μ� 
    print("Sum of values in given range = ", getSum(1, 0, 5, 2, 5))
    # 32 ���
```

__Time Complexity: O(N)__