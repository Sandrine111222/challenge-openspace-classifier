

# Create an Openspace
openspace = Openspace(number_of_tables=6, table_capacity=4)

# List of names
names = ["Aleksei","Amine","Anna","Astha","Brigitta",
         "Bryan","Ena","Esra","Faranges","Frédéric",
         "Hamideh","Héloïse","Imran","Intan K.",
         "Jens","Kristin","Michiel","Nancy","Pierrick",
         "Sandrine","Tim","Viktor","Welederufeal","Živile"]

# Organize seating
openspace.organize(names)

# Display seating
openspace.display()

# Store to a file
openspace.store("output.txt") 





    

