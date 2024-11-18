from injector import inject
import gradio as gr


class SonarrItemListView:

    @inject
    def __init__(self):
        self._init_tab()

    def _init_tab(self):
        with gr.Tab("Sonarr item list"):
            self._init_item_list()

    def _init_item_list(self):
        pass
