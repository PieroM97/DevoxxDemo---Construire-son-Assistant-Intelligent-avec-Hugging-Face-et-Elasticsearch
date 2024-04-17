from elasticsearch import Elasticsearch

class ElasticSearchService:
    def __init__(self, address, port, username, password):
        """
        Initialize Elasticsearch service with provided parameters.

        Args:
            address (str): The address of the Elasticsearch cluster.
            port (int): The port number of the Elasticsearch cluster.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        self.address = address
        self.port = port
        self.username = username
        self.password = password

        # Create Elasticsearch connection
        self.es = Elasticsearch(
            [f"{self.address}:{self.port}"],
            http_auth=(self.username, self.password)
        )

            # Verify connection
        try:
            if self.es.ping():
                print("< Connected to Elasticsearch cluster successfully! > ")
            else:
                print("Failed to connect to Elasticsearch cluster.")
        except Exception as e:
            print(f"An error occurred while connecting to Elasticsearch: {e}")

    def search(self, index, query):
        """
        Perform a search query on the Elasticsearch cluster.

        Args:
            index (str): The index to search within.
            query (dict): The query DSL in dictionary format.

        Returns:
            dict: The search results.
        """
        return self.es.search(index=index, body=query)

    def search_with_knn(self, index, query, field, k=3, num_candidates=100):
        body = {
            "knn": {
                "field": field,
                "query_vector_builder": {
                    "text_embedding": {
                        "model_id": "sentence-transformers__all-minilm-l6-v2",
                        "model_text": query
                    }
                },
                "k": k,
                "num_candidates": num_candidates
            },
                "_source": {
                    "excludes": [field]
                }
        }

        return self.es.search(index=index, body=body)

