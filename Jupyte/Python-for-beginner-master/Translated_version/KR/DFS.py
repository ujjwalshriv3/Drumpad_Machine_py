# �־��� �׷������� DFS��ȸ�� ����ϴ� ���̽�3 ���α׷� 
from collections import defaultdict 

# �� Ŭ������ ����list ǥ���� ����Ͽ� ���� �׷����� ��Ÿ���ϴ�.
class Graph: 

	# ������
	def __init__(self): 

		# �׷����� �����ϱ����� �⺻ dictionary 
		self.graph = defaultdict(list) 

	# �׷����� edge�� �߰��ϱ����� �Լ�function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# DFS���� ����ϴ� �Լ� 
	def DFSUtil(self, v, visited): 

		# ���� ��带 �湮�Ѱ����� ǥ���ϰ� ����ϱ� ���� ǥ�� 
		visited[v] = True
		print(v, end = ' ') 

		# �� ������ ������ ��� ������ ���� �ݺ�
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	# DFS��ȸ�� �����ϴ� �Լ�. 
	# ��� DFSUtil()�� ����մϴ�. 
	def DFS(self, v): 

		# ��� ������ �湮���� ���� ������ ǥ��
		visited = [False] * (len(self.graph)) 

		# DFS��ȸ�� ����ϱ� ���� ��� ����� �Լ��� ȣ���ϼ���. 
		self.DFSUtil(v, visited) 

# Driver �ڵ�

# ���� ���̾�׷����� �־��� �׷����� ����
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("���ϴ� (���� 2 ���� ����)�� DFS�Դϴ�.") 
g.DFS(3) 
