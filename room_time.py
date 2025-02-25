""" The room_time module contains the RoomTime class for handling the available times of a room. """
from datetime import time

# TODO: Clean up docstring testing / overall documentation.
class RoomTime:
    """
    Represents a room time based on a string format (HHMM or HMM).

    >>> RoomTime("930").room_time
    datetime.time(9, 30)

    >>> RoomTime("1230").room_time
    datetime.time(12, 30)

    >>> rt = RoomTime("2560")
    Traceback (most recent call last):
    ...
    ValueError: Invalid time format: '2560'. Expected HHMM with numeric values.

    >>> rt = RoomTime("22")
    Traceback (most recent call last):
    ...
    ValueError: Room time must be a 3 or 4-digit string representing HHMM, given time_string: '22'

    >>> RoomTime("1230") == RoomTime("1230")
    True

    >>> RoomTime("1230") == RoomTime("1240")
    False

    >>> RoomTime("1230") != RoomTime("1230")
    False

    >>> RoomTime("1230") != RoomTime("1240")
    True

    >>> RoomTime("1200") < RoomTime("1240")
    True

    >>> RoomTime("1200") < RoomTime("1200")
    False

    >>> RoomTime("1230") < RoomTime("1200")
    False

    >>> RoomTime("1230") > RoomTime("1200")
    True

    >>> RoomTime("1200") > RoomTime("1200")
    False

    >>> RoomTime("1230") > RoomTime("1400")
    False

    >>> RoomTime("1230") >= RoomTime("1200")
    True

    >>> RoomTime("1200") >= RoomTime("1200")
    True

    >>> RoomTime("1230") >= RoomTime("1300")
    False

    >>> RoomTime("1100") <= RoomTime("1200")
    True

    >>> RoomTime("1200") <= RoomTime("1200")
    True

    >>> RoomTime("1230") <= RoomTime("1200")
    False

    >>> RoomTime("1200") - RoomTime("1200")
    0

    >>> RoomTime("0000") - RoomTime("1200")
    -720

    >>> RoomTime("1200") - RoomTime("0000")
    720
    """
    def __init__(self, time_string: str) -> None:
        self.room_time: time = time_string

    def __eq__(self, other: "RoomTime") -> bool:
        return self._room_time == other.room_time

    def __neq__(self, other: "RoomTime") -> bool:
        return self._room_time != other.room_time

    def __lt__(self, other: "RoomTime") -> bool:
        return self._room_time < other.room_time

    def __gt__(self, other: "RoomTime") -> bool:
        return self._room_time > other.room_time

    def __le__(self, other: "RoomTime") -> bool:
        return self._room_time <= other.room_time

    def __ge__(self, other: "RoomTime") -> bool:
        return self._room_time >= other.room_time

    def __sub__(self, other: "RoomTime") -> int:
        return (60 * (self._room_time.hour - other._room_time.hour)
                 + self._room_time.minute - other.room_time.minute)

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
