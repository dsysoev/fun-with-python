class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print("Before Calling method on Left Subclass")
        super().call_me()
        print("After Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        print("Before Calling method on Right Subclass")
        super().call_me()
        print("After Calling method on Right Subclass")
        self.num_right_calls += 1

class SubclassR(RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        print("Before Calling method on Subclass")
        super().call_me()
        print("After Calling method on Subclass")
        self.num_sub_calls += 1

class Subclass(RightSubclass, LeftSubclass):
    num_sub_calls = 0
    def call_me(self):
        print("Before Calling method on Subclass")
        super().call_me()
        print("After Calling method on Subclass")
        self.num_sub_calls += 1

if __name__ in '__main__':
    Subclass().call_me()
