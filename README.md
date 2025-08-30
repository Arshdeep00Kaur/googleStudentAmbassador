# GenieDocs 📚

A PDF chat application powered by Google Gemini AI and Qdrant vector database. Upload your PDF documents and ask questions about their content with intelligent responses that include page references.

## Features

- 📄 PDF document upload and processing
- 🧠 Google Gemini AI for embeddings and chat completion
- 🔍 Vector-based semantic search using Qdrant
- 📖 Smart chunking of PDF content
- 📍 Page number references in responses
- 🎨 Clean and intuitive Streamlit interface

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Google Gemini API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arshdeep00Kaur/googleStudentAmbassador.git
   cd googleStudentAmbassador
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Start the Qdrant vector database:**
   ```bash
   docker-compose up -d
   ```

## Usage

1. **Start the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload a PDF** using the file uploader

4. **Click "📚 Prepare this PDF"** to index the document

5. **Ask questions** about the PDF content in the text input field

## Project Structure

```
├── app.py              # Main Streamlit application
├── chat.py             # Chat functionality with PDF content
├── indexing.py         # PDF processing and vector indexing
├── docker-compose.yml  # Qdrant database configuration
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## How It Works

1. **PDF Processing**: PDFs are loaded and split into manageable chunks using LangChain's text splitters
2. **Embeddings**: Text chunks are converted to vector embeddings using Google Gemini's embedding model
3. **Vector Storage**: Embeddings are stored in Qdrant vector database for efficient similarity search
4. **Query Processing**: User questions are embedded and matched against stored document vectors
5. **Response Generation**: Relevant context is retrieved and used by Gemini to generate intelligent responses with page references

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini API
- **Vector Database**: Qdrant
- **PDF Processing**: LangChain + PyPDF
- **Container**: Docker

## Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Docker Services
- **Qdrant**: Vector database running on port 6333

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError"**: Make sure all dependencies are installed in your virtual environment
2. **"Connection refused"**: Ensure Docker is running and Qdrant container is started
3. **"API key not found"**: Check that your `.env` file contains a valid `GEMINI_API_KEY`
4. **"Model not found"**: Verify your Google Gemini API access and model availability

### Getting Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

If you encounter any issues, please create an issue in the GitHub repository.
