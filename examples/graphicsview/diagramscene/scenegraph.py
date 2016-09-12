class GraphicsViewSceneGraph(object):
    def __init__(self, scene):
        self.scene = scene
        self.dg = DirectedGraph()

    def set_node_attrs(self, item):
        dg = self.dg
        
        node = dg.node[item]
        
        node['name'] = item.name
        node['pos'] = item.pos().toTuple()
        node['itemType'] = item.diagramType
    
    def build_graph(self):
        dg = self.dg
        dg.clear()

        scene = self.scene        
        items = scene.items()
        
        for item in items:
            if isinstance(item, Arrow):
                si = item.myStartItem
                ei = item.myEndItem        
                dg.add_edge(si, ei)
                self.set_node_attrs(si)
                self.set_node_attrs(ei)
            elif isinstance(item, DiagramItem):
                if not item in dg.node:
                    dg.add_node(item)
                    self.set_node_attrs(item)
            else:
                pass

    def save_scene(self, scenePath=SCENEPATH):
        dg = self.dg

        scene_to_serialize = dict()
        
        sitems = scene_to_serialize['items'] = []
        
        # For serialiazing arrows between items
        item_index = dict()

        for index, (item, data) in enumerate(dg.node.iteritems(), 0):
            item_index[item] = index
            sitems.append(data)
        
        sarrows = scene_to_serialize['arrows'] = []
        for sitem in dg.node:
            sindex = item_index[sitem]
            for eitem in dg.edge[sitem]:
                eindex = item_index[eitem]
                sarrows.append((sindex, eindex))

        sceneFile = open(scenePath, mode='w')
        json.dump(scene_to_serialize, sceneFile)
        sceneFile.close()    

    def load_scene(self, scenePath=SCENEPATH):
        scene = self.scene
        dg = self.dg
        
        scene.clear()
        
        sceneFile = open(scenePath, mode='r')
        deserialized = json.load(sceneFile)
        sceneFile.close()
        
        built_items = []
        
        for itemdata in deserialized['items']:
            itemType = itemdata['itemType']
            name = itemdata['name']
            pos = itemdata['pos']
            
            item = scene.createItem(itemType, name, pos)
            
            built_items.append(item)
            
        for connection in deserialized['arrows']:
            sii, eii = connection
            si = built_items[sii]
            ei = built_items[eii]
            
            scene.createArrowItem(si, ei)

        self.build_graph()
    
    def dump_graph(self):
        dg = self.dg
        
        for item, data in dg.node.iteritems():
            print data['name'], data['pos'], data['itemType']
            for ei in dg.edge[item]:
                print "\t", dg.node[ei]['name']
            print
