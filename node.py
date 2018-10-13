class Node:
  def __init__(self, attribute, value, output = None, attributeValueProbability = None):
    self.attribute = attribute
    self.value = value
    self.output = output #only for leaf nodes
    self.children = []
    self.attributeValueProbability = attributeValueProbability
    
  def addChild(self, child):
    self.children.append(child)
