class Snake():
    def __init__(self, screen_size , row):
        self.size =  (( screen_size - 1 )) // row - 1 
        self.color = (0,255,0)
        self.body_x = [ 270  ]
        self.body_y = [ 270 ]


    def move(self, x, y, apple):

        if self.body_x[0] == 1:
            self.body_x[0] = 0

        if self.body_y[0] == 1:
            self.body_y[0] = 0

        x_pos = self.body_x[0] + x * ( ( self.size ) + 1 )
        y_pos = self.body_y[0] + y * ( ( self.size ) + 1 ) 

        if len(self.body_x) > 1:
            if x_pos == self.body_x[1] and y_pos == self.body_y[1]:
                    if self.body_x[0] - self.body_x[1] > 0:
                        x = 1
                    elif self.body_x[0] - self.body_x[1] < 0:
                        x = -1
                    if self.body_y[0] - self.body_y[1] > 0:
                        y = 1
                    elif self.body_y[0] - self.body_y[1] < 0:
                        y = -1
        
        x_pos = self.body_x[0] + x * ( ( self.size ) + 1 )
        y_pos = self.body_y[0] + y * ( ( self.size ) + 1 ) 
        
        self.body_x = [x_pos]  + self.body_x
        self.body_y = [y_pos] + self.body_y
        
        if apple:
            self.body_x.pop()
            self.body_y.pop()


        if self.body_x[0] == 0:
            self.body_x[0] = 1

        if self.body_y[0] == 0:
            self.body_y[0] = 1
        
