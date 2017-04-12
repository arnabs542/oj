# Memory Management

## [RAII(Resource Acquisition is Initialization)](http://en.wikipedia.org/wiki/RAII)
Resource is hold only in the life cycle.

### [Smart Pointers](https://en.wikipedia.org/wiki/Smart_pointer)
Smart pointers are RAII classes implemented with REFERENCE COUNTING.
Most of crash bugs are caused by referencing a destructed object.
1. Parent-child relation: avoid CIRCULAR REFERENCES of shared_ptr!
2. Pass shared_ptr instead of raw pointers
3. For asynchronous/multi-threaded programs, pass shared_ptr consistently.

# Architecture

## Architecture as a collection of Data Structures

## Use STATE MACHINE, instead of nested callback functions!
Callback hell is evil!

## Parse STATE/DATA, instead of using callback functions

## Synchronize data between threads using lock, signal, variables

## Encapsulate low-level resources as classes, and wrap objects with shared_ptr to manage the resource releasing automatically

## Implement getter and setter methods, if properties are from member objects, not member variables

## Thread safety, thread synchronization


# [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern)
- Creational patterns
	- Singleton: Ensure a class has only one instance, and provide a global point of access to it.
	- Resource acquisition is initialization (RAII): Ensure that resources are properly released by tying them to the lifespan of suitable objects
	- 
- Structural patterns
	- Decorator: Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.
- Behavioural patterns
	- State: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
	- Iterator: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
	- Observer: Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.
	- Null object: Avoid null references by providing a default object.
- Concurrency patterns
	- Lock: One thread puts a "lock" on a resource, preventing other threads from accessing or modifying it.
	- Thread pool: A number of threads are created to perform a number of tasks, which are usually organized in a queue. Typically, there are many more tasks than threads. Can be considered a special case of the object pool pattern.
	- Thread-specific storage: Static or "global" memory local to a thread.



# Common bugs
1. Most of crashes are due to wrong/NULL pointers
2. NULL pointers appear when not initialized, sub-routines return NULL, objects destructed early!
3. Jittering problem
Memory unstable: occupied with other data! This is likely due to objects are
destructed early, watch the life cycle of objects!
4. For NUMERICAL computation programs, pay attention to MEMORY allocation and input DATA FORMAT!
5. In multi-threaded scenario, an asynchronous thread referencing an object that may be destroyed by another object.
Solution:
- Use shared_ptr as strong reference to that object to keep it from being released
- Use weak_ptr to check whether it has expired

```c++
// weak_ptr::expired example
#include <iostream>
#include <memory>

int main () {
  std::shared_ptr<int> shared (new int(10));
  std::weak_ptr<int> weak(shared);

  std::cout << "1. weak " << (weak.expired()?"is":"is not") << " expired\n";

  shared.reset();

  std::cout << "2. weak " << (weak.expired()?"is":"is not") << " expired\n";

  return 0;
```

### Coding tricks

#### STL containers will take care of elements' release automatically, but not allocated memory

#### Macros

```cpp
#define DEBUG_NEW new(__FILE__, __LINE__)
#define new DEBUG_NEW

```

