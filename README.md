# 🎉 **SpaCy Mood Detective**

### *"An NLP project that sniffs the emotional chaos inside any text."*

Because analyzing mood using spaCy **should** be fun — like a detective with espresso.

---

# 🕵️‍♂️ What is this?

**SpaCy Mood Detective** is a tiny-but-mighty NLP app that tries to detect the *mood*, *attitude*, and *chaotic emotional state* in any text, using spaCy under the hood.

It does three things:

1. **Detects moods** →

   Happy, angry, sad, sarcastic, confused, unbothered, "I need sleep", etc.

2. **Highlights emotional phrases** →

   Using spaCy's matcher to mark "emotion triggers".

3. **Gives the text a "Vibe Score™"** →

   A number from **-10 (why are you shouting)** to **+10 (pure serotonin)**.

It's unnecessary. It's dramatic. It's perfect.

---

# 🤖 Why build this?

* It shows off **spaCy NER**, **RuleMatcher**, and **custom pipeline components**.

* It's funny.

* It's the kind of project a recruiter remembers.

  ("He built a *mood detective*?? Bless.")

* You can ship it in 1 day.

* Extendable into anything:

  * sentiment engine

  * toxicity analyzer

  * tone rewriter

  * sass detector (please build this)

---

# 🧩 How it works

```
📥 Text →  

🔍 spaCy pipeline →  

🧠 Mood Detector →  

🎨 Highlight emotional spans →  

📊 Build Vibe Score →  

📤 JSON result
```

### The mood detection uses:

* **PatternMatcher**:

  finds mood words ("love", "lol", "wtf", "bruh", "unfortunately…")

* **Dependency parse**:

  checks if the sentence is active, passive, dramatic, unhinged.

* **Custom spaCy component**:

  calculates a final vibe score using weighted emotional cues.

---

# 🍿 Example

Input:

> "I told him to deploy the backend yesterday but he said 'lol okay' and disappeared."

Output:

```json
{
  "mood": "chaotic frustration",
  "vibe_score": -6,
  "emotional_triggers": [
    {"text": "lol", "type": "sarcasm"},
    {"text": "disappeared", "type": "problem_avoidance"}
  ]
}
```

And yes, this is a real sentence from real engineering teams.

---

# 🛠️ Features

### ✔ Mood Detection

Multiple labels like:

* ecstatic

* mildly stressed

* chaotic tired

* existential

* sarcastic

* "we ball"

### ✔ Mood Phrase Highlighting

Styled console output (or a Streamlit UI) showing the emotional hotspots.

### ✔ Custom spaCy Component

`nlp.add_pipe("mood_detector", last=True)`

### ✔ Vibe Score™

A proprietary formula combining:

* sentiment

* intensity

* emotional words

* the number of times "bro", "please", or "wtf" appears

### ✔ Minimal Setup

Only spaCy, no LLMs needed.

---

# 🧪 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

Or install as a package:

```bash
pip install -e .
```

Clone the repo:

```bash
git clone https://github.com/yourname/spacy-mood-detective
cd spacy-mood-detective
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## 🚀 Usage

### CLI

```bash
python3 detective.py "I'm too tired to deal with this API today."
```

Or make it executable and run directly:

```bash
chmod +x detective.py
./detective.py "I'm too tired to deal with this API today."
```

### 🌐 Web UI (Streamlit)

Launch the interactive web interface:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### 🔌 REST API (FastAPI)

Start the API server:

```bash
python3 api.py
```

Or with uvicorn:

```bash
uvicorn api:app --reload
```

API will be available at `http://localhost:8000`

**API Endpoints:**
- `GET /` - API information
- `GET /health` - Health check
- `POST /analyze` - Analyze single text
- `POST /analyze/batch` - Analyze multiple texts

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "I'm so happy and excited!"}'
```

### 🧪 Run Tests

```bash
pytest tests/
```

---

# 📦 Project Structure

```
spacy-mood-detective/
│
├── mood_detector/
│   ├── __init__.py
│   ├── detector.py        # spaCy custom component
│   └── patterns.py        # mood/match patterns
│
├── tests/
│   ├── __init__.py
│   └── test_detector.py   # Unit tests
│
├── examples/
│   └── sample_texts.txt
│
├── detective.py           # CLI runner
├── app.py                 # Streamlit web UI
├── api.py                 # FastAPI REST API
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
└── README.md
```

---

# 🧙‍♂️ Code Snippet (Core Component)

```python
@Language.factory("mood_detector")
def create_mood_detector(nlp, name):
    return MoodDetector(nlp)

class MoodDetector:
    def __init__(self, nlp):
        self.matcher = Matcher(nlp.vocab)
        for pattern in MOOD_PATTERNS:
            self.matcher.add(pattern["label"], [pattern["pattern"]])

    def __call__(self, doc):
        matches = self.matcher(doc)
        doc._.mood = self._compute_mood(matches, doc)
        doc._.vibe_score = self._compute_vibe_score(matches, doc)
        doc._.emotional_spans = [(doc[start:end], label) for label, start, end in matches]
        return doc
```

Clean, simple, fun.

---

# 🎨 Web UI & API

### ✅ Streamlit Web Interface

Interactive web UI with:
* Real-time mood detection
* Visual vibe score display
* Emotional trigger highlighting
* JSON export
* Example texts

Run with: `streamlit run app.py`

### ✅ FastAPI REST API

Production-ready API with:
* Single text analysis endpoint
* Batch processing endpoint
* OpenAPI/Swagger documentation
* Health check endpoint
* CORS enabled

Run with: `python3 api.py` or `uvicorn api:app --reload`

Access docs at: `http://localhost:8000/docs`

---

# 🌟 Features

### ✅ Implemented

* **30+ mood categories** - Comprehensive emotional detection
* **Custom spaCy component** - Production-ready NLP pipeline
* **CLI interface** - Command-line tool
* **Web UI** - Interactive Streamlit interface
* **REST API** - FastAPI with batch processing
* **Unit tests** - Test coverage
* **Package installation** - Proper Python package setup

### 🚀 Future Add-Ons

* **Sarcasm classifier** - Enhanced sarcasm detection
* **Text rewrite** - Improve vibe score suggestions
* **Toxicity blocker** - Content moderation
* **Slack bot** - Real-time team mood analysis
* **Data visualization** - Charts and graphs
* **Model training** - Custom ML models
* **Multi-language support** - Beyond English

---

# 💬 Contribute

If you have more moods, open a PR.

Because humans invent 3 new emotions every Tuesday.

---

# 🧡 License

MIT. Do whatever. Be chaotic.

# mood-detector
