import os
from typing import List, Optional, Dict

from rag.models.config import Config
from rag.services.mcp_service import MCPService


class TextLoader:
    def __init__(
        self, folder_path: Optional[str] = None, drive_folder_id: Optional[str] = None
    ):
        self.folder_path = folder_path or Config.FOLDER_PATH
        self.drive_folder_id = drive_folder_id
        self.mcp_service = MCPService() if drive_folder_id else None
        self.documents: Dict[str, str] = {}  # Store documents with their IDs

    def load_texts_from_folder(self) -> List[str]:
        """Load texts from both local folder and Google Drive if configured."""
        texts = []

        # Load Google Drive files if configured (prioritize this)
        if self.mcp_service and self.drive_folder_id:
            drive_files = self.mcp_service.list_files(self.drive_folder_id)
            for file in drive_files:
                if file["mimeType"] == "text/plain":
                    content = self.mcp_service.get_file_content(file["id"])
                    if content:
                        self.documents[file["id"]] = content
                        texts.append(content)

        # Load local files as fallback
        if os.path.exists(self.folder_path):
            for filename in os.listdir(self.folder_path):
                if filename.endswith(".txt"):
                    with open(
                        os.path.join(self.folder_path, filename), "r", encoding="utf-8"
                    ) as file:
                        content = file.read()
                        self.documents[filename] = content
                        texts.append(content)

        return texts

    def chunk_text(self, text: str, chunk_size: int = Config.CHUNK_SIZE) -> List[str]:
        """Split text into chunks of specified size."""
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def get_document_by_id(self, doc_id: str) -> Optional[str]:
        """Get a specific document by its ID."""
        return self.documents.get(doc_id)

    def get_all_documents(self) -> Dict[str, str]:
        """Get all loaded documents with their IDs."""
        return self.documents
