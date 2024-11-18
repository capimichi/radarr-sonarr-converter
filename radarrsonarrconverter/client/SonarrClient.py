from typing import List

import requests

from radarrsonarrconverter.model.Episode import Episode
from radarrsonarrconverter.model.Serie import Serie
from radarrsonarrconverter.variable.SonarrApiKeyVariable import SonarrApiKeyVariable
from radarrsonarrconverter.variable.SonarrBaseUrlVariable import SonarrBaseUrlVariable
from injector import inject


class SonarrClient:
    sonarr_base_url: SonarrBaseUrlVariable
    sonarr_api_key: SonarrApiKeyVariable

    @inject
    def __init__(self, sonarr_base_url: SonarrBaseUrlVariable, sonarr_api_key: SonarrApiKeyVariable):
        self.sonarr_base_url = sonarr_base_url
        self.sonarr_api_key = sonarr_api_key

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-Api-Key': self.sonarr_api_key
        }

    def get_series(self) -> List[Serie]:

        url = f"{self.sonarr_base_url}/api/v3/series"

        payload = {}

        response = requests.request("GET", url, headers=self.get_headers(), data=payload)

        rows = response.json()

        series = []

        for row in rows:
            serie = Serie.model_validate(row)
            series.append(serie)

        return series

    def get_episodes(self, serie_id: int, season_number: int) -> List[Episode]:
        serie_id_str = str(serie_id)
        season_number_str = str(season_number)
        url = f"{self.sonarr_base_url}/api/v3/episode?seriesId={serie_id_str}&seasonNumber={season_number_str}"

        payload = {}

        response = requests.request("GET", url, headers=self.get_headers(), data=payload)
        rows = response.json()
        episodes = []

        for row in rows:
            episode = Episode.model_validate(row)
            episodes.append(episode)

        return episodes