
"""
Example Exception

class (Exception):
    ""Raised when ""

    def __init__(self, message=""):
        super().__init__(self.message)

    def __str__(self):
        return self.message
"""


class TagAlreadyExists(Exception):
    """Raised when the inputted tag already exists."""

    def __init__(self, message="The inputted tag already exists."):
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidTag(Exception):
    """Raised when the inputted tag does not exist."""

    def __init__(self, message="The inputted tag does not exist."):
        super().__init__(self.message)

    def __str__(self):
        return self.message


class MemberAlreadyStaff(Exception):
    """Raised when the inputted user is already a staff member."""

    def __init__(self, message="The inputted user is already a staff member."):
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidStaff(Exception):
    """Raised when the inputted member does not exist."""

    def __init__(self, message="The inputted member does not exist."):
        super().__init__(self.message)

    def __str__(self):
        return self.message
