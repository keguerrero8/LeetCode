# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root, res = None):   
        if res == None:
            res = []
        if root is None:
            res.append("N")
            return "N"
        
        res.append(str(root.val))
        
        self.serialize(root.left, res)
        self.serialize(root.right, res)
        
        return "/".join(res) 
        
    def deserialize(self, data):
        if data is "N":
            return None
        vals = data.split("/")
        self.i = 0 
        
        def dfsConstruct():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            
            root.left = dfsConstruct()
            root.right = dfsConstruct()
            
            return root        
        
        return dfsConstruct()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))