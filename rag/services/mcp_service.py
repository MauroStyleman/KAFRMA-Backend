from mcp.server.fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
import io


class MCPService:
    def __init__(self):
        self.mcp = FastMCP("Google Drive RAG")
        self.SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
        self.creds = None
        self.service = None
        self._setup_google_drive()

    def _setup_google_drive(self):
        """Setup Google Drive API credentials and service."""
        # Define paths
        token_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "credentials",
            "token.pickle",
        )
        credentials_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "credentials",
            "credentials.json",
        )

        # Create credentials directory if it doesn't exist
        os.makedirs(os.path.dirname(token_path), exist_ok=True)

        if os.path.exists(token_path):
            with open(token_path, "rb") as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not os.path.exists(credentials_path):
                    raise FileNotFoundError(
                        f"credentials.json not found at {credentials_path}. "
                        "Please download it from Google Cloud Console and place it in the credentials directory."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open(token_path, "wb") as token:
                pickle.dump(self.creds, token)

        self.service = build("drive", "v3", credentials=self.creds)

    @property
    def drive_resource(self):
        """Resource for accessing Google Drive files."""
        return self.mcp.resource("drive://{file_id}")

    def list_files(self, folder_id=None):
        """List files from Google Drive."""
        query = f"'{folder_id}' in parents" if folder_id else None
        results = (
            self.service.files()
            .list(q=query, pageSize=100, fields="files(id, name, mimeType)")
            .execute()
        )
        return results.get("files", [])

    def download_file(self, file_id):
        """Download a file from Google Drive."""
        try:
            request = self.service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownloader(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            file.seek(0)
            return file.read().decode("utf-8")
        except Exception as e:
            print(f"Error downloading file: {e}")
            return None

    def get_file_content(self, file_id):
        """Get content of a file from Google Drive."""
        return self.download_file(file_id)
