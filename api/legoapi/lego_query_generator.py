 # dirty
def get_lego_query_payload(keyword):
    query = {
            "_source": [
                "product_number",
                "locale.en-us",
                "locale.en-us",
                "market.us.skus.item_id",
                "market.us.skus.item_id",
                "availability",
                "themes",
                "product_versions",
                "assets"
            ],
            "from": 0,
            "size": 3,
            "query": {
                "bool": {
                    "must": [],
                    "should": [
                    ],
                    "filter": [
                        {
                            "bool": {
                                "should": [
                                    {
                                        "exists": {
                                            "field": "product_versions.building_instructions"
                                        }
                                    },
                                    {
                                        "range": {
                                            "availability.launchDate": {
                                                "gte": "2025-01-21T01:10:47.561Z"
                                            }
                                        }
                                    }
                                ],
                                "minimum_should_match": 1
                            }
                        }
                    ],
                    "minimum_should_match": 1
                }
            },
            "highlight": {
                "pre_tags": [
                    "<span class=\"keyword\">"
                ],
                "post_tags": [
                    "</span>"
                ],
                "fields": {
                    "*": {
                        "number_of_fragments": 1
                    }
                }
            },
            "aggs": {
                "themes": {
                    "terms": {
                        "field": "themes.id",
                        "size": 200
                    },
                    "aggs": {
                        "theme": {
                            "top_hits": {
                                "_source": {
                                    "includes": [
                                        "themes.id",
                                        "themes.locale.en-us",
                                        "themes.locale.en-us",
                                        "themes.isSubtheme",
                                        "themes.title"
                                    ]
                                },
                                "size": 1
                            }
                        }
                    }
                },
                "years": {
                    "date_histogram": {
                        "field": "availability.launchDate",
                        "interval": "year",
                        "format": "yyyy",
                        "min_doc_count": 1
                    }
                }
            }
    }
    query["query"]["bool"]["should"].append(create_match_query(keyword))
    query["query"]["bool"]["should"].append(create_match_query(keyword))
    print(query)
    return query

    
def create_match_query(query):
    match_query = {
            "multi_match": {
                "type": "best_fields",
                "query": "", # empty
                "fields": [
                    "locale.en-us.title",
                    "locale.en-us.description"
                ]
            }
        }
    match_query["multi_match"]["query"] = query

    return match_query