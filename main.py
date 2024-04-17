import streamlit as st

from service.elastic import ElasticSearchService
from service.llm import *
from streamlit_chat import message

INDEX = "devoxx_talks_ml"

# Load Elasticsearch configuration from config.ini
config = Config("configuration/config.ini")
es_config = config.get_elasticsearch_config()

# Initialize Elasticsearch service
es = ElasticSearchService(
    address=es_config['host'],
    port=es_config['port'],
    username=es_config['username'],
    password=es_config['password']
)

# Streamlit interface
st.title('Devoxx assistant')

def main():

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

        output = es.search_with_knn(index=INDEX, query=prompt, field="dense_embedding.predicted_value")
        response = answer_with_context(prompt, output)

        full_response = ""

        for resp in response:
            full_response += (resp.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})



if __name__ == "__main__":
    main()









