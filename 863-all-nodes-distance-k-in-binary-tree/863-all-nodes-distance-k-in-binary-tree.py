# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        parentNodes = {}
        nodesDistanceK = []
        visited = set()
        node = self.findTargetNodeAndParents(root, target, parentNodes, None)
        
        return self.findNodesDistanceKHelper(node, k, parentNodes, nodesDistanceK, 0, visited)
        

    def findTargetNodeAndParents(self, tree, target, parentNodes, parent):
        if tree is None:
            return None

        parentNodes[tree.val] = parent
        if tree == target:
            return tree

        nodeL = self.findTargetNodeAndParents(tree.left, target, parentNodes, tree)
        nodeR = self.findTargetNodeAndParents(tree.right, target, parentNodes, tree)
        return nodeL if nodeL else nodeR



    def findNodesDistanceKHelper(self, node, k, parentNodes, nodesDistanceK, distance, visited):
        if distance == k:
            nodesDistanceK.append(node.val)
            return nodesDistanceK

        if node is None:
            return nodesDistanceK

        visited.add(node.val)
        if node.left and node.left.val not in visited:
            self.findNodesDistanceKHelper(node.left, k, parentNodes, nodesDistanceK, distance + 1, visited)
        if node.right and node.right.val not in visited:
            self.findNodesDistanceKHelper(node.right, k, parentNodes, nodesDistanceK, distance + 1, visited)
        if node.val in parentNodes and parentNodes[node.val] and parentNodes[node.val].val not in visited:
            self.findNodesDistanceKHelper(parentNodes[node.val], k, parentNodes, nodesDistanceK, distance + 1, visited)

        return nodesDistanceK
        