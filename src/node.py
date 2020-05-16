class Node:
    def __init__(self, x, y, r, parent=None):
        self.parent = parent
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
        self.l_child = None
        self.r_child = None
        self.x = x
        self.y = y
        self.r = r

        self.is_locked = False
        self.left_des_locked = False
        self.right_des_locked = False

    def create_left_child(self):
        des_x = self.x - 500 / (self.depth*0.75 + 1) ** 2.4
        des_y = self.y + 250 / (self.depth + 1)
        des_r = self.r - 2.5
        self.l_child = Node(x=des_x, y=des_y, r=des_r, parent=self)
        return self.l_child

    def create_right_child(self):
        des_x = self.x + 500 / (self.depth*0.75 + 1) ** 2.4
        des_y = self.y + 250 / (self.depth + 1)
        des_r = self.r - 2.5
        self.r_child = Node(x=des_x, y=des_y, r=des_r, parent=self)
        return self.r_child

    def lock(self):
        # Check locking condition
        # - No locked ancestors
        # - No locked descendants
        ancestor_locked = self.check_ancestors()

        if not(ancestor_locked or self.left_des_locked or self.right_des_locked):
            self.is_locked = True
            self.inform_ancestors(locked=True)
            print("Locked node")
            return True
        else:
            print("Could not lock node")
            return False

    def unlock(self):
        if not self.is_locked:
            return
        self.is_locked = False
        self.inform_ancestors(locked=False)
        print("Unlocked Node")

    def check_ancestors(self):
        if self.parent is None:
            return self.is_locked
        else:
            if self.parent.is_locked:
                return True
            else:
                return self.parent.check_ancestors()

    def inform_ancestors(self, locked=False):
        if self.parent is None:
            return
        if self.parent.l_child == self:
            self.parent.left_des_locked = locked
        elif self.parent.r_child == self:
            self.parent.right_des_locked = locked
        self.parent.inform_ancestors(locked)
