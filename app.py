import streamlit as st                                      #streamlit libr is for building the UI, no need to use HTML/CSS directly.
from langchain.chains import LLMChain                       #langchain.chains.LLMChain(class) helps connect the model(gives the response) with a prompt(taken by engine).
from langchain.prompts import PromptTemplate                #PromptTemplate defines how we ask the model something(to structure your prompt in question format)
from langchain.llms import Ollama                           #Ollama integrates your local Phi model with LangChain 
import datetime


st.set_page_config(                                         
    page_title="Explain It Bot",                            #Streamlit function that lets you customize how your app looks and behaves
    page_icon="🤖",                                        #sets the browser tab title tiny icon next to the page title in the tab
    layout="centered",                                      #alignment on the screen
    initial_sidebar_state="collapsed"                       #sets the sidebar when to open ("expanded" – sidebar is open by default, "collapsed" – sidebar is hidden until you click the toggle", auto" – Streamlit decides based on screen size )
)

# Custom Sunset Theme CSS
st.markdown("""                                             
    <style>
        body {
            color: #2d2d2d;
        }
        .stApp {
            background: linear-gradient(to bottom, #ff7e5f, #feb47b);
            font-family: 'Segoe UI', sans-serif;
        }
        .title-box {
            border: 2px solid #6a0572;
            background-color: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            font-size: 40px;
            font-weight: bold;
            color: #6a0572;
            text-align: center;
            margin: 20px auto;
            width: 80%;
            }

        .subtitle {
            text-align: center;
            color: #3c3c3c;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .footer {
            margin-top: 40px;
            font-size: 12px;
            color: #444;
            text-align: center;
        }
        .css-1cpxqw2 edgvbvh3 { background-color: #f0c27b; }
    </style>
""", unsafe_allow_html=True)

# Session state to store history
if "history" not in st.session_state:               #Streamlit resets everything every time you interact with the app — but variables inside st.session_state stores.
    st.session_state.history = []                   #if history doesn't exist, then it initializes it as an empty list. and the list will be used to store the history of questions and answers during the sessions.

# Sidebar
with st.sidebar:                                    # Anything starting inside this "with" block will appear on the sidebar.
    st.markdown("### 🧠 Q&A History")               # Heading to the sidebar
    if st.session_state.history:                    # Checks if there's any history stored. If yes, it will show.
        for idx, item in  enumerate(st.session_state.history[::-1]):             # loops through the history items in reverse order (so most recent question is at the top). enumerate() gives you both the index and the item itself. 
            st.markdown(f"**Q{len(st.session_state.history)-idx}:** {item['q']}")           # ensures that the oldest is Q1, and the newest gets the highest number.
            st.markdown(f"- {item['a']}")
    else:
        st.info("No history yet.")                  # list is still empty

# Title and subtitle
st.markdown('<div class="title-box">🤖 Explain It Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simple AI explanations with local Phi + LangChain</div>', unsafe_allow_html=True)

# Input
question = st.text_input("💬 Ask me anything...")

# Generate and display response
if question:                                        # checks if the user typed something into the input box
    with st.spinner("Thinking..."):                 # adds a loading spinner with the message "Thinking..." while the AI is generating a response.
        llm = Ollama(model="phi")
        prompt = PromptTemplate(
            input_variables=["query"],
            template="Explain this like I'm 12: {query}"
        )
        chain = LLMChain(llm=llm, prompt=prompt)                # connecting the model and the prompt template together in a LangChain chain
        response = chain.run(question)                             # run the chain with the user's question as input. While, response contains the model’s answer.

    # Show answer
    st.success(response)                                # final answer in a green box on the screen.

    # Save history
    st.session_state.history.append({"q": question, "a": response})             # Adds this question/answer pair to your sidebar history.

    # Download option
    filename = f"explanation_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"               #Creates a dynamic filename using the current date and time, so every file has a unique name.
    st.download_button(
        label="💾 Save Explanation",
        data=response,
        file_name=filename,
        mime="text/plain"
    )

# Footer
st.markdown('<div class="footer">Built with Streamlit + LangChain + Phi </div>', unsafe_allow_html=True)
