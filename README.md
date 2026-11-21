# 🤖 Agentic AI Due Diligence Consultant

> An AI-powered multi-agent due diligence system that automates company analysis using **LangGraph**, **Hybrid RAG**, **FAISS**, **Groq LLM**, **Tavily Search**, **Yahoo Finance**, and **Streamlit**.

---

## 📌 Overview

Performing due diligence on a company requires analyzing information from multiple sources such as:

- Latest News
- Financial Statements
- Annual Reports (10-K)
- Legal Proceedings
- Risk Factors
- Regulatory Information

Manually collecting and analyzing this information is time-consuming and often inconsistent.

This project solves this problem by building an **Agentic AI Due Diligence Consultant**, where multiple specialized AI agents collaborate to generate a comprehensive due diligence report.

The system leverages **LangGraph** for agent orchestration, **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** for document intelligence, and **Large Language Models (Groq Llama 3.3 70B)** for reasoning and report generation.

---

## 🚀 Features

- ✅ Multi-Agent AI Architecture using LangGraph
- ✅ Dynamic Planner Agent
- ✅ Dynamic Executor Agent
- ✅ News Analysis Agent
- ✅ Financial Analysis Agent
- ✅ Legal Due Diligence Agent
- ✅ Risk Assessment Agent
- ✅ Final Report Generation Agent
- ✅ Hybrid RAG using Company Annual Reports
- ✅ FAISS Vector Database
- ✅ HuggingFace Sentence Transformers
- ✅ Groq Llama 3.3 70B Integration
- ✅ Tavily Search Integration
- ✅ Yahoo Finance Integration
- ✅ Streamlit Web Application
- ✅ Upload Company Annual Reports (PDF)
- ✅ Automatic Due Diligence Report Generation

---

# 🎯 Problem Statement

Due diligence is a critical process during mergers, acquisitions, investments, and corporate evaluations.

Analysts typically spend hours gathering data from:

- Annual Reports
- News Articles
- Legal Databases
- Financial Statements
- Regulatory Filings

This project automates the entire workflow by orchestrating multiple AI agents that independently analyze different aspects of a company and collaboratively generate a professional due diligence report.
# 🏗️ System Architecture

```
                           User

                             │

                             ▼

                     Streamlit Frontend

                             │

                             ▼

                    LangGraph Workflow

                             │

                             ▼

                      Planner Agent

                             │

                             ▼

                     Executor Agent

        ┌──────────────┬──────────────┬──────────────┬──────────────┐

        ▼              ▼              ▼              ▼

    News Agent    Finance Agent   Legal Agent    Risk Agent

                                          │

                                          ▼

                                  Hybrid RAG Pipeline

                                          │

                            Company Annual Report (PDF)

                                          │

                                   PDF Loader

                                          │

                                    Text Splitter

                                          │

                             HuggingFace Embeddings

                                          │

                                 FAISS Vector Store

                                          │

                                     Retriever

                                          │

                                          ▼

                               Groq Llama 3.3 70B

                                          │

                                          ▼

                               Report Generator Agent

                                          │

                                          ▼

                          Professional Due Diligence Report
```

---

## 📸 Application Screenshots
<img width="1837" height="807" alt="image" src="https://github.com/user-attachments/assets/29961ec1-d933-4e7c-857c-91a0a79df420" />
<img width="1805" height="815" alt="image" src="https://github.com/user-attachments/assets/294374d3-4933-4559-8db8-91a017dc2016" />
<img width="1792" height="768" alt="image" src="https://github.com/user-attachments/assets/18e25a4d-9d27-4758-8b37-a1870b57ffa4" />
<img width="1886" height="728" alt="image" src="https://github.com/user-attachments/assets/c0b52171-2bd4-4fd8-854f-44853cae0e67" />

# 🛠️ Tech Stack

## Programming Language

- Python 3.10+

---

## AI Frameworks

- LangGraph
- LangChain
- HuggingFace
- FAISS

---

## Large Language Model

- Groq
- Llama 3.3 70B Versatile

---

## Retrieval-Augmented Generation

- FAISS
- Sentence Transformers
- HuggingFace Embeddings

---

## Search APIs

- Tavily Search API

---

## Financial Data

- Yahoo Finance

---

## Frontend

- Streamlit

---

## Other Libraries

- PyPDF
- dotenv
- requests
- pandas
- yfinance
# 📂 Project Structure

```
agentic-ai-due-diligence/

│

├── backend/

│ ├── agents/

│ ├── executor/

│ ├── graph/

│ ├── rag/

│ ├── services/

│ ├── tools/

│

├── frontend/

│ └── app.py

│

├── data/

│ └── documents/

│

├── screenshots/

│

├── requirements.txt

├── README.md

├── .env.example

└── .gitignore
```
# ⚙️ Workflow

## Step 1

The user enters:

- Company Name
- Query
- Company Annual Report (PDF)

---

## Step 2

The Planner Agent analyzes the query and determines which specialist agents are required.

---

## Step 3

The Executor dynamically invokes the selected agents.

---

## Step 4

Each agent performs its specific task:

### 📰 News Agent

- Retrieves latest company news
- Summarizes major announcements
- Identifies opportunities and risks

---

### 💰 Finance Agent

- Fetches financial information using Yahoo Finance
- Evaluates profitability
- Reviews business strength
- Generates investment outlook

---

### ⚖️ Legal Agent

Uses Hybrid RAG.

Sources:

- Latest Web Information
- Company Annual Report

Provides:

- Litigation
- Regulatory Investigations
- Compliance Risks
- Legal Risk Rating

---

### ⚠️ Risk Agent

Analyzes:

- Financial Risks
- Operational Risks
- Cybersecurity Risks
- Regulatory Risks
- Market Risks

---

### 📄 Report Generator

Combines outputs from all agents into a structured Due Diligence Report.
# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/agentic-ai-due-diligence.git
```

Move inside the project

```bash
cd agentic-ai-due-diligence
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Run Streamlit

```bash
streamlit run frontend/app.py
```
# 🚀 Future Enhancements

- Persistent FAISS Indexing
- PDF Report Export
- Docker Deployment
- Authentication
- Multi-Company Comparison
- Real-Time Monitoring
- Azure/OpenAI Integration
- Cloud Deployment
- Multi-Document RAG
- Agent Execution Dashboard

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Agentic AI
- Multi-Agent Systems
- LangGraph
- Hybrid RAG
- Vector Databases
- FAISS
- Prompt Engineering
- Retrieval-Augmented Generation
- Streamlit
- LLM Integration
- Financial Data Analysis
- Legal Due Diligence Automation

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Noor Tandon**

Computer Engineering Student

Thapar Institute of Engineering and Technology

GitHub: https://github.com/Noor-2004-git



---

⭐ If you found this project useful, consider giving it a star!
