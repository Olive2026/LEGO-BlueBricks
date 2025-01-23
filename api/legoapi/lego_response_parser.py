# extract what I need
# what I need to extract: total number, list of object with name, description, first prod image, manual image, and manual link
def parse_response(data):
    print(data["_shards"]["successful"])