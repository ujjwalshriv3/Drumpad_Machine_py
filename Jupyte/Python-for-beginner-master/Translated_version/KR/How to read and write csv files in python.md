# ���̽㿡�� CSV ������ �а� ���� ���

������ �������⿡ �Ϲ������� ���Ǵ�, CSV ������, ���̽� ǥ�� ���̺귯���� ����Ͽ� ���� �аų� �ۼ��� �� �ֽ��ϴ�.

# ����: CSV ���Ͽ��� �� �б�
���� ���α׷��� �����ٿ��� ��ǥ�� ���е� ���ڿ��� �����ϴ� csv ������ ������ �н��ϴ�.

```python
import csv
with open('eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))
```

���:
```bash
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

# ����: 2���� list���� CSV ���� �ۼ�
���� ���α׷��� 2���� list�� ���ڿ��� csv ������ ����ϴ�.

```python
import csv
output_list = [
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Baked Beans'],
    ['Spam', 'Lovely Spam', 'Wonderful Spam']
]
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in output_list:
        spamwriter.writerow(row)
```

���α׷��� �����ϸ� `output_list` �� ���� �����ϴ� csv ������ �����˴ϴ�. �� ���� ����� �� �ٿ� �ش��մϴ�.