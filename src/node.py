class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.l_child = None
        self.r_child = None

        self.locked = False
        self.left_des_locked = False
        self.right_des_locked = False

    def create_left_child(self):
        self.l_child = Node(parent=self)

    def create_right_child(self):
        self.r_child = Node(parent=self)

    def lock(self):
        # Check locking condition
        # - No locked ancestors
        # - No locked descendants
        ancestor_locked = self.check_ancestors()

        if not(ancestor_locked or self.left_des_locked or self.right_des_locked):
            self.locked = True
            self.inform_ancestors(locked=True)

    def unlock(self):
        self.locked = False
        self.inform_ancestors(locked=False)

    def check_ancestors(self):
        if self.parent is None:
            return self.locked
        else:
            if self.locked:
                return self.locked
            else:
                return self.check_ancestors()

    def inform_ancestors(self, locked=False):
        if self.parent is None:
            return
        if self.parent.l_child == self:
            self.parent.left_des_locked = locked
        elif self.parent.r_child == self:
            self.parent.right_des_locked = locked
        self.parent.inform_ancestors(locked)


if __name__ == '__main__':
    rootNode = Node()
