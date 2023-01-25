from elasticsearch import Elasticsearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("ELASTICSEARCH_USERNAME")
password = os.environ.get("ELASTICSEARCH_PASSWORD")

es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=(username, password),
    verify_certs=False,
    ca_certs='./rootCA.pem',
    client_cert='./client.pem',
    client_key='./client.key',
)

def es_search(body):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body=body)
	return results


def T2S_basic_search(metaphores_meaning=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"match": {
						"metaphores.meaning" : metaphores_meaning
					}
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def S2T_basic_search(metaphores_meta=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"match": {
						"metaphores.meta" : metaphores_meta
					}
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def T2S_inner_hits_search(metaphores_meaning=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"match": {
						"metaphores.meaning" : metaphores_meaning
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def S2T_inner_hits_search(metaphores_meta=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"match": {
						"metaphores.meta" : metaphores_meta
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def T2S_fuzzy_match_inner_hits_search(metaphores_meaning=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"fuzzy": {
						"metaphores.meaning": {
							"value": metaphores_meaning,
							"fuzziness": 2
						}
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def S2T_fuzzy_match_inner_hits_search(metaphores_meta=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
				"path": "metaphores",
				"query": {
					"fuzzy": {
						"metaphores.meta": {
							"value": metaphores_meta,
							"fuzziness": 2
						}
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def T2S_phrase_match_slop_inner_hits_search(metaphores_meaning=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
			"path": "metaphores",
				"query": {
					"match_phrase": {
						"metaphores.meaning" : {
							"query":metaphores_meaning,
							"slop":2,
							"prefix_length":1,
							"max_expansions":10
						}
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def S2T_phrase_fuzzy_match_slop_inner_hits_search(metaphores_meta="", slop=None, 
prefix_length=1, max_expansion=10):
	if not slop:
		slop = int(len(metaphores_meta.split())/5)
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested": {
			"path": "metaphores",
				"query": {
					"match_phrase": {
						"metaphores.meta" : {
							"query":metaphores_meta,
							"slop":slop,
							"prefix_length":prefix_length,
							"max_expansions":max_expansion
						}
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def T2S_more_like_inner_hits_search(metaphores_meaning=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested" : {
				"path" : "metaphores",
				"query" : {
					"more_like_this" : {
						"fields" : ["metaphores.meaning"],
						"like" : metaphores_meaning,
						"min_term_freq" : 1,
						"max_query_terms" : 12
					}
				},
				"inner_hits": {
					"_source": ["metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results

def S2T_more_like_inner_hits_search(metaphores_meta=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"nested" : {
				"path" : "metaphores",
				"query" : {
					"more_like_this" : {
						"fields" : ["metaphores.meta"],
						"like" : metaphores_meta,
						"min_term_freq" : 1,
						"max_query_terms" : 12
					}
				},
				"inner_hits": {
					"_source": ["singer","lyrics","metaphores.meta", "metaphores.meaning"]
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results

def lyrics_more_like_search(phrase=""):
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"more_like_this" : {
				"fields" : ["lyrics"],
				"like" : phrase,
				"min_term_freq" : 1,
				"max_query_terms" : 12,
				"boost_terms" : 2.0
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


def lyrics_phrase_search(phrase="",slop=None):
	if not slop:
		slop = int(len(phrase.split())/5)
	results = es.search(index=os.environ.get("ELASTICSEARCH_INDEX"), body={
		"query": {
			"match_phrase": {
				"text": {
					"query": phrase,
					"slop": slop,
				}
			}
		},
		"sort": [
			{
				"_score": {
					"order": "desc"
				}
			}
		]
	})

	return results


