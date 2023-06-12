import nltk
nltk.download('punkt')


corpus = {
    "d1": "Map Reduce est un patron de conception de développement informatique, inventé par Google, dans lequel sont effectués des calculs \
        parallèles, et souvent distribués, de données potentiellement très volumineuses, typiquement supérieures en taille à un téraoctet.",
    "d2": "Les termes « map » et « reduce », et les concepts sous-jacents, sont empruntés aux langages de programmation fonctionnelle utilisés \
        pour leur construction (map et reduce de la programmation fonctionnelle et des langages de programmation tableau).",
    "d3": "Il permet de manipuler de grandes quantités de données en les distribuant dans un cluster de machines pour être traitées. Ce modèle \
        connaît un vif succès auprès de sociétés possédant d'importants centres de traitement de données telles Amazon et Facebook.",
    "d4": "Map Reduce commence aussi à être utilisé au sein du Cloud computing. De nombreux framework ont vu le jour afin d'implémenter le Map \
        Reduce. Le plus connu est Hadoop qui a été développé par Apache Software Foundation et Google était à l’origine du Map Reduce.",
    "d5": "Ces framework possèdent des inconvénients qui réduisent considérablement ses performances notamment envmilieu hétérogène. \
        Des framework permettant d'améliorer les performances de Hadoop et les performancesvglobales, tant en termes de vitesse de \
        traitement qu'en consommation électrique, commencent à voir le jour.",
    "d6": "C’est un modèle de programmation popularisé par Google. Il est principalement utilisé pour la manipulation et le traitement d’un \
        nombre important de données au sein d’un cluster de noeuds."
}

terms = ["google", "framework", "map", "et"]


def tokenize_text(document):
    return [i.lower() for i in nltk.word_tokenize(document) if i.isalpha()]

def count_words(tokens):
    return nltk.FreqDist(tokens)

def calculate_tf(counts, total_words):
    return {word: f"{count}/{total_words}" for word, count in counts.items()}

def process_documents(corpus, terms):
    for name, document in corpus.items():
        tokens = tokenize_text(document)
        stopwords = [word for word in tokens if word in terms]
        word_counts = count_words(stopwords)
        total_words = len(tokens)
        tf = calculate_tf(word_counts, total_words)
        
        print(f"Document: {name}")
        print(f"Document size: {total_words}")
        print(f"Stopwords sizes: {dict(word_counts)}")
        print(f"TF calculation: {tf}")
        print("\n")


if __name__ == "__main__":
    process_documents(corpus, terms)


# words = {}
# for name, document in corpus.items():
#     tokens = [i.lower() for i in nltk.word_tokenize(document) if i.isalpha()]
    
#     stopwords = [word for word in tokens if word in terms]
#     counts = nltk.FreqDist(stopwords)
#     total_words = len(tokens)
    
#     tf = {word: f"{count}/{total_words}" for word, count in counts.items()}
    
#     print(f"document size: {total_words}")
#     print(f"stopwords sizes: {dict(counts)}")
#     print(f"calcul tf: {tf}")
#     print("\n")
