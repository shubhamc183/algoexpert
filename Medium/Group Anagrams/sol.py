# T.C: O(w * nlog(n)), w = no. of words
# S.C: O(w * n), n = length of longest word
def groupAnagrams(words):
    anagrams = {}
    solution = []
    for i in range(len(words)):
        word_sorted = ''.join(sorted(words[i]))
        anagrams[word_sorted] = anagrams.get(word_sorted, []) + [i]
    for anagram_indexes in anagrams.values():
        solution.append([words[index] for index in anagram_indexes])
    return solution

