import json
import random
import re
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Response
from starlette.middleware.cors import CORSMiddleware

from rag.models.prompt_engineering import generate_image_with_context
from rag.models.schemas import TourRequest, PuzzleRequest, HintRequest
from rag.services.rag_service import RAGService
from rag.utils.helpers import setup_logging
from wikipedia_info.wikipedia_summary import get_wiki_info
from wordle.wordle import (
    load_words,
    WordleInput,
    find_best_context_match,
    is_word_valid,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load environment variables from .env file
load_dotenv()

app = FastAPI()


# Setup logging
setup_logging()

# Initialize the RAG service with Google Drive folder ID if available
drive_folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
rag_service = RAGService(drive_folder_id=drive_folder_id)
# Start API service with: uvicorn story_generator.api:app --reload OR run this script

origins = [
    "http://192.168.0.150",  # Add your local network IP address
    "http://192.168.0.217",  # Add your local network IP address
    "http://localhost",  # Allow localhost
    "http://localhost:3000",  # Add your Expo app's URL if using React Native's dev server
    "http://172.20.10.8",  # Add your local network IP address
    "http://127.0.0.1",  # Also allow localhost
    "http://192.168.0.184",  # Add your local network IP address
    "http://172.20.10.4",  # Add your local network IP address
    "http://172.20.10.3",  # Add your local network IP address
    "http://172.20.10.2",  # Add your local network IP address
    "http://192.168.188.67",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins if you need
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.post("/generate-tour")
async def generate_tour(request: TourRequest):
    try:
        # Construct the query as a JSON object
        query_data = {
            "name": request.name,
            "job": request.job,
            "age": request.age,
            "hobbies": request.hobbies,
        }

        # Convert the query data to a JSON string
        query = json.dumps(query_data)

        # Pass the JSON string to the RAG service
        response = rag_service.get_story_response(query)

        # Remove markdown-style JSON code block (```json ... ```)
        cleaned_response = re.sub(
            r"```json\s+([\s\S]+?)\s+```", r"\1", response
        ).strip()
        print(cleaned_response)

        # Decode JSON if it is double-encoded as a string
        response_json = json.loads(cleaned_response)
        return response_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-wordle")
async def generate_wordle(request: PuzzleRequest):
    try:
        query_data = {
            "location": request.location,
            "location_info": request.location_info,
            "user_interests": request.user_interests,
            "user_job": request.user_job,
            "location_story": request.location_story,
        }

        # Convert the query data to a JSON string
        query = json.dumps(query_data)

        # Pass the query string to the RAG service's get_wordle_response method
        response = rag_service.get_wordle_response(query)

        # Clean and decode the response as necessary
        cleaned_response = re.sub(
            r"```json\s+([\s\S]+?)\s+```", r"\1", response
        ).strip()

        response_json = json.loads(cleaned_response)
        return response_json

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-puzzle")
async def generate_puzzle(request: PuzzleRequest):
    try:
        # Construct the query as a JSON object
        query_data = {
            "location": request.location,
            "location_info": request.location_info,
            "user_interests": request.user_interests,
            "user_job": request.user_job,
            "location_story": request.location_story,
        }

        # Convert the query data to a JSON string
        query = json.dumps(query_data)

        if random.choices([True, False], weights=[70, 30])[0]:
            response = rag_service.get_image_url_with_puzzle(request.location)
            print(response)
            if response is None:
                response = rag_service.get_puzzle_response(query)
                print(response)
        else:
            response = rag_service.get_puzzle_response(query)
            print(response)

        # Remove markdown-style JSON code block (```json ... ```)
        cleaned_response = re.sub(
            r"```json\s+([\s\S]+?)\s+```", r"\1", response
        ).strip()
        print(cleaned_response)

        # Decode JSON if it is double-encoded as a string
        response_json = json.loads(cleaned_response)
        print(response_json)

        return response_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/hint")
async def hint(request: HintRequest):
    try:

        query_data = {
            "location": request.location,
            "question": request.question,
            "answer": request.answer,
            "hint_level": request.hint_level,
        }
        query = json.dumps(query_data)
        response = rag_service.get_hint(query)
        cleaned_response = re.sub(
            r"```json\s+([\s\S]+?)\s+```", r"\1", response
        ).strip()
        print(cleaned_response)
        response_json = json.loads(cleaned_response)
        print(response_json)

        return response_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/extra_info/{title}")
async def extra_info(title: str):
    try:
        response = get_wiki_info(title)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/validate-word")
async def validate_word(request: dict):
    word = request.get("word", "").strip()
    answer = request.get("answer", "").strip()

    if not word:
        raise HTTPException(status_code=400, detail="Word is required.")

    if is_word_valid(word) or word.lower().strip() == answer.lower().strip():
        return {"valid": True}
    else:
        return {"valid": False}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
