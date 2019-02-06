import spacy, feedparser
from collections import defaultdict

nlp = spacy.load('en_core_web_lg')


def extract_people(doc):
    # Merge any entities that are split across tokens
    for ent in doc.ents:
        ent.merge()

    # Get a list of all the people mentioned in the text.
    people_names = [entity.text for entity in doc.ents if entity.label_ == "PERSON"]

    # Filter out names that aren't both a first and last name.
    people_names = [name for name in people_names if len(name.split(" ")) == 2]

    # Converting the list to a set removes any duplicate names.
    return list(set(people_names))


# Parse the podcast feed
feed_object = feedparser.parse("https://www.npr.org/rss/podcast.php?id=510309")

# Grab the show description and list of episodes
show_description = feed_object.feed.description
podcast_episodes = feed_object.entries

# Grab the hosts of the show from the show description
doc = nlp(show_description)
hosts = extract_people(doc)

# Create dictionaries to track appearances
appearance_count = defaultdict(int)
appearance_list = defaultdict(list)

# Loop through each episode in the podcast feed
for episode in podcast_episodes:
    # Grab the episode's title and description text
    episode_title = episode.title
    episode_description = episode.summary

    # Get a list of people that appear in the show description
    doc = nlp(episode_description)
    people_in_episode = extract_people(doc)

    # Record who appeared in the episode (if they aren't a host)
    for person in people_in_episode:
        if person not in hosts:
            appearance_count[person] += 1
            appearance_list[person].append(episode_title)

# Now let's find the Top 3 most frequent guests on this podcast:
most_frequent_guests = sorted(appearance_count, key=appearance_count.get, reverse=True)[0:3]

# Print out the results
print(f"Show hosts: {hosts}")

for person in most_frequent_guests:
    # Next, let's look up all the specific episodes that a particular person appeared on:
    print(f"{person} appeared on the following episodes:")

    for episode_title in appearance_list[person]:
        print(" - {}".format(episode_title))

    print()
