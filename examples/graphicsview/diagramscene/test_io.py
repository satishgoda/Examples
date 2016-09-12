serialized = {
'items': [],
'arrows': []
}

sitems = serialized['items']
sarrows = serialized['arrows']

item_list = []
arrows = []

for item in scene.items():
    if isinstance(item, DiagramItem):            
        data = {}
        data['name'] = item.name
        data['itemType'] = item.diagramType
        data['pos'] = item.pos().toTuple()
        sitems.append(data)
        item_list.append(item)
    elif isinstance(item, Arrow):
        arrows.append(item)

for arrow in arrows:
    sindex = item_list.index(arrow.myStartItem)
    eindex = item_list.index(arrow.myEndItem)
    sarrows.append((sindex, eindex))

print sitems
print sarrows
print serialized

deserialized = {'arrows': [(1, 0), (2, 0), (4, 1), (5, 1), (3, 2), (5, 3), (6, 3)],
 'items': [{'itemType': 3, 'name': u'Farm', 'pos': (2674.0, 3148.0)},
  {'itemType': 0, 'name': u'Render2', 'pos': (2932.0, 2842.0)},
  {'itemType': 0, 'name': u'Render1', 'pos': (2426.0, 2890.0)},
  {'itemType': 1, 'name': u'Merge1', 'pos': (2432.0, 2590.0)},
  {'itemType': 0, 'name': u'Sim3', 'pos': (2972.0, 2278.0)},
  {'itemType': 0, 'name': u'Sim2', 'pos': (2620.0, 2270.0)},
  {'itemType': 0, 'name': u'Sim1', 'pos': (2287.333333333333, 2264.0)}]}
