import operator


"""
    1st approach: trie
    - a trie node only need children, is_word and count
    - for insert, just insert
    - for search, 
        1. search node in a trie
        2. dfs
        3. sort

    Time of insert      O(lenfth of a word)
    Time of search      O(nlogn) because of the sort
    1180 ms, faster than 64.25%
"""


class Trie(object):
    def __init__(self, children, is_word, count):
        self.children = children
        self.is_word = is_word
        self.count = count


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.history = ''
        self.trie = Trie({}, False, 0)
        for i in range(len(sentences)):
            self._insert(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self._insert(self.history, 0)
            self.history = ''
            return []
        else:
            self.history += c
            return self._search()

    def _insert(self, sentence, count):
        cur = self.trie
        for i in range(len(sentence)):
            w = sentence[i]
            temp = None
            if w in cur.children:
                temp = cur.children[w]
            else:
                temp = Trie({}, False, 0)
            if i == len(sentence) - 1:
                temp.is_word = True
                if count == 0:
                    temp.count += 1
                else:
                    temp.count = count
            cur.children[w] = temp
            cur = temp

    def _search(self):
        """
        1. search node in a trie
        2. dfs
        3. sort
        """
        # search
        prefix = self.history
        target = self.trie
        for w in prefix:
            if w not in target.children:
                return []
            target = target.children[w]
        leafs = []

        # dfs
        def dfs(node, route):
            if node.is_word:
                # trick: use negative count and enjoy the simple python sort
                leafs.append((-node.count, prefix+route))
            for key in node.children:
                dfs(node.children[key], route+key)
        dfs(target, "")
        leafs = sorted(leafs)

        # sort
        return [x[1] for x in leafs[:3]]


sentences = ['i love you', 'island', 'ironman', 'i love leetcode', 'ia']
times = [5, 3, 2, 2, 2]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input('p'))
print(obj.input('#'))
print(obj.trie)

print("-----")

"""
    2nd approach: trie
    - a trie node only need children and count
    - for insert, just insert
    - for search, 
        1. search node in a trie
        2. dfs
        3. sort

    Time of insert      O(lenfth of a word)
    Time of search      O(nlogn) because of the sort
    1180 ms, faster than 20.08%
"""


class Trie(object):
    def __init__(self):
        self.children = {}
        self.count = 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.history = ''
        self.trie = Trie()
        for i in range(len(sentences)):
            self._insert(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self._insert(self.history)
            self.history = ''
            return []
        else:
            self.history += c
            return self._search()

    def _insert(self, sentence, count=1):
        """
        1. traversal to insert a word into the trie
        """
        cur = self.trie
        for c in sentence:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.count += count

    def _search(self):
        """
        1. search node in a trie
        2. dfs
        3. sort
        """
        # search
        prefix = self.history
        cur = self.trie
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        leafs = []

        # dfs
        def dfs(node, path):
            if node.count > 0:
                leafs.append((node.count, path))
            for key in node.children:
                dfs(node.children[key], path+key)
        dfs(cur, prefix)

        # python cmp
        def mycmp(a, b):
            # if we want descending and a > b, we return -1
            if a[0] > b[0]:
                return -1
            elif a[0] < b[0]:
                return 1
            else:
                # if we want ascending and a < b, we return -1
                if a[1] < b[1]:
                    return -1
                return 1
        # sort using cmp
        leafs = sorted(leafs, cmp=mycmp)

        # sort
        return [x[1] for x in leafs[:3]]


sentences = ['i love you', 'island', 'ironman', 'i love leetcode', 'ia']
times = [5, 3, 2, 2, 2]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input('p'))
print(obj.input('#'))
print(obj.trie)
