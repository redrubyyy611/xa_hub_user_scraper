import enum

ROBLOX_GROUP_BASE_SEARCH_URL: str = (
    "https://groups.roblox.com/v1/groups/{}/roles/{}/users?limit=100&sortOrder=Desc"
)
"""Base URL for the Roblox group API to search for users."""

# ======================
# XA Hub group constants
# ======================

# IDS
XA_HUB_GROUP_ID: int = 35310933
"""Roblox group ID for the XA Hub group."""

XA_HUB_MEMBER_ROLE_ID: int = 234922010
"""Roblox role ID for the XA Hub member role."""

XA_HUB_OWNER_ROBLOX_ID: int = 2953444466
"""Roblox ID for the XA Hub owner."""

XA_HUB_ADMIN_ROBLOX_IDS: list[int] = [5509421902, 2678492533]
"""Roblox IDs for the XA Hub admins."""

# Files
XA_HUB_USERS_FILE: str = "data/xa_hub/xa_hub_users.txt"
"""File path for the list of XA Hub usernames/user ID pairs text file."""

XA_HUB_USER_IDS_JSON_FILE: str = "data/xa_hub/xa_hub_users.json"
"""File path for the list of XA Hub users (raw Roblox group request data)."""

XA_HUB_USER_IDS_TXT_FILE: str = "data/xa_hub/xa_hub_user_ids.txt"
"""File path for the list of XA Hub user IDs text file."""

# ===================
# XPP group constants
# ===================

# IDS

XPP_GROUP_ID: int = 35713343
"""Roblox group ID for the XPP group."""

XPP_MEMBER_ROLE_ID: int = 317842014

"""Roblox role ID for the XPP member role."""

XPP_OWNER_ROBLOX_ID: int = 8114858907
"""Roblox ID for the XPP owner."""

XPP_ADMIN_ROBLOX_IDS: list[int] = [3212616083, 5544028566, 3874719377, 4241141996]
"""Roblox IDs for the XPP admins."""

# Files
XPP_USERS_FILE: str = "data/xpp/xpp_users.txt"
"""File path for the list of XPP usernames/user ID pairs text file."""

XPP_USER_IDS_JSON_FILE: str = "data/xpp/xpp_users.json"
"""File path for the list of XPP users (raw Roblox group request data)."""

XPP_USER_IDS_TXT_FILE: str = "data/xpp/xpp_user_ids.txt"
"""File path for the list of XPP user IDs text file."""


class RobloxHackingGroups(enum.Enum):
    """
    Enum of Roblox hacking groups with their names and aliases.
    """
    XA_HUB = {
        "name": "XA Hub",
        "aliases": ["xa", "xa_hub"],
    }
    XPP = {
        "name": "XPP",
        "aliases": ["xpp", "xpp_group"],
    }
