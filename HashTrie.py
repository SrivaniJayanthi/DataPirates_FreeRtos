class TrieNode:
    def __init__(self):
        self.children = {}  # Hash table to store child nodes
        self.is_end_of_word = False


class HashTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print("Search unsuccessful")
                return False
            node = node.children[char]
        if node.is_end_of_word:
            print("Searched word successfully")
            return True
        else:
            print("Search unsuccessful")
            return False

    def delete(self, word):
        def _delete_helper(node, word, index):
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    return len(node.children) == 0
                return False

            char = word[index]
            if char not in node.children:
                return False

            should_delete = _delete_helper(node.children[char], word, index + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0

            return False

        deleted = _delete_helper(self.root, word, 0)
        if deleted:
            print("Deleted word:", word)

    def print_words(self):
        print("Words in the hash Trie are:")
        words = []
        self._print_words_helper(self.root, "", words)
        print(words)

    def _print_words_helper(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._print_words_helper(child, prefix + char, words)


# Example usage:
hash_trie = HashTrie()
hash_trie.insert("hello")
hash_trie.insert("hi")
hash_trie.insert("bye")

hash_trie.search("hello")  # Output: Searched word successfully
hash_trie.search("goodbye")  # Output: Search unsuccessful

hash_trie.delete("hello")  # Output: Deleted word: hello
hash_trie.search("hello")  # Output: Search unsuccessful

hash_trie.print_words()
