import java.io.IOException;
import java.io.PushbackInputStream;

public class Task {
	private static enum TOKEN_TYPE {
		L_BRACKET,
		R_BRACKET,
		ADD,
		MINUS,
		MUL,
		DIV,
		NUMBER,
		NIL
	}

	static int next_number;

	static PushbackInputStream pis = new PushbackInputStream(System.in);

	private static TOKEN_TYPE scanner() throws IOException {
		int c;
		while (true) {
			c = pis.read();
			if (Character.isWhitespace(c)) {
				continue;
			}
			break;
		};
		if (c == '+') {
			return TOKEN_TYPE.ADD;
		}
		else if (c == '-') {
			return TOKEN_TYPE.MINUS;
		}
		else if (c == '*') {
			return TOKEN_TYPE.MUL;
		}
		else if (c == '/') {
			return TOKEN_TYPE.DIV;
		}
		else if (Character.isLetter(c)) {
			next_number = Character.toUpperCase(c) - 'A';
			int x = pis.read();
			while(Character.isLetter(x) || Character.isWhitespace(x)){
				if (Character.isWhitespace(x)) {
					x = pis.read();
					continue;
				}
				next_number *= 10;
				next_number += Character.toUpperCase(x) - 'A';
				x = pis.read();
			};
			pis.unread(x);
			return TOKEN_TYPE.NUMBER;
		}
		else if (c == '(') {
			return TOKEN_TYPE.L_BRACKET;
		}
		else if (c == ')') {
			return TOKEN_TYPE.R_BRACKET;
		}
		return TOKEN_TYPE.NIL;
	}

	private static TOKEN_TYPE next_token = TOKEN_TYPE.NIL;

	private static TOKEN_TYPE match(TOKEN_TYPE got_token) throws IOException {
		if (got_token == next_token) {
			next_token = scanner();
		}
		else {
			;
		}
		return next_token;
	}

	private static int expr() throws IOException {
		int acc;
		acc = term();
		while (next_token == TOKEN_TYPE.ADD || next_token == TOKEN_TYPE.MINUS) {
			if (next_token == TOKEN_TYPE.ADD) {
				match(TOKEN_TYPE.ADD);
				acc += term();
			}
			else if (next_token == TOKEN_TYPE.MINUS) {
				match(TOKEN_TYPE.MINUS);
				acc -= term();
			};
		};
		return acc;
	}

	private static int term() throws IOException {
		int acc;
		acc = factor();
		while (next_token == TOKEN_TYPE.MUL || next_token == TOKEN_TYPE.DIV) {
			if (next_token == TOKEN_TYPE.MUL) {
				match(TOKEN_TYPE.MUL);
				acc *= factor();
			}
			else if (next_token == TOKEN_TYPE.DIV) {
				match(TOKEN_TYPE.DIV);
				acc /= factor();
			};
		};
		return acc;
	}

	private static int factor() throws IOException {
		int r = 0;
		if (next_token == TOKEN_TYPE.NUMBER) {
			r = next_number;
			match(TOKEN_TYPE.NUMBER);
		}
		else if (next_token == TOKEN_TYPE.L_BRACKET) {
			match(TOKEN_TYPE.L_BRACKET);
			r = expr();
			match(TOKEN_TYPE.R_BRACKET);
		}
		return r;
	}

	public static void main(String[] args) throws IOException {
		match(TOKEN_TYPE.NIL);
		System.out.println(String.format("%d", expr()));
	}
}

