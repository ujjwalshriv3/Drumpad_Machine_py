# ���̽㿡�� ���� �б�

## �����͸� �д¹�

```python
file=open("filename","r")
data=file.read()
```

## �� ����� ����ϸ� ���ڵ� �� ������ �а� ���� �����͸� ��Ͽ� ������ �� �ֽ��ϴ�

```python
with open("enter your file_name","r",encoding='UTF8') as title:
        title=title.readlines() 
```

## ������ ���¹�

```python
file=open("filename","w")
file.write("Enter your data that needs to be written in the file")
```

## ������ ���� �� �ٸ� ���

```python
with open("file_name", "w") as f:
   f.write("data")
```
