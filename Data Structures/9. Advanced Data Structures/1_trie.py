class Trie:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1
    

    def add_word(self, word):
        # Start checking from root(*) by initializing the current_node as root.
        current_node = self
        # We need to put every character of the word in trie.
        for char in word:
            # Check if the current character is there in children of the current node.
            found_in_children = False
            for child_node in current_node.children:
                # If the current character is there in children of the current node,
                # increase count and set the child_node as current node
                if(child_node.char == char):
                    child_node.counter += 1
                    # Sort the children on the basis of count, such that words with greater frequency are suggested first.
                    current_node.children.sort(key = lambda x: x.counter, reverse=True)
                    current_node = child_node
                    found_in_children = True
                    break
            
            # If the current character is NOT there in children of the current node, 
            # create a new_child_node, add this to the children of the current node and set this node as the current.
            if (not found_in_children):
                new_child_node = Trie(char)
                current_node.children.append(new_child_node)
                current_node = new_child_node
        
        # If all the characters of the words are done, mark it as finished word.
        current_node.word_finished = True
    

    def search_word(self, word):
        current_node = self
        for char in word:
            found_in_children = False
            for child_node in current_node.children:
                if(child_node.char == char):
                    current_node = child_node
                    found_in_children = True
                    break
            
            if (not found_in_children and word != "*"):
                print("Word = {} : NOT Found. Spelling  Mistake".format(word))
                break
        
        if(found_in_children):
            print("Word = {} : Found {} times.".format(word, current_node.counter))

        return (found_in_children, current_node)
    

    def word_suggest(self, word):
        found, node = self.search_word(word)
        if(found or word == "*"):
            if(word == "*"):
                word = ""
                
            suggestions = self.word_suggest_util(node, word, [])
            print("Suggestions are:")
            for w in suggestions:
                print(w, end=" ")
            print("\n")
        
    

    def word_suggest_util(self, node, word, word_list):
        if node.word_finished:
            word_list.append(word)
        
        for child_node in node.children:
            self.word_suggest_util(child_node, word+child_node.char, word_list)
        
        return word_list



trie = Trie("*")
trie.add_word("hackathon")
trie.add_word("hack")
trie.add_word("ham")
trie.add_word("hamilton")
trie.add_word("hammer")

trie.word_suggest("hac")
trie.word_suggest("hack")
trie.word_suggest("hackathon")
trie.word_suggest("ha")
trie.word_suggest("hammer")
trie.search_word("hamlet")
