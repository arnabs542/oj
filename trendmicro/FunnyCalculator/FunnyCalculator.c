#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    L_BRACKET,
    R_BRACKET,
    ADD,
    MINUS,
    MUL,
    DIV,
    NUMBER,
    NIL
} TOKEN_TYPE;

static int next_number;
TOKEN_TYPE scanner (void){
    char c;
    while(1){
        c = fgetc(stdin);
        if (isblank(c)) {
            continue;
        }
        break;
    };
    if (c == '+') {
        return ADD;
    }
    else if (c == '-') {
        return MINUS;
    }
    else if (c == '*') {
        return MUL;
    }
    else if (c == '/') {
        return DIV;
    }
    else if (isalpha(c)) {
        next_number = (int) toupper(c) - 65;
        char x = fgetc(stdin);
        while(isalpha(x) || isblank(x)){
            if (isblank(x)) {
            x = fgetc(stdin);
                continue;
            }
            next_number *= 10;
            next_number += (int) toupper(x) - 65;
            x = fgetc(stdin);
        };
        ungetc(x, stdin);
        return NUMBER;
    }
    else if (c == '(') {
        return L_BRACKET;
    }
    else if (c == ')') {
        return R_BRACKET;
    }
    return NIL;
};

static TOKEN_TYPE next_token = NIL;
TOKEN_TYPE match(TOKEN_TYPE got_token){
    if (got_token == next_token) {
        next_token = scanner();
    }
    else {
        ;
    }
    return next_token;
}

/*
 * <expr> -> <term> { + - <term> }
 * <term> -> <factor> { * / <factor> }
 * <factor> -> N | ( <expr> )
 */
int expr(void);
int term(void);
int factor(void);

int expr(void) {
    int acc;
    acc = term();
    while (next_token == ADD || next_token == MINUS) {
        if (next_token == ADD) {
            match(ADD);
            acc += term();
        }
        else if (next_token == MINUS) {
            match(MINUS);
            acc -= term();
        };
    };
    return acc;
};

int term(void) {
    int acc;
    acc = factor();
    while (next_token == MUL || next_token == DIV) {
        if (next_token == MUL) {
            match(MUL);
            acc *= factor();
        }
        else if (next_token == DIV) {
            match(DIV);
            acc /= factor();
        };
    };
    return acc;
};

int factor(void) {
    int r;
    if (next_token == NUMBER) {
        r = next_number;
        match(NUMBER);
    }
    else if (next_token == L_BRACKET) {
        match(L_BRACKET);
        r = expr();
        match(R_BRACKET);
    }
    return r;
};

int main(void){
    match(NIL);
    printf("%d\n", expr());
    return 0;
};
