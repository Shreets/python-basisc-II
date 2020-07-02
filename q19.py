# 19. Write a Python class to find validity of a string of parentheses
# , '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order' \
# 'for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


class Brackets:
    def validate(self, string):
        bkt_list = list(string)
        if len(string) % 2 != 0:
            return False
        elif (bkt_list.index('(') < bkt_list.index(')')) or (bkt_list.index('{') < bkt_list.index('}')) or (
                bkt_list.index('[') < bkt_list.index(']')):
            if (bkt_list.count('(') == bkt_list.count(')')) or (bkt_list.count('{') == bkt_list.count('}')) or (
                    bkt_list.count('[') == bkt_list.count(']')):
                return True
        else:
            return False


bracket1 = Brackets().validate('[{([)]}]')  # true
bracket2 = Brackets().validate('()[]{}')  # true
bracket3 = Brackets().validate('[{(}]')  # false
bracket4 = Brackets().validate('{{{')  # false
bracket5 = Brackets().validate('((()))')  #true
print(bracket1)
print(bracket2)
print(bracket3)
print(bracket4)
print(bracket5)
