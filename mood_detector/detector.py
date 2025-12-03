"""
Custom spaCy component for mood detection.
"""

from spacy import Language
from spacy.matcher import Matcher
from spacy.tokens import Doc
from typing import List, Tuple, Dict, Any

from .patterns import MOOD_PATTERNS, EMOTIONAL_TRIGGERS, VIBE_WEIGHTS, MOOD_LABELS


# Register custom extension attributes
Doc.set_extension("mood", default=None, force=True)
Doc.set_extension("vibe_score", default=0, force=True)
Doc.set_extension("emotional_spans", default=[], force=True)
Doc.set_extension("emotional_triggers", default=[], force=True)


@Language.factory("mood_detector")
def create_mood_detector(nlp: Language, name: str):
    """Factory function to create the mood detector component."""
    return MoodDetector(nlp)


class MoodDetector:
    """Custom spaCy component that detects mood and calculates vibe scores."""
    
    def __init__(self, nlp: Language):
        """Initialize the mood detector with patterns."""
        self.nlp = nlp
        self.matcher = Matcher(nlp.vocab)
        
        # Add all mood patterns to the matcher
        for pattern in MOOD_PATTERNS:
            self.matcher.add(pattern["label"], [pattern["pattern"]])
    
    def __call__(self, doc: Doc) -> Doc:
        """Process the document and add mood information."""
        # Find matches (returns list of (match_id, start, end) tuples)
        matches = self.matcher(doc)
        
        # Convert match IDs to labels
        match_data = [
            (self.nlp.vocab.strings[match_id], start, end)
            for match_id, start, end in matches
        ]
        
        # Compute mood
        doc._.mood = self._compute_mood(match_data, doc)
        
        # Compute vibe score
        doc._.vibe_score = self._compute_vibe_score(match_data, doc)
        
        # Extract emotional spans
        doc._.emotional_spans = [
            (doc[start:end].text, label) 
            for label, start, end in match_data
        ]
        
        # Extract emotional triggers
        doc._.emotional_triggers = self._extract_emotional_triggers(doc, match_data)
        
        return doc
    
    def _compute_mood(self, matches: List[Tuple[str, int, int]], doc: Doc) -> str:
        """Determine the primary mood from matches."""
        if not matches:
            return "neutral"
        
        # Count occurrences of each mood label
        mood_counts: Dict[str, int] = {}
        for label, start, end in matches:
            mood_counts[label] = mood_counts.get(label, 0) + 1
        
        # Find the most common mood
        if not mood_counts:
            return "neutral"
        
        # Check for combinations first
        moods_present = set(mood_counts.keys())
        
        # Special combinations (order matters - more specific first)
        if "TIRED" in moods_present and "STRESSED" in moods_present and "ANXIETY" in moods_present:
            return "overwhelming exhaustion"
        if "TIRED" in moods_present and "STRESSED" in moods_present:
            return "chaotic tired"
        if "ANGRY" in moods_present and "PROBLEM_AVOIDANCE" in moods_present:
            return "chaotic frustration"
        if "ANGRY" in moods_present and "SAD" in moods_present:
            return "bitter sadness"
        if "SAD" in moods_present and "LONGING" in moods_present:
            return "melancholic longing"
        if "ANXIETY" in moods_present and "STRESSED" in moods_present:
            return "anxious stress"
        if "SARCASTIC" in moods_present and "CONFUSED" in moods_present:
            return "sarcastic confusion"
        if "TIRED" in moods_present and "EXISTENTIAL" in moods_present:
            return "existential tired"
        if "SAD" in moods_present and "DESPAIR" in moods_present:
            return "deep despair"
        if "HAPPY" in moods_present and "EXCITED" in moods_present:
            return "joyful excitement"
        if "LOVE" in moods_present and "GRATITUDE" in moods_present:
            return "grateful love"
        if "RELIEF" in moods_present and "HAPPY" in moods_present:
            return "relieved happiness"
        if "SURPRISE" in moods_present and "HAPPY" in moods_present:
            return "delighted surprise"
        if "SURPRISE" in moods_present and "ANGRY" in moods_present:
            return "shocked anger"
        if "DISAPPOINTMENT" in moods_present and "SAD" in moods_present:
            return "disappointed sadness"
        if "REGRET" in moods_present and "SAD" in moods_present:
            return "regretful sadness"
        
        # Find the most common mood
        primary_mood = max(mood_counts.items(), key=lambda x: x[1])[0]
        
        # Return the human-readable mood label
        return MOOD_LABELS.get(primary_mood, primary_mood.lower())
    
    def _compute_vibe_score(self, matches: List[Tuple[str, int, int]], doc: Doc) -> int:
        """Calculate the vibe score from -10 to +10."""
        if not matches:
            return 0
        
        score = 0
        mood_counts: Dict[str, int] = {}
        
        # Count mood occurrences
        for label, start, end in matches:
            mood_counts[label] = mood_counts.get(label, 0) + 1
        
        # Calculate weighted score
        for label, count in mood_counts.items():
            weight = VIBE_WEIGHTS.get(label, 0)
            # Apply diminishing returns for multiple occurrences
            score += weight * min(count, 3)  # Cap at 3x per mood type
        
        # Adjust based on text characteristics
        text_lower = doc.text.lower()
        
        # Intensity modifiers
        intensity_words = ["very", "really", "extremely", "so", "incredibly", "absolutely", "completely", "totally", "utterly", "absolutely", "quite", "pretty", "super", "ultra", "mega", "insanely", "ridiculously"]
        intensity_count = sum(1 for word in intensity_words if word in text_lower)
        if intensity_count > 0:
            score = int(score * (1.0 + (intensity_count * 0.15)))  # Scale with intensity
        
        # Exclamation marks increase intensity (positive or negative)
        exclamation_count = doc.text.count("!")
        if score > 0:
            score += min(exclamation_count, 4)  # Positive intensity
        else:
            score -= min(exclamation_count, 4)  # Negative intensity
        
        # Question marks (confusion/uncertainty)
        question_count = doc.text.count("?")
        score -= min(question_count, 3)
        
        # All caps detection (shouting - usually negative)
        caps_ratio = sum(1 for c in doc.text if c.isupper()) / max(len(doc.text), 1)
        if caps_ratio > 0.7 and len(doc.text) > 5:
            score -= 4
        
        # Casual words boost (slightly positive)
        casual_words = ["bro", "bruh", "dude", "lol", "haha", "lmao", "hehe"]
        casual_count = sum(1 for word in casual_words if word in text_lower)
        score += min(casual_count, 2)
        
        # Emoji-like words (positive)
        emoji_words = ["<3", "❤️", "😊", "😄", "😁", "😍", "🥰", "😎", "🔥", "✨", "🌟"]
        emoji_count = sum(1 for word in emoji_words if word in doc.text)
        score += min(emoji_count, 3)
        
        # Negative intensifiers
        negative_intensifiers = ["absolutely", "completely", "totally", "utterly"]
        if any(word in text_lower for word in negative_intensifiers) and score < 0:
            score = int(score * 1.3)  # Amplify negative emotions
        
        # Positive intensifiers
        positive_intensifiers = ["absolutely", "completely", "totally", "utterly"]
        if any(word in text_lower for word in positive_intensifiers) and score > 0:
            score = int(score * 1.3)  # Amplify positive emotions
        
        # Clamp to -10 to +10
        score = max(-10, min(10, score))
        
        return score
    
    def _extract_emotional_triggers(
        self, doc: Doc, matches: List[Tuple[str, int, int]]
    ) -> List[Dict[str, Any]]:
        """Extract emotional triggers from the document."""
        triggers = []
        text_lower = doc.text.lower()
        
        # Check for trigger phrases
        for trigger_type, trigger_words in EMOTIONAL_TRIGGERS.items():
            for word in trigger_words:
                if word in text_lower:
                    # Find the span in the original text
                    start_idx = text_lower.find(word)
                    if start_idx != -1:
                        end_idx = start_idx + len(word)
                        triggers.append({
                            "text": doc.text[start_idx:end_idx],
                            "type": trigger_type
                        })
                        break  # Only add once per trigger type
        
        # Also add matched spans
        for label, start, end in matches:
            trigger_text = doc[start:end].text
            trigger_type = label.lower().replace("_", " ")
            triggers.append({
                "text": trigger_text,
                "type": trigger_type
            })
        
        return triggers

