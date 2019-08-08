from binary_tree import tree_node
from binary_tree import binary_tree

class binary_search_tree:
    def __init__(self):
        self.root = None
        self.num_items = 0
    def __setitem__(self, key, value):
        if self.root:
            self.set_aux(key,value,self.root)
        else:
            self.root = tree_node(key,value)
            self.num_items+=1

    def set_aux(self,key,value,current):
        if current is None:
            raise ValueError("got stuck?")
        elif current.left is None and current.right is None:
            if key < current.key:
                current.left = tree_node(key,value)
                self.num_items+=1
            elif key > current.key:
                current.right = tree_node(key, value)
                self.num_items += 1
            else:
                current.value = value
        else:
            if key < current.key:
                if current.left:
                    self.set_aux(key,value,current.left)
                else:
                    current.left = tree_node(key,value)
            elif key > current.key:
                if current.right:
                    self.set_aux(key,value,current.right)
                else:
                    current.right = tree_node(key,value)
            else:
                current.value = value
    def __getitem__(self, key):
        if self.root:
            return self.get_aux(key,self.root)
        else:
            raise KeyError("na mate")

    def get_aux(self,key,current):
        if current is None:
            raise KeyError("is no good my dude")
        elif current.key == key:
            return current.value
        elif current.key > key:
            return self.get_aux(key,current.left)
        elif current.key < key:
            return self.get_aux(key,current.right)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __str__(self):
        return self.in_order()
    def __len__(self):
        return self.num_items

binary_search_tree.post_order = binary_tree.post_order
binary_search_tree.in_order = binary_tree.in_order
binary_search_tree.in_order_aux = binary_tree.in_order_aux

B = binary_search_tree()
B[0] = "hello"
print(B)
print(1,len(B))
B[5] = "there"
print(B)
print(2,len(B))
B[5] = "world"
print(B)
print(2,len(B))
B[3] = "thing beneath world"
print(B)
B[-5] = "left of root"

print(B)
print(B[-5],"should be left of root")

print(99999 in B)