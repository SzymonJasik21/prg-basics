# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True  
   def set_channel(self, new_channel_no):
      self.new_channel_no = new_channel_no
  
   def show_status(self):
      if self.is_on == True:
         print("Tv is on")
      else:
         print("Tv is off")
      