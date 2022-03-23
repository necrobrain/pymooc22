def row_correct(sudoku_matrix: list, row_nr):
    
    row_list = []
    
    for i in sudoku_matrix[row_nr]:
        row_list.append(i)
        if row_list.count(i) > 1 and i != 0:
            return False
    
    return True

def column_correct(sudoku_matrix: list, column_nr: int):
    
    column = []
    
    for row in sudoku_matrix:
        column.append(row[column_nr])
        if column.count(row[column_nr]) > 1 and row[column_nr] != 0:
            return False 
    
    return True

def block_correct(sudoku: list, row_no: int, column_nr: int):
    
    i = 0
    block = []
    
    while i < 3:
        j = 0
        while j < 3:
            block.append(sudoku[row_no+j][column_nr+i])
            j += 1
        i += 1
    
    for number in block:
        if block.count(number) > 1 and number != 0:
            return False
    
    return True

def sudoku_grid_correct(sudoku: list):
    
    i = 0
        
    for row in sudoku:
        check = row_correct(sudoku, i)
        if not check:
            return False
        i += 1
    
    i = 0
    
    for row in sudoku:
        check = column_correct(sudoku, i)
        if not check:
            return False
        i += 1
        
    blocks = [
        [0,0], [0,3], [3,0], 
        [3,3], [3,6], [0,6],
        [6,3], [6,6], [6,0]
        ]
    
    for block in blocks:
        x, y = block
        check = block_correct(sudoku, x, y)
        if not check:
            return False
    
    return True


if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku))