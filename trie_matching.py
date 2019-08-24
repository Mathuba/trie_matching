# python3
import sys

NA = -1
GENOMICS = ['A', 'C', 'G', 'T']

class Node:
	def __init__ (self):
		self.value = None
		self.next = [NA] * 4


def insert(root, gene_sequence):
	current_node = root
	for symbol in gene_sequence:
		symbol_index = GENOMICS.index(symbol)
		if current_node.next[symbol_index] == NA:
			current_node.next[symbol_index] = Node()
		current_node = current_node.next[symbol_index]
	current_node.value = gene_sequence

def build_trie(patterns):
	tree = Node()
	for pattern in patterns:
		insert(tree, pattern)
	return tree

def solve (text, n, patterns):
	result = []

	trie = build_trie(patterns)
	print("trie next at least: ", trie.next)

	return result



text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
