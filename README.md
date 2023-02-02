# Sinhala_metaphore_search_IR_mini_project

## Setting Up

### Clone the Repository

### Install Elasticsearch plugins

`$ ./bin/elasticsearch-plugin install analysis-icu`

`$ ./bin/elasticsearch-plugin install analysis-phonetic`

### Add index 

From `index/index.json` file, insert mappings and settings

```json
{
  "ss_100": {
    "aliases": {},
    "mappings": {
      "_meta": {
        "created_by": "file-data-visualizer"
      },
      "properties": {
        "index": {
          "type": "long"
        },
        "lyrics": {
          "type": "text",
          "analyzer": "icu_edge_ngram_analyzer"
        },
        "meta_phonetics": {
          "type": "nested",
          "properties": {
            "meta": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "phonetic": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "metaphores": {
          "type": "nested",
          "properties": {
            "meaning": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "meta": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "singer": {
          "type": "text"
        },
        "title": {
          "type": "text"
        }
      }
    },
    "settings": {
      "index": {
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_content"
            }
          }
        },
        "number_of_shards": "1",
        "provided_name": "ss_100",
        "creation_date": "1674662222176",
        "analysis": {
          "filter": {
            "sin_stop": {
              "type": "stop",
              "stopwords": [
                "සහ",
                "සමග",
                "සමඟ",
                "අහා",
                "ආහ්",
                "ආ",
                "ඕහෝ",
                "අනේ",
                "අඳෝ",
                "අපොයි",
                "අපෝ",
                "අයියෝ",
                "ආයි",
                "ඌයි",
                "චී",
                "චිහ්",
                "චික්",
                "හෝ‍",
                "දෝ",
                "දෝහෝ",
                "මෙන්",
                "සේ",
                "වැනි",
                "බඳු",
                "වන්",
                "අයුරු",
                "අයුරින්",
                "ලෙස",
                "වැඩි",
                "ශ්‍රී",
                "හා",
                "ය",
                "නිසා",
                "නිසාවෙන්",
                "බවට",
                "බව",
                "බවෙන්",
                "නම්",
                "වැඩි",
                "සිට",
                "දී",
                "මහා",
                "මහ",
                "පමණ",
                "පමණින්",
                "පමන",
                "වන",
                "විට",
                "විටින්",
                "මේ",
                "මෙලෙස",
                "මෙයින්",
                "ඇති",
                "ලෙස",
                "සිදු",
                "වශයෙන්",
                "යන",
                "සඳහා",
                "මගින්",
                "හෝ‍",
                "ඉතා",
                "ඒ",
                "එම",
                "ද",
                "අතර",
                "විසින්",
                "සමග",
                "පිළිබඳව",
                "පිළිබඳ",
                "පිලිබඳව",
                "පිලිබඳ",
                "තුළ",
                "බව",
                "වැනි",
                "මහ",
                "මෙම",
                "මෙහි",
                "මේ",
                "වෙත",
                "වෙතින්",
                "වෙතට",
                "වෙනුවෙන්",
                "වෙනුවට",
                "වෙන",
                "ගැන",
                "නෑ",
                "අනුව",
                "නව",
                "පිළිබඳ",
                "විශේෂ",
                "දැනට",
                "එහෙන්",
                "මෙහෙන්",
                "එහේ",
                "මෙහේ",
                "ම",
                "තවත්",
                "තව",
                "සහ",
                "දක්වා",
                "ට",
                "ගේ",
                "එ",
                "ක",
                "ක්",
                "බවත්",
                "බවද",
                "මත",
                "ඇතුලු",
                "ඇතුළු",
                "මෙසේ",
                "වඩා",
                "වඩාත්ම",
                "නිති",
                "නිතිත්",
                "නිතොර",
                "නිතර",
                "ඉක්බිති",
                "දැන්",
                "යලි",
                "පුන",
                "ඉතින්",
                "සිට",
                "සිටන්",
                "පටන්",
                "තෙක්",
                "දක්වා",
                "සා",
                "තාක්",
                "තුවක්",
                "පවා",
                "ද",
                "හෝ‍",
                "වත්",
                "විනා",
                "හැර",
                "මිස",
                "මුත්",
                "කිම",
                "කිම්",
                "ඇයි",
                "මන්ද",
                "හෙවත්",
                "නොහොත්",
                "පතා",
                "පාසා",
                "ගානෙ",
                "තව",
                "ඉතා",
                "බොහෝ",
                "වහා",
                "සෙද",
                "සැනින්",
                "හනික",
                "එම්බා",
                "එම්බල",
                "බොල",
                "නම්",
                "වනාහි",
                "කලී",
                "ඉඳුරා",
                "අන්න",
                "ඔන්න",
                "මෙන්න",
                "උදෙසා",
                "පිණිස",
                "සඳහා",
                "අරබයා",
                "නිසා",
                "එනිසා",
                "එබැවින්",
                "බැවින්",
                "හෙයින්",
                "සේක්",
                "සේක",
                "ගැන",
                "අනුව",
                "පරිදි",
                "විට",
                "තෙක්",
                "මෙතෙක්",
                "මේතාක්",
                "තුරු",
                "තුරා",
                "තුරාවට",
                "තුලින්",
                "නමුත්",
                "එනමුත්",
                "වස්",
                "මෙන්",
                "ලෙස",
                "පරිදි",
                "එහෙත්"
              ]
            },
            "edge_ngram_filter": {
              "type": "edge_ngram",
              "min_gram": "1",
              "max_gram": "10"
            }
          },
          "analyzer": {
            "icu_edge_ngram_analyzer": {
              "filter": [
                "lowercase",
                "sin_stop",
                "edge_ngram_filter"
              ],
              "type": "custom",
              "tokenizer": "icu_tokenizer"
            }
          },
          "tokenizer": {
            "icu_tokenizer": {
              "type": "icu_tokenizer"
            }
          }
        },
        "number_of_replicas": "1",
        "uuid": "vltFr8KDRPe1vozF-FJ6Kg",
        "version": {
          "created": "8060099"
        }
      }
    }
  }
}
```

From `index/Corpus.json` file, insert documents.

### install dependencies

`$ pip install streamlit json pandas`

or

`$ pip install -i requirements.txt`

### Run the app

`$ cd app`

`$ streamlit run app.py`