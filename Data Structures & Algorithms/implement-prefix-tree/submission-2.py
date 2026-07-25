class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, s:str):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]

        return node
        
        