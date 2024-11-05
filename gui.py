import PySimpleGUI as psg
import database
import shopping

# -create pop up window:
""" 
layout = [[psg.Text(
    text="Create your Shopping List",
    font=('Calibri', 20),
    expand_x=True,
    justification = 'center'
           )]]

window = psg.Window("Create your Shopping List", layout, size=(500,250))

while True:
    event, values = window.read()
    
    print(event, values)
    
    if event in (None, 'Exit'):
        break

window.close() """


# Creat text element:

""" grocery = psg.popup_get_text('What do you want?', title=' Buy grocery')
print('The product is: ',  grocery)

amount = psg.popup_get_text('How much do you want? (Kg)', title=f'Amount of {grocery}')
print(f'The amount is. {amount} Kg')

grocery = "Papaya"

ch = psg.popup_yes_no(f"We do not have {grocery}.\n Would you like something else?", title= 'Alternative?')


 """
 
 # Text and input Layout
 
""" layout = [
    [psg.Text('Granny Smith'), psg.OK()],
    [psg.Text('Forländer'), psg.OK()],
    [psg.Text('Timtin'), psg.OK()],
    [psg.Exit()]
 ]
 
window = psg.Window('Shopping List', layout)
 
while True:
     event = window.read()
     print(event)
     
     if event == psg.WIN_CLOSED or event in ['OK', 'OK0', 'OK1']:
         break

window.close() """


import PySimpleGUI as sg


grocery_list = shopping.get_grocery('Apple')

# Sample data for the table
data = [
    list(grocery_list[0]),
    list(grocery_list[1]),
    list(grocery_list[2])
]

# Table headings
headings = ["Name", "Brand", "Price/Kg"]

# Define the layout
layout = [[sg.Text(heading, size=(15, 1), justification='center') for heading in headings]]  # Header row

for i, row in enumerate(data):
    row_layout = [
        sg.Text(row[0], size=(15, 1), justification='left'),
        sg.Text(row[1], size=(15, 1), justification='left'),
        sg.Text(row[2], size=(15, 1), justification='centre'),
        sg.Button("OK", key=f"OK_{i}")  # Unique key for each button
    ]
    layout.append(row_layout)

# Create the window
window = sg.Window("Chose your grocery", layout)

# Event loop
while True:
    event, values = window.read()
    print(event)
    if event == sg.WINDOW_CLOSED or event in ["OK_0", "OK_1", "OK_2"]:
        break

window.close()
