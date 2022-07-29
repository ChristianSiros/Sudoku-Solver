class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0
        self.candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.num_candidates = len(self.candidates)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def get_candidates(self):
        return self.candidates
    
    def get_num_candidates(self):
        return self.num_candidates