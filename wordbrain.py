import sys
import copy
import enchant

# txt = '''
# PFL
# IYY
# GST
# '''  

# txt = '''
# DUUQWP
# MMCKKK
# BZXQLL
# '''

txt = '''
----
-nrd
hoco
rtre
'''

Dict = enchant.Dict("en_US")

class Cell():
   def __init__(self, letter):
      self.letter = letter
      self.visited = False      
   def __str__(self):
      return '(%s,%s)' % (self.letter, self.visited)

class Row():
   def __init__(self, list):
      self.row = list      
   def __getitem__(self, i):
      if i < 0:
         raise IndexError
      return self.row[i]  
   def __len__(self):
      return len(self.row)
      
class Grid():
   def __init__(self, txt):      
      self.rows = []
      for line in txt.split('\n'):
         if line:
            l = Row([Cell(x) for x in line])
            self.rows.append(l)
      self.width = len(self.rows[0])
      self.height = len(self.rows)
            
   def __getitem__(self, i):
      if i < 0:
         raise IndexError
      return self.rows[i]
      
   def __str__(self):
      out = ''
      for line in self.rows:
         for x in line:
            out = out + str(x)
         out = out + '\n'
      return out
            
def solve(grid, part, row, col, wordlen, results):
   #print part, row, col, wordlen
   grid = copy.deepcopy(grid)
   try:
      cell = grid[row][col]
   except IndexError:
      return
   if cell.letter == '-':
      return
   if cell.visited:
      return      
   cell.visited = True
   part = part + grid[row][col].letter
   if len(part) == wordlen:
      word = ''.join(part)
      if Dict.check(word) and word not in results:
         print word
         results[word] = 1
   elif len(part) < wordlen:
      
      #  r-1,c-1 r-1,c  r-1,c+1
      #  r,  c-1    X   r,c+1
      #  r+1,c-1 r+1,c  r+1,c+1
      
      solve(grid, part, row-1, col-1, wordlen, results)
      solve(grid, part, row-1, col, wordlen, results)
      solve(grid, part, row-1, col+1, wordlen, results)      
      solve(grid, part, row, col-1, wordlen, results)
      solve(grid, part, row, col+1, wordlen, results)      
      solve(grid, part, row+1, col-1, wordlen, results)
      solve(grid, part, row+1, col, wordlen, results)
      solve(grid, part, row+1, col+1, wordlen, results)
      
def main():
   wordlen = int(sys.argv[1])
   grid = Grid(txt)
   results = {}
   for r in range(grid.height):
      for c in range(grid.width):
         g = copy.deepcopy(grid)
         solve(g, '', r, c, wordlen, results)
         #return

if __name__ == '__main__':
   main()