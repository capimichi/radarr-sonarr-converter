from typing import Optional

from injector import inject
from pydantic import BaseModel

class Season(BaseModel):

    seasonNumber: Optional[int] = None
    monitored: Optional[bool] = None