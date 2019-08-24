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

def prefix_trie_matching(text, trie):
	i_index = 0
	symbol = text[i_index]
	symbol_index = GENOMICS.index(symbol)
	current_node = trie
	
	while True:
		if current_node.value is not None:
			return current_node.value
		elif current_node.next[symbol_index] != NA:
			i_index += 1
			if len(text) > i_index:
				symbol = text[i_index]
			elif i_index == len(text) - 1:
				symbol = text[-1]
			if i_index > len(text):
				break
			current_node = current_node.next[symbol_index]
			symbol_index = GENOMICS.index(symbol)
		else:
			return False


def solve (text, patterns):
	result = []
	text_length = len(text)

	trie = build_trie(patterns)
	for i in range(text_length):
		found = prefix_trie_matching(text[i:], trie)
		if found:
			result.append(i)

	return result



text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
