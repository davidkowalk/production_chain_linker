import json
from sys import argv
from engine.graph_gen import get_graph
from engine.console_interface import loop

helpstr = """
    Syntax:

    python3 <path> [-h <head> <amount>] [-d]

    ------------------------------------------

    -h  Specify the head object and the units per time to be produced
    -d  dump
"""

def input_head():
    id = input("Head Node: ")
    amount = float("Amount")

def decode_args(args):

    if not len(args) >= 2:
        raise ValueError("Must provide path.")

    path = args[1]

    arg_formatted = dict()
    arg_formatted["path"] = path

    if "-h" in args:
        pos = args.index("-h")

        if len(args) < pos+2:
            raise ValueError("-h requires arguments:\n\n"+helpstr)

        try:
            arg_formatted["head"] = {"id": args[pos+1], "amount": float(args[pos+2])}
        except:
            raise ValueError("Please provide a valid floating point value for the amount per time.")

    if "-d" in args:
        arg_formatted["dump"] = True
    else:
        arg_formatted["dump"] = False

    return arg_formatted

def main(args):

    argv = decode_args(args)


    if argv["dump"]:
        print("Arguments: "+json.dumps(argv, indent=2)+"\n")

    with open(argv["path"]) as f:
        jobj = json.load(f)

    if argv["dump"]:
        print("Production Chain:"+json.dumps(jobj, indent=2)+"\n")

    if "head" in argv:
        head_id, head_amount = argv["head"]["id"], argv["head"]["amount"]
    else:
        head_id, head_amount = input_head()

    graph, nodes = get_graph(jobj, head_id)

    if argv["dump"]:
        print(graph)

    loop(graph, nodes)

if __name__ == '__main__':
    main(argv)
