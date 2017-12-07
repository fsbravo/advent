import re

class SimpleNode(object):

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.parents = []


class SimpleTree(object):

    def __init__(self, data):
        self.nodes = {n: SimpleNode(n, w, c) for n, w, c in data}
        # set parents
        for node in self.nodes.values():
            for n in node.children:
                self.nodes[n].parents.append(node.name)

    def find_root(self):
        for n in self.nodes.values():
            if len(n.parents) == 0:
                return n.name

    def find_wrong_weight(self):
        n = self.find_root()
        node = self.nodes[n]
        while True:
            children_weights = [self.find_weight(c) for c in
                                node.children]
            mode = max(children_weights, key=children_weights.count)
            print node.name
            print mode
            print children_weights
            inconsistent = False
            for i, w in enumerate(children_weights):
                if w != mode:
                    node = self.nodes[node.children[i]]
                    inconsistent = True
                    difference = w - mode
                    break
            # found node which is consistent
            if not inconsistent:
                # calculate required difference
                return node.weight - difference


    def find_weight(self, n):
        node = self.nodes[n]
        weight = node.weight
        for c in node.children:
            weight += self.find_weight(c)
        return weight


def find_bottom(infile):
    data = retrieve_data(infile)
    # create all nodes
    tree = SimpleTree(data)
    return tree.find_root()


def get_tree(infile):
    data = retrieve_data(infile)
    return SimpleTree(data)


def find_wrong_weight(infile):
    data = retrieve_data(infile)
    tree = SimpleTree(data)
    return tree.find_wrong_weight()


def retrieve_data(infile):
    data = []
    with open(infile, 'r') as fin:
        for l in fin:
            pattern = '(?P<name>[a-z]+)+.*?(?P<weight>[0-9]+)+\)(?P<rest>.*)?'
            res = re.search(pattern, l)
            name = res.group('name')
            weight = int(res.group('weight'))
            if len(res.group('rest')) > 3:
                rest = res.group('rest')[3:].split(',')
                rest = [r.strip() for r in rest]
            else:
                rest = []
            data.append((name, weight, rest))
    return data