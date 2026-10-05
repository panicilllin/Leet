"""
359. Logger Rate Limiter
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
"""

class Logger:
    def __init__(self):
        self.dict = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = timestamp
            return True
        else:
            if timestamp - self.dict.get(message) >= 10:
                self.dict[message] = timestamp
                return True
            else:
                return False


if __name__ == '__main__':
    a = Logger()
    print(a.shouldPrintMessage(1, "foo"))
    print(a.shouldPrintMessage(2,"bar"))
    print(a.shouldPrintMessage(3,"foo"))
    print(a.shouldPrintMessage(8,"bar"))
    print(a.shouldPrintMessage(10,"foo"))
    print(a.shouldPrintMessage(11,"foo"))