from datetime import datetime
from typing import Optional


class User:
    id: str
    login: str
    display_name: str
    type: str
    broadcaster_type: str
    description: str
    profile_image_url: str
    offline_image_url: str
    view_count: int
    email: Optional[str]
    created_at: Optional[datetime]

    def __init__(
        self,
        id: str,
        login: str,
        display_name: str,
        type: str,
        broadcaster_type: str,
        description: str,
        profile_image_url: str,
        offline_image_url: str,
        view_count: int,
        email: Optional[str] = None,
        created_at: Optional[str] = None
    ) -> None:
        self.id = id
        self.login = login
        self.display_name = display_name
        self.type = type
        self.broadcaster_type = broadcaster_type
        self.description = description
        self.profile_image_url = profile_image_url
        self.offline_image_url = offline_image_url
        self.view_count = view_count
        self.email = email
        self.created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ") if created_at else None
