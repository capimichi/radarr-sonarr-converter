from radarrsonarrconverter.variable.RadarrApiKeyVariable import RadarrApiKeyVariable
from radarrsonarrconverter.variable.RadarrBaseUrlVariable import RadarrBaseUrlVariable
from injector import inject


class RadarrClient:
    radarr_base_url: RadarrBaseUrlVariable
    radarr_api_key: RadarrApiKeyVariable

    @inject
    def __init__(self, radarr_base_url: RadarrBaseUrlVariable, radarr_api_key: RadarrApiKeyVariable):
        self.radarr_base_url = radarr_base_url
        self.radarr_api_key = radarr_api_key
