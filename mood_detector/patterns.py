"""
Mood patterns for the SpaCy Mood Detective.

Comprehensive patterns for detecting various emotional states and triggers.
"""

# Mood patterns for Matcher
MOOD_PATTERNS = [
    # Extreme positive emotions
    {
        "label": "ECSTATIC",
        "pattern": [{"LOWER": {"IN": ["love", "amazing", "fantastic", "perfect", "awesome", "brilliant", "wonderful", "incredible", "phenomenal", "spectacular", "outstanding", "marvelous", "magnificent", "sublime", "divine", "heavenly", "blissful", "euphoric", "thrilled", "overjoyed", "elated", "jubilant"]}}]
    },
    {
        "label": "HAPPY",
        "pattern": [{"LOWER": {"IN": ["happy", "glad", "excited", "joy", "yay", "woohoo", "great", "good", "nice", "pleased", "delighted", "cheerful", "joyful", "merry", "jolly", "upbeat", "positive", "optimistic", "sunny", "bright", "smiling", "grinning", "laughing", "giggling", "chuckling"]}}]
    },
    {
        "label": "WE_BALL",
        "pattern": [{"LOWER": {"IN": ["we", "ball", "let's", "go", "yesss", "yes!", "yeah", "yep", "yup", "hell", "yeah", "let's", "go", "here", "we", "go", "game", "on", "bring", "it", "on"]}}]
    },
    {
        "label": "GRATITUDE",
        "pattern": [{"LOWER": {"IN": ["thank", "thanks", "thankful", "grateful", "appreciate", "appreciation", "blessed", "blessing", "gratitude"]}}]
    },
    {
        "label": "PRIDE",
        "pattern": [{"LOWER": {"IN": ["proud", "pride", "accomplished", "achievement", "success", "successful", "victory", "won", "win", "champion", "championship", "triumph", "triumphant"]}}]
    },
    {
        "label": "RELIEF",
        "pattern": [{"LOWER": {"IN": ["relief", "relieved", "phew", "finally", "whew"]}}]
    },
    {
        "label": "RELIEF",
        "pattern": [{"LOWER": "sigh"}, {"LOWER": "of"}, {"LOWER": "relief"}]
    },
    {
        "label": "RELIEF",
        "pattern": [{"LOWER": "at"}, {"LOWER": "last"}]
    },
    {
        "label": "HOPE",
        "pattern": [{"LOWER": {"IN": ["hope", "hopeful", "hoping", "wish", "wishing", "pray", "praying", "optimistic", "optimism", "faith", "believe", "believing", "trust", "confident", "confidence"]}}]
    },
    {
        "label": "LOVE",
        "pattern": [{"LOWER": {"IN": ["love", "loving", "adore", "adoring", "cherish", "cherishing", "treasure", "treasuring", "affection", "affectionate", "fond", "fondness", "devotion", "devoted", "passion", "passionate", "romance", "romantic", "heart", "hearts"]}}]
    },
    {
        "label": "CALM",
        "pattern": [{"LOWER": {"IN": ["calm", "peaceful", "peace", "serene", "serenity", "tranquil", "tranquility", "zen", "relaxed", "relaxing", "chill", "chilling", "mellow", "laid", "back", "easygoing", "cool", "collected"]}}]
    },
    
    # Negative emotions - Anger and frustration
    {
        "label": "ANGRY",
        "pattern": [{"LOWER": {"IN": ["angry", "mad", "furious", "rage", "hate", "annoyed", "frustrated", "pissed", "irritated", "irritating", "livid", "enraged", "outraged", "fuming", "seething", "boiling", "steaming", "livid", "incensed", "infuriated", "resentful", "resentment", "bitter", "bitterness", "hostile", "hostility", "aggressive", "aggression", "rage", "raging"]}}]
    },
    {
        "label": "SAD",
        "pattern": [{"LOWER": {"IN": ["sad", "depressed", "down", "upset", "crying", "tears", "unhappy", "miserable", "lonely", "homesick", "nostalgic", "melancholy", "melancholic", "gloomy", "gloom", "sorrow", "sorrowful", "grief", "grieving", "mourning", "mournful", "heartbroken", "heartbreak", "devastated", "devastation", "crushed", "disheartened", "dejected", "despondent", "despair", "hopeless", "hopelessness", "bleak", "dismal", "woeful", "woe"]}}]
    },
    {
        "label": "LONGING",
        "pattern": [{"LOWER": {"IN": ["miss", "missing", "wish", "wishing", "longing", "yearn", "yearning", "crave", "craving", "ache", "aching", "homesick", "nostalgic", "nostalgia", "homesickness"]}}]
    },
    {
        "label": "ANXIETY",
        "pattern": [{"LOWER": {"IN": ["anxious", "anxiety", "worried", "worry", "worries", "nervous", "nervousness", "uneasy", "uneasiness", "apprehensive", "apprehension", "fearful", "fear", "afraid", "scared", "terrified", "terror", "panic", "panicking", "panicked", "dread", "dreading", "horrified", "horror", "paranoid", "paranoia", "fret", "fretting", "stressed", "stress", "pressure", "pressured", "overwhelmed", "overwhelming"]}}]
    },
    {
        "label": "STRESSED",
        "pattern": [{"LOWER": {"IN": ["stress", "stressed", "overwhelmed", "pressure", "pressured", "strained", "tension", "tense", "tight", "squeezed", "crushed", "burdened", "burden", "weight", "weighed", "down"]}}]
    },
    {
        "label": "TIRED",
        "pattern": [{"LOWER": {"IN": ["tired", "exhausted", "sleepy", "drained", "burned", "out", "fatigue", "fatigued", "weary", "weariness", "worn", "out", "spent", "drained", "drained", "depleted", "zapped", "zoned", "out", "dead", "tired", "beat", "wiped", "out", "knackered", "shattered"]}}]
    },
    {
        "label": "DISAPPOINTMENT",
        "pattern": [{"LOWER": {"IN": ["disappointed", "disappointment", "let", "down", "disheartened", "disheartening", "discouraged", "discouraging", "dismayed", "dismay", "disillusioned", "disillusionment", "disenchanted", "disenchantment", "dissatisfied", "dissatisfaction", "unfulfilled", "unfulfilling"]}}]
    },
    {
        "label": "REGRET",
        "pattern": [{"LOWER": {"IN": ["regret", "regretting", "regretted", "sorry", "apologize", "apology", "remorse", "remorseful", "guilt", "guilty", "ashamed", "shame", "shameful", "embarrassed", "embarrassment", "embarrassing", "humiliated", "humiliation", "mortified", "mortification"]}}]
    },
    {
        "label": "JEALOUSY",
        "pattern": [{"LOWER": {"IN": ["jealous", "jealousy", "envious", "envy", "covet", "coveting", "resentful", "resentment", "bitter", "bitterness"]}}]
    },
    {
        "label": "DISGUST",
        "pattern": [{"LOWER": {"IN": ["disgust", "disgusted", "disgusting", "revolting", "revolted", "repulsed", "repulsive", "repugnant", "appalled", "appalling", "sickened", "sickening", "nauseated", "nauseating", "gross", "grossed", "out", "yuck", "ew", "eww", "ugh", "yikes"]}}]
    },
    {
        "label": "BOREDOM",
        "pattern": [{"LOWER": {"IN": ["bored", "boring", "boredom", "tedious", "tedium", "dull", "dullness", "monotonous", "monotony", "uninteresting", "uninspiring", "mundane", "routine", "repetitive", "repetition", "stale", "stagnant"]}}]
    },
    {
        "label": "DESPAIR",
        "pattern": [{"LOWER": {"IN": ["despair", "despairing", "hopeless", "hopelessness", "helpless", "helplessness", "powerless", "powerlessness", "defeated", "defeat", "defeated", "giving", "up", "surrendered", "surrender", "resigned", "resignation"]}}]
    },
    
    # Sarcasm and casual
    {
        "label": "SARCASTIC",
        "pattern": [{"LOWER": {"IN": ["lol", "sure", "okay", "right", "yeah", "totally", "obviously", "clearly", "absolutely", "definitely", "certainly", "naturally", "indeed", "exactly", "precisely", "sarcasm", "sarcastic", "sarcastically", "ironic", "irony", "ironically"]}}]
    },
    {
        "label": "SARCASTIC",
        "pattern": [{"LOWER": "of"}, {"LOWER": "course"}]
    },
    {
        "label": "UNBOTHERED",
        "pattern": [{"LOWER": {"IN": ["whatever", "idc", "don't", "care", "meh", "eh", "ok", "fine", "alright", "sure", "whatever", "whatevs", "don't", "mind", "indifferent", "indifference", "apathetic", "apathy", "nonchalant", "nonchalance", "unconcerned", "unconcern"]}}]
    },
    
    # Confusion and uncertainty
    {
        "label": "CONFUSED",
        "pattern": [{"LOWER": {"IN": ["confused", "confusion", "what", "huh", "wtf", "why", "how", "lost", "unclear", "unclear", "bewildered", "bewilderment", "baffled", "baffling", "perplexed", "perplexing", "puzzled", "puzzling", "mystified", "mystifying", "disoriented", "disorientation", "dazed", "dazed", "stunned", "stunning", "stumped", "clueless", "cluelessness"]}}]
    },
    {
        "label": "SURPRISE",
        "pattern": [{"LOWER": {"IN": ["surprised", "surprise", "shocked", "shock", "shocking", "amazed", "amazing", "astonished", "astonishing", "astounded", "astounding", "stunned", "stunning", "staggered", "staggering", "bewildered", "bewilderment", "flabbergasted", "gobsmacked", "whoa", "wow", "omg", "holy", "cow"]}}]
    },
    
    # Existential and philosophical
    {
        "label": "EXISTENTIAL",
        "pattern": [{"LOWER": {"IN": ["why", "exist", "existence", "meaning", "meaningless", "meaninglessness", "purpose", "purposeless", "life", "universe", "everything", "nothing", "void", "emptiness", "empty", "pointless", "pointlessness", "absurd", "absurdity", "absurdism", "nihilistic", "nihilism", "philosophical", "philosophy", "deep", "thoughts"]}}]
    },
    
    # Problem avoidance and procrastination
    {
        "label": "PROBLEM_AVOIDANCE",
        "pattern": [{"LOWER": {"IN": ["disappeared", "ignored", "avoid", "skip", "later", "tomorrow", "maybe", "procrastinate", "procrastinating", "procrastination", "postpone", "postponing", "delay", "delaying", "stall", "stalling", "evade", "evading", "dodge", "dodging", "shirk", "shirking", "neglect", "neglecting", "abandon", "abandoning"]}}]
    },
    
    # Casual expressions and internet slang
    {
        "label": "CASUAL",
        "pattern": [{"LOWER": {"IN": ["bruh", "bro", "dude", "man", "yo", "hey", "sup", "what's", "up", "wassup", "yoo", "ayy", "ay", "haha", "hahaha", "lmao", "lmfao", "rofl", "lol", "lolz", "hehe", "hehehe", "teehee", "tee", "hee"]}}]
    },
    
    # Urgency and importance
    {
        "label": "URGENT",
        "pattern": [{"LOWER": {"IN": ["urgent", "urgency", "asap", "as", "soon", "as", "possible", "now", "immediately", "critical", "critically", "emergency", "emergencies", "please", "hurry", "hurrying", "rushed", "rushing", "hastily", "hasty", "quickly", "quick", "fast", "swiftly", "swift", "promptly", "prompt", "instant", "instantly", "right", "away", "stat"]}}]
    },
    
    # Excitement and enthusiasm
    {
        "label": "EXCITED",
        "pattern": [{"LOWER": {"IN": ["excited", "excitement", "exhilarated", "exhilarating", "thrilled", "thrilling", "pumped", "pumped", "up", "hyped", "hyped", "up", "psyched", "psyched", "up", "stoked", "stoked", "up", "energized", "energizing", "energetic", "energy", "enthusiastic", "enthusiasm", "eager", "eagerness", "anticipation", "anticipating", "anticipatory"]}}]
    },
    
    # Multi-word patterns for common phrases
    {
        "label": "SAD",
        "pattern": [{"LOWER": "can't"}, {"LOWER": {"IN": ["even", "deal", "handle", "take"]}}]
    },
    {
        "label": "ANXIETY",
        "pattern": [{"LOWER": {"IN": ["i", "im", "i'm"]}}, {"LOWER": {"IN": ["freaking", "freaking", "out", "panicking", "stressing"]}}]
    },
    {
        "label": "TIRED",
        "pattern": [{"LOWER": {"IN": ["need", "needing"]}}, {"LOWER": {"IN": ["sleep", "rest", "break", "nap"]}}]
    },
    {
        "label": "RELIEF",
        "pattern": [{"LOWER": "thank"}, {"LOWER": {"IN": ["god", "goodness", "heavens"]}}]
    },
    {
        "label": "SURPRISE",
        "pattern": [{"LOWER": {"IN": ["no", "oh"]}}, {"LOWER": {"IN": ["way", "my", "god"]}}]
    },
    {
        "label": "EXISTENTIAL",
        "pattern": [{"LOWER": "this"}, {"LOWER": "is"}, {"LOWER": "fine"}]
    },
    {
        "label": "ANGRY",
        "pattern": [{"LOWER": {"IN": ["are", "you"]}}, {"LOWER": {"IN": ["kidding", "serious", "joking"]}}]
    },
]

# Emotional trigger phrases (for highlighting)
EMOTIONAL_TRIGGERS = {
    "sarcasm": ["lol", "sure", "okay", "right", "totally", "obviously", "of course", "absolutely", "sarcastic"],
    "frustration": ["wtf", "seriously", "come on", "ugh", "argh", "frustrated", "annoyed", "irritated"],
    "excitement": ["amazing", "awesome", "incredible", "wow", "yay", "woohoo", "excited", "thrilled", "pumped"],
    "tiredness": ["tired", "exhausted", "sleepy", "need sleep", "burned out", "drained", "wiped out"],
    "longing": ["miss", "missing", "wish", "longing", "homesick", "nostalgic", "yearning"],
    "confusion": ["what", "huh", "confused", "unclear", "lost", "baffled", "perplexed"],
    "problem_avoidance": ["disappeared", "ignored", "later", "tomorrow", "maybe", "procrastinate"],
    "casual": ["bruh", "bro", "dude", "lol", "ok", "haha", "lmao"],
    "urgency": ["asap", "urgent", "now", "immediately", "please", "hurry"],
    "anxiety": ["anxious", "worried", "nervous", "stressed", "panic", "fear"],
    "sadness": ["sad", "depressed", "crying", "lonely", "miserable", "heartbroken"],
    "anger": ["angry", "mad", "furious", "rage", "hate", "pissed", "livid"],
    "love": ["love", "adore", "cherish", "affection", "heart", "hearts"],
    "gratitude": ["thank", "thanks", "grateful", "appreciate", "blessed"],
    "surprise": ["surprised", "shocked", "amazed", "wow", "omg", "no way"],
    "disappointment": ["disappointed", "let down", "disheartened", "discouraged"],
    "regret": ["regret", "sorry", "guilt", "ashamed", "embarrassed"],
    "boredom": ["bored", "boring", "tedious", "dull", "mundane"],
    "calm": ["calm", "peaceful", "relaxed", "chill", "zen", "serene"],
}

# Vibe score weights (comprehensive)
VIBE_WEIGHTS = {
    "ECSTATIC": 9,
    "HAPPY": 6,
    "WE_BALL": 7,
    "GRATITUDE": 7,
    "PRIDE": 6,
    "RELIEF": 5,
    "HOPE": 4,
    "LOVE": 8,
    "CALM": 3,
    "EXCITED": 7,
    "ANGRY": -8,
    "SAD": -7,
    "LONGING": -6,
    "ANXIETY": -6,
    "STRESSED": -5,
    "TIRED": -4,
    "DISAPPOINTMENT": -5,
    "REGRET": -5,
    "JEALOUSY": -4,
    "DISGUST": -6,
    "BOREDOM": -3,
    "DESPAIR": -8,
    "SARCASTIC": -3,
    "UNBOTHERED": -1,
    "CONFUSED": -2,
    "SURPRISE": 2,  # Can be positive or negative, neutral
    "EXISTENTIAL": -4,
    "PROBLEM_AVOIDANCE": -4,
    "CASUAL": 1,
    "URGENT": -2,
}

# Mood labels mapping (human-readable)
MOOD_LABELS = {
    "ECSTATIC": "ecstatic",
    "HAPPY": "happy",
    "WE_BALL": "we ball",
    "GRATITUDE": "grateful",
    "PRIDE": "proud",
    "RELIEF": "relieved",
    "HOPE": "hopeful",
    "LOVE": "loving",
    "CALM": "calm",
    "EXCITED": "excited",
    "ANGRY": "angry",
    "SAD": "sad",
    "LONGING": "nostalgic",
    "ANXIETY": "anxious",
    "STRESSED": "mildly stressed",
    "TIRED": "chaotic tired",
    "DISAPPOINTMENT": "disappointed",
    "REGRET": "regretful",
    "JEALOUSY": "jealous",
    "DISGUST": "disgusted",
    "BOREDOM": "bored",
    "DESPAIR": "despairing",
    "SARCASTIC": "sarcastic",
    "UNBOTHERED": "unbothered",
    "CONFUSED": "confused",
    "SURPRISE": "surprised",
    "EXISTENTIAL": "existential",
    "PROBLEM_AVOIDANCE": "chaotic frustration",
    "CASUAL": "casual",
    "URGENT": "urgent",
}
