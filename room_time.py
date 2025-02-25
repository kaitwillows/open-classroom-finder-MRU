""" The room_time module contains the RoomTime class for handling the available times of a room. """
from datetime import time

class RoomTime:
    """
    Represents a room time based on a string format (HHMM or HMM).

    >>> rt = RoomTime("930")
    >>> rt.room_time
    datetime.time(9, 30)

    >>> rt = RoomTime("1230")
    >>> rt.room_time
    datetime.time(12, 30)

    >>> rt = RoomTime("2560")
    Traceback (most recent call last):
    ...
    ValueError: Invalid time format: '2560'. Expected HHMM with numeric values.

    >>> rt = RoomTime("22")
    Traceback (most recent call last):
    ...
    ValueError: Room time must be a 3 or 4-digit string representing HHMM, given time_string: '22'
    """
    def __init__(self, time_string: str) -> None:
        self.room_time: time = time_string

    def __gt__(self, other: "RoomTime") -> bool:
        # TODO: Implement this and remaining comparisons.
        return True

    @property
    def room_time(self) -> time:
        return self._room_time

    @room_time.setter
    def room_time(self, time_string: str) -> None:
        TIME_LENGTH: int = len(time_string)
        minute_index: int = None

        if TIME_LENGTH == 3:
            minute_index = 1
        elif TIME_LENGTH == 4:
            minute_index = 2
        else:
            raise ValueError(
                f"Room time must be a 3 or 4-digit string representing HHMM, given time_string: '{time_string}'")

        try:
            self._room_time = time(
                hour=int(time_string[0:minute_index]),
                minute=int(time_string[minute_index:TIME_LENGTH])
            )
        except ValueError as e:
            raise ValueError(f"Invalid time format: '{time_string}'. Expected HHMM with numeric values.") from e

if __name__ == "__main__":
    import doctest
    doctest.testmod()
