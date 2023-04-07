# BeautifulSoup�� ������?

BeautifulSoup�� www.crummy.com�� ���̽� ���̺귯���Դϴ�.

**Ư¡��:**

Beautiful Soup�� ����� �ִ� ��� ���� parsing�ϰ� tree traversal���մϴ�.

-�������� ��� ��ũ�� ã��.
-Ư�� Ŭ���� ��ü ã��
-abc.com�� ��ġ�ϴ� URL ã��
-ǥ ���� ã��
-Ư�� �ؽ�Ʈ ã��

**��ġ**

```sh
pip install beautifulsoup4
```

�ý��ۿ� pip�� ��ġ�Ǿ� �ִ��� Ȯ���Ͻʽÿ�. cmd�� pip�� ��ġ�ߴ��� Ȯ���Ͻʽÿ�:

```sh
pip --version
```

***�ϴ¹�***

*�⺻���� ����*

```python
from bs4 import BeautifulSoup

# beautifulsoup4 ��������

soup = BeautifulSoup(html_doc, 'html.parser')

# html_doc�� html parser�� ���� �м��մϴ� (��� ������ �ٸ� parser�� �ֽ��ϴ�)
```

*�ҽ��ڵ�*

```python
print(soup.prettify())                

#������ ��ü �ҽ��ڵ带 ���˵� ������� ����ϴ�.
```

*��� ��ũ ã��*

```python
for a in soup.findAll('a',href=True):
    print(a.text)
```

*Ư�� Ŭ���� div ��ü ã��*

```python
mydivs = soup.findAll("div", { "class" : "stylelistrow" })
```

*��� ���̺� ã��*

```python
tables = soup.findAll("table")

for table in tables:
    if table.findParent("table") is None:
        print(str(table))
```

**�߰� �б�:**

 - [Python Web Scraping Tutorial using BeautifulSoup](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
 - [Web scraping and parsing with Beautiful Soup 4 Introduction](https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/)
 - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [Stackoverflow Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)
