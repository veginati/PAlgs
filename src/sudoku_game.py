class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_list_dict = [set({}) for i in range(len(board))]
        col_list_dict = [set({}) for i in range(len(board))]
        dict_set = [[set({}) for i in range(3)] for j in range(3)]
        last_row = 0
        last_col = 0
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] != ".":
                    row_list_dict[i].add(int(board[i][j]))
                    col_list_dict[j].add(int(board[i][j]))
                    dict_set[i / 3][j / 3].add(int(board[i][j]))
                else:
                    last_row = i
                    last_col = j
        self.helper(board, row_list_dict, col_list_dict, 0, 0, last_row, last_col, dict_set)
        return board

    def helper(self, board, row_dict, col_dict, row_index, col_index, last_row, last_col, dict_set):
        # print(row_index,col_index)
        if row_index == last_row and col_index == last_col:
            return True

        for i in range(row_index, len(board)):
            for j in range(col_index, len(board)):
                if board[i][j] == ".":
                    for num in range(1, len(board) + 1):
                        if num not in row_dict[i] and num not in col_dict[j] and num not in dict_set[i / 3][j / 3]:
                            row_dict[i].add(num)
                            col_dict[j].add(num)
                            dict_set[i / 3][j / 3].add(num)
                            board[i][j] = str(num)
                            if self.helper(board, row_dict, col_dict, i, j, last_row, last_col, dict_set):
                                return True
                            else:
                                row_dict[i].remove(num)
                                col_dict[j].remove(num)
                                dict_set[i / 3][j / 3].remove(num)
                                board[i][j] = "."
                if board[i][j] == ".":
                    return False
            col_index = 0

        return False