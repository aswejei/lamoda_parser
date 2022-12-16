class Parser:
    def __init__(self, card_str: str):
        self._current_card: str = card_str

    def print_current_card_raw(self):
        print(self._current_card)

    def get_current_card_parsed(self):
        parsed_card = self._parse_card()
        print(parsed_card)
        return parsed_card

    def _parse_card(self):
        parsed_card = dict(zip(('price', 'description'),self._current_card.split('р.')))
        parsed_card['price'] = parsed_card['price'] + 'р.'
        if parsed_card['description'][0] == ' ':
            parsed_card['description'] = parsed_card['description'][1:]
        return parsed_card
