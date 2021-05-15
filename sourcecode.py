def find_next_empty(puzzle):
  #It will find the next empty row ,col on the Puzzle that's not filled yet ---> rep with -1
  # return row , col tuple or ( (None , None ) if there's None)
  #We are using 0-8 for our indices
  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1:
        return r,c 
  
  return None , None #If no spaces in the puzzle are empty(-1)


def is_valid( puzzle, guess, row, col):
  # Figure out whether the guess at the row/col of the puzzle is valid guess then return True otherwise return False.

  #Let's Start with the Row 
  row_vals = puzzle[row]
  if guess in row_vals:
    return False
  
  # Now it is the turn of the column 
  # Column is a bit more trickier
  #what we can do is to create a new list 

  #col_vals = []
  #for i in range(9):
   # col_vals.append(puzzle[i][col])
    # OR the other method
  col_vals = [puzzle[i][col] for i in range(9)]
  if guess in col_vals:
    return False

  # And Now It's the Turn for Square 
  #This is also a lit bit Tricky , but we want to get 3x3 matrix and it should iterate over 3 values of row/compile.
  row_start = (row // 3 ) * 3
  col_start = (col // 3 ) * 3

  for r in range(row_start , row_start + 3 ):
    for c in range(col_start , col_start + 3 ):
      if puzzle[r][c] == guess:
        return False


  #If we get here with all thses checks 
  return True



def solve_sudoku(puzzle):
  # We will be solving it using Backtracking
  #Our puzzle is a list of lists , where each list represents a row in our sudoku puzzle.
  #Mutate puzzle to be the solution (If solution Exists)

  
  #Step 1 : Choose Somewhere on the Puzzle to make a Guess 
  row , col = find_next_empty(puzzle)
  #Step 1.1 : If there are nowhwre left , then we're done because we are only allowed valid inputs
  if row is None:
    return True

  #Step 2 : If there is a place to put a number, then make a guess between 1 to 9 
  for guess in range(1, 10):
    #Step 3 : Check if this is a valid 
    if is_valid(puzzle, guess, row, col):
      #Step 3.1 : If this is valid , then place that guess on the puzzle!!!
      puzzle[row][col] = guess
      #Now Recursion using this Puzzle!

      #Step 4 : Recursively call our function
      if solve_sudoku(puzzle):
        return True

    #Step 5 : If it's not Valid OR our guess does not solve the Puzzle , then we need , then we need to backtrack and try a new number
    puzzle[row][col] = -1 #Reset the Guess 

  #Step 6 : If none of the number we tried works out , Then this puzzle is UNSOLVABLE!!!
  return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)


