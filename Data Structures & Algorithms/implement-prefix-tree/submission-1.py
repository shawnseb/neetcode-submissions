class PrefixTree:

    def __init__(self):
        self.start = TrieNode('1')
        

    def insert(self, word: str) -> None:
        index = 0
        current = self.start
        answer = 0
        while index < len(word):
            answer = -1
            char = word[index]
            if char not in current.children:
                break;
            
            current = current.children[char]
            
            index = index + 1
            
        
        while index < len(word):
            char = word[index]
            current.children[char] = TrieNode(char)
            current = current.children[char]
            index = index + 1
        current.end = True

                

            

        


    def search(self, word: str) -> bool:
        current = self.start
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        index = 0
        current = self.start
        answer = 0
        while index < len(prefix):
            answer = -1
            char = prefix[index]
            if char not in current.children:
                return False
            
            current = current.children[char]
            
            if index == len(prefix) -1:
                return True
            index = index + 1
        return False
        
class TrieNode:
    def __init__(self, letter: char):
        self.children={}
        self.letter = letter
        self.end = False
