import json


def process_result(response,q_type):
    # response = json.loads(response_string) # convert the response string to json

    table = []

    if q_type == "meta" or q_type == "meaning":
        for hit in response['hits']['hits']:
            singer = hit['_source']['singer']
            lyrics = hit['_source']['lyrics']
            for inner_hit in hit['inner_hits']['metaphores']['hits']['hits']:
                # try:
                meta = inner_hit['_source']['meta']
                # except Exception:
                    # meta = ""
                meaning = inner_hit['_source']['meaning']
# 
                table.append({"Singer":singer,"Lyrics":lyrics,"Metaphore":meta,"Meaning":meaning})

    else:
        for hit in response['hits']['hits']:
            singer = hit['_source']['singer']
            lyrics = hit['_source']['lyrics']
            table.append({"Singer":singer,"Lyrics":lyrics})

    return table

                # print(f"singer: {singer}, lyrics: {lyrics}, meta: {meta}, meaning: {meaning}")
        