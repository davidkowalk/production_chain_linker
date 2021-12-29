import json

def get_graph(chain, head):
    #print(json.dumps(chain[head]))

    return get_node(chain, head)

def get_node(chain, node_id, log = None):

    if log == None:
        log = list()

    print(node_id)

    head = Node(node_id)
    if node_id in log:
        print(f"Warning: Circular production chain!\n\"{node_id}\" requires itself.")
        return head

    node_json = chain[node_id]

    if "requires" in node_json:
        for entry in node_json["requires"]:
            head.add_child(get_node(chain, entry, log+[node_id]))

    return head

class Node:

    def __init__(self, id):
        self.id = id
        self.children = list()


    def add_child(self, node):
        """
        Takes Node Object and appends it to own list
        """

        self.children.append(node)
