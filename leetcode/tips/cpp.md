# To avoid memory leak, we have to manage it properly

## [RAII(Resource Acquisition is Initialization)](http://en.wikipedia.org/wiki/RAII)

## [Smart Pointers](https://en.wikipedia.org/wiki/Smart_pointer)

## STL containers will take care of element pointers' release automatically

## Coding tricks

### Macros

```cpp
#define DEBUG_NEW new(__FILE__, __LINE__)
#define new DEBUG_NEW
```
