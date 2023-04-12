#!/usr/bin/python3
"""MyInt rebel module"""


class MyInt(int):
    """MyInt is a rebel"""

    def __eq__(self, other):
        """Equal operator"""

        return (int(self) != other)

    def __ne__(self, other):
        """Not equal operator"""

        return (int(self) == other)
