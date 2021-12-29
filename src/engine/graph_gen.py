import json

def get_graph(chain, head):
    #print(json.dumps(chain[head]))

    nodes = dict()

    return get_node(chain, head, nodes = nodes), nodes

def get_node(chain, node_id, nodes = None, log = None):

    if log == None:
        log = list()

    # Remove duplicate nodes
    if node_id in nodes:
        return nodes[node_id]


    #print(node_id)

    head = Node(node_id)
    nodes[node_id] = head

    if node_id in log:
        print(f"Warning: Circular production chain!\n\"{node_id}\" requires itself.")
        return head

    node_json = chain[node_id]

    if "requires" in node_json:
        for entry in node_json["requires"]:
            head.add_child(get_node(chain, entry, nodes = nodes, log=log+[node_id]), node_json["requires"][entry])

    return head

class Node:

    def __init__(self, id):
        self.id = id
        self.children = list()
        self.scale = list()
        self.total = 0 #Will hold the total of weighted occurences in tree

    #def __repr__(self):
    #    return str(self)

    def __str__(self, amount = 1, level = 0):
        output = " "*level+"-"+self.id+f" ({amount})\n"
        for child in self.children:
            output += child.__str__(self.scale[self.children.index(child)],level+1)

        return output

    def reset_count(self):
        self.total = 0

        for child in self.children:
            child.reset_count()

        # Set total for all items to 0

    def count(self, amount):
        # Add volume to own total
        self.total += amount

        # Add total to children times how often the mother-node got increased
        for child in self.children:
            child.count(self.scale[self.children.index(child)]*amount)

    def add_child(self, node, amount):
        """
        Takes Node Object and appends it to own list
        """

        self.children.append(node)
        self.scale.append(amount)
