from typing import Optional

from pydantic import BaseModel, Field


class RobloxGroupUser(BaseModel):
    """
    A user in a Roblox group.
    """

    hasVerifiedBadge: bool
    """The user's verified badge status."""

    userId: int
    """The user's ID."""

    username: str
    """The user's username."""

    displayName: str
    """The user's display name."""

    def __str__(self):
        return f"{self.username} ({self.userId})"


class RobloxGroupResponse(BaseModel):
    """ "
    A response from the Roblox group API.
    """

    previousPageCursor: str
    """Cursor for the previous page of results."""

    nextPageCursor: Optional[str] = None
    """Cursor for the next page of results."""

    data: list[RobloxGroupUser] = Field(default_factory=list)
    """List of users in the group."""
