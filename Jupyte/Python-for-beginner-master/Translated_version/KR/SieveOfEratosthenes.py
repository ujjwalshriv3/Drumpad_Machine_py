import math

N=int(input("�Ҽ����� ã�� ������ �Է��Ͻʽÿ�."))
primeflag=[0 for i in range(N+1)]
for i in range(2,int(math.sqrt(N))+1):
    for j in range(i*i,N+1,i):
        primeflag[j]=1
primeflag[0]=1
primeflag[1]=1
for i in range(N):
    if primeflag[i]==0:
        print(str(i) + "�� �Ҽ��Դϴ�.")
