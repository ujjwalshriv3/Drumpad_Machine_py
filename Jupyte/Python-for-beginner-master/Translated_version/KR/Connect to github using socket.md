# ���̽㿡���� ���� ���α׷��� ����
# �� ���α׷��� ���ϵ��� ����Ͽ� github.com�� �����մϴ�.
```python
import socket
import sys

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("���� ������")

except socket.error as error:
    print("���� ���� ���� {}".format(error))

port = 80   # default port for socket

try:
    host_ip = socket.gethostbyname('www.github.com')

except socket.gaierror:
    print("ȣ��Ʈ�� Ȯ���ϴ� �߿� ������ �߻��߽��ϴ�.")
    sys.exit()

# ������ �����ϱ�
soc.connect((host_ip, port))

print("������ ��Ʈ���� github�� ���������� ����� == {}".format(host_ip))
```