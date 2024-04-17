# DevoxxDemo - Construire son Assistant Intelligent avec Hugging Face et Elasticsearch

This system utilizes OpenAI and connects to an Elasticsearch cluster for retrieval-based augmentation. Below are instructions on how to configure the `config.ini` file and set up the Docker image.

## Configuration

1. **Create `config.ini`**: Inside the `configuration` folder, create a file named `config.ini`.

2. **Edit `config.ini`**:

   ```ini
   [elasticsearch]
   host = YOUR_ADDRESS
   port = YOUR_PORT
   username = YOUR_ELASTICSEARCH_USERNAME
   password = YOUR_ELASTICSEARCH_PASSWORD
   
   [openai]
   api_key = YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_ELASTICSEARCH_USERNAME`, `YOUR_ELASTICSEARCH_PASSWORD`, and `YOUR_OPENAI_API_KEY` with your own Elasticsearch credentials and OpenAI API key respectively.

## Docker Setup

1. **Build Docker Image**:

   Navigate to the directory containing the `Dockerfile` and run the following command:

   ```bash
   docker build -t devoxx-chatbot .
   ```

   This command will build a Docker image named `devoxx-chatbot`.

2. **Run Docker Container**:

   Once the image is built, you can run a Docker container using the following command:

   ```bash
   docker run -p 8501:8501 devoxx-chatbot
   ```

   This command will start the Docker container, and your system will be accessible at `http://localhost:8501` in your browser.

## Accessing the System

After setting up the Docker container, you can access the retrieval augmented generation system via your web browser by visiting `http://localhost:8501`.

---

Feel free to customize this README further to fit your specific system's setup and requirements.
