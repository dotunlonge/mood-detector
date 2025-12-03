#!/usr/bin/env python3
"""
Streamlit web UI for SpaCy Mood Detective
"""

import streamlit as st
import spacy
from mood_detector import create_mood_detector
import json
from typing import Dict, Any


@st.cache_resource
def load_model():
    """Load spaCy model with mood detector (cached)."""
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        st.error("❌ spaCy model 'en_core_web_sm' not found. Please run: `python -m spacy download en_core_web_sm`")
        st.stop()
    
    if "mood_detector" not in nlp.pipe_names:
        nlp.add_pipe("mood_detector", last=True)
    
    return nlp


def analyze_text(text: str, nlp) -> Dict[str, Any]:
    """Analyze text and return mood detection results."""
    doc = nlp(text)
    
    return {
        "text": text,
        "mood": doc._.mood,
        "vibe_score": doc._.vibe_score,
        "emotional_triggers": doc._.emotional_triggers,
        "emotional_spans": doc._.emotional_spans,
    }


def get_vibe_emoji(score: int) -> str:
    """Get emoji based on vibe score."""
    if score >= 7:
        return "🌟✨"
    elif score >= 4:
        return "😊"
    elif score >= 1:
        return "🙂"
    elif score >= -3:
        return "😐"
    elif score >= -6:
        return "😕"
    else:
        return "💀"


def get_vibe_description(score: int) -> str:
    """Get description based on vibe score."""
    if score >= 7:
        return "Pure serotonin"
    elif score >= 4:
        return "Pretty good vibes"
    elif score >= 1:
        return "Neutral-positive"
    elif score >= -3:
        return "Meh"
    elif score >= -6:
        return "Not great"
    else:
        return "Why are you shouting"


def main():
    st.set_page_config(
        page_title="🕵️‍♂️ SpaCy Mood Detective",
        page_icon="🕵️‍♂️",
        layout="wide"
    )
    
    st.title("🕵️‍♂️ SpaCy Mood Detective")
    st.markdown("### *An NLP project that sniffs the emotional chaos inside any text.*")
    st.markdown("---")
    
    # Load model
    nlp = load_model()
    
    # Sidebar
    with st.sidebar:
        st.header("📊 About")
        st.markdown("""
        **SpaCy Mood Detective** detects the mood, attitude, and emotional state in any text.
        
        - Uses custom spaCy components
        - Pattern matching for 30+ moods
        - Vibe Score™ from -10 to +10
        - Highlights emotional triggers
        """)
        
        st.header("🎯 Quick Examples")
        example_texts = [
            "I'm so incredibly happy and excited! This is amazing!",
            "I'm too tired to deal with this API today.",
            "I miss my mum",
            "Thank you so much! I'm really grateful!",
            "I'm anxious and stressed about everything.",
        ]
        
        for example in example_texts:
            if st.button(f"📝 {example[:40]}...", key=example):
                st.session_state.example_text = example
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Enter Text")
        
        # Get text input
        default_text = st.session_state.get("example_text", "")
        text_input = st.text_area(
            "Type or paste your text here:",
            value=default_text,
            height=150,
            placeholder="I told him to deploy the backend yesterday but he said 'lol okay' and disappeared."
        )
        
        if st.button("🔍 Detect Mood", type="primary", use_container_width=True):
            if text_input.strip():
                with st.spinner("🕵️‍♂️ Analyzing emotional chaos..."):
                    result = analyze_text(text_input, nlp)
                    st.session_state.result = result
            else:
                st.warning("⚠️ Please enter some text first!")
    
    with col2:
        st.header("📊 Stats")
        if "result" in st.session_state:
            result = st.session_state.result
            st.metric("Vibe Score™", f"{result['vibe_score']}/10", delta=None)
            st.metric("Mood", result['mood'].title())
            st.metric("Triggers Found", len(result['emotional_triggers']))
    
    # Display results
    if "result" in st.session_state:
        result = st.session_state.result
        
        st.markdown("---")
        st.header("🎭 Detection Results")
        
        # Mood and Vibe Score
        col1, col2, col3 = st.columns(3)
        
        with col1:
            emoji = get_vibe_emoji(result['vibe_score'])
            st.markdown(f"### {emoji} Vibe Score™")
            st.markdown(f"## **{result['vibe_score']}/10**")
            st.caption(get_vibe_description(result['vibe_score']))
        
        with col2:
            st.markdown(f"### 🎭 Detected Mood")
            st.markdown(f"## **{result['mood'].title()}**")
        
        with col3:
            st.markdown(f"### 🎯 Emotional Triggers")
            st.markdown(f"## **{len(result['emotional_triggers'])}** found")
        
        # Highlighted text
        st.markdown("### 📝 Text with Highlights")
        highlighted_text = result['text']
        
        # Create a simple highlight display
        st.code(highlighted_text, language=None)
        
        # Emotional triggers breakdown
        if result['emotional_triggers']:
            st.markdown("### 🎯 Emotional Triggers Breakdown")
            
            # Group triggers by type
            trigger_groups = {}
            for trigger in result['emotional_triggers']:
                trigger_type = trigger['type']
                if trigger_type not in trigger_groups:
                    trigger_groups[trigger_type] = []
                trigger_groups[trigger_type].append(trigger['text'])
            
            # Display in columns
            cols = st.columns(min(3, len(trigger_groups)))
            for idx, (trigger_type, texts) in enumerate(trigger_groups.items()):
                with cols[idx % len(cols)]:
                    st.markdown(f"**{trigger_type.title()}**")
                    for text in set(texts):  # Remove duplicates
                        st.code(text, language=None)
        
        # JSON output (expandable)
        with st.expander("📋 View Raw JSON"):
            st.json(result)
        
        # Share/Export
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "💾 Download JSON",
                data=json.dumps(result, indent=2),
                file_name="mood_detection.json",
                mime="application/json"
            )
        with col2:
            if st.button("🔄 Analyze Another"):
                st.session_state.result = None
                st.session_state.example_text = ""
                st.rerun()


if __name__ == "__main__":
    main()

