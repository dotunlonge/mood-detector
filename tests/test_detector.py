"""
Tests for the Mood Detective
"""

import pytest
import spacy
from mood_detector import create_mood_detector


@pytest.fixture
def nlp():
    """Load spaCy model with mood detector."""
    nlp = spacy.load("en_core_web_sm")
    if "mood_detector" not in nlp.pipe_names:
        nlp.add_pipe("mood_detector", last=True)
    return nlp


def test_happy_text(nlp):
    """Test detection of happy mood."""
    text = "I'm so happy and excited! This is amazing!"
    doc = nlp(text)
    
    assert doc._.mood is not None
    assert doc._.vibe_score > 0
    assert len(doc._.emotional_triggers) > 0


def test_sad_text(nlp):
    """Test detection of sad mood."""
    text = "I'm so sad and lonely. I miss my mum."
    doc = nlp(text)
    
    assert doc._.mood is not None
    assert doc._.vibe_score < 0
    assert len(doc._.emotional_triggers) > 0


def test_angry_text(nlp):
    """Test detection of angry mood."""
    text = "I'm so angry and frustrated! This is ridiculous!"
    doc = nlp(text)
    
    assert doc._.mood is not None
    assert doc._.vibe_score < 0


def test_neutral_text(nlp):
    """Test neutral text."""
    text = "The weather is nice today."
    doc = nlp(text)
    
    assert doc._.mood is not None
    assert doc._.vibe_score == 0 or abs(doc._.vibe_score) < 3


def test_vibe_score_range(nlp):
    """Test that vibe scores are in valid range."""
    texts = [
        "I'm so incredibly happy! This is amazing!",
        "I'm so sad and depressed.",
        "The cat sat on the mat.",
    ]
    
    for text in texts:
        doc = nlp(text)
        assert -10 <= doc._.vibe_score <= 10, f"Vibe score {doc._.vibe_score} out of range for: {text}"


def test_emotional_triggers_format(nlp):
    """Test that emotional triggers have correct format."""
    text = "I'm happy and excited!"
    doc = nlp(text)
    
    for trigger in doc._.emotional_triggers:
        assert "text" in trigger
        assert "type" in trigger
        assert isinstance(trigger["text"], str)
        assert isinstance(trigger["type"], str)

