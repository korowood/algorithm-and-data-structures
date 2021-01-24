"""
TEST1
input:
1+(2*2-3).

output:
2
__________
TEST2
input:
1+a+1.

output:
WRONG
"""

ADD, SUB = "+", "-"
MUL, DIV = "*", "/"
LEFT_P, RIGHT_P = "(", ")"
DIGITS = "0123456789"
END_SYMBOL = "."

OPS = ADD + SUB + MUL + DIV + LEFT_P + RIGHT_P
ALPHABET = DIGITS + OPS + END_SYMBOL


class Lexer:
    def __init__(self, string):
        self.my_str = string
        self.iter = 0
        self.ended = False

    def next_token(self):
        key = ""
        elem = self.my_str[self.iter]
        if elem not in ALPHABET:
            raise ValueError()
        if elem in OPS:
            key = elem
        elif elem == END_SYMBOL:
            self.ended = True
        else:
            while elem in DIGITS:
                key += elem
                self.iter += 1
                elem = self.my_str[self.iter]
            self.iter -= 1
        self.iter += 1
        return key


class Parser:
    def __init__(self):
        self.tokens = None
        self.token_cnt = 0
        self.iter = 0

    def parse(self, lexer):
        self.tokens = self.get(lexer)
        self.token_cnt = len(self.tokens)
        result = self.expression()
        if self.iter != self.token_cnt - 1:
            raise ValueError()
        return result

    def expression(self):
        first = self.term()
        while self.iter < self.token_cnt:
            operator = self.tokens[self.iter]
            if operator != ADD and operator != SUB:
                break
            else:
                self.iter += 1
            second = self.term()
            if operator == ADD:
                first += second
            else:
                first -= second
        return first

    def term(self):
        first = self.factor()
        while self.iter < self.token_cnt:
            operator = self.tokens[self.iter]
            if operator != MUL and operator != DIV:
                break
            else:
                self.iter += 1
            second = self.factor()
            if operator == MUL:
                first *= second
            else:
                first /= second
        return first

    def factor(self):
        next_token = self.tokens[self.iter]
        if next_token == LEFT_P:
            self.iter += 1
            result = self.expression()
            if self.iter < self.token_cnt:
                expected_bracket = self.tokens[self.iter]
            else:
                raise ValueError()
            if self.iter < self.token_cnt and expected_bracket == RIGHT_P:
                self.iter += 1
                return result
            raise ValueError()
        self.iter += 1
        return int(next_token)

    @staticmethod
    def get(lexer):
        all_tokens = []
        while not lexer.ended:
            token = lexer.next_token()
            all_tokens.append(token)
        return all_tokens


ms = input()

flag = False
ans = 0
new_lexer = Lexer(ms)
parser = Parser()

try:
    ans = parser.parse(new_lexer)
except ValueError as e:
    flag = True

if flag:
    print("WRONG")
else:
    print(ans)
