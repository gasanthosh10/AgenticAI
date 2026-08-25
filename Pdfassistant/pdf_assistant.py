import typer
from typing import Optional, List

from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.embedder.sentence_transformer import SentenceTransformerEmbedder
from phi.llm.groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"


knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://images.icc-cricket.com/image/upload/prd/v1sjpeistunm3ecsdwwc.pdf"
    ],
    vector_db=PgVector2(
        collection="cricket",
        db_url=db_url,
        embedder=SentenceTransformerEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    ),
)

knowledge_base.load(recreate=False)


storage = PgAssistantStorage(
    table_name="pdf_assistant",
    db_url=db_url
)


def pdf_assistant(new: bool = False, user: str = "user"):

    run_id: Optional[str] = None

    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)

        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,

        llm=Groq(
            model="openai/gpt-oss-20b"
        ),

        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,
    )

    if run_id is None:
        run_id = assistant.run_id
        print(f"Started Run: {run_id}\n")
    else:
        print(f"Continuing Run: {run_id}\n")

    assistant.cli_app(markdown=True)


if __name__ == "__main__":
    typer.run(pdf_assistant)
     