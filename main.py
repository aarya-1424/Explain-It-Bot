from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Load the local model (phi) using Ollama
llm = Ollama(model="phi")

print("🤖 Explain It Bot is ready to use local model (phi)!\n")

while True:
    query = input("Ask something to explain (or type 'exit' to quit): ")
    if query.lower() == "exit":
        print("👋 Bye!")
        break

    # Customize how you prompt phi
    prompt = f"Explain this in simple terms: {query}"
    response = llm.invoke(prompt)

    print("\n🧠", response, "\n")
