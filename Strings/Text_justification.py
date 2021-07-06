#https://leetcode.com/problems/text-justification/submissions/  -- refer the problem from here

from math import ceil

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        current_index=0 #current word of the array words- index
        result=[] #final result
        
        while current_index<len(words):
            line_length=0 #current_line has certain number of words, this is the total length of all the characters
            current_line=[] #the number of words that can be included sticking to maxWidth
            
            #pushing the new words but taking care that it wont exceed the maxWidth 
            while current_index<len(words) and len(words[current_index])+len(current_line)+line_length-1 <maxWidth:
                current_line.append(words[current_index])
                line_length+=len(words[current_index])
                current_index+=1
                
            #finding the right number of spacing between each words in a line
            
            #this is the minimum number of space that has to be there between each word
            line_spaces=len(current_line)-1
            
            #if we have used all the word in the array words then we stick to the minimum spacing
            #else we subtract the total number of characters from the maxWidth and give the required number of space
            word_spacing=line_spaces if current_index==len(words) else maxWidth-line_length
            
            
            #time to finalise the end result' lines one by one
            line=""
            for word in current_line:
                line+=word
                if line_spaces>0:
                    spaces=ceil(word_spacing/line_spaces)
                    line_spaces-=1
                    word_spacing=word_spacing-spaces
                    line+=" "*spaces
            
            #if any required then add spaces in the end as well
            line+=" "*(maxWidth-len(line))
            
            result.append(line)
            
        return result
            
