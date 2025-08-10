🤖 Explain It Bot

Your AI-powered explainer for any topic

Explain It Bot is a Streamlit-based chatbot built with LangChain and a local LLM Phi(via Ollama) that explains complex topics in a clear, easy-to-understand way. It supports conversational interactions, history tracking, and exporting explanations for later reference.


🚀 Features - 

Local AI Processing – Runs completely on your machine using Ollama (no API costs).
Powered by LangChain – For intelligent prompt handling & context management.
Simple, Modern UI – Built in Streamlit with responsive design.
Export Functionality – Save explanations as text or PDF.
History Tracking – View previous questions & answers in the sidebar.


🛠 Tech Stack - 

Frontend: Streamlit
Backend / AI: LangChain + Ollama (using Phi model)
Languages: Python
Other Libraries: dotenv, pandas (for history), fpdf (for PDF export)


📂 Project Structure

Explain-It-Bot/
│
├── app.py                 # Main Streamlit application  
├── requirements.txt       # Python dependencies  
├── .env                   # Environment variables (ignored in GitHub)  
├── bot_logic.py           # LangChain pipeline for generating explanations  
├── export_utils.py        # Functions to export answers to text/PDF  
├── styles.css             # Optional custom styles  
└── README.md              # Project documentation



🤝 Contributing -

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.


✨ Acknowledgements

LangChain
Streamlit
Ollama
