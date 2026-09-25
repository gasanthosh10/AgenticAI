# 🤖 Agentic Research & Knowledge Assistant

**RAG + Multi-Tool AI** — an evolving agentic AI research assistant that combines Large Language Models, Retrieval-Augmented Generation (RAG), vector search, document understanding, and external tools to produce grounded, context-aware answers.

The project is being built incrementally: starting with a reliable **PDF-based RAG system** and progressing toward a **multi-tool agentic research assistant** capable of selecting and combining different information sources.

![Status](https://img.shields.io/badge/status-active--development-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Langflow](https://img.shields.io/badge/workflow-Langflow-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20%2F%20Llama%203.2-lightgrey)


## 📖 Table of Contents

- [Project Status](#-project-status)
- [Problem Statement](#-problem-statement)
- [Core Concept](#-core-concept)
- [Current Architecture](#️-current-architecture)
- [PDF RAG Pipeline](#-pdf-rag-pipeline)
- [Current Features](#-current-features)
- [Data Flow](#-data-flow)
- [Technology Stack](#️-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#️-installation)
- [Ollama Configuration](#-ollama-configuration)
- [Running Langflow](#-running-langflow)
- [Running the PDF RAG Workflow](#-running-the-pdf-rag-workflow)
- [Example Workflow](#-example-workflow)
- [Development Progress](#-development-progress)
- [Roadmap](#️-roadmap)
- [Security](#-security)
- [Long-Term Vision](#-long-term-vision)
- [Skills Demonstrated](#-skills-demonstrated)
- [Key Learning Areas](#-key-learning-areas)
- [Current Limitations](#-current-limitations)
- [Future Extensions](#-future-extensions)
- [Author](#-author)

---

## 📌 Project Status

**🚧 Ongoing — Active Development**

**Current stage:** the core Agent + PDF RAG architecture has been implemented and tested.

**Planned evolution:**

| Area | Description |
|---|---|
| 🌐 | External web search |
| 🧠 | Intelligent tool selection |
| 🔎 | Advanced RAG techniques |
| 🔗 | Multi-source information synthesis |
| 💬 | Conversation memory |
| 📊 | RAG and agent evaluation |
| ⚡ | Performance optimization |
| 🖥️ | Dedicated frontend |
| 🚀 | Production deployment |


## 🎯 Problem Statement

Traditional document question-answering systems are usually limited to the information contained within a fixed collection of documents. General-purpose AI assistants, on the other hand, may not have access to private or user-provided documents.

This project bridges these two capabilities by building an **Agentic Research & Knowledge Assistant** that can work with both private knowledge sources and external information.

The long-term system is designed to:

1. Understand the user's query.
2. Determine what type of information is required.
3. Select an appropriate tool or knowledge source.
4. Retrieve relevant information.
5. Process and synthesize the retrieved context.
6. Generate a grounded and useful response.
7. Maintain conversational context when required.



## 🧠 Core Concept

The project follows an agent-centric architecture. This diagram represents the **long-term target system** — the current implementation covers the Agent + PDF/RAG portion, and additional tools are being added progressively.

                         ┌───────────────────┐
                         │       User        │
                         │       Query       │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │       Agent       │
                         │     Llama 3.2     │
                         └─────────┬─────────┘
                                   │
                         ┌─────────┴─────────┐
                         │  Tool Selection   │
                         └─────────┬─────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  ▼                ▼                ▼
           ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
           │ PDF / RAG   │  │ Web Search  │  │ Future Tools │
           │   Search    │  │             │  │    / APIs    │
           └──────┬──────┘  └──────┬──────┘  └──────┬───────┘
                  │                │                │
                  └────────────────┼────────────────┘
                                   ▼
                         ┌───────────────────┐
                         │    Information    │
                         │     Synthesis     │
                         └─────────┬─────────┘
                                   ▼
                         ┌───────────────────┐
                         │  Grounded Answer  │
                         └───────────────────┘


## 🏗️ Current Architecture

The current working implementation focuses on a local LLM and a PDF-based RAG system.

                         ┌────────────────────┐
                         │     Chat Input     │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │   Langflow Agent   │
                         │     Llama 3.2      │
                         │       Ollama       │
                         └─────────┬──────────┘
                                   │
                             PDF Search Tool
                                   │
                                   ▼
                         ┌────────────────────┐
                         │  Chroma Vector DB  │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │  Relevant Document │
                         │       Chunks       │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │    Chat Output     │
                         │   Grounded Answer  │
                         └────────────────────┘
```

---

## 📄 PDF RAG Pipeline

**Ingestion**

```text
PDF Document
      │
      ▼
┌──────────────┐
│   Read File  │
└──────┬───────┘
       ▼
┌──────────────┐
│  Split Text  │
└──────┬───────┘
       ▼
┌──────────────┐
│  Embeddings  │
└──────┬───────┘
       ▼
┌──────────────┐
│    Chroma    │
│ Vector Store │
└──────────────┘
```

**Retrieval** (kept separate from ingestion)


User Query → Agent → PDF Search Tool → Chroma Retrieval → Relevant Chunks → Agent → Answer


> Separating ingestion from retrieval prevents the document-processing pipeline from being unnecessarily re-executed every time the Agent performs a search.


## ✨ Current Features

### 1. Langflow Agent
The central AI workflow is implemented using **Langflow**:

```text
Chat Input → Agent → Chat Output
```

The Agent provides the reasoning layer that interacts with available tools.

### 2. Local LLM with Ollama
The current language model is **Llama 3.2**, served locally through **Ollama**, providing a local inference environment for experimenting with agentic AI and RAG workflows.

### 3. PDF Document Ingestion
PDF documents can be loaded and processed for retrieval:

```text
PDF → Read → Split → Embed → Store
```

### 4. Text Chunking
| Setting | Value |
|---|---|
| Chunk Size | 1000 |
| Chunk Overlap | 200 |

Documents are divided into smaller sections before embedding so relevant portions can be retrieved efficiently.

### 5. Local Embeddings
The project uses **nomic-embed-text** via Ollama. Document chunks are converted into vector representations that enable semantic similarity search.

### 6. Chroma Vector Database
**Chroma** is used as the vector database, with persistent local storage at:

```text
./chroma_data
```

### 7. Agent-Driven Document Retrieval
The Chroma retrieval component is exposed to the Agent as a search tool. For document-related questions, the Agent retrieves relevant information from the uploaded PDF before generating its response — the foundation for document-grounded QA.

### 8. Persistent Local Knowledge Base
The vector database persists locally rather than being recreated as a temporary store, allowing the knowledge base to be reused across development sessions.

---

## 🔄 Data Flow


                  DOCUMENT INGESTION
                         │
                         ▼
                      PDF File
                         │
                         ▼
                     Read File
                         │
                         ▼
                    Split Text
                         │
                         ▼
                     Embedding
                         │
                         ▼
                  Chroma Vector DB
                         │
                    RETRIEVAL
                         │
                         ▼
                     User Query
                         │
                         ▼
                        Agent
                         │
                         ▼
                 PDF Search Tool
                         │
                         ▼
                  Chroma Retrieval
                         │
                         ▼
                 Relevant Context
                         │
                         ▼
                        Agent
                         │
                         ▼
                 Grounded Response


## 🛠️ Technology Stack

| Category | Tools / Concepts |
|---|---|
| **Programming** | Python |
| **AI / LLM** | Llama 3.2, Ollama, Large Language Models, Agentic AI, Tool Calling, RAG |
| **Document Processing** | Document Ingestion, Text Chunking, Embeddings, Semantic Search, Contextual Retrieval |
| **AI Workflow** | Langflow |
| **Vector Database** | Chroma |
| **Embedding Model** | nomic-embed-text |
| **Development** | Git, GitHub, VS Code, Python Virtual Environment |


## 📂 Project Structure

AgenticAI/
│
├── flows/
│   └── AGENT.json
│
├── Pdfassistant/
│   └── requirements.txt
│
├── .gitignore
├── GIT_COMMANDS.md
└── README.md
```

**Local / generated files** (intentionally excluded from Git):

```text
.venv/
.venv312/
.env
chroma_data/
*.sqlite3
```

These files are generated locally or may contain environment-specific information.

---

## ⚙️ Installation

### Prerequisites
- Python
- Ollama
- Git
- GitHub account

### 1. Clone the Repository
```bash
git clone https://github.com/gasanthosh10/AgenticAI.git
cd AgenticAI
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

Activate it on Windows:
```bash
.venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r Pdfassistant/requirements.txt
```

Current project requirements include:
```text
langflow==1.11.5
```

---

## 🦙 Ollama Configuration

Install Ollama and make sure its service is running, then pull the required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Verify the models are available:
```bash
ollama list
```

Expected models:
```text
llama3.2
nomic-embed-text
```

---

## 🚀 Running Langflow

Start Langflow with:
```bash
uv run langflow run --host 127.0.0.1 --port 7860
```

Then open:
- http://localhost:7860
- or http://127.0.0.1:7860

---

## 📚 Running the PDF RAG Workflow

| Step | Action |
|---|---|
| 1 | **Load a PDF** — provide a document through the Langflow file input |
| 2 | **Split the document** — Chunk Size = 1000, Chunk Overlap = 200 |
| 3 | **Generate embeddings** — using `nomic-embed-text` |
| 4 | **Store embeddings** — in Chroma, at `./chroma_data` |
| 5 | **Connect retrieval to the Agent** — configure the Chroma retrieval component as an Agent tool |
| 6 | **Ask questions** — via the Chat Input; the Agent retrieves relevant context and generates a response |

---

## 🧪 Example Workflow

**Document-Based Question**

> **User:** According to the uploaded PDF, what are the main topics discussed?

```text
Receive Query
     ↓
Identify Document-Based Question
     ↓
Use PDF Search Tool
     ↓
Retrieve Relevant Chunks
     ↓
Process Context
     ↓
Generate Answer
```

---

## 📊 Development Progress

| Component | Status |
|---|---|
| Project architecture | ✅ Completed |
| Langflow setup | ✅ Completed |
| Ollama setup | ✅ Completed |
| Llama 3.2 integration | ✅ Completed |
| Chat Input → Agent → Chat Output | ✅ Completed |
| PDF ingestion | ✅ Completed |
| Text chunking | ✅ Completed |
| Embedding generation | ✅ Completed |
| Chroma vector storage | ✅ Completed |
| Semantic document retrieval | ✅ Completed |
| PDF search as Agent tool | ✅ Completed |
| Separate ingestion/retrieval architecture | ✅ Completed |
| Persistent local vector storage | ✅ Completed |
| External web search | 🔄 Next Phase |
| Dynamic tool selection | 🔄 Next Phase |
| Multi-source reasoning | 🔄 Planned |
| Advanced RAG | 🔄 Planned |
| Query rewriting | 🔄 Planned |
| Reranking | 🔄 Planned |
| Conversation memory | 🔄 Planned |
| Evaluation framework | 🔄 Planned |
| Performance benchmarking | 🔄 Planned |
| Frontend application | 🔄 Planned |
| Production deployment | 🔄 Planned |

---

## 🛣️ Roadmap

### Phase 1 — Core Agent + PDF RAG ✅ Completed
Langflow Agent · Local Llama 3.2 · Ollama integration · PDF ingestion · Text chunking · Local embeddings · Chroma vector storage · Semantic retrieval · Agent-based PDF search · Persistent vector storage · Separate ingestion/retrieval architecture

### Phase 2 — External Web Search
Integrate an external web search tool so the system can retrieve information not available in the local document knowledge base.

```text
User Query → Agent → Determine Information Source
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
          PDF Search     Web Search      Direct Answer
```

### Phase 3 — Intelligent Tool Selection
The Agent dynamically selects the appropriate tool, e.g.:

- *"What does the uploaded document say about neural networks?"* → **PDF Search**
- *"What are the latest developments in AI?"* → **Web Search**

The long-term objective is for the Agent to determine the required information source rather than relying on a fixed workflow.

### Phase 4 — Multi-Source Reasoning
Combine information from multiple sources:

```text
User Query → Agent
                │
     ┌──────────┴──────────┐
     ▼                     ▼
PDF Knowledge          Web Search
     │                     │
     └──────────┬──────────┘
                ▼
        Context Fusion
                │
                ▼
     Information Synthesis
                │
                ▼
          Final Answer
```

### Phase 5 — Advanced RAG
Query rewriting · Multi-query retrieval · Metadata filtering · Improved/contextual chunking · Reranking · Context compression · Hybrid retrieval · Source attribution · Improved citation handling

### Phase 6 — Agentic Planning
```text
Understand → Plan → Select Tool → Execute Tool → Inspect Result
   → Retrieve More Information if Required → Synthesize → Generate Final Response
```

### Phase 7 — Conversation Memory
Support better multi-turn conversations, e.g.:

> **User:** What is this research paper about? → *[document-grounded answer]*
> **User:** What methodology did they use? → *[uses prior context + retrieves the relevant section]*

### Phase 8 — Evaluation & Benchmarking
| Category | Potential Metrics |
|---|---|
| **Retrieval** | Context relevance, retrieval precision/recall, top-K accuracy |
| **Answer** | Answer relevance, faithfulness, groundedness, context utilization, hallucination analysis |
| **Agent** | Tool-selection accuracy, tool execution success rate, multi-step task completion |
| **Performance** | Embedding latency, retrieval latency, LLM latency, end-to-end response time |

### Phase 9 — Production-Ready System
Dedicated web frontend · Backend API · Authentication · User sessions · Conversation history · Persistent memory · Logging · Monitoring · Evaluation dashboard · Dockerization · Cloud deployment · Scalable vector database · Error handling · Security improvements

---

## 🔐 Security

Sensitive information should never be committed to the repository. The project excludes the following from Git version control:

```text
.env
.venv/
.venv312/
chroma_data/
*.sqlite3
```

API keys, credentials, tokens, passwords, and other secrets must never be hardcoded into source files or committed to the repository.

---

## 📈 Long-Term Vision

The ultimate goal is to transform the current PDF RAG system into a complete Agentic Research & Knowledge Assistant.

                         ┌─────────────────────┐
                         │        User         │
                         └──────────┬──────────┘
                                    ▼
                         ┌─────────────────────┐
                         │   Agentic Planner   │
                         └──────────┬──────────┘
                                    ▼
                         ┌─────────────────────┐
                         │   Tool Selection    │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             ▼                      ▼                      ▼
      ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
      │ PDF / RAG    │       │ Web Search   │       │ Future Tools │
      │ Knowledge    │       │              │       │ / APIs       │
      └──────┬───────┘       └──────┬───────┘       └──────┬───────┘
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │  Context Evaluation │
                         │  & Information      │
                         │  Synthesis          │
                         └──────────┬──────────┘
                                    ▼
                         ┌─────────────────────┐
                         │  Grounded Response  │
                         └─────────────────────┘
```

The project is intentionally designed to evolve over multiple development phases, with each phase building on the existing Agentic AI and RAG foundation.

---

## 🎓 Skills Demonstrated

Python · Large Language Models · Local LLM Deployment · Agentic AI · Retrieval-Augmented Generation · Prompt Engineering · Tool Calling · Vector Databases · Embeddings · Semantic Search · Document Processing · Langflow · Ollama · Chroma · AI System Architecture · Git · GitHub · Evaluation and Benchmarking

---

## 📌 Key Learning Areas

| Area | Description |
|---|---|
| **Agentic AI** | Understanding how AI agents can interact with tools and make decisions about information retrieval. |
| **RAG** | Understanding how external knowledge can be retrieved and provided to an LLM as contextual information. |
| **Vector Search** | Understanding how documents can be converted into embeddings and searched based on semantic similarity. |
| **Tool Calling** | Understanding how an agent can interact with external capabilities rather than relying only on its language model. |
| **Local AI** | Understanding how LLMs and embedding models can be executed locally using Ollama. |
| **AI System Design** | Designing modular AI pipelines that can progressively evolve from a basic prototype into a larger production-oriented system. |

---

## 🚧 Current Limitations

- The knowledge base is currently focused on PDF documents.
- External web search is part of the next development phase.
- Dynamic multi-tool selection is not yet the final implementation.
- Advanced retrieval techniques are still planned.
- Evaluation and benchmarking are not yet finalized.
- Production deployment has not yet been implemented.

These limitations are part of the planned development roadmap.

---

## 🔮 Future Extensions

🌐 Web search · 📑 Multiple document formats · 🗄️ SQL/database tools · 🔌 External APIs · 🧠 Long-term memory · 🔄 Autonomous multi-step workflows · 🔍 Hybrid search · 🏆 Reranking models · 📊 Evaluation dashboards · 👥 Multi-user support · 🔐 Authentication · ☁️ Cloud deployment · 🐳 Docker-based deployment · 🖥️ Interactive frontend · 📈 Observability and monitoring

---

## 👨‍💻 Author

**Santhosh G.A**
GitHub: [github.com/gasanthosh10](https://github.com/gasanthosh10)

---

## 📜 Project Status

🚧 **Active Development**

The current implementation successfully establishes the foundation of an Agentic AI + PDF RAG system using Langflow, Ollama, Llama 3.2, embeddings, and Chroma. The project will continue to evolve toward a complete multi-tool Agentic Research & Knowledge Assistant with external search, intelligent tool selection, advanced RAG, multi-source reasoning, conversation memory, evaluation, and production deployment.