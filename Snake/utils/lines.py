class Lines():  
    def __init__(self, screen_size, row):
        self.row = row
        self.screen_size = screen_size
        self.row_spacing = self.screen_size // self.row

        self.color = (255,255,255) 

