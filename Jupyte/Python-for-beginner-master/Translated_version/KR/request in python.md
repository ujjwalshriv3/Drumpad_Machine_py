### ���̺귯�� �ʿ�

�����ϰ� ����ϱ� ���� Requests ���̺귯���� ����� ���Դϴ�. �Ʒ��� ���� ��ġ�ϼ���.

```sh
pip install requests
```

## ������ ����

```python
import requests

r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=Bengaluru')
print (r.text)
```
��û-������ ������ ��ü `r`�� ����ϴ�. `requests.get` �޼ҵ�� `googleapis`������ get ��û�� �����ϴ�. ���� ������ ������ `r.text`�� ����մϴ�.

���� �ڵ带 ������ `r.status_code`�� ����Ͻʽÿ�.

## post ��û ����

```python
import requests
 
url = 'http://httpbin.org/post'
payload = {'a':'test', 'b':'my post request'}
r = requests.post(url, data=payload) 
print(r.json())

data = r.json()
print(data['form'])
```

���� ���� `httpbin`�� �Խ� ��û�� �����ϴ�. `payload`�� �Խ� ��û���� �������� �������Դϴ�. `r.json()`�� ��ü ���� �޽����� ����ϰ� `data['form']`�� ���̷ε�� ���� �����͸� ����մϴ�.
