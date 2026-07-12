class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        relevant_users = self.following[userId]|{userId}

        for followed_user in relevant_users:
            user_tweets = self.tweets[followed_user]

            if user_tweets:
                last_index = len(user_tweets) - 1
                timestamp, tweet_id = user_tweets[last_index]

                heapq.heappush(heap,(-timestamp, tweet_id, followed_user, last_index))

        while heap and len(feed) < 10:
            neg_time, tweet_id, tweet_user, index = heapq.heappop(heap)
            feed.append(tweet_id)

            previous_index = index - 1

            if previous_index >= 0:
                timestamp, previous_tweet_id = self.tweets[tweet_user][previous_index]

                heapq.heappush(heap, (-timestamp, previous_tweet_id, tweet_user, previous_index))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[follwerId].discard(followeeId)
        
