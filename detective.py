#!/usr/bin/env python3
"""
SpaCy Mood Detective - CLI runner

Usage:
    python detective.py "Your text here"
    python detective.py --file examples/sample_texts.txt
"""

import json
import sys
import argparse
from pathlib import Path

import spacy
from mood_detector import create_mood_detector


def load_nlp_model():
    """Load spaCy model and add mood detector component."""
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("❌ Error: spaCy model 'en_core_web_sm' not found.")
        print("   Please run: python -m spacy download en_core_web_sm")
        sys.exit(1)
    
    # Add the mood detector component
    if "mood_detector" not in nlp.pipe_names:
        nlp.add_pipe("mood_detector", last=True)
    
    return nlp


def analyze_text(text: str, nlp) -> dict:
    """Analyze text and return mood detection results."""
    doc = nlp(text)
    
    result = {
        "text": text,
        "mood": doc._.mood,
        "vibe_score": doc._.vibe_score,
        "emotional_triggers": doc._.emotional_triggers,
    }
    
    return result


def format_output(result: dict, json_output: bool = False) -> str:
    """Format the output for display."""
    if json_output:
        return json.dumps(result, indent=2)
    
    # Pretty text output
    output = []
    output.append("\n" + "=" * 60)
    output.append("🕵️‍♂️  SPA CY MOOD DETECTIVE REPORT")
    output.append("=" * 60)
    output.append(f"\n📝 Text: {result['text']}")
    output.append(f"\n🎭 Detected Mood: {result['mood']}")
    output.append(f"\n📊 Vibe Score™: {result['vibe_score']}/10")
    
    # Vibe score visualization
    score = result['vibe_score']
    if score >= 7:
        emoji = "🌟✨"
        vibe_desc = "Pure serotonin"
    elif score >= 4:
        emoji = "😊"
        vibe_desc = "Pretty good vibes"
    elif score >= 1:
        emoji = "🙂"
        vibe_desc = "Neutral-positive"
    elif score >= -3:
        emoji = "😐"
        vibe_desc = "Meh"
    elif score >= -6:
        emoji = "😕"
        vibe_desc = "Not great"
    else:
        emoji = "💀"
        vibe_desc = "Why are you shouting"
    
    output.append(f"   {emoji} {vibe_desc}")
    
    # Emotional triggers
    if result['emotional_triggers']:
        output.append(f"\n🎯 Emotional Triggers ({len(result['emotional_triggers'])}):")
        for trigger in result['emotional_triggers'][:10]:  # Limit to 10
            output.append(f"   • \"{trigger['text']}\" → {trigger['type']}")
    
    output.append("\n" + "=" * 60 + "\n")
    
    return "\n".join(output)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="🕵️‍♂️ SpaCy Mood Detective - Detect emotional chaos in text"
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to analyze for mood"
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        help="Path to file containing text to analyze"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results as JSON"
    )
    
    args = parser.parse_args()
    
    # Get input text
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"❌ Error: File not found: {args.file}")
            sys.exit(1)
        text = file_path.read_text().strip()
    elif args.text:
        text = args.text
    else:
        # Interactive mode
        print("🕵️‍♂️  SpaCy Mood Detective")
        print("Enter text to analyze (Ctrl+D or Ctrl+Z to finish):")
        try:
            text = sys.stdin.read().strip()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
        
        if not text:
            print("❌ No text provided.")
            sys.exit(1)
    
    # Load model and analyze
    nlp = load_nlp_model()
    result = analyze_text(text, nlp)
    
    # Output results
    output = format_output(result, json_output=args.json)
    print(output)


if __name__ == "__main__":
    main()

