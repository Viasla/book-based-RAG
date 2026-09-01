# Plan

The main goal of this plan, is to create RAG, which based on certain documents (`.pdf` file) and user's question, can generate accurate response. By certain documents I mean mathematical and IT literature.

To test accuracy, I prepared 5 documents:
- [The Java Language Specification](../resources/test/jls26.pdf), [The Java Virtual Machine Specification](../resources/test/jvms26.pdf): I think those are good choice as a first documents for testing entire pipeline, because they are highly structured and don't require sophisticated methods of text extraction.
- [A First Course in Probability](../resources/test/a_first_course_in_probability.pdf), [Grinstead and Snell’s Introduction to Probability](../resources/test/prob.pdf), [An introduction to measure theory](../resources/test/Terence-Tao-Measure-Theory.pdf): Those books are harder to parse because of LaTeX, which require advanced tools to extract those formulas.

## Steps

To achieve project goal, I think it's necessary to make a configurable pipeline from pdf file to generated response, where it's possible to change method of chunking, embedding generation, retrieving and response generation to test which methods work best.

### 1. RAG structure

1. Create abstraction layer for each RAG step:
    1. From pdf file to chunks:
        1. Chunker.
    2. From chunks to embeddings:
        1. Encoders.
    3. From embeddings to best matches:
        1. Retriever,
        2. ANN search (include indexing),
        3. Metric.
    4. From retrieved information to response:
        1. Fusier,
        2. LLM (Wrapper for LLM APIs).
2. Create modular pipeline, so each RAG step could interact with each other.

### 2. Abstract layer implementation

[Source](https://link.springer.com/content/pdf/10.1007/s10462-026-11605-7.pdf).

1. Implement each RAG step with different methods:
    1. Chunker:
        1. The chunking with fixed length,
        2. The semantic chunking,
        3. The content-based chunking.
    2. Encoders:
        1. LLM-based Encoders:
            1. Sentence Transformers,
            2. FlagEmbedding,
            3. FastEmbed,
            4. Other encoders.
    3. Retriever (based on database, design retriever):
        1. Databases:
            1. LMDB,
            2. RocksDB.
    4. ANN search:
        1. Indexing:
            1. The InVerted File system with Product Quantization,
            2. The Hierarchical Navigable Small World,
            3. Tree-based Indexing.
    5. Metric:
        1. Cosine Similarity,
        2. Euclidean similarity,
        3. Manhattan distance.
    6. Fusier:
        1. Query-based fusion.
    7. LLM:
        1. Various models which provide Groq API,
        2. Other freely available.

### 3. Test Environment

Currently I don't have exact vision on what should I test.

1. Create tests for chunking stage,
2. Create tests for knowledge database,
3. Create tests for retrival fusion,
4. Create questions for each book to check correctness of answers.

---

# Reports

- [31.08.2026 - 04.08.2026](reports/1.md)