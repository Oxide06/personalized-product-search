# Personalized Product Search

A search engine for Amazon Electronics products that combines classical information retrieval and semantic search.

## Features

### V1

* Amazon Electronics dataset
* BM25 retrieval
* Product indexing
* Interactive CLI

### V2

* Sentence Transformers
* Dense embeddings
* FAISS vector search
* Semantic retrieval

## Dataset

Amazon Reviews 2023 Electronics Metadata

Products Indexed:

* 10,000 products (semantic search)
* 50,000 products (BM25)

## Architecture

### BM25

Query -> Tokenization -> BM25 -> Results

### Semantic Search

Query -> MiniLM Embedding -> FAISS -> Results

## Example

Query:

gaming mouse

Semantic Search retrieves products that are conceptually related even when exact keywords differ.

Example:

wireless pointer

can retrieve:

* wireless mouse
* presenter mouse
* optical pen mouse

## Tech Stack

* Python
* Pandas
* Rank-BM25
* Sentence Transformers
* FAISS

## Future Work

* Hybrid Retrieval
* Personalized Ranking
* Learning to Rank
* Recommendation Engine

## Status

V2 Complete
