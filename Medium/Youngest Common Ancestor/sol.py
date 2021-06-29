# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# T.C: O(h)
# S.C: O(h)
def getYoungestCommonAncestor1(topAncestor, descendantOne, descendantTwo):
    ancestors_of_one = {}
    while descendantOne:
        ancestors_of_one[descendantOne.name] = True
        descendantOne = descendantOne.ancestor
        while descendantTwo:
        if descendantTwo.name in ancestors_of_one:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor


def get_hieght(descendant, topAncestor):
    h = 0
    while descendant != topAncestor:
        h += 1
        descendant = descendant.ancestor
    return h

# T.C: O(h)
# S.C: O(1)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    hieght_one = get_hieght(descendantOne, topAncestor)
    hieght_two = get_hieght(descendantTwo, topAncestor)
    bottom_descendant = descendantOne if hieght_one > hieght_two else descendantTwo
    other_descendant = descendantTwo if hieght_one > hieght_two else descendantOne
    for i in range(abs(hieght_one - hieght_two)):
        bottom_descendant = bottom_descendant.ancestor
    # now both descendant are at same level
    while bottom_descendant and other_descendant:
        if bottom_descendant.name == other_descendant.name:
            return other_descendant
        bottom_descendant = bottom_descendant.ancestor
        other_descendant = other_descendant.ancestor
