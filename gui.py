
import PySimpleGUI as psg
import shopping



from screeninfo import get_monitors

# Get the width of the primary monitor (or specify a different monitor if needed)
primary_monitor = get_monitors()[0]  # You can change the index to select a different monitor
monitor_width = primary_monitor.width
monitor_height = primary_monitor.height

# Define the layout of the window

headings = ["Grocery", "Name", "Brand", "Price/Kg"]

layout = [
    [psg.Column([[psg.Text(heading, size=(15, 1), justification="center")
                 for heading in headings]], 
                element_justification="center", expand_x=True)],
    [psg.Column([[psg.Text("Live Data:", key="data_text", size=(20, 1), justification="center")]], 
                element_justification="center", expand_x=True)],
    [psg.Column([[psg.Button("Add grocery"), psg.Button("Exit")]], 
                element_justification="center", expand_x=True)],
    
]

# Create the window with the screen width
window = psg.Window(
    "Create Your shopping list:", 
    layout, 
    size=(monitor_width, monitor_height),  # Set height as needed
    finalize=True
)

data = ""

# Event loop to update the window
while True:
    # Check for events like button clicks
    event, values = window.read(timeout=100)  # Timeout in milliseconds
    
    print("event:", event)
    # event: Add grocery

    if event == "Add grocery":
        data = shopping.create_shopping_list()
        
    # If the user closes the window or clicks "Exit", exit the loop
    if event == psg.WINDOW_CLOSED or event == "Exit":
        break

    # Update the window with the new data
    window["data_text"].update(f"Live Data: {data}")

# Close the window when the loop is done
window.close()

print(data)
