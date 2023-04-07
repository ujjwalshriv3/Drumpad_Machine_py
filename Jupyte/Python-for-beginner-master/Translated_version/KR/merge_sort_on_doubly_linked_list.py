# ���� linked list�� ���� ���� ���α׷�

# ���� linked list�� ��� 
class Node: 
	
	# ���ο� ��带 �����ϴ� ������
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList: 

	# �� ���� linked list ������
	def __init__(self): 
		self.head = None

	# 2 ���� linked����Ʈ�� �����ϴ� ��� 
	def merge(self, first, second): 
		
		# ù ��° linked list�� ����ִ� ���
		if first is None: 
			return second 
		
		# �� ��° linked list�� ����ִ� ���
		if second is None: 
			return first 

		# �� ���� ���� ������.
		if first.data < second.data: 
			first.next = self.merge(first.next, second) 
			first.next.prev = first 
			first.prev = None
			return first 
		else: 
			second.next = self.merge(first, second.next) 
			second.next.prev = second 
			second.prev = None
			return second 

	# ���������� �ϴ� �Լ�
	def mergeSort(self, tempHead): 
		if tempHead is None: 
			return tempHead 
		if tempHead.next is None: 
			return tempHead 
		
		second = self.split(tempHead) 
		
		# �¿� �ݺ� 
		tempHead = self.mergeSort(tempHead) 
		second = self.mergeSort(second) 

		# ���� �� ������ ����
		return self.merge(tempHead, second) 

	# ���� linked list (DLL)�� ���� ũ���� �� DLL�� ����
	def split(self, tempHead): 
		fast = slow = tempHead 
		while(True): 
			if fast.next is None: 
				break
			if fast.next.next is None: 
				break
			fast = fast.next.next
			slow = slow.next
			
		temp = slow.next
		slow.next = None
		return temp 
		
			
	# list�� ���� ������ ���� ������ �־�����,list�� �տ� ���ο� ��带 �����մϴ�
	def push(self, new_data): 

		# 1. ��� �Ҵ� 
		# 2. �����͸� �� �ȿ� �ֱ�
		new_node = Node(new_data) 

		# 3. �� ��� ������ ����, ���� ��带 ���� (�̹� None)���� ����ϴ�.
		new_node.next = self.head 

		# 4. ��� ����� prev�� new_node�� ����
		if self.head is not None: 
			self.head.prev = new_node 

		# 5. �� ��带 ���� Ű���� ��带 �̵�
		self.head = new_node 


	def printList(self, node): 
		temp = node 
		print("���� �����͸� ����Ͽ� ��ȸ ��ȸ")
		while(node is not None): 
			print (node.data, end=" ") 
			temp = node 
			node = node.next
		print ("\n���� �����͸� ����� ������ ��ȸ")
		while(temp): 
			print (temp.data, end=" ")
			temp = temp.prev

# �� ����� �׽�Ʈ�ϴ� ����̹� ���α׷�
dll = DoublyLinkedList() 
dll.push(5) 
dll.push(20); 
dll.push(4); 
dll.push(3); 
dll.push(30) 
dll.push(10); 
dll.head = dll.mergeSort(dll.head) 
print ("Linked List after sorting")
dll.printList(dll.head) 
