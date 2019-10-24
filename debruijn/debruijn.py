import os
import statistics
import argparse
import networkx as nx

def solve_bubble():
    pass


def simplify_bubbles():
    pass


def solve_entry_tips():
    pass


def solve_out_tips():
    pass

def read_fastq(fpath):
    '''
    Reads fastq and return a list of sequences
    '''
    with open(fpath, 'r') as file:
        for _ in file:
            yield next(file)[:-1]
            next(file)
            next(file)

def cut_kmer(seq, kmersize):
    '''
    Returns a list of kmer
    '''
    for i in range(len(seq)-kmersize+1):
        yield seq[i:i+kmersize]

def build_kmer_dict(fpath, kmersize):
    '''
    Returns a dictionnary of kmer and their occurence
    '''
    dico = {}
    for seq in read_fastq(fpath):
        for kmer in cut_kmer(seq, kmersize):
            if kmer not in dico.keys():
                dico[kmer] = 1
            else:
                dico[kmer] += 1
    return dico

def build_graph(kmer_dict):
    '''
    Builds the graph of kmer
    '''
    graph = nx.DiGraph()
    for key in kmer_dict:
        graph.add_edge(key[:-1], key[1:], weight=kmer_dict[key])
    return graph

def get_starting_nodes(graph):
    '''
    Returns a list of starting nodes
    '''
    start_node = []
    for kmer in graph:
        if list(graph.predecessors(kmer)) == []:
            start_node.append(kmer)
    return start_node

def get_sink_nodes(graph):
    '''
    Returns a list of end nodes
    '''
    sink_nodes = []
    for kmer in graph:
        if list(graph.successors(kmer)) == []:
            sink_nodes.append(kmer)
    return sink_nodes

def get_contigs(graph, start_nodes, end_nodes):
    '''
    Returns a list of tuples (contig, length of contig)
    '''
    contigs = []
    for strt in start_nodes:
        for end in end_nodes:
            if list(nx.all_simple_paths(graph, strt, end)) != []:
                short_path = nx.shortest_path(graph, strt, end)
                contig = []
                for i in range(len(short_path)-1):
                    contig.append(short_path[i][0])
                    flag = i
                contig.append(short_path[flag+1])
                join_contig = ''.join(contig)
                size_contig = len(join_contig)
                contigs.append((join_contig, size_contig))
    return contigs

def fill(text, width=80):
    '''
    Split text with a line return to respect fasta format
    '''
    return os.linesep.join(text[i:i+width] for i in range(0, len(text), width))

def save_contigs(contigs, file_name):
    '''
    Returns a file containing the contigs
    '''
    file_out = open(file_name, 'w')
    for i in range(len(contigs)):
        file_out.write('>contig_' + str(i) + ' len=' + str(contigs[i][1]) + '\n')
        file_out.write(fill(contigs[i][0]) + '\n')
    file_out.close()


def std(val_list):
    '''
    Returns the standard deviation of a list
    '''
    return statistics.stdev(val_list)

def path_average_weight(graph, path):
    '''
    Returns average weight
    '''
    grph = graph.subgraph(path)
    wght = []
    for line in grph.edges(data=True):
        wght.append(line[2]['weight'])
    avg_wght = statistics.mean(wght)
    return avg_wght


def remove_paths(graph, path_list, delete_entry_node, delete_sink_node):
    '''
    Removes the paths and returns a clean graph
    '''
    for path in path_list:
        if delete_entry_node:
            graph.remove_node(path[0])
        if delete_sink_node:
            graph.remove_node(path[-1])
        for i in range(1, len(path)-1):
            graph.remove_node(path[i])
    return graph

def select_best_path(Gr, path_list, path_len, avg_wght, delete_entry_node, delete_sink_node):
    pass


def main():
    '''
    main function
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i")
    parser.add_argument("-k")
    parser.add_argument("-o")
    args = parser.parse_args()

    #read_fastq(args.i)
    kmer_dict = build_kmer_dict(args.i, 21)
    graphe = build_graph(kmer_dict)
    start_nodes = get_starting_nodes(graphe)
    end_nodes = get_sink_nodes(graphe)
    contigs = get_contigs(graphe, start_nodes, end_nodes)
    save_contigs(contigs, "file_d.txt")

if __name__ == "__main__":
    main()
