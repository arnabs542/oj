/**
 *
 *
359.Logger Rate Limiter
Easy

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

SOLUTION
================================================================================

1. Hash - keep track of last time logged

Complexity: O(1)

2. Hash - keep track of next earliest time allowed to log

Complexity: O(1)

 *
 */

#include <debug.hpp>

class Logger {
public:
    Logger() {}

    bool shouldPrintMessage(int timestamp, string message) {
        bool result;
        //result = shouldPrintMessageHash(timestamp, message);
        result = shouldPrintMessageHashAllowedTime(timestamp, message);

        cout << timestamp << " " << message << " " << result << endl;

        return result;
    }

    bool shouldPrintMessageHash(int timestamp, string message) {
        if (!mTable.count(message) || timestamp - mTable[message] >= 10) {
            mTable[message] = timestamp;
            return true;
        }
        return false;
    }

    bool shouldPrintMessageHashAllowedTime(int timestamp, string message) {
        if (timestamp < mTable[message]) return false;
        mTable[message] = timestamp + 10;

        return true;
    }

private:
    unordered_map<string, int> mTable;
};

int test() {
    Logger logger;

    // logging string "foo" at timestamp 1
    assert(logger.shouldPrintMessage(1, "foo") == true);

    // logging string "bar" at timestamp 2
    assert(logger.shouldPrintMessage(2,"bar") == true);

    // logging string "foo" at timestamp 3
    assert(logger.shouldPrintMessage(3,"foo") == false);

    // logging string "bar" at timestamp 8
    assert(logger.shouldPrintMessage(8,"bar") == false);

    // logging string "foo" at timestamp 10
    assert(logger.shouldPrintMessage(10,"foo") == false);

    // logging string "foo" at timestamp 11
    assert(logger.shouldPrintMessage(11,"foo") == true);

    cout << "test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    return test();
}
