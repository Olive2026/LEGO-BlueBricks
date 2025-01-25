# extract what I need
# what I need to extract: total number, list of object with name, description, first prod image, manual image, and manual link
def parse_response(data):
    total = data["hits"]["total"]["value"]
    print("total = {}".format(total))

    manuals = []

    for manual in data["hits"]["hits"]:
        manuals.append(create_manual(manual))
    
    return {
        "totals":total,
        "manuals":manuals
    }


def create_manual(raw_manual):
    
    title = raw_manual["_source"]["locale"]["en-us"]["title"]
    return {
        "title":title
        
    }

