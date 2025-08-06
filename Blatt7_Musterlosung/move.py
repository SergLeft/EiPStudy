room = ['Curtain', [['Lamp'], 'Vacuum cleaner', 'Curtain', 'Laundry basket', 'Mouse', [['Printer'], 'Slippers', 'Air conditioner', ['Computer', [['Charger'], 'Vase', 'Broom', 'Mirror', 'Vacuum cleaner', 'Heater', [['Mop'], 'Dresser', [], 'Cleaning supplies', ['Candles'], ['Coat rack', ['Speakers'], [], 'Mirror', 'Television', 'Mouse', 'Side table', [[['Sheets'], ['Soap', 'Backpack'], ['Mouse', 'Printer'], 'Conditioner', 'Jewelry box', 'Vase', 'Newspaper', 'Handbag', 'Keyboard', 'Shower curtain', 'Towel', 'Candles', 'Comforter', 'Computer', 'Clock', 'Printer', [], 'Wardrobe', ['Speakers'], 'Chair', 'Remote control', ['Wardrobe'], 'Hairbrush', 'Sunglasses', [], 'Air conditioner', 'Dresser', 'Shoes', ['Light switch'], 'Mop', [], 'Clothes hanger', 'Conditioner', 'Remote control', 'Hat', [], 'Toilet', 'Cleaning supplies', 'Handbag', 'Lamp', 'Heater', 'Vase', [], [], [], [[['Pillow', 'Dresser', 'Plant'], 'Hat', ['Vacuum cleaner', 'Toilet'], ['Keyboard', 'Handbag', ['Soap dispenser'], 'Speakers', 'Keyboard', ['Dresser'], ['Makeup', [], 'Hat', [], 'Pillow', [], 'Gloves', 'Tissue box', ['Broom', 'Light switch'], 'Newspaper', 'Rug', [], 'Pillow', 'Soap dispenser', 'Paper', ['Alarm clock', [], 'Fan', 'Clothes hanger', [], 'Computer', 'Book', 'Laundry basket', 'Pillow', 'Charger', ['Speakers', 'Comb', 'Toothpaste'], 'Toothpaste', [[['Ironing board'], 'Coffee table', [], [[], [], [], 'Television', ['Picture frame'], 'Makeup', ['Wardrobe', 'Rug', 'DVDs', [['Coasters', 'Coat rack', [], 'Recycling bin', 'Game console', 'Closet', 'Sofa', 'Iron', 'Laundry basket', 'Mop', 'Fan', ['Umbrella'], 'Makeup', ['Coat rack', 'Sunglasses'], [], 'Paper', 'Alarm clock', 'Comb', 'Clothes hanger', 'Vacuum cleaner', 'Soap dispenser', ['Magazine', ['Comforter', 'Sofa'], ['DVD player'], 'Iron', 'Desk', 'Remote control', ['Vase'], 'DVD player', [[], 'Comb', 'Sink', 'Hairbrush', ['Sofa', 'Keyboard', 'Notebook'], 'Clock', 'Charger', 'Blinds', 'Coffee table', 'Remote control', 'Toothbrush', ['Hand sanitizer', [[[['Game console'], 'Medicine cabinet', 'Clock', 'Bucket', 'Side table', 'Ironing board', 'Soap', 'Cushion', 'Toilet', 'Medicine cabinet', 'Outlet', 'Mirror', ['Alarm clock', [], 'Wallet', ['Desk', 'Towel', [], 'Soap', 'Slippers', ['Backpack'], 'Computer', 'Toothpaste', 'Side table', ['Newspaper'], ['Mop', 'Slippers'], 'Charger', 'Broom', 'Candles', 'Light switch', ['Coat rack'], 'Outlet', ['Telephone'], 'Alarm clock', 'Tissue box', [['Tissue box', [[], 'Vase', [[['Wallet'], [[['Shampoo', [], [], 'Wallet', 'Monitor', 'Medicine cabinet']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], 'Slippers', 'Laundry basket', 'Air conditioner', 'Soap', 'Wallet', 'Comforter', 'Printer', []]


def count_items(l):
    if isinstance(l, list):  # Rekursionsfall
        count = 0
        for a in l:
            count += count_items(a)
        return count
    else:  # Basisfall
        return 1


def count_boxes(l):
    if isinstance(l, list):  # Rekursionsfall
        count = 1
        for a in l:
            count += count_boxes(a)
        return count
    return 0  # Basisfall


def find_in_box(l, box: list):
    if isinstance(l, list):  # Rekursionsfall
        # Prüfe ob alle Elemente in der aktuellen Box sind
        found = True
        for item in box:
            found = found and item in l
        if found:
            return True
        # Prüfe ob alle Elemente in einer Box sind, die in der aktuellen Box ist
        for a in l:
            if find_in_box(a, box):
                return True
    return False  # Basisfall


def unpack(l):
    # Rekursionfall: l ist eine Liste wir erstellen eine große Liste in die wir die Elemente von l und die entpackten unterlisten von l hinzufügen
    # Basisfall: Gebe das Element in einer Liste zurück
    if isinstance(l, list):
        f = []
        for a in l:
            # unpack(a) gibt entweder eine entpackte Box oder ein einzelnes Element in einer Liste zurück
            f += unpack(a)
        return f
    else:
        return [l]


print(count_items(room))
print(count_boxes(room))
print(find_in_box(room, ['Soap dispenser', 'Paper']))  # sanity check
print(find_in_box(room, ['DVDs', 'DVD player', 'Television']))
print(unpack(room))
