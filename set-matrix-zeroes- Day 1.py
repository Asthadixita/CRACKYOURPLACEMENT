class Solution(object):
    def setZeroes(self, matrix):
         row=len(matrix)
         col=len(matrix[0])
         r,c=[],[]


         for i in range(row):
             for j in range(col):
                 if(matrix[i][j]==0):
                    # print('indexes', i,j)
                     r.append(i)
                     c.append(j)
                    
        # print(matrix)
         for elements in r:
             for j in range(col):
                 matrix[elements][j]=0
           
         for elements in c:
             for j in range(row):
                 matrix[j][elements]=0

         return matrix
        