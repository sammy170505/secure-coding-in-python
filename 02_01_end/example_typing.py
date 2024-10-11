class User:
    """system user"""

    def __init__(self, trusted=False):
        self.trusted = trusted

    @property
    def can_login(self):
        """only let's trusted friends read secrets"""
        return self.trusted


def login(user):
    """Gives access to users with privileges."""
    if user.can_login is True:
        print("All our secrets!!! 😨 😩 😱")
    else:
        print("No secrets for you!")


hacker = User(trusted=False)

friend = User(trusted=True)

login(hacker)
login(friend)
