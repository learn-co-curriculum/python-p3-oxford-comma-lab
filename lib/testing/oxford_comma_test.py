from oxford_comma import (
    oxford_comma
)

class TestOxfordComma:
    '''Module oxford_comma.py'''

    def test_with_one_element(self):
        '''returns a string without any additional formatting when given a 1-element list'''
        assert(oxford_comma(["kiwi"]) == "kiwi")

    def test_with_two_elements(self):
        '''adds "and" between elements when given a 2-element '''
        assert(oxford_comma(["kiwi", "durian"]) == "kiwi and durian")

    def test_with_three_elements(self):
        '''adds commas plus a final "and" when given a 3-element list'''
        assert(oxford_comma(["kiwi", "durian", "starfruit"]) == "kiwi, durian, and starfruit")

    def test_with_more_than_three_elements(self):
        '''correctly formats lists of lengths greater than three'''
        assert(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]) == "kiwi, durian, starfruit, mangos, and dragon fruits")
        assert(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits", "lychees", "pomelos"]) == "kiwi, durian, starfruit, mangos, dragon fruits, lychees, and pomelos")
