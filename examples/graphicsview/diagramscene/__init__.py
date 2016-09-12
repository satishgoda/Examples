SCENEPATH = "F:\\diagramscene.json"

from diagramscene.sceneview import MainWindow, Arrow, DiagramItem
from diagramscene.scenegraph import GraphicsViewSceneGraph

__all__ = ("Arrow", "DiagramItem", 
           "GraphicsViewSceneGraph", 
           "MainWindow")

__author__ = 'satishgoda'
__version__ = "0.0.1"


sceneWindow = None
scene = None
view = None
scenegraph = None

def test():
    global sceneWindow
    global scene
    global view
    global scenegraph
    
    from diagramscene import MainWindow
    from diagramscene import GraphicsViewSceneGraph
    
    sceneWindow = MainWindow()
    sceneWindow.setGeometry(100, 100, 800, 500)
    sceneWindow.show()
    
    scene = sceneWindow.scene
    
    scenegraph = GraphicsViewSceneGraph(scene)
    
"""
In [1]: from diagramscene import test
In [2]: test()
In [3]: from diagramscene import scenegraph
In [4]: scenegraph.load_scene()
In [5]: scenegraph.build_graph()
In [6]: scenegraph.save_scene()
In [7]: scenegraph.scene.clear()
In [8]: scenegraph.load_scene()
"""
