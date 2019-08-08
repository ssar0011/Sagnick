class tree_node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __setitem__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{"+self.key+","+self.value+"}"

class binary_tree:
    def __init__(self):
        self.root = None
        self.num_items = 0

    def __len__(self):
        return self.num_items

    def __str__(self):
        return self.post_order()

    def post_order(self):
        return self.post_order_aux(self.root)

    def post_order_aux(self,current):
        if current is None:
            return ""
        left_string = self.post_order_aux(current.left)
        right_string = self.post_order_aux(current.right)
        return left_string+" "+right_string+" "+str(current)

    def insert_main(self,path_to_insert,key,value):
        if len(path_to_insert)==0:
            if self.root is None:
                self.root = tree_node(key,value)
            else:
                self.root[key] = value
        else:
            self.insert(self.root,path_to_insert,key,value)

    def insert(self,current,path_to_insert,key,value):
        if current is None:
            raise ValueError("path must exist first")
        elif len(path_to_insert) == 1:
            new_node = tree_node(key,value)
            if path_to_insert[0] == "0":
                if current.left is None:
                    current.left = new_node
                else:
                    current.left[key]=value
            elif path_to_insert[0] == "1":
                if current.right is None:
                    current.right = new_node
                else:
                    current.right[key]=value
            else:
                raise ValueError("path must only contain 0s and 1s")
        else:
            if path_to_insert[0] == "0":
                self.insert(current.left,path_to_insert[1:],key,value)
            elif path_to_insert[0] == "1":
                self.insert(current.right,path_to_insert[1:],key,value)
            else:
                raise ValueError("path must only contain 0s and 1s")
    def search(self,path_to_insert,key):
        if self.root:
            return self.search_aux(self.root,path_to_insert,key)
        else:
            raise KeyError("no root")

    def search_aux(self,current,path_to_insert,key):
        if current is None:
            raise KeyError("key not found")
        elif len(path_to_insert)==0:
            return current.value
        else:
            if path_to_insert[0]=="0":
                return self.search_aux(current.left,path_to_insert[1:],key)
            elif path_to_insert[0]=="1":
                return self.search_aux(current.right,path_to_insert[1:],key)
            else:
                raise ValueError("path is stupid")

B = binary_tree()
B.insert_main("","root?","root?")
#B.insert_main("2","not root?","not root?")
B.insert_main("0","left","left")
B.insert_main("00","leftleft","leftleft")
B.insert_main("0","newleft","be there")
B.insert_main("1","right","thing")
B.insert_main("11","rightright","other thing")

print(B.search("11","right"))
print(B.search("","root?"))

print(B)