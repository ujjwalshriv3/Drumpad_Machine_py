# ���̽� ���Խ�

#### ���Խ��� ���ڿ����� ���� ��ġ�� ���˴ϴ�. Ư�� ������ �ؼ��ϴ� ��ȿ�� ��ȭ ��ȣ, ���� ���� �ּҸ� ã�� ���� ������ ��ġ��Ű�� �Ϲ����� ����� �����մϴ�. �Ϲ����� �˻� ����� ����ϴ� ���� ������ �۾��Դϴ�. ���Խ��� ���� ���丶Ÿ�� ����Ͽ� ���������� �����˴ϴ�.


### re.search(pattern, string)

���ڿ����� ó�� ��Ÿ���� ���ϰ� ��ġ�ϴ� index�� ���ڿ��� �����ϴ� ��ġ�ϴ� ��ü�� ��ȯ�մϴ�.

```python
import re  #import regex module

# ���ڿ� �տ� r�� �߰��ϸ� ���� ���ڿ��̵˴ϴ�.
print(re.search('n', r'ba\n'))
```

���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(3, 4), match='n'>
```

### ��ü ��ġ �޼ҵ�

| Method        | Functionality                               |
| ------------- | -------------                               |
| start()       | ��ġ�ϴ� ���ڿ��� ����index�� ��ȯ          |
| end()         | ��ġ�ϴ� ���ڿ��� ��index�� ��ȯ            |
| span()        | ���� �� �� index�� tuple�� ��ȯ             |
| group()       | ��ġ�ϴ� ���ڿ��� ��ȯ                      |

 
```python
import re 

print(re.search('ab', '12abcd').start()) 
print(re.search('ab', '12abcd').end())  
print(re.search('ab', '12abcd').span())  
print(re.search('ab', '12abcd').group())
```
���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
2
4
(2, 4)
ab
```

### re.match(pattern, string) 

���ڿ��� ���ۺκп��� ������ ��ġ��Ű��(prefix ��ġ) ��ġ�ϴ� ��ü�� ��ȯ�մϴ�.

```python
import re 

print(re.match('abc', 'abcdef'))
```
���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(0, 3), match='abc'>
```

### re.findall(pattern, string) 

���ڿ����� ������ ����׸��� ã�� ��ġ�ϴ� ���ڿ� list�� ��ȯ�մϴ�.

```python
import re 

print(re.findall('[0-9]+', '12ad123cd'))
```

##### ���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
['12', '123']
```

### re.sub(pattern, repla, string)

���ڿ��� ��� ��ġ �׸��� repla�� �ٲٰ� ������ ���ڿ��� ��ȯ

```python
import re 

print(re.sub('ab', 'cd', 'habcabc'))
```

##### ���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
hcdccdc
```

### re.compile(pattern)

������ �������Ͽ� ���Խ� ��ü�� ��ȯ�մϴ�. �� ��ü�� match(), search() �� ��Ÿ �޼ҵ带 ����Ͽ� ��ġ��Ű�� �� ����� �� �ֽ��ϴ�.

```python
import re 

p = re.compile('ab') #p can be reused
print(p.search('cab')) 
```

���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(1, 3), match='ab'>
```

## �ݺ�
##### \*�� 0�� �̻��� ���๮�� �߻��� ��ġ��Ű�µ� ���˴ϴ�.
##### ? ���๮���� 0�Ǵ�1  �߻��� ��ġ��Ű�µ� ���˴ϴ�.
##### + �� �ϳ� �̻��� ���๮�� �߻��� ��ġ��Ű�µ� ���˴ϴ�.
##### {x,y}�� �ּ� x �߻� �� ���๮���� �ִ� y �߻��� ��ġ��Ű�µ� ���˴ϴ�.

```python
import re

print(re.search('ab*c', 'abbbbbc')) 
print(re.search('ab?c', 'ac'))
print(re.search('ab+c', 'abbc'))
print(re.search('a{1,4}', 'aaabcd'))
```
���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(0, 7), match='abbbbbc'>
<_sre.SRE_Match object; span=(0, 2), match='ac'>
<_sre.SRE_Match object; span=(0, 4), match='abbc'>
<_sre.SRE_Match object; span=(0, 3), match='aaa'>
```

# ��Ÿ ����

##### [] �� ��ġ��ų ���ڱ׷��� ���� �� ���˴ϴ�.
##### [0-9] �� ��� �������� ��ġ�� �� �ֽ��ϴ�
##### [a-d] �� a, b, c �Ǵ� d�� ��ġ�� �� �ֽ��ϴ�
##### ^ �� ��ġ�ϴ� ���ڸ� ���ܽ�Ű�µ� ���˴ϴ�
##### .  ���๮�ڸ� ������ ��� ���ڿ� ��ġ

```python
import re

print(re.search('[a-c]{2}', 'dmacf')) 
print(re.search('[0-9]{3}', 'aa123'))
print(re.search('[^a-c]', 'ca1d'))
print(re.search('.+', 'aaabcd\n'))
```
���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(2, 4), match='ac'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='1'>
<_sre.SRE_Match object; span=(0, 6), match='aaabcd'>
```

##### \ w�� [a-zA-Z0-9_]�� �ش��ϴ� ��� ���ĺ� ���ڿ� ��ġ�մϴ�.
##### \ d�� [0-9]�� �ش��ϴ� ��� ���ڿ� ��ġ�մϴ�.
##### \ W�� [^ a-zA-Z0-9_]�� ������ �����ڰ� �ƴ� ���ڿ� ��ġ�մϴ�.
##### \ D�� [^ 0-9]�� ���� 10 ������ �ƴ� ���ڿ� ��ġ�մϴ�.
##### \ s�� ���� ���ڿ� ��ġ

```python
import re

print(re.search('\w\w', 'c123')) 
print(re.search('\d\d\d', 'aa123bc'))
print(re.search('\W', 'ca\n'))
print(re.search('\D', '123c23'))
print(re.search('\s', 'how are'))
```
���� ���α׷� ����� �����ϸ� ������ �����ϴ�: 

```bash
<_sre.SRE_Match object; span=(0, 2), match='c1'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='\n'>
<_sre.SRE_Match object; span=(3, 4), match='c'>
<_sre.SRE_Match object; span=(3, 4), match=' '>
```
