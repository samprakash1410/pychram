class Button:
  def click(self):
    return "Button clicked so many times"

class Checkbox:
  def click(self):
    return "Checkbox toggled for web pages"

def handle_click(ui_element):
  print(ui_element.click())

# Create UI elements
button = Button()
checkbox = Checkbox()

# Handle clicks on different elements
handle_click(button)    
handle_click(checkbox)  
