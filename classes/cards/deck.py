__author__ = 'joe'

import json


class Deck(object):

    def __init__(self, json_file_path):
        self.cards = []
        with open(json_file_path, 'r') as json_file:
            json_payload = ''.join(json_file.readlines())
            self.json_root= json.loads(json_payload)
        for card in self.json_root.get('cards', []):
            self.add_card(card)

    def add_card(self, card):
        module= 'cards.card'
        class_name= card.get('card_type')
        card_data= card.get('card_data')
        kwargs= {}
        for constructor_arg in card_data:
            kwargs.update(constructor_arg)
        imported_module= __import__(module, fromlist=['all'])
        class_= getattr(imported_module, class_name)
        instance= class_(self, class_name, **kwargs)
        self.cards.append(instance)