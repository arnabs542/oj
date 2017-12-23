#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow
another user and is able to see the 10 most recent tweets in the user's news feed.
Your design should support the following methods:

1. postTweet(userId, tweetId): Compose a new tweet.
2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user
herself. Tweets must be ordered from most recent to least recent.
3. follow(followerId, followeeId): Follower follows a followee.
4. unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);


==============================================================================================
SOLUTION

Determine the core data structure and algorithm for data and operation.

User tweets: HASH TABLE <userId, List<tweetId>>, O(1)
follow list: SET to enable O(1) follow and unfollow, O(1)
getNewsFeed: MIN HEAP, to get latest feed efficiently, O(1). But completely ordered is required,
so binary search tree may be better.

The problem is when a user posts a tweet, we need to update the user's tweet list and its
followers' tweet list. And when a user unfollows another one, his news feed should be updated
correspondingly: delete operation is involved.

One possible way is brute force solution. Every time getNewsFeed is called, we construct
the ordered tweets from scratch. This is a top K from m sorted list problem.

Using a heap, the time complexity for getNewsFeed: O(10*(M + logM)), where M is the number
of followees.

----------------------------------------------------------------------------------------------
TEST

Edge cases:
    - query from empty
    - remove from empty
    - add and remove
    - maximum size(full container)
    - a user follow himself(follow: two same userIds)

----------------------------------------------------------------------------------------------
OPTIMIZATION

Using collections.defaultdict will be faster than calling setdefault every time.

'''

import time
import heapq
import collections


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.users = set() # set<userId>
        # self.tweets = {} # map<userId, List<tweetId, time>>
        # self.followees = {} # <followeeUserId, set<followerUserId>>
        self.tweets = collections.defaultdict(list) # map<userId, List<tweetId, time>>
        self.followees = collections.defaultdict(set) # <followeeUserId, set<followerUserId>>
        self.tweetSequence = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # self.tweets.setdefault(userId, [])
        self.tweetSequence += 1
        self.tweets[userId].append((self.tweetSequence, tweetId)) # ascending according to time stamp


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed
        must be posted by users who the user followed or by the user herself. Tweets must be ordered
        from most recent to least recent.

        :type userId: int
        :rtype: List[int]
        """

        result = []
        userIdList = list(self.followees.get(userId, [])) + [userId]

        # heap with max size, #followees + 1
        # use tuple for custom compare key
        tweetHeap = []
        for i, uid in enumerate(userIdList):
            if 1 <= len(self.tweets.get(uid, [])):
                tweet = self.tweets[uid][-1]
                item = (-tweet[0], tweet[1], i, len(self.tweets[uid]) - 1)
                heapq.heappush(tweetHeap, item) # tuple(value, index of user, index of tweet)
        # print('heap top: ', tweetHeap and tweetHeap[0])
        while len(result) < 10 and tweetHeap:
            t, tid, i, j = tweetHeap[0]
            result.append(tid)
            if j - 1 >= 0:
                j -= 1
                tweet = self.tweets[userIdList[i]][j]
                item = (-tweet[0], tweet[1], i, j)
                heapq.heapreplace(tweetHeap, item)
            else:
                heapq.heappop(tweetHeap)

        return result


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        # self.followees.setdefault(followerId, set())
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followees:
            return
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


        # class Index(int):
            # # def __init__(self, *args, **kwargs):
                # # super().__init__(*args, **kwargs)
                # # pass

            # def __lt__(self, a):
                # return userIdList[self] < userIdList[a]
                # pass
        # indices = [0 for _ in users]
        # i = 0

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def test():
    obj = Twitter()

    feeds = obj.getNewsFeed(1)
    assert(feeds == [])
    feeds = obj.getNewsFeed(2)
    assert(feeds == [])

    obj.postTweet(1, 't11')
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t11'])

    obj.follow(1, 1) # follow himself
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t11'])

    obj.postTweet(2, 't22')
    obj.follow(1, 2)
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t22', 't11'])

    obj.unfollow(1, 2)
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t11'])

    obj.unfollow(1, 2)
    # edge case: unfollow a non-followee
    obj.unfollow(1, 2)
    obj.unfollow(1, 4)
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t11'])

    obj.follow(2, 1)
    feeds = obj.getNewsFeed(1)
    print(feeds)
    assert(feeds == ['t11'])

    feeds = obj.getNewsFeed(2)
    print(feeds)
    assert(feeds == ['t22', 't11'])

    obj.postTweet(1, 't12')
    obj.postTweet(1, 't13')
    obj.postTweet(1, 't14')
    obj.postTweet(1, 't15')
    obj.postTweet(2, 't22')
    obj.postTweet(2, 't23')
    obj.postTweet(2, 't24')
    obj.postTweet(2, 't25')
    obj.postTweet(2, 't26')
    obj.postTweet(2, 't27')
    obj.postTweet(2, 't28')
    feeds = obj.getNewsFeed(2)
    print(feeds)
    assert(feeds == ['t28', 't27', 't26', 't25', 't24', 't23', 't22', 't15', 't14', 't13'])

    print("self test passed")

if __name__ == '__main__':
    test()
