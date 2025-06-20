# LangChain App

This repository demonstrates how to build a custom **LangChain Agent application** that can dynamically choose tools to respond to user queries. It leverages LangChain's **AgentExecutor** to orchestrate reasoning and tool usage through a language model.

## 📄 File Description

- `app.py`  
  The main application script that brings together:
  
  - 🧠 **Agent Setup**: A function-based agent is created using `initialize_agent` with the type `"chat-conversational-react-description"`.  
  - 🛠️ **Tool Integration**: Tools (like custom functions or APIs) are defined and passed to the agent. These tools allow the agent to access external information and perform operations beyond basic LLM output.  
  - 🧾 **Prompt Customization**: Uses `ChatPromptTemplate` to guide agent behavior.  
  - 💬 **AgentExecutor**: Handles planning, reasoning, and tool invocation. It takes user input and allows the agent to decide whether to use a tool or respond directly.  
  - 🎯 **Use Case**: The agent accepts contextual user input (name, country, question) and intelligently routes the query through the tools or directly to the LLM.

This file serves as a clean example of a **Conversational Agent** that blends custom logic with tool-assisted LLM output.

## Environment Variables

To use this project, create a `.env` file in the root directory with your API keys:

```env
OPENAI_API_KEY="your_openai_key"
ANTHROPIC_API_KEY="your_anthropic_key"
GOOGLE_API_KEY="your_google_key"
HUGGINGFACEHUB_API_KEY="your_huggingfacehub_key"
```

### Dont have closed-source API key ? 
Refer to the repo [**Models_in_LangChain**](https://github.com/naveenreddy0911/Models_in_LangChain) for using open-sourced Hugging Face chat models (via API or locally).
