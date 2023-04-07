import math

# ������ �Լ�
n = math.sqrt(int(input()))
print(n)

# x���� ũ�ų� ���� ���� ���� ����.
n = math.ceil(float(input()))
print(n)

# ���밪�� ��ȯ
n = math.fabs(int(input()))
print(n)

# x�� ���丮���� ��ȯ
n = math.factorial(int(input()))
print(n)

# x������ ���� ū ������ ��ȯ
n = math.floor(float(input()))
print(n)

# x�� y�� ���� ���� �������� ��ȯ
x = int(input())
y = int(input()) 
n = math.fmod(x,y)
print(n)

# x�� ������ ������ ��(m, e)���� ��ȯ
m = math.exp(float(input()))
print(m)

# iterable�� ��Ȯ�� �ε� �Ҽ��� �հ��� ��ȯ�մϴ�
print(math.fsum(range(10)))

# x�� ���Ѵ��̰ų� NaN�� �ƴ� ��� True�� ��ȯ�մϴ� (���ڰ� �ƴ�).
x = int(input())
print(math.isfinite(x))	

# x�� ���� ���Ѵ��̰ų� ���� ���Ѵ��̸� True�� ��ȯ�մϴ�
x = int(input())
print(math.isinf(x))

# x�� NaN�̸� True�� ��ȯ�մϴ�
x = int(input())
print(math.isnan(x))

# x * (2**i) ��ȯ
x = int(input())
i = int(input())
print(math.ldexp(x, i))

# x�� �м��� �����κ��� ��ȯ
x = int(input())
print(math.modf(x))	

# �߸� ���� �� x�� ��ȯ�մϴ�
x = int(input())
print(math.trunc(x))

#  e**x ��ȯ
x = int(input())
print(math.exp(x))

# e**x - 1 ��ȯ
x = int(input())
print(math.expm1(x))

# x�� �α�ȭ�� ���� ������ ��ȯ�մϴ� (�⺻���� e).
x = int(input())
base = 10
print(math.log(x, base))

# 1 + x�� �ڿ��α׸� ��ȯ�մϴ�
x = int(input())
print(math.log1p(x))

# x�� ���� 2 �� �α� ���� ��ȯ�մϴ�
x= int(input())
print(math.log2(x))

# x�� ���� 10 �� �α� ���� ��ȯ�մϴ�
x =int(input())
print(math.log10(x))

# x�� �ŵ����� y�� �ø�
x = int(input())
y = int(input())
print(math.pow(x, y))

# x�� �������� ��ȯ
x =int(input())
print(math.sqrt(x))

# x�� ��ũ �ڻ����� ��ȯ�մϴ�
x =int(input())
print(math.acos(x))

# x�� ��ũ ������ ��ȯ�մϴ�
x = int(input())
print(math.asin(x))	

# x�� ��ũ ź��Ʈ�� ��ȯ
x = float(input())
print(math.atan(x))

# x�� ��ũ ź��Ʈ�� ��ȯ
x = float(input())
print(math.atan(x))

# atan (y / x)�� ��ȯ�մϴ�
x = int(input())
y = int(input())
print(math.atan2(y, x))

# x�� �ڻ����� ��ȯ�մϴ�
x = int(input())
print(math.cos(x))

# ��Ŭ���� ǥ���� ��ȯ�մϴ�. sqrt (x * x + y * y)
x = int(input())
y = int(input())
print(math.hypot(x, y))

# x�� ������ ��ȯ�մϴ�
x = int(input())
print(math.sin(x))

# x�� ź��Ʈ�� ��ȯ
x = int(input())
print(math.tan(x))

# ���� x�� ���ȿ��� ������ ��ȯ�մϴ�
x = int(input())
print(math.degrees(x))

# ���� x�� ������ �������� ��ȯ
x = int(input())
print(math.radians(x))

# x�� ���ְ� �ڻ����� ���մϴ�
x = int(input())
print(math.acosh(x))

# x�� ���ְ� ������ ��ȯ�մϴ�
x = int(input())
print(math.asinh(x))

# x�� �ְ� �ڻ����� ��ȯ�մϴ�
x = int(input())
print(math.cosh(x))

# x�� �ְ� ������ ��ȯ�մϴ�
x = int(input())
print(math.sinh(x))

# x�� �ְ� ź��Ʈ�� ��ȯ�մϴ�
x = int(input())
print(math.tanh(x))

# x���� ���� �Լ��� ��ȯ
x = int(input())
print(math.erf(x))

# x���� �󺸿��� �Լ��� ��ȯ�մϴ�
x = int(input())
print(math.erfc(x))

# x���� ���� �Լ��� ��ȯ�մϴ�
x = int(input())
print(math.gamma(x))

# x���� ���� �Լ��� ���� ���� �ڿ� �α׸� ��ȯ�մϴ�
x = int(input())
print(math.lgamma(x))

# ���� ���, ���ֿ� ������ ���� (3.14159 ...)
print(math.pi)

# ���� ��� e (2.71828 ...)
print(math.e)
