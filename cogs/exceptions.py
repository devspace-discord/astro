
"""
Example Exception

class (Exception):
    ""Raised when ""

    def __init__(self, message=""):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
"""


class TagAlreadyExists(Exception):
    """Raised when the inputted tag already exists."""

    def __init__(self, message="The inputted tag already exists."):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class InvalidTag(Exception):
    """Raised when the inputted tag does not exist."""

    def __init__(self, message="The inputted tag does not exist."):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class MemberAlreadyStaff(Exception):
    """Raised when the inputted user is already a staff member."""

    def __init__(self, message="The inputted user is already a staff member."):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class InvalidStaff(Exception):
    """Raised when the inputted member does not exist."""

    def __init__(self, message="The inputted member does not exist."):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class InsufficientPermissions(Exception):
    """Raised when a user tries to execute a command they do not have permissions for"""

    def __init__(self, message="A user tried to execute a command that they do not have permissions for"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class ReactionRoleAlreadyExists(Exception):
    ""Raised when the inputted reaction role already exists""

    def __init__(self, message="The inputted reaction role already exists"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
