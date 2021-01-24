"""
TEST1
input:
Podarok(Moroz-Ded Moroz)*2.

output:
4100
__________
TEST2
input:
Snegurochka-30.

output:
-20
"""

import operator
from collections import deque
from enum import Enum

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
PLUS, MINUS, MUL = '+', '-', '*'


class NamedFunction:
    def __init__(self, name, op):
        self.name = name
        self.op = op

    def __call__(self, *args, **kwargs):
        return self.op(*args, **kwargs)


FUNCTIONS = [NamedFunction('Podarok', lambda x: x + 5 if x > 0 else abs(x))]


class ParseException(Exception):
    pass


class TokenType(Enum):
    OPERATOR = 0
    BRACKET = 1
    NUMBER = 2
    STRING = 3
    FUNCTIONS = 4
    END = 5


class Token:
    BRACKETS = {OPEN_BRACKET, CLOSE_BRACKET}
    OPERATORS_MAP = {PLUS: operator.add, MINUS: operator.sub, MUL: operator.mul}
    FUNCTIONS_MAP = {fun.name: fun for fun in FUNCTIONS}
    CONST = {'Ded Moroz': 2020, 'Moroz': -30, 'Snegurochka': 10}
    END = '.'

    def __init__(self, token_type: TokenType, value, op=None):
        self.token_type = token_type
        self.value = value
        self.op = op

    @staticmethod
    def parse(value):
        if value == Token.END:
            return Token(TokenType.END, value)
        if value in Token.BRACKETS:
            return Token(TokenType.BRACKET, value)
        if value in Token.OPERATORS_MAP:
            return Token(TokenType.OPERATOR, value, Token.OPERATORS_MAP[value])
        try:
            int_value = int(value)
            return Token(TokenType.NUMBER, int_value)
        except ValueError:
            return Token(TokenType.STRING, value)

    def __str__(self):
        return str(self.value)


class Lexer:
    def __init__(self, string):
        self.string = string
        self.cur_pos = 0
        self.last_pos = deque()

    def is_end(self):
        return self.cur_pos == len(self.string)

    def revert(self):
        self.cur_pos = self.last_pos.pop()

    def _try_parse_chars(self, chars):
        chars = ''.join(chars)
        if chars in Token.CONST:
            return Token(TokenType.NUMBER, Token.CONST[chars])
        if chars in Token.FUNCTIONS_MAP:
            return Token(TokenType.FUNCTIONS, chars, Token.FUNCTIONS_MAP[chars])
        try:
            int_value = int(chars)
            return Token(TokenType.NUMBER, int_value)
        except:
            raise ParseException()

    def next_token(self):
        cur_pos = self.cur_pos
        self.last_pos.append(cur_pos)
        if self.is_end():
            raise ParseException()
        chars = []
        has_number = False
        has_char = False
        while cur_pos < len(self.string):
            cur_char = self.string[cur_pos]
            cur_token = Token.parse(cur_char)

            is_number = cur_token.token_type == TokenType.NUMBER
            is_char = cur_token.token_type == TokenType.STRING
            is_not_const = not is_number and not is_char

            has_char = has_char or is_char
            has_number = has_number or is_number

            if is_not_const and len(chars) == 0:
                self.cur_pos = cur_pos + 1
                return cur_token

            if (is_char and has_number) or (is_number and has_char) or (is_not_const and len(chars) > 0):
                self.cur_pos = cur_pos
                return self._try_parse_chars(chars)

            if not is_not_const:
                cur_pos += 1
                chars.append(cur_char)
            else:
                raise ParseException()
        self.cur_pos = cur_pos
        return Token.parse(''.join(chars))


class Parser:
    def __init__(self, string):
        self.lexer = Lexer(string)

    def inner_parse_fun(self, fun_token):
        open_bracket = self.lexer.next_token()
        if open_bracket.value != OPEN_BRACKET:
            raise ParseException()
        argument = self.parse_additive()
        close_bracket = self.lexer.next_token()
        if close_bracket.value != CLOSE_BRACKET:
            raise ParseException()
        return Token(TokenType.NUMBER, fun_token.op(argument.value))

    def parse_operand(self):
        token = self.lexer.next_token()
        if token.value == OPEN_BRACKET:
            res = self.parse_additive()
            token2 = self.lexer.next_token()
            if token2.value != CLOSE_BRACKET:
                raise ParseException()
            return res
        if token.token_type == TokenType.NUMBER:
            return Token(TokenType.NUMBER, token.value)
        if token.token_type == TokenType.FUNCTIONS:
            return self.inner_parse_fun(token)
        raise ParseException()

    def parse_mult(self):
        first = self.parse_operand()
        while not self.lexer.is_end():
            op = self.lexer.next_token()
            if op.value != MUL:
                self.lexer.revert()
                break
            second = self.parse_operand()
            first = Token(TokenType.NUMBER, op.op(first.value, second.value))
        return first

    def parse_additive(self):
        operand1 = self.parse_mult()
        while not self.lexer.is_end():
            op = self.lexer.next_token()
            if op.value not in {PLUS, MINUS}:
                self.lexer.revert()
                break
            operand2 = self.parse_mult()
            operand1 = Token(TokenType.NUMBER, op.op(operand1.value, operand2.value))
        return operand1

    def parse(self):
        expr = self.parse_additive()
        if self.lexer.next_token().token_type != TokenType.END:
            raise ParseException()
        return expr


if __name__ == '__main__':
    s = input()
    parser = Parser(s)
    try:
        print(parser.parse())
    except ParseException:
        print('WRONG')