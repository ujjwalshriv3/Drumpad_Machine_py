# ���̺귯�� �������� �� ���� �ν��Ͻ� �ۼ�
import socket
s = socket.socket()
  
# port �����ϱ� 
port = 5056                
  
s.connect(('127.0.0.1', port)) 
  
# �����κ��� ������ �ޱ�(����)
recievs_data = s.recv(1024) 

print(recievs_data.decode())

s.close()     
