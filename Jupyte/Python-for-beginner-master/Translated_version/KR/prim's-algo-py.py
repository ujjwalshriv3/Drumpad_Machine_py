class Graph:
    def __init__(self):
        # �ش� ���� ��ü�� ���εǴ� Ű�� ���� �� dictionary
        self.vertices = {}

    def add_vertex(self, key):
        """�־��� Ű�� ���� �������� �׷����� �߰�."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        """�ش� Ű�� ���� ��ü�� ��ȯ�մϴ�."""
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        """�־��� ���Է� src_key���� dest_key�� �����ڸ��� �߰��Ͻʽÿ�."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        """src_key���� dest_key������ �����ڸ��� ������ True�� ��ȯ�մϴ�."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def display(self):
        print('Vertices: ', end='')
        for v in self:
            print(v.get_key(), end=' ')
        print()

        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """�� ������ ��ü�� �ش��ϴ� ���� Ű."""
        return self.key

    def add_neighbour(self, dest, weight):
        """�� �������� ������ �𼭸� ����ġ�� ������� �����Ͻʽÿ�."""
        self.points_to[dest] = weight

    def get_neighbours(self):
        """�� ������ ����Ű�� ��� ������ ��ȯ�մϴ�. """
        return self.points_to.keys()

    def get_weight(self, dest):
        """�� �������� ������������ �����ڸ� ����ġ�� ����ϴ�."""
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        """�� ������ dest�� ����Ű�� True�� ��ȯ�մϴ�"""
        return dest in self.points_to


def mst_prim(g):
    """����� �׷���g�� �ּ� ��� ���� Ʈ���� ��ȯ�մϴ�."""
    mst = Graph()  # MST�� ���� �� ���ο� Graph ��ü ����

    # �׷����� ����ִ� ���
    if not g:
        return mst

    nearest_neighbour = {}
    smallest_distance = {}
    unvisited = set(g)

    u = next(iter(g))  # g���� �ϳ��� �������� �����Ͻʽÿ�
    mst.add_vertex(u.get_key())  # MST�� �纻�� �߰��Ͻʽÿ�
    unvisited.remove(u)

    for n in u.get_neighbours():
        if n is u:
            continue
        nearest_neighbour[n] = mst.get_vertex(u.get_key())
        smallest_distance[n] = u.get_weight(n)

    while (smallest_distance):
        outside_mst = min(smallest_distance, key=smallest_distance.get)
        # MST ���ο��� ���� ����� �̿��� ��´�
        inside_mst = nearest_neighbour[outside_mst]
        mst.add_vertex(outside_mst.get_key())
        mst.add_edge(outside_mst.get_key(), inside_mst.get_key(),
                     smallest_distance[outside_mst])
        mst.add_edge(inside_mst.get_key(), outside_mst.get_key(),
                     smallest_distance[outside_mst])
        unvisited.remove(outside_mst)
        del smallest_distance[outside_mst]
        del nearest_neighbour[outside_mst]
        for n in outside_mst.get_neighbours():
            if n in unvisited:
                if n not in smallest_distance:
                    smallest_distance[n] = outside_mst.get_weight(n)
                    nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())
                else:
                    if smallest_distance[n] > outside_mst.get_weight(n):
                        smallest_distance[n] = outside_mst.get_weight(n)
                        nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())

    return mst


g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')

    elif operation == 'mst':
        mst = mst_prim(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()

    elif operation == 'display':
        g.display()
        print()

    elif operation == 'quit':
        break
