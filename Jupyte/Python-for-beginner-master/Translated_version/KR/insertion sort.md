
	def insertionsort(seq):
		for sliceEnd in range(len(seq)):
			# �� �ݺ����� ��� �� ���� �� �����̽��� ����ϴ�.
			# seq [0 : sliceEnd]�� (��) �̹� ���ĵǾ����ϴ�
			# ���ĵ� �����̽��� �������� ������ �� ù��° ��Ҹ� �ùٸ� ��ġ�� ���������� �̵�
			pos = sliceEnd
			while pos > 0 and seq[pos] < seq[pos-1]:
				(seq[pos],seq[pos-1]) = (seq[pos-1].seq[pos])
				pos = pos-1
		return seq
