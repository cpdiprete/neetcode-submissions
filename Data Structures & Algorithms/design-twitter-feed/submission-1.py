class Twitter:

    def __init__(self):
        self.followers = dict()
        self.following = dict()
        self.tweets = [] # Add them to a stack,
         

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])
    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"----- all tweets: {self.tweets} ")
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.followers:
            self.followers[userId] = set()
        # need to get the 3 most recent 
        i = len(self.tweets) - 1
        tweetsFeed = []
        if len(self.tweets) == 0:
            return tweetsFeed
        while i >= 0 and len(tweetsFeed) < 10:
            curTweeter = self.tweets[i][0]
            if curTweeter in self.following[userId] or curTweeter == userId:
                tweetsFeed.append(self.tweets[i][1])
            i -= 1
        print(f"users following: {self.following[userId]}")
        return tweetsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId want to follow followeeID
        if followerId not in self.following:
            self.following[followerId] = set()
        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        self.following[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId unfollows followeeId
        # remove follower from self.followers[followeeId]
        # remove followeeID from self.following[followerId] 
        # print(f"prior to unfollow {self.following[followerId]}")
        # print(f"After unfollow {self.following[followerId]}")
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)