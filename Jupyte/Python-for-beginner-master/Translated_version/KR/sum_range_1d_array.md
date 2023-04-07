# ���̽㿡�� �־��� 1���� �迭�� �־��� ���������� �հ踦 ã���ʽÿ�.

```python
def find_sum_in_range(min_range, max_range, input_data):
    total_sum = 0
    for item in input_data:
        if min_range <= item <= max_range:
            total_sum += item
    return total_sum
```

����� ������ �������Դϴ�:

#�Է�

```python
min_range = 0
max_range = 1000
input_data = [10, 20, 5, 99, -19, 8372, 7468]
```

# ���

```python
find_sum_in_range(min_range, max_range, input_data)
```

```sh
134
```

## ���⵵

- �ð����⵵ - `O(n)`
- �������⵵ - `O(1)`
