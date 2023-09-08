class Square:
    def __init__(self, row, col, mark=""):
        self.mark = mark
        self.col = col
        self.row = row

    def has_mark(self):
        return self.mark != ""
    
    def isempty(self):
        return not self.has_mark()


