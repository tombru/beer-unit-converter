import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from conv import l_to_ebc, srm_to_ebc

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def l_to_ebc(self, query):
        return '%s °L = %s EBC' % (query, l_to_ebc(query)) if query and query.isdigit() else ''

    def srm_to_ebc(self, query):
        return '%s SRM = %s EBC' % (query, srm_to_ebc(query)) if query and query.isdigit() else ''

    def on_event(self, event, extension):
        query = event.get_argument()
        items = [
            ExtensionResultItem(icon='images/icon.png',
                                name='°L -> EBC',
                                description='Lovibind to EBC',
                                on_enter=ExtensionCustomAction({'res': self.l_to_ebc(query)}, keep_app_open=True)),
            ExtensionResultItem(icon='images/icon.png',
                                name='SRM -> EBC',
                                description='SRM to EBC',
                                on_enter=ExtensionCustomAction({'res': self.srm_to_ebc(query)}, keep_app_open=True))
        ]
        logger.info('preferences %s' % json.dumps(extension.preferences))
        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['res'],
                                                           on_enter=HideWindowAction())])


if __name__ == '__main__':
    DemoExtension().run()
