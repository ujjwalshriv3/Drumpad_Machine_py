# ���̺귯�� ���� ���� �� ���� �ν��Ͻ� �ۼ�
import socket                
s = socket.socket()          
print ("������ ���������� ����������ϴ�.")

# ��Ʈ
port = 5056                
  
s.bind(('127.0.0.1', port))          

# �ִ� 5���� ������ ���� �� �ֽ��ϴ�
s.listen(5)      
print ("������ ������Դϴ�." )           

while True: 
  
   c, addr = s.accept()      
   print ('���� �ּҷκ��� ������ ���������� :', addr )
  
   c.send('�������ּż� �����մϴ�.'.encode())
  
   c.close() 
