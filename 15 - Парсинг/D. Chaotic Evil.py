"""
TEST1
input:
typedef eightbytes unsigned char[8]
sizeof eightbytes
alignof eightbytes

output:
8
1
__________
TEST2
input:
typedef verylong struct {
long[2];
unsigned short int[4];
}
sizeof verylong
alignof verylong

output:
24
8
__________
TEST3
input:
typedef verylong struct {
long[2];
unsigned short int[4];
}
typedef evenlonger struct {
verylong[4];
}
sizeof evenlonger
alignof evenlonger
typedef arr evenlonger[123]
sizeof arr
alignof arr

output:
96
8
11808
8
"""

import sys


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"

TYPES = {
    "bool": [1, 1],
    "char": [1, 1],
    "signed char": [1, 1],
    "unsigned char": [1, 1],
    "short": [2, 2],
    "signed short": [2, 2],
    "short int": [2, 2],
    "signed short int": [2, 2],
    "unsigned short": [2, 2],
    "unsigned short int": [2, 2],
    "int": [4, 4],
    "signed": [4, 4],
    "signed int": [4, 4],
    "unsigned": [4, 4],
    "unsigned int": [4, 4],
    "long": [8, 8],
    "signed long": [8, 8],
    "long int": [8, 8],
    "signed long int": [8, 8],
    "unsigned long": [8, 8],
    "unsigned long int": [8, 8],
    "long long": [8, 8],
    "signed long long": [8, 8],
    "long long int": [8, 8],
    "signed long long int": [8, 8],
    "unsigned long long": [8, 8],
    "unsigned long long int": [8, 8]
}

FUNC_TYPEDEF = "typedef"
FUNC_SIZEOF = "sizeof"
FUNC_ALIGNOF = "alignof"
STRUCT = "struct"
LEFT_SQ_B = "["
LEFT_CR_B = "{"
RIGHT_SQ_B = "]"
RIGHT_CR_B = "}"
SEMICOLON = ";"
DELIMITER = " "
NEW_LINE = "\n"
ONE_SYMBOL_TOKENS = [LEFT_SQ_B, LEFT_CR_B, RIGHT_SQ_B, RIGHT_CR_B, SEMICOLON, DELIMITER, NEW_LINE]
END_SYMBOL = "."


class Lexer:
    def __init__(self):
        self.str = ""
        self.i = 0
        self.all_tokens = []
        self.inside_struct = False

    def split_into_tokens(self, s):
        if not self.inside_struct:
            if s[-2] == LEFT_CR_B:
                self.inside_struct = True
                self.get_tokens_before_struct(s[:-1])
            else:
                self.get_tokens_outside_struct(s)
        else:
            if s[0] == RIGHT_CR_B:
                self.inside_struct = False
                self.all_tokens.append(RIGHT_CR_B)
            else:
                self.get_tokens_inside_struct(s)

    def get_tokens_before_struct(self, s):
        i = 0
        s_len = len(s)
        while i < s_len - 1:
            current_token = ""
            symbol = s[i]
            if symbol in ONE_SYMBOL_TOKENS:
                current_token = symbol
            elif symbol in DIGITS:
                while symbol in DIGITS:
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(int(current_token))
            elif symbol in LETTERS:
                while symbol in LETTERS:
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(current_token)
            i += 1

    def get_tokens_outside_struct(self, s):
        delim_found = 0
        i = 0
        s_len = len(s)
        searching_type = False
        while i < s_len:
            current_token = ""
            symbol = s[i]
            if symbol in DIGITS:
                while symbol in DIGITS:
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(int(current_token))
            elif symbol in LETTERS:
                while symbol in LETTERS or (symbol == DELIMITER and searching_type):
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(current_token)
                if current_token in [FUNC_ALIGNOF, FUNC_SIZEOF] or delim_found == 2:
                    searching_type = True
            elif symbol in ONE_SYMBOL_TOKENS:
                current_token = symbol
                if symbol == DELIMITER:
                    delim_found += 1
                if delim_found == 2:
                    searching_type = True
            i += 1

    def get_tokens_inside_struct(self, s):
        i = 0
        s_len = len(s)
        while i < s_len:
            current_token = ""
            symbol = s[i]
            if symbol in DIGITS:
                while symbol in DIGITS:
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(int(current_token))
            elif symbol in LETTERS or symbol == DELIMITER:
                while symbol in LETTERS or symbol == DELIMITER:
                    current_token += symbol
                    i += 1
                    symbol = s[i]
                i -= 1
                self.all_tokens.append(current_token)
            elif symbol in ONE_SYMBOL_TOKENS:
                current_token = symbol
            i += 1

    def get_tokens(self):
        #print(self.all_tokens)
        return self.all_tokens


class Parser:
    def __init__(self):
        self.tokens = None
        self.token_cnt = 0
        self.i = 0
        self.state = "INITIAL"

    def get_tokens(self, lexer):
        self.tokens = lexer.get_tokens()
        self.token_cnt = len(self.tokens)

    def parse(self):
        while self.i < self.token_cnt:
            if self.tokens[self.i] == FUNC_SIZEOF:
                var, n = self.get_var_name()
                ans.append(str(n * TYPES[var][0]))
                self.i += 2
            elif self.tokens[self.i] == FUNC_ALIGNOF:
                var, n = self.get_var_name()
                ans.append(str(TYPES[var][1]))
                self.i += 2
            elif self.tokens[self.i] == FUNC_TYPEDEF:
                self.define_type()

    def get_var_name(self):
        var = self.tokens[self.i + 1]
        try:
            n = self.tokens[self.i + 2]
        except:
            n = None
        if not isinstance(n, int):
            n = 1
        else:
            self.i += 1
        return var, n

    def define_type(self):
        type_name = self.tokens[self.i + 1]
        type_size = 0
        type_align = 1
        if self.tokens[self.i + 2] == STRUCT:
            self.i += 3
            while self.tokens[self.i] != RIGHT_CR_B:
                n = 1
                inner_type_name = self.tokens[self.i]
                if isinstance(self.tokens[self.i + 1], int):
                    n = self.tokens[self.i + 1]
                    self.i += 1
                # type_size += n * TYPES[inner_type_name][0]
                type_size = self.calc_size(type_size, n, inner_type_name)
                type_align = max(type_align, TYPES[inner_type_name][1])
                self.i += 1
            type_size = self.fix_size(type_size, type_align)
            TYPES[type_name] = [type_size, type_align]
        else:
            self.i += 2
            n = 1
            inner_type_name = self.tokens[self.i]
            if isinstance(self.tokens[self.i + 1], int):
                n = self.tokens[self.i + 1]
                self.i += 1
            type_size = n * TYPES[inner_type_name][0]
            type_align = TYPES[inner_type_name][1]
            type_size = self.fix_size(type_size, type_align)
            TYPES[type_name] = [type_size, type_align]
        self.i += 1

    def calc_size(self, type_size, n, type_name):
        type_align = TYPES[type_name][1]
        type_size_updated = self.fix_size(type_size, type_align)
        type_size_updated += n * TYPES[type_name][0]
        return type_size_updated

    def fix_size(self, t_size, t_align):
        rem = t_size % t_align
        if rem == 0:
            return t_size
        return t_size - rem + t_align


lexer = Lexer()
ans = []

for line in sys.stdin.buffer.read().decode().splitlines():
    lexer.split_into_tokens(line + "\n")
    #print(j, lexer.all_tokens)

parser = Parser()
parser.get_tokens(lexer)
parser.parse()

print("\n".join(ans))
