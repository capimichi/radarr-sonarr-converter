import gradio as gr

from radarrsonarrconverter.container.DefaultContainer import DefaultContainer
from radarrsonarrconverter.view.RadarrItemListView import RadarrItemListView
from radarrsonarrconverter.view.SonarrItemListView import SonarrItemListView

default_container: DefaultContainer = DefaultContainer.getInstance()

with gr.Blocks() as app:
    radarr_item_list_view: RadarrItemListView = default_container.get(RadarrItemListView)
    sonarr_item_list_view: SonarrItemListView = default_container.get(SonarrItemListView)

app.launch()
