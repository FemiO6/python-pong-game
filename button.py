class Button():
   #Button class allowing for the initialisation of button type properties
    def __init__(self, image, pos, text_input, font, base_colour, secondary_colour):
        self.image = image
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.font = font
        self.base_colour = base_colour
        self.secondary_colour = secondary_colour
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_colour)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.text_rect = self.text.get_rect(center=(self.pos_x, self.pos_y))

    #creating a update method to display image and text to screen
    def update(self, screen):
        if self.image is not None:
           screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        
    #Checks for inputs (if we have pressed the button)
    def Check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
        #change colour method to check if user mouse is above button allwoing for it to change to secondary colour
    def Colourchange(self,position):        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.secondary_colour)
        else:
            self.text = self.font.render(self.text_input, True, self.base_colour)