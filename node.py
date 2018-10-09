class Node:
  def __init__(self, attribute, value, output = None):
    self.attribute = attribute
    self.value = value
    self.output = output #only for leaf nodes
    self.children = []
    
  def addChild(self, child):
    self.children.append(child)
