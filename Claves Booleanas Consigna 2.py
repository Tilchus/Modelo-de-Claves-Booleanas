import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
################################
## Descargar recursos de NLTK ##
################################
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
###########################
#####corpus- Consigna 2 ###
###########################
documents_historia = {
    "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
    "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
}
#################################
##2.Preprocesamiento de texto ###
#################################
stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return set([word for word in tokens if word.isalnum() and word not in stop_words])

# 3. Construcción del índice invertido
index_historia = {}
for doc_id, text in documents_historia.items():
    words = preprocess(text)
    for word in words:
        if word not in index_historia:
            index_historia[word] = set()
        index_historia[word].add(doc_id)
#############################################
##4.Función de búsqueda booleana secuencial##
#############################################
def boolean_search_historia(query):
    terms = query.split()
    if not terms:
        return set()
        
    result_set = set(documents_historia.keys())
    i = 0
    while i < len(terms):
        term = terms[i]
        if term == "AND":
            i += 1
            if i < len(terms):
                result_set &= index_historia.get(terms[i].lower(), set())
        elif term == "OR":
            i += 1
            if i < len(terms):
                result_set |= index_historia.get(terms[i].lower(), set())
        elif term == "NOT":
            i += 1
            if i < len(terms):
                result_set -= index_historia.get(terms[i].lower(), set())
        else:
            result_set &= index_historia.get(term.lower(), set())
        i += 1
    return result_set
#################################
##########Interfaz consola#######
#################################
if __name__ == "__main__":
    print("="*60)
    print("MÓDULO DE CLAVES BOOLEANAS - CONSIGNA 2: CIVILIZACIONES")
    print("="*60)
    print("Ejemplos válidos: 'egipcios AND pirámides' o 'civilización OR mayas' ")
    
    while True:
        user_query = input("\nIngrese una consulta booleana (o 'salir' para terminar): ").strip()
        if user_query.lower() == 'salir':
            print("Finalizando ejecución.")
            break
        if not user_query:
            continue
            
        resultados = boolean_search_historia(user_query)
        print(f"📄 Documentos encontrados: {resultados}")