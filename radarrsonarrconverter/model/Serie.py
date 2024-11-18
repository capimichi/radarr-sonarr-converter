from typing import Optional, List

from injector import inject
from pydantic import BaseModel

from radarrsonarrconverter.model.Season import Season


class Serie(BaseModel):

    id: Optional[int] = None
    title: Optional[str] = None
    seasons: Optional[List[Season]] = None
