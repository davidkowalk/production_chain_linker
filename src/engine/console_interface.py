modified_scale = False
current_scale = 0

def loop(chain_tree, nodes: dict):
    while True:
        print("-"*20)

        print("Options:\n\
                [1] Print Production chain.\n\
                [2] Specify units per time to be produced.\n\
                [3] Get amount of an item in the chain to be produced\n\
                [4] Exit")

        try:
            choice = int(input("> "))

            if choice == 0 or choice > 4:
                print("Please choose between one of the options.")
                continue
        except:
            print("Please choose between one of the options.")
            continue

        if choice == 1:
            print(chain_tree)
        elif choice == 2:
            scale_ui(chain_tree)
        elif choice == 3:
            total_node_ui(nodes)
        elif choice == 4:
            exit()

def scale_ui(chain_tree):
    global current_scale, modified_scale
    print(f"\nCurrent Production: {current_scale}/(Unit of time)\nPlease set new scale:", end = "")
    try:
        new_scale = float(input())
    except:
        print("Please input a valid floating point number.")
        return

    current_scale = new_scale
    set_tree_scale(chain_tree, new_scale)

    print("-=New scale set!=-")

def set_tree_scale(head, scale):
    global modified_scale

    # First Reset the counter
    if not modified_scale:
        modified_scale = True
    else:
        head.reset_count() #clear count for entire tree

    head.count(scale)

def total_node_ui(node_list):
    print("\nPlease select a node:")
    i = 1
    lookup = dict()
    print("[0] -Go Back-")
    for node in node_list:
        print(f"[{i}] {node_list[node].id}")
        lookup[i] = node_list[node]
        i += 1

    while True:
        try:
            i = int(input("> "))
        except:
            print("Please select one of the options")
            continue

        if i == 0:
            return

        if i not in lookup:
            print("Please select one of the options")
            continue


        calc_amount(lookup[i])

def calc_amount(node):
    print(f"\n{node.id}: {node.total}/(Unit of time)\n")
