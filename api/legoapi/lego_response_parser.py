# extract what I need
# what I need to extract: total number, list of object with name, description, first prod image, manual image, and manual link
def parse_response(data):
    total = data["hits"]["total"]["value"]
    print("total = {}".format(total))

    manuals = []

    for manual in data["hits"]["hits"]:
        manual_object = create_manual(manual)
        if manual_object != None :
            manuals.append(manual_object)
    
    return {
        "totals":total,
        "manuals":manuals
    }


def create_manual(raw_manual):

    try:
        latest_product_version = raw_manual["_source"]["product_versions"][-1]
        manual_pdf = latest_product_version["building_instructions"][0]["file"]["url"]
        manual_img = latest_product_version["building_instructions"][0]["image"]["url"]

        image = raw_manual["_source"]["assets"][0]["assetFiles"][0]["url"]
        product_num = raw_manual["_source"]["product_number"]
        manufacture_date = raw_manual["_source"]["availability"]["launchDate"]
        lego_group = raw_manual["_source"]["themes"][0]["locale"]["en-us"]["display_title"]
        title = raw_manual["_source"]["locale"]["en-us"]["title"]

        return {
            "title":title,
            "cover_image":image,
            "manual_url":manual_pdf,
            "manual_image":manual_img,
            "product_num":product_num,
            "manufacture_date":manufacture_date,
            "lego_group":lego_group
         }
         # this is a map
    except IndexError:
        return None
    # -1 shows very last object


# The first item in product versions that contians a bulding isntrcution with outh the warning on it
# .... need to check whether this is same for others