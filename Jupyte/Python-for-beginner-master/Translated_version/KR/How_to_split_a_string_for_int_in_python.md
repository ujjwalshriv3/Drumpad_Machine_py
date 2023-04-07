# ���̽㿡�� int�� ���ڿ��� ������ ���

�̸� ���ؼ��� ���� ���̽��� ����Ƽ�� `split ()` �Լ��� ����ؾ��ϸ�, ���� ��ȣ�� ���� ���ڿ��� �����մϴ�.
#����

`string.split(separator, max)`
<br/>
`separator`	��������. ���ڿ��� ���� �� �� ����� ���б�ȣ�� �����մϴ�. �⺻���� �����Դϴ�.
<br/>
`max`	��������. ���� ���� �����մϴ�. �⺻���� -1�̸� "��� �߻�"�Դϴ�.

# ���

�Է�
```
string = "ONE TWO"
one = string.split(' ')[0] # ['ONE']
two = string.split(' ')[1] # ['TWO']
```
`[i]` �� � �ܾ ������ �������� ��Ÿ���ϴ�. ���⼭ i�� �и��� �ܾ��� ��ġ�� ��Ÿ���ϴ�.
<br/>

# INT�� ����� ��� ���
```
string = "02-04-1994"

 string.split('-')  # ['02', 04', '1994']
 
day = string.split('-')[0]  # ['02']
month = string.split('-')[1] # ['04']
year = string.split('-')[2] # ['1994']

day = int(day)
month = int(month)
year = int(year)

print(day,month,year) # output is 2 4 1994
```
