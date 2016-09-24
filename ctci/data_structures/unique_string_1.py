import unittest 

# first attempt 
def unique_string(string):
    chars = []
    counter = 0 
    for n in string: 
        if n not in chars: 
            chars.append(n)
        else:
            counter +=1 
    return counter < 1 

#use set 
def unique_string_set(string): 
    return len(string) == len(set(string))

#use only str data structures
def unique_string_no_other_structures(string):
    for letter in string: 
        if string.count(letter) > 1: 
            return False 
    print('hi')
    return True 


class TestStringMethods(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique_string(test_string)
            set_value = unique_string_set(test_string)
            unique_struct = unique_string_no_other_structures(test_string)
            
            self.assertFalse(actual)
            self.assertTrue(set_value)
            self.assertTrue(unique_struct)


        # false check
        for test_string in self.dataF:
            actual = unique_string(test_string)
            set_value = unique_string_set(test_string)
            unique_struct = unique_string_no_other_structures(test_string)

            self.assertFalse(actual)
            self.assertFalse(set_value)
            self.assertFalse(unique_struct)

if __name__ == '__main__':
    unittest.main()
