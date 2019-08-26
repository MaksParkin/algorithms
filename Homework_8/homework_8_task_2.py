# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.


from collections import Counter, deque


source_string = input("Введите фразу из трех слов:")


def huffman_tree(string_to_compress):
    freq_dict = Counter(string_to_compress)
    sorted_freq = deque(sorted(freq_dict.items(), key=lambda item: item[1]))
    if len(sorted_freq) != 1:
        while len(sorted_freq) > 1:
            weight = sorted_freq[0][1] + sorted_freq[1][1]
            comb = {0: sorted_freq.popleft()[0],
                    1: sorted_freq.popleft()[0]}
            for i, freq in enumerate(sorted_freq):
                if weight > freq[1]:
                    continue
                else:
                    sorted_freq.insert(i, (comb, weight))
                    break
            else:
                sorted_freq.append((comb, weight))
        else:
            weight = sorted_freq[0][1]
            comb = {0: sorted_freq.popleft()[0], 1: None}
            sorted_freq.append((comb, weight))
        return sorted_freq[0][0]


code_table = {}


def huffman_comp(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        huffman_comp(tree[0], path=f'{path}0')
        huffman_comp(tree[1], path=f'{path}1')


huffman_comp(huffman_tree(source_string))

for i in source_string:
    print(code_table[i], end=' ')
