class Rectangle:
 def __init__(self, width, height):
   self.width = width
   self.height = height

#set functions
 def set_width(self, width):
    self.width = width
   
 def set_height(self, height):
    self.height = height
#get functions
 def get_area(self):
   return self.width * self.height
 
 def get_perimeter(self):
   return 2 * self.width + 2 * self.height
 
 def get_diagonal(self):
   return (self.width ** 2 + self.height ** 2) ** .5

 def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for a picture"
    else:
      return ("*" * self.width + "\n") * self.height

 def get_amount_inside(self, squ):
   return self.width // squ.width * self.height // squ.height

 def __str__(self):
   return ('Rectangle(width='+ str(self.width)+', height='+str(self.height)+'')
   
#using Rectangle class to inherit the get functions into square class
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
#set function
  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return('Square(side='+ str(self.width)+')')

  def set_width(self,side):
    self.width = side
  
  def set_height(self,side):
    self.height = side

  