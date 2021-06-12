def _get_char_map(word):
    _ = {}
    for char in word:
        _[char] = 1 + _.get(char, 0)
    return _

# T.C: O(n*l); n is the no. of words & l is length of longest word
# S.C: O(C); where C is the number of different character across all words
def minimumCharactersForWords(words):
     _max_map = {}
    for word in words:
        word_map = _get_char_map(word)
        for _char, _max in word_map.items():
            _max_map[_char] = max(_max, _max_map.get(_char, 0))
     _ = []
    for char, occurance in _max_map.items():
        for i in range(occurance):
            _.append(char)
    return _
