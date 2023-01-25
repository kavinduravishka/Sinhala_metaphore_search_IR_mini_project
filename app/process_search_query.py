import re
import json
# import es

def process_search_query(query):
    possible_keywords = {}
    possible_keywords["artist"] = ['ගායකයා', 'ගයනවා', 'ගායනා', 'ගැයු', "ගැයූ", 'ගයන', 'ගයපු', 'කියපු', 'කියන']
    possible_keywords["artist_names"] = ["කරුණාරත්න", "දිවුල්ගනේ", "ටී", "එම්", "ජයරත්න", "ගුණදාස","කපුගේ",
     "ඩබ්ලිව්", "ඩී", "අමරදේව", "සනත්", "නන්දසිරි", "එඩ්වඩ්", "ජයකොඩි", "වික්ටර්", "රත්නායක"]
    possible_keywords["meta"] = ["උපමා", "රූපක","රූපකයන්", "උපමාවන්" , "උපමාව", "ව්‍යන්ගාර්තයන්", "ව්‍යන්ගාර්තය", "ව්‍යන්ගාර්ත", "පිළිබඳව","පිළිබඳ", "පිලිබඳව", "පිලිබඳ", ]
    possible_keywords["meaning"] = ["උපමේයන්", "උපමේය", "රූපිතයන්", "රූපිතය", "රූපිත", "උපමාවල", "තේරුම", "අර්ථය", "අර්තය"]
    

    stopwords = ["සහ","සමග","සමඟ","සඳහා",
        "විසින්","සමග", "පිළිබඳව","පිළිබඳ", "පිලිබඳව", "පිලිබඳ", "තුළ","බව","වැනි","මහ",
        "වෙනුවෙන්","වෙනුවට","ගැන","පිළිබඳ",
        "හෙවත්","නොහොත්",
        "උදෙසා","පිණිස","සඳහා","ගැන"]

    tokens = query.strip().split(" ")

    frequent_words = ['ගීත', 'සින්දු', 'ගී', 'ගීය', 'ගීතය', 'සින්දුව',"ගීතවල"]

    singer=[]
    for token in tokens:
        if token in possible_keywords["artist_names"]:
            singer.append(token.strip())

    out_query = ""
    for token in tokens:
        try:
            count = int(token)
            continue
        except Exception:
            pass
        if any(token in l for l in [possible_keywords["artist"],possible_keywords["artist_names"],possible_keywords["meaning"],possible_keywords["meta"],stopwords,frequent_words]):
            continue
        else:
            out_query += token + " "

    out_query = out_query.strip()

    meaning_flag = False
    for token in tokens:
        if token in possible_keywords["meaning"]:
            meaning_flag =True
            break
    
    metaphore_flag=False
    for token in tokens:
        if token in possible_keywords["meta"]:
            metaphore_flag=True
            break

    count = -1
    for token in tokens:
        try:
            count = int(token)
            break
        except Exception:
            pass

    return {"singer":singer,"out_query":out_query,"metaphore_flag":metaphore_flag,"meaning_flag":meaning_flag, "counts":count}




def generate_query(query):
    query_data = process_search_query(query)

    elastic_query_body = {
        "query":{
            "bool":{
                "must":[

                ]
            }
        },
        "sort": [
            {
                "_score": {
                    "order": "desc"
                }
            }
        ]
    }

    if query_data["counts"] > 0:
        elastic_query_body["size"] = query_data["counts"]

    
    if len(query_data["singer"]) > 0:
        dis_max= {
            "queries": [],
            "tie_breaker": 1
        }

        for singer in query_data["singer"]:
            dis_max["queries"].append({"match":{"singer":singer}})

        elastic_query_body["query"]["bool"]["must"].append({"dis_max" : dis_max})


    if query_data["metaphore_flag"]:
        if query_data["out_query"] != "":
            nested = {
                "path": "metaphores",
                "query": {
                        "match": {
                        "metaphores.meaning" : query_data["out_query"]
                    }
                },
                "inner_hits": {
                    "_source": ["metaphores.meta","metaphores.meaning"]
                }
            }
        else:
            nested = {
                "path": "metaphores",
                "query": {
                        "match_all": {}
                },
                "inner_hits": {
                    "_source": ["metaphores.meaning","metaphores.meta"]
                }
            }
        q_type = "meta"
        elastic_query_body["query"]["bool"]["must"].append({"nested":nested})

    elif query_data["meaning_flag"]:
        if query_data["out_query"] != "":
            nested = {
                "path": "metaphores",
                "query": {
                        "match": {
                        "metaphores.meta" : query_data["out_query"]
                    }
                },
                "inner_hits": {
                    "_source": ["metaphores.meta","metaphores.meaning"]
                }
            }
        else:
            nested = {
                "path": "metaphores",
                "query": {
                        "match_all": {}
                },
                "inner_hits": {
                    "_source": ["metaphores.meta","metaphores.meaning"]
                }
            }
        q_type = "meaning"
        elastic_query_body["query"]["bool"]["must"].append({"nested":nested})

    else:
        q_type = "lyrics"
        elastic_query_body["query"]["bool"]["must"].append({"match":{"lyrics" : query_data["out_query"]}})

    
    print(elastic_query_body)
    return {"body":elastic_query_body,"type":q_type}


# print(generate_query("සනත් නන්දසිරි විසින් ගැයූ උපමා"))