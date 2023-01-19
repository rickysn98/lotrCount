import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Load the text data from a txt file
with open("data_books/TheFellowshipOfTheRing.txt", "r", encoding = "ISO-8859-1") as f:
    books_data = f.read()

# Tokenize the text data
books_data = word_tokenize(books_data)

# Convert all words to lowercase
books_data = [word.lower() for word in books_data]

# Remove punctuation
books_data = [word.translate(str.maketrans('', '', string.punctuation)) for word in books_data]

# Remove stop words
stop_words = set(stopwords.words("english"))
books_data = [word for word in books_data if word not in stop_words]

# Count the occurrences of specific characters
characters = ["frodo", "sam", "merry", "pippin", "aragorn", "boromir", "legolas", "gimli", "gandalf"]
char_count = {char: books_data.count(char) for char in characters}
char_count = pd.DataFrame.from_dict(char_count, orient='index', columns=['count'])
char_count = char_count.sort_values(by='count', ascending=False)

# Plot the character counts
char_count.plot(kind="bar", color="green")
plt.xlabel("Character")
plt.ylabel("Count")
plt.title("Mentions of characters in the Fellowship of the Ring")
plt.show()

# Count the occurrences of specific locations
locations = ["hobbiton", "rivendell", "edoras", "tirith", "mordor", "helm's", "rohan"]
loc_count = {}
for location in locations:
    loc_count[location] = books_data.count(location)
loc_count = pd.DataFrame.from_dict(loc_count, orient='index', columns=['count'])
loc_count = loc_count.sort_values(by=['count'], ascending=False)

# Plot the location counts
loc_count.plot(kind="bar", color="blue")
plt.xlabel("Location")
plt.ylabel("Count")
plt.title("Mentions of locations in the Fellowship of the Ring")
plt.show()
