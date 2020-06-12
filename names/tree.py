class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root
        # we can check this by checking if self is None
        if self is None:
            # if not insert here
            self = BSTNode(value)
        # else there is a root check
        # THE ABOVE CODE IS NOT NECESSARY
        else:
            # if the value < root's value, go left
            if value < self.value:
                # if true, go left
                if self.left:
                    self.left.insert(value)
                else:
                    # if no self.left put value here
                    self.left = BSTNode(value)
            # if value >= root's value, go right
            else:
                # if true, go right
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is less than the current value, go left
        if target < self.value:
            # if target equals self.left
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True
