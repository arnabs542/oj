#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#include <unistd.h>

#define CAT_SYMBOLE  '\xFF'

#pragma mark - convert regular expression to NFA

char*
re2post(char *re)
{
	int nalt, natom;
	static char buf[8000];
	char *dst;
	dst = buf;
	nalt = 0;   // number of alternation
	natom = 0;  // number of atomic parts
	if(strlen(re) >= sizeof buf/2)
		return NULL;
	for(char *pre = re; *pre; pre++){
		switch(*pre){
		case '*':
			if(!natom)
				return NULL;
			*dst++ = *pre;
			break;
		default: // ATOMIC literal character
			/*maybe insert CONCATENATION*/
			if(natom > 1){
				--natom;
				*dst++ = CAT_SYMBOLE;
			}
			*dst++ = *pre;
			natom++;
			break;
		}
	}
	while(--natom > 0)
		*dst++ = CAT_SYMBOLE;
	for(; nalt > 0; nalt--)
		*dst++ = '|';
	*dst = 0;
	fprintf(stdout, "re2post: %s => %s\n", re, buf);
	fflush(stdout);
	return buf;
}

#pragma mark - REPRESENTATION

enum
{
	Match = 256,
	Split = 257
};

typedef struct State State;
struct State
{
	int c;			// the character
	State *out;		// a outgoing linked state
	State *out1;	// another outgoing linked state
	int lastlist;	// used during execution
};

State matchstate = { Match };	/* matching state */
int nstate;

/* Allocate and initialize State */
State*
state(int c, State *out, State *out1)
{
	State *s;

	nstate++;
	s           = malloc(sizeof *s);
	s->lastlist = 0;
	s->c        = c;
	s->out      = out;
	s->out1     = out1;
	return s;
}

typedef struct Frag Frag;
typedef union Ptrlist Ptrlist;
struct Frag
{
	State *start;	// points at the start state
	Ptrlist *out;	// list of dangling outgoing arrows not yet connected to anything
};

/* Initialize Frag struct. */
Frag
frag(State *start, Ptrlist *out)
{
	Frag n = { start, out };
	return n;
}

/*
 * Since the out pointers in the list are always
 * uninitialized, we use the pointers themselves
 * as storage for the Ptrlists.
 */
union Ptrlist
{
	Ptrlist *next;
	State *s;
};

#pragma mark - HELPER FUNCTIONS TO MANIPULATE POINTER LISTS

/* Create singleton list containing just outp. */
Ptrlist*
list1(State **outp)
{
	Ptrlist *l;

	// take a State* pointer's address as Ptrlist* pointer's value
	// so that l->s is exactly the same as the State* pointer
	l = (Ptrlist*)outp;
	l->next = NULL;  // set the state* pointer's value to NULL
	return l;
}

/* Patch the list of states at out to point to start.
 * Connects the dangling arrows in the pointer list l to state s
 */
void
patch(Ptrlist *l, State *s)
{
	Ptrlist *next;

	for(; l; l=next){
		next = l->next;
		l->s = s;
	}
}

/* Join(concatenate) the two lists l1 and l2, returning the combination. */
Ptrlist*
append(Ptrlist *l1, Ptrlist *l2)
{
	Ptrlist *oldl1;

	oldl1 = l1;
	while(l1->next)
		l1 = l1->next;
	l1->next = l2;
	return oldl1;
}

State*
post2nfa(char *postfix)
{
	char *p;
	Frag stack[1000], *stackp, e1, e2, e;
	State *s;

	// fprintf(stderr, "postfix: %s\n", postfix);

	if(postfix == NULL)
		return NULL;
	nstate = 0;

	#define push(s) *stackp++ = s
	#define pop() *--stackp

	stackp = stack;
	for(p=postfix; *p; p++){
		switch(*p){
		default:	/* literal characters */
			/*fprintf(stdout, "literal characters: %c, %x\n", *p, *p);*/
			s = state(*p, NULL, NULL);
			push(frag(s, list1(&s->out)));
			break;
		case CAT_SYMBOLE:	/* catenate */
			e2 = pop();
			e1 = pop();
			patch(e1.out, e2.start);
			push(frag(e1.start, e2.out));
			break;
		case '*':	/* zero or more */
			e = pop();
			s = state(Split, e.start, NULL);
			patch(e.out, s);
			push(frag(s, list1(&s->out1)));
			break;
		}
	}

	e = pop();
	if(stackp != stack)
		return NULL;

	patch(e.out, &matchstate);
	return e.start;
#undef pop
#undef push
}

#pragma mark - Simulating the NFA

typedef struct List List;
struct List
{
	State **s;
	int n;
};
List l1, l2;
static int listid;

void addstate(List*, State*);
void step(List*, int, List*);

List*
startlist(State *start, List *l)
{
	l->n = 0;
	listid++;
	addstate(l, start);
	return l;
}

int
ismatch(List *l)
{
	int i;

	for(i=0; i<l->n; i++)
		if(l->s[i] == &matchstate)
			return 1;
	return 0;
}

void
addstate(List *l, State *s)
{
	if(s == NULL || s->lastlist == listid)
		return;
	s->lastlist = listid;
	if(s->c == Split){
		/* follow unlabeled arrows */
		addstate(l, s->out);
		addstate(l, s->out1);
		return;
	}
	l->s[l->n++] = s;
}

void
step(List *clist, int c, List *nlist)
{
	int i;
	State *s;

	listid++;
	nlist->n = 0;
	for(i=0; i<clist->n; i++){
		s = clist->s[i];
		if(s->c == c || s->c == '.')
			addstate(nlist, s->out);
	}
}

int
match(State *start, char *s)
{
	int c;
	List *clist, *nlist, *t;

	/* l1 and l2 are preallocated globals to avoid allocation on every iteration */
	clist = startlist(start, &l1);
	nlist = &l2;
	for(; *s; s++){
		c = *s;
		step(clist, c, nlist);
		t = clist; clist = nlist; nlist = t;	/* swap clist, nlist */
	}
	return ismatch(clist);
}

// match string with a regular expression
bool
rematch(char *re, char *s)
{
    if (!strlen(re) && !strlen(s))
		return true;

	char *post   = re2post(re);
	State *start = post2nfa(post);

	l1.s = malloc(nstate * sizeof l1.s[0]);
	l2.s = malloc(nstate * sizeof l2.s[0]);

	bool result = match(start, s);

	return result;
}

bool
isMatch(char *s, char *p)
{
    return rematch(p, s);
}

void test()
{
	assert(isMatch("", ""));
	assert(isMatch("a", "a"));
	/*assert(isMatch("你*好", "好"));*/
	assert(!isMatch("abc", "abx"));
	assert(isMatch("aa", ".*"));
	assert(isMatch("", ".*"));
	assert(isMatch("", "a*"));
	assert(isMatch("a", "a**"));
	assert(isMatch("aab", "c*a*b*"));
	assert(!isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"));
	assert(isMatch("aaab", "a*a*a*c*b*"));
	assert(isMatch(
		    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
		    ,
		    "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
		    "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
		    "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
		    "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
		    "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*b*b"
		    ));
	fprintf(stdout, "self test passed!\n");
	fflush(stdout);
}

int main()
{
	test();
}
