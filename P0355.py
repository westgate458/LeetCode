#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:31:28 2019

@author: Tianqi Guo
"""

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        if userId not in self.users:
            self.users[userId] = {'follows':set([userId]),'posts':[]}
        self.users[userId]['posts'].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            self.users[userId] = {'follows':set([userId]),'posts':[]}
        
        posts = [], []
        for user in self.users[userId]['follows']:
            posts += self.users[user]['posts']
     
        return [post[1] for post in sorted(posts,reverse=True)[:10]]
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users:
            self.users[followerId] = {'follows':set([followerId]),'posts':[]}
                
        if followeeId not in self.users:
            self.users[followeeId] = {'follows':set([followeeId]),'posts':[]}
        
        self.users[followerId]['follows'].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId and followerId in self.users and followeeId in self.users[followerId]['follows']:
            self.users[followerId]['follows'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)