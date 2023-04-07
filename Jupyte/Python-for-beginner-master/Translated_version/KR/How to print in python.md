## ���̽� print()

```python
print("Python")
```

## print()�� ���� ��ü�� ������ �����ϴ�:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```  
## print()�Ű�����
##objects - �μ� ���. *�� �̻��� ��ü������ �� ������ ��Ÿ���ϴ�.
##sep - ��ü�� sep�� ���е˴ϴ�. �⺻��: ' '
##end - end�� �������� �μ�˴ϴ�
##file - write (string) �޼ҵ尡�ִ� ��ü�����մϴ�. �����ϸ� sys.stdout�� ���Ǿ� ȭ�鿡 ��ü�� �μ��մϴ�.
##flush - ���̸� ��Ʈ���� ������ flushed�˴ϴ�. �⺻�� : False
```

## ���̽㿡�� ������ �ִ� print()
���� ���� ����� �ֽ��ϴ�. �׵� �� �ϳ��� f-string�� ����ϰ� �ֽ��ϴ�.
```python
last_name = "ȫ"
first_name = "�浿"
print(f"�ȳ�. �� �̸��� {first_name} {last_name}�̾�.")
```
