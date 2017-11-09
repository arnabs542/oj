#include <functional>
#include <map>
#include <iostream>

using namespace std;
/*
 *
 * memoized decorator.
 *
 * implemented uses factory design pattern.
 */
template <typename ReturnType, typename... Args>
class Memoized {
    map<tuple<Args...>, ReturnType> cache; // hash table to cache/memoize the function result
    function<ReturnType(Args...)> fn; // the function that will execute the real logic

    public:
    Memoized(function<ReturnType(Args...)> _fn): fn(_fn) {}

    ReturnType operator() (Args... args)
    {
        //cout << "function called" << endl;
        tuple<Args...> key = make_tuple(args...);
        if (cache.find(key) != cache.end()) {
            //cout << "key found" << endl;
            return cache[key];
        }
        return cache[key] = fn(args...);
    }

    bool contains(Args... args) {
        return cache.count(make_tuple(args...));
    }
};

template <typename ReturnType, typename... Args>
std::function<ReturnType (Args...)>
memoize(function<ReturnType (Args...)> func)
{
    std::map<std::tuple<Args...>, ReturnType> cache;
    return ([=](Args... args) mutable {
            std::tuple<Args...> t(args...);
            if (cache.find(t) == cache.end())
                cache[t] = func(args...);
            return cache[t];
    });
}
