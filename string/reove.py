class Solution(object):
    def removeComments(self, source):
        result = []
        in_block = False
        newline = ""
        
        for line in source:
            i = 0
            while i < len(line):
                
                # Start of block comment
                if not in_block and i+1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2
                
                # End of block comment
                elif in_block and i+1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2
                
                # Single line comment
                elif not in_block and i+1 < len(line) and line[i:i+2] == "//":
                    break
                
                # Normal character
                elif not in_block:
                    newline += line[i]
                    i += 1
                
                else:
                    i += 1
            
            if not in_block and newline:
                result.append(newline)
                newline = ""
        
        return result
