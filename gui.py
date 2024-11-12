import PySimpleGUI as psg
import shopping
import articial_intelligence

from screeninfo import get_monitors

# Get the width of the primary monitor (or specify a different monitor if needed)
primary_monitor = get_monitors()[
    0
]  # You can change the index to select a different monitor
monitor_width = primary_monitor.width
monitor_height = primary_monitor.height

# Define the layout of the window

headings = ["Grocery", "Name", "Brand", "Price / Kg", "Amount [Kg]", "Price [€]"]

# Define the layout with a styled table and the total price display right below it
layout = [
    [
        psg.Table(
            values=[],  # Initially empty table
            headings=headings,
            auto_size_columns=False,
            display_row_numbers=False,
            justification="center",
            key="shopping_table",  # Key to update the table
            num_rows=10,  # Set the number of visible rows
            row_height=25,
            col_widths=[15 for _ in headings],  # Set each column to be 15 units wide
            font=("Arial", 12),  # Arial font for table content
            text_color="white",  # Text color for content
            background_color="black",  # Background color for content rows
            header_text_color="white",  # White text for headings
            header_background_color="black",  # Dark background color for headings
        )
    ],
    # Use a column to align the total price on the right side of the window, just under the table
    [
        psg.Column(
            [
                [
                    psg.Text(
                        "Total Price:",
                        font=("Arial", 12, "bold"),
                        background_color="black",
                    )
                ],
                [
                    psg.Text(
                        "",
                        key="total_price_text",
                        font=("Arial", 12),
                        background_color="black",
                    )
                ],
            ],
            justification="center",
            background_color="black",
        )
    ],  # Right justify the column contents
    
    # Empty row to create space before the buttons
    [psg.Text("")],  # This row can be used to add space between elements
    # Buttons
    [
        psg.Button("Add grocery", font=("Arial", 12)),
        psg.Button("Delete grocery", font=("Arial", 12)),
        psg.Button("Exit", font=("Arial", 12)),
    ],
    
     # Empty rows to create space before the buttons
    [psg.Text("")],
    [psg.Text("")],
    
    [psg.Button("Save and send shopping list", font=("Arial", 12))],
    
]

# Create the window with the screen width
window = psg.Window(
    "Create Your shopping list:",
    layout,
    size=(monitor_width, monitor_height),  # Set height as needed
    element_justification="center",
    finalize=True,
)

shopping_list = []
total_price = 0

# Event loop to update the window
while True:
    # Check for events like button clicks
    event, values = window.read(timeout=100)  # Timeout in milliseconds

    print("event:", event)
    # event: Add grocery

    if event == "Add grocery":
        list = shopping.create_shopping_list()
        if list != None:
            shopping_list.extend(list)
            total_price = 0
            for item in shopping_list:
                total_price += item[5]

            total_price = round(total_price, 2)
    
    if event == "Delete grocery":
        grocery = psg.popup_get_text("What do you want to delete?", title=" Delete grocery")
        
        groceries = []
        
        for item in shopping_list:
            groceries.append(item[0])
        
        if grocery in groceries:
            index = groceries.index(grocery)
            shopping_list.pop(index)
        else:
            phrase, guess =  articial_intelligence.guess_grocery(groceries, grocery)
            question = psg.popup_yes_no(phrase)
            
            if question == "Yes":
                if guess in groceries:
                    index = groceries.index(guess)
                    shopping_list.pop(index)
        
        total_price = 0
        for item in shopping_list:
            total_price += item[5]

        total_price = round(total_price, 2)
        
        print("grocery", grocery)
        print("shopping list: ", shopping_list)

    #if shopping_list != []:
        # Update the window with the new data
    window["shopping_table"].update(shopping_list)

    #if total_price != 0:
        # Update the total price display
    window["total_price_text"].update(f"{total_price} €")  # Format as currency
    
    # If the user clicks save and send
    
    if event == "Save and send shopping list":
        # Writing to a text file with formatted columns
        
        
        shopping_name = psg.popup_get_text("Name your shopping list", title=" Name")
        if shopping_name == None:
            shopping_name = "Shopping List"
        
        with open(f"lists/{shopping_name}.txt", "w") as file:
            shopping_list.insert(0,headings)
            for row in shopping_list:
                file.write("{:<10} {:<15} {:<25} {:<15} {:<15} {:<15} \n".format(*row))  # Left-align with specific widths
            file.write(f"\nTotal Price: {total_price}")
        
        # Enter code for sending the text file as an email to a recipient.
        
        break
    
    # If the user closes the window or clicks "Exit", exit the loop
    if event == psg.WINDOW_CLOSED or event == "Exit":
        break


# Close the window when the loop is done
window.close()
