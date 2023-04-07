# �÷��� ��⿡�� ������ ������ ������ ���Ե��ֽ��ϴ�.
# https://docs.python.org/3/library/collections.html#module-collections
import collections

# namedtuple() �� fields��� �̸��ٿ��� ����Ŭ������ Ʃ���� �����մϴ�.
Person = collections.namedtuple('person',('name','age','height'))
chaz = Person(name='Chaz', age='29', height='180cm')
print(chaz.age)

# �Ϲ�Ʃ��ó�� Ǯ���� �ֽ��ϴ�.
name, age, height = chaz

# defaultdict�� ����ϸ� ����ϸ� �������� �ʴ� Ű�� ������ �� ����� �⺻�� �Ǵ� Ÿ���� ������ �� �ֽ��ϴ�.
d = collections.defaultdict(int)
d['foo'] += 1
print(d['foo'])

# OrderedDict�� �׸��� �ֹ��ϰų� pop�ϱ� ���� �߰� �޼ҵ尡�ִ� dict�� ���� Ŭ�����Դϴ�.
d = collections.OrderedDict({'apple':'fruit', 'carrot':'vegetable'})
print(d['apple'])
d.move_to_end('apple')
d.popitem()

# ChainMap�� ���� ����ó�� �۵��ϱ� ���� ���� ������ ��Ͽ� �����մϴ�.
# ������ ���������� �˻��ǰ� Ű�� ù ��° �˻� ���� ��ȯ�˴ϴ�.
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(collections.ChainMap(adjustments, baseline)))

# adjustments�� ���� ChainMap�� �߰��� ù ��° �����̱� ������ ��ȯ�ȴ�.
print(collections.ChainMap(adjustments, baseline)['art'])

# Counters ��ü�� iterable�� ���ؼ� �׸��� ���� ���� �� ���ִ� ����� �����մϴ�.
# �׸��� Ű�� ����ǰ� ������ ���˴ϴ�
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
