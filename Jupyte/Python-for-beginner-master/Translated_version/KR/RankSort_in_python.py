# ranksort
# �迭�� �����ϴ� �� �ٸ� ���
# ������Ҹ� ���� ũ�� N�� �迭 A�� �Է��մϴ�.
# A�� ��Ҹ� A [0] <= A [1] <= A [2] <= .... <= A [n-1]�� �������մϴ�.

# ����ڰ� � ũ��� �迭A �Է� 
A = [i for i in input().split()]
# N�� A�� �����Դϴ�
N = len(A)
# �迭R�� �迭A�� �� ����� ������ �����մϴ�.
R=[0 for i in range(N)]
for j in range(1,N):
    for i in range(j):
        if A[i] <= A[j]:
            R[j] = R[j] + 1
        else:
            R[i] = R[i] + 1
# �迭U�� �迭R�� ��ҷ� index�� ���� �迭A�� ��Ҹ� �����մϴ�.
# U�� A�� ���ĵ� �迭�Դϴ�
U = [0 for i in range(N)]
for j in range(N):
    U[R[j]-1] = A[j]
# ���ĵ� �迭A�� ����ϴ�.
for j in range(N):
    A[j] = int(U[j])

print(A)
