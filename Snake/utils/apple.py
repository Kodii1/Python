class Apple():
    def __init__(self, screen_size , row ):
        self.color = (225,0,0)
        self.screen_size = screen_size
        self.row = row
        self.size = (( screen_size - 1 )) // row - 1 
        self.map_up_left_corner = [ 0, 0 ]
        self.place = []
