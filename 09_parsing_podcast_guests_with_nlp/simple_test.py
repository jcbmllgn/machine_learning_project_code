import feedparser

# Bulleye's podcast feed url
podcast_feed_url = "https://www.npr.org/rss/podcast.php?id=510309"

# Parse the xml feed
feed_object = feedparser.parse(podcast_feed_url)

# Grab the show description and list of episodes
show_description = feed_object.feed.description
podcast_episodes = feed_object.entries

print(show_description)

episode_summary = podcast_episodes[0].summary
print(episode_summary)