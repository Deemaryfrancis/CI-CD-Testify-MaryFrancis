import HelloWorld
import unittest

class Testmain(unittest.TestCase):

    def test_addition(self):
        self.AssertEqual(main.addition(1 , 2), 3, "Should be 3" )
        self.AssertEqual(main.addition(5 , 5), 10, "Should be 10" )
        self.AssertEqual(main.addition(40, 20), 60, "Should be 60" )
        self.AssertEqual(main.addition(-3 , 2), -1, "Should be -1" )
    
if __name__ == '_main_':
    unittest()