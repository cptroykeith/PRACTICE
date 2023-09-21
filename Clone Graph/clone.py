class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Dictionary to store the clone of each node
        node_clone = {}
        
        def dfs(original_node):
            if original_node not in node_clone:
                # Create a clone of the node
                clone = Node(original_node.val)
                node_clone[original_node] = clone
                
                # Recursively clone neighbors
                clone.neighbors = [dfs(neighbor) for neighbor in original_node.neighbors]
            
            return node_clone[original_node]
        
        return dfs(node)
