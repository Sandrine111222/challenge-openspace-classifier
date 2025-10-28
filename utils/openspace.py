from table import Table 
from typing import List
import random

class Openspace:

    """Here we create a class that represents the openspace with the tables, each with a specific number of seats."""

    def __init__(self, number_of_tables: int, table_capacity: int) -> None:

        """First, we initialize an Openspace with a number of tables and fixed number of seats per table.

        :param number_of_tables: The total number of tables in the openspace.
        :param table_capacity: The number of seats per table.
        :return: None. """

        self.number_of_tables: int = number_of_tables
        self.tables: list[Table] = [Table(table_capacity) for _ in range(number_of_tables)]

    def organize(self, names: list[str]) -> None:

        """Second, we randomly assign the people to the seats across the tables.

        :param names: A list of strings representing the names of people to assign to seats.
        :return: None"""
        random.shuffle(names)
            #  This will shuffle the names randomly when placing them on the seats.
        for name in names:
            assigned = False
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                # This means no seats are free.
                print(f"No more free seats for {name}.")

    def __str__(self) -> str:

        """Third, we show how the persons will be seated around the tables, readable to all.

        :return: None. """
        lines: list[str] = ["Openspace seat arrangement\n"]
        for i, table in enumerate(self.tables, start=1):
            lines.append(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                occupant = seat.occupant if not seat.free else "Free"
                lines.append(f"  Seat {j}: {occupant}")
            lines.append("")  
                  # This provides us with a blank line between tables
        return "\n".join(lines)

    def display(self) -> None:
         
         """Fourth, we display the previous string of how people are seated in a format readable to anyone.
         
         :return: None."""
         print(self.__str__())

    def store (self, filename: str)-> None:
         
        """Last, we store the seat arrangement in a text file.
         
        :return: None."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))
        print(f"Seating arrangement successfully written to '{filename}'.")
         
    
        

        