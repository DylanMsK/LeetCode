class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.exists: bool = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.exists = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.exists

    def startsWith(self, prefix: str) -> bool:
        node = self._find(prefix)
        return node is not None

    def _find(self, word) -> Optional[TrieNode]:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                break
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)