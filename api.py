#!/usr/bin/env python3
"""
FastAPI REST API for SpaCy Mood Detective
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import spacy
from mood_detector import create_mood_detector

# Initialize FastAPI app
app = FastAPI(
    title="SpaCy Mood Detective API",
    description="An NLP API that detects emotional chaos in text",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError("spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm")

if "mood_detector" not in nlp.pipe_names:
    nlp.add_pipe("mood_detector", last=True)


# Request/Response models
class TextRequest(BaseModel):
    text: str


class Trigger(BaseModel):
    text: str
    type: str


class MoodResponse(BaseModel):
    text: str
    mood: str
    vibe_score: int
    emotional_triggers: List[Trigger]
    emotional_spans: List[Dict[str, Any]]


class BatchTextRequest(BaseModel):
    texts: List[str]


class BatchMoodResponse(BaseModel):
    results: List[MoodResponse]
    total_analyzed: int


@app.get("/")
async def root():
    """API root endpoint."""
    return {
        "message": "🕵️‍♂️ SpaCy Mood Detective API",
        "version": "1.0.0",
        "endpoints": {
            "/analyze": "POST - Analyze single text",
            "/analyze/batch": "POST - Analyze multiple texts",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": True}


@app.post("/analyze", response_model=MoodResponse)
async def analyze_text(request: TextRequest):
    """
    Analyze a single text for mood detection.
    
    - **text**: The text to analyze
    - Returns: Mood, vibe score, and emotional triggers
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    doc = nlp(request.text)
    
    return MoodResponse(
        text=request.text,
        mood=doc._.mood,
        vibe_score=doc._.vibe_score,
        emotional_triggers=[
            Trigger(text=t["text"], type=t["type"])
            for t in doc._.emotional_triggers
        ],
        emotional_spans=[
            {"text": span[0], "label": span[1]}
            for span in doc._.emotional_spans
        ]
    )


@app.post("/analyze/batch", response_model=BatchMoodResponse)
async def analyze_batch(request: BatchTextRequest):
    """
    Analyze multiple texts in batch.
    
    - **texts**: List of texts to analyze
    - Returns: List of mood detection results
    """
    if not request.texts:
        raise HTTPException(status_code=400, detail="Texts list cannot be empty")
    
    results = []
    for text in request.texts:
        if not text.strip():
            continue
        
        doc = nlp(text)
        results.append(MoodResponse(
            text=text,
            mood=doc._.mood,
            vibe_score=doc._.vibe_score,
            emotional_triggers=[
                Trigger(text=t["text"], type=t["type"])
                for t in doc._.emotional_triggers
            ],
            emotional_spans=[
                {"text": span[0], "label": span[1]}
                for span in doc._.emotional_spans
            ]
        ))
    
    return BatchMoodResponse(
        results=results,
        total_analyzed=len(results)
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

