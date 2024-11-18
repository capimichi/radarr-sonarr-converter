from typing import Optional

from injector import inject
from pydantic import BaseModel

class Episode(BaseModel):

    id: Optional[int] = None
    episodeNumber: Optional[int] = None
    seriesId: Optional[int] = None
    seasonNumber: Optional[int] = None
    monitored: Optional[bool] = None
    title: Optional[str] = None
    hasFile: Optional[bool] = None