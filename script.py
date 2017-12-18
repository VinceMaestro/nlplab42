from embeddings import EmbeddingsDictionary

dictionary = EmbeddingsDictionary(100000);
neighbors_geek = dictionary.w2neighbors('geek', 10);
neighbors_man = dictionary.w2neighbors('man', 10);
neighbors_woman = dictionary.w2neighbors('woman', 10);

dictionary.analogy('ai', 'human', 'concert');
