import argparse
import networkx as nx

def get_starting_nodes():
    pass


def std():
    pass


def get_sink_nodes():
    pass


def path_average_weight():
    pass


def remove_paths():
    pass


def select_best_path():
    pass


def save_contigs():
    pass


def get_contigs():
    pass


def solve_bubble():
    pass


def simplify_bubbles():
    pass


def solve_entry_tips():
    pass


def solve_out_tips():
    pass

def read_fastq(fpath):
    with open(fpath, 'r') as file:
        for line in file:
            yield (next(file)[:-1])
            next(file)
            next(file)

def cut_kmer(seq,kmersize):
    for i in range(len(seq)-kmersize+1):
        yield seq[i:i+kmersize]

def build_kmer_dict(fpath,kmersize):
    dico = {}
    for seq in read_fastq(fpath):
        for kmer in cut_kmer(seq, kmersize):
            if kmer not in dico.keys():
                dico[kmer] = 1
            else:
                dico[kmer] += 1
    return dico

def build_graph(dic):
    graph = nx.DiGraph()
    for key in dic:
        graph.add_edge(key[:-1], key[1:], weight = dic[key])
    return graph

def get_starting_nodes(Gr):
    start_node = []
    for kmer in Gr:
        if len(Gr.predecessors(kmer)) == 0:
            start_node.append(kmer)
    return start_node

def get_sink_nodes(Gr):
    sink_nodes = []
    for kmer in Gr:
        if len(Gr.successors(kmer)) == 0:
            sink_node.append(kmer)
    return sink_nodes

def get_contigs(graphe, start_node, sink_node):
    contig = []








def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i")
    parser.add_argument("-k")
    parser.add_argument("-o")
    args = parser.parse_args()

    #read_fastq(args.i)
    dict_kmer = build_kmer_dict(args.i, 21)
    build_graph(dict_kmer)


if __name__ == "__main__":
    main()
