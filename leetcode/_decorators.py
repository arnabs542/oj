#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A decorator is a callable that receives a function as argument,
and returns a callable closure to implement decorator pattern (design pattern).

A decorator can receive parameters and it must return another callable
that takes a function as parameter, and return a callable.

"""

from functools import partial
import time

class memoizeMethod(object):
    """
    Cache the return value of a function, including a class method.

    This class is meant to be used as a decorator of methods. The return value
    from a given method invocation will be cached on the instance whose method
    was invoked. All arguments passed to a method decorated with memoize must
    be hashable.

    If a memoized method is invoked directly on its class the result will not
    be cached. Instead the method will be invoked like a static method:
    class Obj(object):
        @memoize
        def add_to(self, arg):
            return self + arg
    Obj.add_to(1) # not enough arguments
    Obj.add_to(1, 2) # returns 3, result is not cached
    """

    def __init__(self, func):
        super().__init__()
        self.func = func

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return partial(self, obj)

    def __call__(self, *args, **kw):
        obj = args[0]
        try:
            cache = obj.__cache
        except AttributeError:
            cache = obj.__cache = {}
        key = (self.func, args[1:], frozenset(kw.items()))
        try:
            res = cache[key]
        except KeyError:
            res = cache[key] = self.func(*args, **kw)
        return res

class memoize:
    '''
    Memoize Decorator.

    Caches a function's return value using its arguments as key.

    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]

def timeit(method):
    '''
    A Python decorator for measuring the execution time of methods
    '''

    def timed(*args, **kw):
        '''
        closure
        '''
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        # print('%2.2f milliseconds elapsed, function: %r params: (%r, %r) ' %
              # ((te - ts) * 1000, method.__name__, args, kw))
        print('function: %r returned in %2.2fms' %
              (method.__name__, (te - ts) * 1000))
        return result

    return timed

def safeRun(msg):
    """
    Safely run a function, with try except, and print out custom message.

    It need to be implemented with nested closure.
    """
    def f(func):
        def decorated(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print("ERROR msg: {msg}, exception: {exception}".format(msg=msg, exception=e))

        return decorated
    return f


def test():

    # TEST memoize decorator
    # example usage
    class Test(object):
        v = 0

        @memoizeMethod
        def inc_add(self, arg):
            self.v += 1
            return self.v + arg

    t = Test()
    assert t.inc_add(2) == t.inc_add(2)
    assert Test.inc_add(t, 2) != Test.inc_add(t, 2)

    # TEST timeit decorator
    class Foo(object):

        @timeit
        def foo(self, a=2, b=3):
            time.sleep(0.2)

    @timeit
    def f1():
        time.sleep(1)
        print('f1')

    @timeit
    def f2(a):
        # time.sleep(0.2)
        print('f2', a)

    @timeit
    def f3(a, *args, **kw):
        time.sleep(0.3)
        print('f3', args, kw)

    f1()
    f2(42)
    f3(42, 43, foo=2)
    Foo().foo()

    @safeRun('ERROR CATCHED!')
    def errorFunc():
        raise Exception("errorFunc run error")

    errorFunc()

    print("self test passed")


if __name__ == "__main__":
    test()
