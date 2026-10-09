class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root_node

        for character in word:
            if character not in current_node.children:
                new_node = TrieNode()
                current_node.children[character] = new_node
                current_node = new_node
            else:
                current_node = current_node.children[character]

        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        current_node = self.root_node

        for character in word:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return False
        
        return current_node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root_node

        for character in prefix:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return False

        return True
        
        