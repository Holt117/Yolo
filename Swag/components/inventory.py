import tcod as libtcod

from game_messages import Message


class Inventory:
    def __init__(selfs, capacity):
        self.capacity = capacity
        self.item = []

    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.appent({
                'item_added': None,
                'message': Message('You cannot carry any more, you inventory is full', libtcod.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}!'.format(item.name), libtcod.blue)
            })

            self.items.append(item)

        return results
