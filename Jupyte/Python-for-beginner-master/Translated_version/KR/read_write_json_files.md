# JSON ���� �б� �� ����

���� JSON ������ �д� ����� �˷��ֽʽÿ�
�̸� ���ؼ��� "json"���̺귯���� ���Խ��Ѿ��մϴ�.
```python
import json
```

���� ���α׷����� json����(�� ���������� test.json)�� "open"�ؾ��մϴ�.
������ .py ���ϰ� ������ ������ �ִٰ� �����ϸ� ������ �����ϴ�:
```python
json_file = open("test.json", 'r')
```
open�Լ��� �ι�° �Ű� �������ִ� char 'r'�� test.json ������ �а�ʹٴ� ���� �ǹ��մϴ�.

���� test.json�� �������� ���ڿ��� ����ϴ�:
```python
json_text = json_file.read
```

�������� ���̽㿡�� dict�� ���� json �ؽ�Ʈ�� ������ �����ؾ��մϴ�:
```python
json_dic = json.loads(json_text)
```
�̰��� �� ���� json ������ �������� ������ ����� ���Դϴ�.

���� �̰��� json ���� �� ��� :
```json
{
	"students": [
		{
			"name": "John Brown",
			"age": "18"
		},
		{
			"name": "Ana Miranda",
			"age": "19" 
		}
	],
	"teachers": [
		{
			"name": "Peter Black",
			"age": "30"
		},
		{
			"name": "Mandy White",
			"age": "28"
		}
	]
}
```
���� ��� Ana�� ���̸� �˰� �ͽ��ٸ�, ������ �������Դϴ�:
```python
print(json_dic["students"][1]["age"])
#output: 19
```
json���ϳ����� �ΰ��� Ű( "�л�"�� "����")�� ���� �� dictionary�̸� �� Ű�� ��� dictionary���� �ִ� list���Դϴ�.

���� ���̽����� �ڽ��� json������ �ۼ��Ϸ����մϴ�.
json�� dictionary�̶�� ���� �˾ҽ��ϴ�. �׷��Ƿ� Ű�� �������� �����Ǿ� �ֽ��ϴ�.
json�� ���� ��� ���ô�. test.json�� ������ ���α׷����� dictionary���� �׸� "���ۼ�"�ؾ��մϴ�.
������ �������Դϴ�:
```python
school = {}

school["students"] = [{"name":"John Brown", "age":18}]
school["students"].append({"name":"Ana Miranda", "age":19})

teachers = [{"name":"Peter Black", "age":30}, {"name":"Mandy White", "age":28}]

school["teachers"] = teachers	
```
append�� list�� �� ���� ������ �߰��ϴ� �޼ҵ��Դϴ�. �� ���, School ["students"]�� append �޼ҵ尡 ���Ǳ� ���� �ϳ��� dictionary���ִ� list���� �� �� �ֽ��ϴ�.

���� ���� ���� .json ������ �ۼ��ϰ� �ۼ��ϴ� ���Դϴ�.
�д� �Ͱ� ���������� json ���̺귯���� �ʿ��մϴ�. ���� ������ ������� ���� �ͼ� ������ �����մϴ� :
```python
json_file = open("our_file.json", 'w')
json.dump(school, json_file)
```
�׸��� �������ϴ�. �б� dictionary�� ���� ���� �Լ����� �ۼ��� our_file.json ���Ͽ� �ֽ��ϴ�.
���� 'w'�� �츮�� �������Ͽ� �� ������ �ǹ��մϴ�.