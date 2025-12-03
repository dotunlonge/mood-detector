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
pip install spacy
python -m spacy download en_core_web_sm
```

Clone the repo:

```bash
git clone https://github.com/yourname/spacy-mood-detective
cd spacy-mood-detective
```

Run it:

```bash
python3 detective.py "I'm too tired to deal with this API today."
```

Or make it executable and run directly:

```bash
chmod +x detective.py
./detective.py "I'm too tired to deal with this API today."
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
├── examples/
│   └── sample_texts.txt
│
├── detective.py           # CLI runner
├── README.md
└── requirements.txt
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

# 🎨 Optional: Web UI

Add a tiny **Streamlit** or **Gradio** interface:

* Type text

* Detect mood

* Highlight phrases

* Massive emojis for mood output

People will love it.

---

# 🌟 Ideas for Future Add-Ons

* **Sarcasm classifier**

* **"Breakup message detector"**

* **Text rewrite to improve vibe score**

* **Toxicity blocker**

* **Slack bot** that analyzes team messages

* **API endpoint** for mood-as-a-service (MaaS)

---

# 💬 Contribute

If you have more moods, open a PR.

Because humans invent 3 new emotions every Tuesday.

---

# 🧡 License

MIT. Do whatever. Be chaotic.

# mood-detector
