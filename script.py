class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        visited = set()     
        
        def findIfExists(r,c,i):
            if i == len(word):  
                return True
            if r < 0 or r >= R or c < 0 or c >= C or word[i] != board[r][c] or (r,c) in visited:  
                return False

            visited.add((r,c)) 

            temp = findIfExists(r-1,c,i+1) or findIfExists(r+1,c,i+1) or findIfExists(r,c+1,i+1) or findIfExists(r,c-1,i+1) 

            visited.remove((r,c)) 
            
            return temp

        for r in range(R):
            for c in range(C):
                if findIfExists(r,c,0):
                    return True

        return False
