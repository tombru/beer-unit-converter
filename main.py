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

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query  = event.get_argument()
        if query == None:
            query = ''
        #item_name = extension.preferences['item_name']
        data = {'new_name': '%s EBC' % ((2.65 * int(query))-1.2)} #EBC=(Lx2.65) - 1.2
        items = [ExtensionResultItem(icon='images/icon.png',
                                             name='L -> EBC',
                                             description='Lovibind to EBC',
                                             on_enter=ExtensionCustomAction(data, keep_app_open=True))]
        logger.info('preferences %s' % json.dumps(extension.preferences))
        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['new_name'],
                                                           on_enter=HideWindowAction())])


if __name__ == '__main__':
    DemoExtension().run()
