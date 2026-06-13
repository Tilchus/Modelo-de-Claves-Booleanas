
##################################
###LIBRERIAS######################
##################################
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
##################################
# Descargar recursos de NLTK 
##################################
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
##################################
###### 1.Corpus-Consigna 1 #######
##################################
documents = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}
######################################
##### 2.Preprocesamiento de texto#####
######################################
stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return set([word for word in tokens if word.isalnum() and word not in stop_words])
########################################
##3.Construcción del índice invertido###
########################################
index = {}
for doc_id, text in documents.items():
    words = preprocess(text)
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)
#############################################
#4.Función de búsqueda booleana secuenciaL  #
#############################################
def boolean_search(query):
    terms = query.split()
    if not terms:
        return set()
        
    result_set = set(documents.keys())
    i = 0
    while i < len(terms):
        term = terms[i]
        if term == "AND":
            i += 1
            if i < len(terms):
                result_set &= index.get(terms[i].lower(), set())
        elif term == "OR":
            i += 1
            if i < len(terms):
                result_set |= index.get(terms[i].lower(), set())
        elif term == "NOT":
            i += 1
            if i < len(terms):
                result_set -= index.get(terms[i].lower(), set())
        else:
            result_set &= index.get(term.lower(), set())
        i += 1
    return result_set
#################################
##########Interfaz consola#######
#################################
if __name__ == "__main__":
    print("="*60)
    print("MÓDULO DE CLAVES BOOLEANAS - CONSIGNA 1: ECOSISTEMA de IA")
    print("="*60)
    print("Ejemplos válidos: 'inteligencia AND artificial' o 'aprendizaje OR redes'")
    
    while True:
        user_query = input("\n[IA] Ingrese consulta booleana (o 'salir'): ").strip()
        if user_query.lower() == 'salir':
            print("Finalizando ejecución del módulo.")
            break
        if not user_query:
            continue
            
        resultados = boolean_search(user_query)
        print(f"📄 Documentos encontrados: {resultados}")