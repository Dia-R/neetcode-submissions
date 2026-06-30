class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setList = [[set() for i in range(3)] for j in range(3)]
        
        
        for row in range(9):
            numSet= set()
            numSet2= set()
            for col in range(9):
                num = board[row][col]
                num2 = board[col][row]

                if num != '.':
                    if num in numSet :
                        return False
                    numSet.add(num)
                    if num in setList[row//3][col//3]:
                        return False
                    setList[row//3][col//3].add(num)
                

                if num2 != '.':
                    if num2 in numSet2:
                        return False
                    numSet2.add(num2)

                
        
        return True


        '''
        O(n^2)
        easy solution:
        check each row, check each colum
        check each square



        '''