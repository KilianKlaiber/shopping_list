import csv

# List of groceries with their type and descriptions
groceries = [
    ["Apple", "fruit", "An apple is a round, edible fruit produced by an apple tree."],
    ["Potato", "vegetable", "The potato is a starchy root vegetable native to the Americas that is consumed as a staple food in many parts of the world."],
    ["Banana", "fruit", "Bananas are elongated, edible fruits produced by various species of large herbaceous flowering plants in the genus Musa."],
    ["Carrot", "vegetable", "Carrots are root vegetables, typically orange in color, that are crisp and sweet."],
    ["Chicken breast", "protein", "Chicken breast is a lean cut of meat from the chest of a chicken, known for being a good source of protein."],
    ["Broccoli", "vegetable", "Broccoli is an edible green plant in the cabbage family, whose large flowering head and stalk are eaten as a vegetable."],
    ["Salmon", "protein", "Salmon is a fatty fish rich in omega-3 fatty acids, commonly consumed grilled, baked, or smoked."],
    ["Orange", "fruit", "Oranges are citrus fruits known for their juicy, sweet-tart flavor and high vitamin C content."],
    ["Rice", "grain", "Rice is a staple food in many cultures, consisting of small grains that are cooked and eaten as a side or main dish."],
    ["Eggs", "dairy/protein", "Eggs are laid by birds, especially chickens, and are commonly consumed for their protein-rich whites and nutrient-dense yolks."],
    ["Tomato", "fruit/vegetable", "Tomatoes are edible berries of the tomato plant, used in salads, sauces, and many cuisines around the world."],
    ["Almonds", "snack", "Almonds are the edible seeds of the almond tree, commonly eaten raw, roasted, or as a component of various dishes."],
    ["Lettuce", "vegetable", "Lettuce is a leafy green vegetable often used in salads and sandwiches."],
    ["Beef steak", "protein", "Beef steak is a slice of meat cut from the flesh of a cow, typically cooked by grilling or pan-frying."],
    ["Milk", "dairy", "Milk is a nutrient-rich liquid food produced by mammals, commonly consumed as a beverage or used in cooking."],
    ["Quinoa", "grain", "Quinoa is a seed that is cooked and eaten like a grain, known for being high in protein and gluten-free."],
    ["Yogurt", "dairy", "Yogurt is a fermented dairy product made by adding bacteria to milk, known for its creamy texture and probiotic content."],
    ["Spinach", "vegetable", "Spinach is a leafy green vegetable that is rich in iron and vitamins, often used in salads or cooked dishes."],
    ["Cheese", "dairy", "Cheese is a dairy product made from curdled milk, available in many varieties and used in cooking or eaten on its own."],
    ["Oats", "grain", "Oats are whole grains that are commonly used to make oatmeal or baked into various goods, providing a healthy source of fiber."]
]

# Define the CSV file path
csv_file_path = '/home/dci-student/Python/shopping_list/groceries_list.csv'

# Write the list to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Type", "Description"])
    writer.writerows(groceries)

