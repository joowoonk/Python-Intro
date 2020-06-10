class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            # compare the value to the root's value to determine which direction
            # we're gonna go in 
            # if the value < root's value 
        if value < self.value:
                # go left 
                # how do we go left?
                # we have to check if there is another node on the left side
            if self.left: 
                    # then self.left is a Node 
                    # now what?
                self.left.insert(value)
            else:
                    # then we can park the value here
                self.left = BSTNode(value)
            # else the value >= root's value 
        else:
                # go right
                # how do we go right? 
                # we have to check if there is another node on the right side 
            if self.right:
                    # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
