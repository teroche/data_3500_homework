# Step 1: import required libraries
import json
import requests

# Step 2: set up the URL
url = "https://api.datamuse.com/words?rel_trg=cow"

# Step 3: send the request
req = requests.get(url)

# Step 4: convert JSON text into a Python object (list of dictionaries)
dct1 = json.loads(req.text)

# Step 5: loop through each dictionary in the list
for word in dct1:
    
    # Step 6: check if the word is "cheese"
    if word["word"] == "cheese":
        
        # Step 7: print the word and its score
        print(word["word"], word["score"])
