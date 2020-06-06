from collections import Counter


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.right = right
        self.left = left
        self.value = value


def huffman(string):
    string_count = Counter(string)

    if len(string_count) == 1:
        node = MyNode(None)
        node.left(list(string_count.keys()[0]))
        node.right = MyNode(None)
        string_count = {node: None}

    while len(string_count) > 1:
        temp = string_count.most_common()[:-3:-1]
        node = MyNode(None)
        del string_count[temp[0][0]]
        del string_count[temp[1][0]]
        if isinstance(temp[0][0], str):
            node.left = MyNode(temp[0][0])
        else:
            node.left = temp[0][0]
        if isinstance(temp[1][0], str):
            node.right = MyNode(temp[1][0])
        else:
            node.right = temp[1][0]
        string_count[node] = temp[0][1] + temp[1][1]
    return letter_coding(list(string_count.keys())[0], string)


def letter_coding(tree, str_to_code, way='', info=dict()):
    if isinstance(tree.value, str):
        info[tree.value] = way
        return info
    letter_coding(tree.left, str_to_code, way + '0', info)
    letter_coding(tree.right, str_to_code, way + '1', info)

    return string_coding(info, str_to_code)


def string_coding(codes, object_):
    code = ''
    for letter in object_:
        if letter in codes:
            code += str(codes[letter])
    return code, codes


def decoding(code, codes):
    initial_line = ''
    spam = str()
    for letter in code:
        spam += letter
        for key, value in codes.items():
            if spam == value:
                initial_line += key
                spam = ''
    return initial_line


string = str(input('Введите строку для уменьшения веса: '))
str_to_decode, info = huffman(string)
print(f'Сжатая строка: {str_to_decode}')
decoded_str = decoding(str_to_decode, info)
print(f'Расжатая строка: {decoded_str}')

print(f'Сжатая и расжатая строки совпадают') if string == decoded_str else print(f'Сжатые и расжатые строки не '
                                                                                 f'совпадают')
