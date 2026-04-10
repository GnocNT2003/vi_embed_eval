# Models for evaluation
MODELS = [
    {
        "name": "AITeamVN/Vietnamese_Embedding",
        "label": "AITeamVN",
        # BGE-M3 fine-tuned on 300K Vietnamese triplets; 2048-token context
    },
    # {
    #     "name": "dangvantuan/vietnamese-document-embedding",
    #     "label": "VN-DocEmbed",
    #     "trust_remote_code": True,
    #     # Best for long passages; 8096-token context window
    # },
    # {
    #     "name": "Alibaba-NLP/gte-multilingual-base",
    #     "label": "Alibaba-gte-mul-base",
    #     "trust_remote_code": True,
    #     # Multilingual high-performance model in General Text Embedding
    # },
    {
        "name": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "label": "Paraphrase-mul-MiniLM-L12-v2"
        # Lightweight multilangual model
    },
    {
        "name": "BAAI/bge-m3",
        "label": "BGE-M3",
        # General multilingual baseline
    },
]

# Evaluate at these cutoffs
K_VALUES   = [1, 5, 10]
