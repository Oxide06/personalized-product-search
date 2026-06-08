# Personalized Product Search

A retrieval-based search engine built on Amazon Electronics product metadata.

## Overview

This project explores how modern search systems retrieve relevant products from a large catalog.

Version 1 implements:

* Product ingestion
* Text preprocessing
* BM25 retrieval
* Interactive search CLI
* Persistent BM25 index

Dataset:

* Amazon Reviews 2023
* Electronics metadata
* 50,000 products

## Architecture

Query

↓

BM25 Retrieval

↓

Top K Products

## Example

Search:

gaming mouse

Results:

1. Glorious Model O Gaming Mouse
2. LinGear Gaming Mouse
3. RGB Gaming Keyboard and Mouse Combo

## Installation

```bash
pip install -r requirements.txt
```

Build index:

```bash
python -m src.retrieval.build_index
```

Run:

```bash
python -m src.main
```

## Future Work

* Dense Retrieval (Sentence Transformers)
* FAISS Vector Search
* Hybrid Search
* Personalized Ranking
* Learning to Rank

## Project Status

Version 1 Complete
