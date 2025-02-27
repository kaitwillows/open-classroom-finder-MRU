""" The room_time module contains the RoomTime class for handling the available times of a room. """
from datetime import time

class RoomTime:
    """
    A RoomTime for handling time comparisons, a bit silly but nice to have abstraction on functionality instead of
    purely relying on the time class.

    Operators:
        __eq__, __neq__, __lt__, __gt__, __le__, __ge__, __sub__

    Properties:
        room_time
    """
    def __init__(self, time_string: str) -> None:
        """Initialize a time for a room.

        Arguments:
            time_string (str): The HHMM or HMM of the time.
        """
        self.room_time: time = time_string

    def __eq__(self, other: "RoomTime") -> bool:
        """If the two room_time properties are equivalent.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if both room_time properties are equivalent.

        Examples:
            >>> RoomTime("1230") == RoomTime("1230")
            True

            >>> RoomTime("1230") == RoomTime("1240")
            False
        """
        return self._room_time == other.room_time

    def __neq__(self, other: "RoomTime") -> bool:
        """If the two room_time properties are not equivalent.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if both room_time properties are not equivalent.
        
        Examples:
            >>> RoomTime("1230") != RoomTime("1230")
            False

            >>> RoomTime("1230") != RoomTime("1240")
            True
        """
        return not self._room_time == other.room_time

    def __lt__(self, other: "RoomTime") -> bool:
        """If the left hand room comes before the right hand.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if the left hand room comes before the right hand.
        
        Examples:
            >>> RoomTime("1200") < RoomTime("1240")
            True

            >>> RoomTime("1200") < RoomTime("1200")
            False

            >>> RoomTime("1230") < RoomTime("1200")
            False
        """
        return self._room_time < other.room_time

    def __gt__(self, other: "RoomTime") -> bool:
        """If the left hand room comes after the right hand.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if the left hand room comes after the right hand.
        
        Examples:
            >>> RoomTime("1230") > RoomTime("1200")
            True

            >>> RoomTime("1200") > RoomTime("1200")
            False

            >>> RoomTime("1230") > RoomTime("1400")
            False
        """
        return self._room_time > other.room_time

    def __le__(self, other: "RoomTime") -> bool:
        """If the left hand room comes before or at the same time as the right hand.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if the left hand room comes before or at the same time as the right hand.
        
        Examples:
            >>> RoomTime("1100") <= RoomTime("1200")
            True

            >>> RoomTime("1200") <= RoomTime("1200")
            True

            >>> RoomTime("1230") <= RoomTime("1200")
            False
        """
        return self._room_time <= other.room_time

    def __ge__(self, other: "RoomTime") -> bool:
        """If the left hand room comes after or at the same time as the right hand.

        Arguments:
            other (RoomTime): The compared RoomTime.

        Returns:
            bool: True if the left hand room comes after or at the same time as the right hand.
        
        Examples:
            >>> RoomTime("1230") >= RoomTime("1200")
            True

            >>> RoomTime("1200") >= RoomTime("1200")
            True

            >>> RoomTime("1230") >= RoomTime("1300")
            False
        """
        return self._room_time >= other.room_time

    def __sub__(self, other: "RoomTime") -> int:
        """Subtract the right hand operator from the left hand.
        Note: It might not be desirable to do it this way, for example, maybe another time should be returned instead
        of the minutes difference. However, if we were to create another RoomTime, it wouldn't make sense to have
        negative values.

        Arguments:
            other (RoomTime): The RoomTime to be subtracted from the caller.

        Returns:
            int: The difference in minutes.

        Examples:
            >>> RoomTime("1200") - RoomTime("1200")
            0

            >>> RoomTime("0000") - RoomTime("1200")
            -720

            >>> RoomTime("1200") - RoomTime("0000")
            720
        """
        return (60 * (self._room_time.hour - other._room_time.hour)
                 + self._room_time.minute - other.room_time.minute)

    @property
    def room_time(self) -> time:
        """Getter for self._room_time.

        Returns:
            time: The time object of this room_time.
        """
        return self._room_time

    @room_time.setter
    def room_time(self, time_string: str) -> None:
        """Setter for self._room_time.

        Arguments:
            time_string (str): The HHMM or HMM string for the room time.

        Raises:
            ValueError: If the time is not a 3 or 4 digit string.
            ValueError: If an invalid value such as a character is passed.

        Examples:
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
        """
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
