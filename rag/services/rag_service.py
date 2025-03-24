import os
import json
import re
from typing import List, Dict, Tuple

from openai import OpenAI
from rag.services.text_loader import TextLoader
from rag.services.embedding_service import EmbeddingService
from rag.services.faiss_service import FAISSService
from rag.models.prompt_engineering import (
    generate_story_message,
    generate_puzzle_message,
    generate_hint,
    generate_image_with_context,
    generate_wordle,
)


class RAGService:
    def __init__(self, drive_folder_id=None):
        # Initialize services
        self.text_loader = TextLoader(drive_folder_id=drive_folder_id)
        self.embedding_service = EmbeddingService()
        self.faiss_service = FAISSService(self.embedding_service)

        # Load text data and build FAISS index
        self.documents = self.text_loader.load_texts_from_folder()
        self.full_text = "\n".join(self.documents)
        self.chunks = self.text_loader.chunk_text(self.full_text)
        self.faiss_service.build_index(self.chunks)

        # Initialize OpenAI client
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER1_API_KEY environment variable is not set.")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1", api_key=self.api_key
        )

    def get_context_string(self, contexts: List[Tuple[str, float]]) -> str:
        """Convert contexts to a formatted string."""
        return (
            " ".join([context[0] for context in contexts])
            if contexts
            else "Could not find any historical context."
        )

    def get_story_response(self, query):
        try:
            # Parse the JSON query
            query_data = json.loads(query)

            # Extract user information
            name = query_data.get("name")
            job = query_data.get("job")
            age = query_data.get("age")
            hobbies = query_data.get("hobbies")

            if not all([name, job, age, hobbies]):
                raise ValueError("Missing required fields in the query.")

            # Get relevant contexts
            relevant_contexts = self.faiss_service.search(query, top_k=15)
            local_history_context = self.get_context_string(relevant_contexts)

            # Generate response
            system_message = generate_story_message(name, job, age, hobbies)
            messages = [
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": f"{query}\n\nContext:\n{local_history_context}",
                },
            ]

            completion = self.client.chat.completions.create(
                model="google/gemini-2.0-pro-exp-02-05:free",
                messages=messages,
            )

            return completion.choices[0].message.content

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the query.")

    def get_puzzle_response(self, query):
        try:
            query_data = json.loads(query)
            location = query_data.get("location")
            location_info = query_data.get("location_info")
            user_interests = query_data.get("user_interests")
            user_job = query_data.get("user_job")
            location_story = query_data.get("location_story")

            if not all(
                [location, location_info, user_interests, user_job, location_story]
            ):
                raise ValueError("Missing required fields in the query.")

            relevant_contexts = self.faiss_service.search(query, top_k=15)
            local_history_context = self.get_context_string(relevant_contexts)

            system_message = generate_puzzle_message(
                location, location_info, user_interests, user_job, location_story
            )
            messages = [
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": f"{query}\n\nContext:\n{local_history_context}",
                },
            ]

            completion = self.client.chat.completions.create(
                model="google/gemini-2.0-pro-exp-02-05:free",
                messages=messages,
            )

            return completion.choices[0].message.content

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the query.")

    def get_wordle_response(self, query):
        try:
            query_data = json.loads(query)
            location = query_data.get("location")
            location_info = query_data.get("location_info")
            user_interests = query_data.get("user_interests")
            user_job = query_data.get("user_job")
            location_story = query_data.get("location_story")

            if not all(
                [location, location_info, user_interests, user_job, location_story]
            ):
                raise ValueError("Missing required fields in the query.")

            relevant_contexts = self.faiss_service.search(query, top_k=15)
            local_history_context = self.get_context_string(relevant_contexts)

            system_message = generate_wordle(
                location, location_info, user_interests, user_job, location_story
            )
            messages = [
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": f"{query}\n\nContext:\n{local_history_context}",
                },
            ]

            completion = self.client.chat.completions.create(
                model="google/gemini-2.0-flash-lite-preview-02-05:free",
                messages=messages,
            )

            return completion.choices[0].message.content

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the query.")

    def get_hint(self, query):
        try:
            query_data = json.loads(query)
            location = query_data.get("location")
            question = query_data.get("question")
            answer = query_data.get("answer")
            hint_level = query_data.get("hint_level")

            if not all([location, question, answer, hint_level]):
                raise ValueError("Missing required fields in the query.")

            relevant_contexts = self.faiss_service.search(query, top_k=15)
            local_history_context = self.get_context_string(relevant_contexts)

            system_message = generate_hint(location, question, answer, hint_level)
            messages = [
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": f"{query}\n\nContext:\n{local_history_context}",
                },
            ]

            completion = self.client.chat.completions.create(
                model="google/gemini-2.0-pro-exp-02-05:free",
                messages=messages,
            )

            return completion.choices[0].message.content

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the query.")

    def get_image_url_with_puzzle(self, location: str):
        try:
            if not location:
                raise ValueError("Missing required location parameter.")

            queries = [
                f"Laat me de context over de afbeelding van {location} zien en de context van die afbeelding"
            ]
            relevant_contexts = []
            seen_contexts = set()

            for q in queries:
                results = self.faiss_service.search(q, top_k=300)
                for context in results:
                    if context[0] not in seen_contexts:
                        relevant_contexts.append(context)
                        seen_contexts.add(context[0])

            image_contexts = []
            for context in relevant_contexts:
                if (
                    "afbeelding" in context[0].lower()
                    and "context" in context[0].lower()
                    and location.lower() in context[0].lower()
                    and re.search(
                        r"afbeelding\s*[:,-]?\s*" + re.escape(location.lower()),
                        context[0].lower(),
                    )
                ):
                    image_contexts.append(context[0])

            if not image_contexts:
                return None

            system_message = generate_image_with_context(location)
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"\nContext:\n{''.join(image_contexts)}"},
            ]

            completion = self.client.chat.completions.create(
                model="google/gemini-2.0-pro-exp-02-05:free",
                messages=messages,
            )

            return completion.choices[0].message.content

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the query.")
