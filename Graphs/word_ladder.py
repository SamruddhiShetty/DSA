#run time= len(wordList)*Len(word)*26*Len(word)--while comparison

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        words=set(wordList)
        queue=[]
        depth, level=0, 0
        queue.append(beginWord)
        while queue:
            depth+=1
            level+=len(queue)
            while level:
                word=queue.pop(0)
                for i in range(len(word)):
                    for j in range(97, 123):
                        dummy=word[:i]+chr(j)+word[i+1:]
                        if dummy==endWord:
                            return depth+1
                        if dummy in words:
                            queue.append(dummy)
                            words.remove(dummy)
                level-=1
        return 0
                        
                    
        
