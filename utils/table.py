# table.py
from typing import Optional, List


class Seat:
    """Represents a single seat, which can be free or occupied."""

    def __init__(self, free: bool = True, occupant: Optional[str] = None) -> None:
        """
        Initialize a Seat.

        :param free: Whether the seat is free. Defaults to True.
        :param occupant: Name of the occupant. Defaults to None.
        """
        self.free: bool = free
        self.occupant: Optional[str] = occupant

    def set_occupant(self, name: str) -> None:
        """Assign a person to the seat if it is free."""
        if self.free:
            self.occupant = name
            self.free = False
        else:
            print(f"Seat already occupied by {self.occupant}.")

    def remove_occupant(self) -> Optional[str]:
        """Remove the occupant and return their name, or None if free."""
        if not self.free:
            previous_occupant = self.occupant
            self.occupant = None
            self.free = True
            return previous_occupant
        return None

    def __str__(self) -> str:
        return self.occupant if not self.free else "Free"


class Table:
    """Represents a table with multiple seats."""

    def __init__(self, capacity: int) -> None:
        """
        Initialize a Table.

        :param capacity: Number of seats at the table.
        """
        self.capacity: int = capacity
        self.seats: List[Seat] = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        """Check if there is at least one free seat."""
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """Assign a person to the first free seat."""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def __str__(self) -> str:
        return "\n".join(f"  Seat {i+1}: {str(seat)}" for i, seat in enumerate(self.seats))



