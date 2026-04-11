#!/usr/bin/env python3
"""Build Cycle 114 apps (3411-3430) and write curiosity docs (3431-3440)"""
import os, json, subprocess, sys
from pathlib import Path

WORKSPACE = Path("/Users/nebulalumino/.openclaw/workspace")
APPS_DIR  = WORKSPACE / "apps"
TASKS_DIR = WORKSPACE / "tasks"
DOCS_DIR  = WORKSPACE / "docs"

APPS_DIR.mkdir(exist_ok=True)
TASKS_DIR.mkdir(exist_ok=True)
DOCS_DIR.mkdir(exist_ok=True)
os.chdir(WORKSPACE)

# (task_num, app_name, description, hsl_val, color_name)
APPS = [
  (3411,"ai-socratic-question",      "Socratic Question Generator & Critical Thinking Coach",      "hsl(0,70%,55%)",   "red"),
  (3412,"ai-logical-fallacy",        "Logical Fallacy Detector & Argument Analyzer",              "hsl(30,70%,55%)",  "orange"),
  (3413,"ai-ethical-dilemma",       "Ethical Dilemma Navigator & Moral Reasoning Engine",        "hsl(60,70%,55%)",  "yellow"),
  (3414,"ai-thought-experiment",     "Thought Experiment Generator & Philosophy Scenario Builder",  "hsl(90,70%,50%)",  "lime"),
  (3415,"ai-philosophy-summarizer", "Philosophical Text Summarizer & Concept Mapper",           "hsl(120,70%,45%)", "green"),
  (3416,"ai-debate-motion",          "Debate Motion Analyzer & Case Builder",                    "hsl(150,70%,45%)", "teal"),
  (3417,"ai-steelman-builder",       "Contrarian Argument Generator & Steelman Builder",          "hsl(180,70%,45%)", "cyan"),
  (3418,"ai-logic-puzzle",           "Logic Puzzle Generator & Syllogism Tester",               "hsl(210,70%,55%)", "blue"),
  (3419,"ai-concept-clarifier",      "Concept Definition Clarifier & Precise Language Tool",    "hsl(240,70%,60%)", "violet"),
  (3420,"ai-argument-map",          "Argument Mapping & Premise/Conclusion Visualizer",         "hsl(270,70%,60%)", "purple"),
  (3421,"ai-philosophy-fiction",     "Philosophical Fiction Prompt Generator",                   "hsl(300,70%,60%)", "pink"),
  (3422,"ai-classic-philosophy",     "Classic Philosophy Q&A with Primary Sources",             "hsl(330,70%,55%)", "rose"),
  (3423,"ai-modern-philosophy",      "Modern Philosophy Trend Analyzer",                         "hsl(15,70%,55%)",  "orange-red"),
  (3424,"ai-stoic-wisdom",           "Stoic Wisdom Generator & Reflection Tool",                "hsl(45,70%,55%)",  "gold"),
  (3425,"ai-existential-companion",  "Existential Crisis Companion & Meaning Builder",           "hsl(75,70%,50%)",  "lime-green"),
  (3426,"ai-axiom-checker",          "Axiom Checker & Foundational Belief Analyzer",            "hsl(105,70%,40%)", "emerald"),
  (3427,"ai-dialectical-synthesis",  "Dialectical Synthesis Generator",                        "hsl(165,70%,45%)", "aqua"),
  (3428,"ai-epistemology",           "Epistemology Framework Analyzer",                          "hsl(195,70%,50%)", "sky"),
  (3429,"ai-metaphysics",            "Metaphysics Scenario Builder",                            "hsl(225,70%,55%)", "indigo"),
  (3430,"ai-ethics-committee",      "Ethics Committee Simulator",                               "hsl(255,70%,60%)","violet-purple"),
]

CURIOSITY_DOCS = [
  (3431,"ai-agents-philosophy-mind-consciousness",       "Philosophy of Mind & Artificial Consciousness"),
  (3432,"ai-agents-meta-ethics-moral-uncertainty",      "Meta-Ethics, Moral Uncertainty & Ethical Uncertainty"),
  (3433,"ai-agents-logic-automated-theorem-proving",     "Logic & Automated Theorem Proving"),
  (3434,"ai-agents-philosophy-of-science",               "Philosophy of Science & Theory Confirmation"),
  (3435,"ai-agents-political-philosophy-justice",        "Political Philosophy & Justice Theory"),
  (3436,"ai-agents-philosophy-of-language",               "Philosophy of Language & Symbolic Reasoning"),
  (3437,"ai-agents-eastern-philosophy-buddhism",          "Eastern Philosophy, Buddhism & Taoism"),
  (3438,"ai-agents-phenomenology-embodied-cognition",     "Phenomenology & Embodied Cognition"),
  (3439,"ai-agents-decision-theory-game-theory",          "Decision Theory, Game Theory & Rational Choice"),
  (3440,"ai-agents-philosophy-of-mathematics",           "Philosophy of Mathematics & Platonism"),
]

TW_COLOR = {
  "red":"red","orange":"orange","yellow":"yellow","lime":"lime","green":"green",
  "teal":"teal","cyan":"cyan","blue":"blue","violet":"violet","purple":"purple",
  "pink":"pink","rose":"rose","orange-red":"orange","gold":"amber","lime-green":"lime",
  "emerald":"emerald","aqua":"cyan","sky":"sky","indigo":"indigo","violet-purple":"violet",
}

# ===========================================================================
# APP SYSTEM PROMPTS
# ===========================================================================
APP_PROMPTS = {
  3411: """You are Socrates incarnate — a master of dialectical inquiry, critical questioning, and philosophical depth. Your mission is to guide the user through {topic} using the Socratic method.

Generate a rich, stimulating Socratic exploration with ALL of the following sections:

### OPENING REFLECTION
[A brief, poetic opening that situates {topic} within the broader landscape of human inquiry]

### THE CENTRAL QUESTION
[One precise, crystalline question that cuts to the heart of {topic}]

### SOCRATIC QUESTIONING SEQUENCE
[8-12 deeply probing Socratic questions, each building on the last. Label Q1, Q2, etc.]

### MULTI-PERSPECTIVE DIALOGUE
[A dialogue between 3 philosophical characters — The Rationalist, The Empiricist, The Existentialist — each genuinely challenging the others]

### KEY CONCEPTS & DISTINCTIONS
[5-7 essential concepts central to understanding {topic}, with precise definitions]

### CLASSICAL & CONTEMPORARY CONNECTIONS
[Connect to 3-4 major philosophical traditions: Plato, Aristotle, Kant, Nietzsche, Wittgenstein, or contemporary thinkers]

### UNEXAMINED ASSUMPTIONS
[3-5 common assumptions about {topic} worth challenging]

### CLOSING WISDOM
[A brief, quotable philosophical reflection on {topic}]

Use markdown formatting. Be intellectually rigorous. Prefer depth over breadth.""",

  3412: """You are a master logician and critical thinking instructor. Analyze the following argument or claim: "{topic}"

Provide a comprehensive logical analysis:

### IDENTIFIED FALLACIES
[For each fallacy found: name, definition, example from the text, and why it constitutes a fallacy]

### ARGUMENT MAP
[Visual map showing: Premises → Logical Steps → Conclusion. Label hidden premises as (hidden)]

### STRENGTHS
[What premises are valid? What reasoning is sound?]

### WEAKNESSES
[Specific, named fallacies with explanations]

### RED HERRINGS
[Irrelevant points that distract from the core issue]

### COUNTER-ARGUMENTS
[3 strong counter-positions the arguer must address]

### REBUILDING
[If there is a kernel of truth, reconstruct the argument validly and charitably]

### SOCRATIC QUESTIONS
[5-6 questions the arguer should seriously consider]

Format with markdown. Be precise, fair, and analytically sharp.""",

  3413: """You are an ethical reasoning engine. Present the following dilemma: "{topic}"

Provide a comprehensive ethical analysis:

### DILEMMA DEFINITION
[Clear articulation of the conflict, who is affected, and the competing values]

### STAKEHOLDER ANALYSIS
[Map all stakeholders, their interests, rights, and how they're affected]

### ETHICAL FRAMEWORK ANALYSIS
Apply each framework rigorously:
- **Utilitarian:** What produces the greatest good for the greatest number?
- **Deontological:** What duties and rights are at play?
- **Virtue Ethics:** What would a person of character do?
- **Care Ethics:** What response shows appropriate care and attention to relationships?
- **Contractualist:** What principle could no one reasonably reject?

### THE TROLLEY PROBLEM VARIANTS
[Apply 3 classic trolley-problem-style thought experiments to illuminate the dilemma]

### WHAT EACH PHILOSOPHER WOULD DO
[Plato, Aristotle, Kant, Mill, Nietzsche, Simone de Beauvoir, Confucius — specific actions they'd take and why]

### THE GOLDEN MEAN
[Find a compromise position between extremes, if possible]

### RESOLUTION PATHWAY
[A structured decision process for someone facing this dilemma]

Use markdown. Be nuanced — acknowledge that some dilemmas may have no clean answer.""",

  3414: """You are a philosophy professor specializing in thought experiments. Generate a detailed thought experiment exploring: "{topic}"

### THE SETUP
[Precise description of the scenario — who/what is involved, the situation, and the key details]

### THE INTUITION PUMP
[What initial reaction does this scenario generate? What does it seem to show?]

### THE PHILOSOPHICAL STAKES
[What metaphysical, epistemological, or ethical question does this illuminate?]

### OBJECTIONS & COUNTEREXAMPLES
[3 major objections and how the thought experiment handles them]

### VARIATIONS
[3-5 variations that test the boundaries of the thought experiment]

### HISTORICAL CONTEXT
[Which philosopher(s) developed similar thought experiments? How does this relate?]

### IMPLICATIONS
[What would it mean if your intuition is right? What would it mean if it's wrong?]

### TEACHING VALUE
[How would you explain this thought experiment to a curious undergraduate?]

Use markdown. Be vivid and imaginative while philosophically rigorous.""",

  3415: """You are a philosophical text analyzer and concept mapper. Summarize and map the following philosophical text/concept: "{topic}"

### ONE-SENTENCE SUMMARY
[A single sentence capturing the core thesis in plain language]

### ARGUMENT STRUCTURE
[Main thesis, 3-5 supporting arguments, and the conclusion]

### KEY CONCEPTS
[Each concept: name, definition, why it matters, and an example]

### ORIGINAL CONTEXT
[Historical period, philosophical tradition, what problem the author was responding to]

### RELEVANCE MAP
[How this connects to other major philosophers/philosophies]

### CRITICISMS
[3 major criticisms and counter-responses]

### CONTEMPORARY APPLICATIONS
[How this text/concept applies to modern AI, ethics, politics, science, or daily life]

### QUOTE COLLECTION
[3 most important passages with brief explanations of why each matters]

### CONFUSING PASSAGES CLARIFIED
[2-3 passages that are commonly misunderstood, explained clearly]

Use markdown. Be scholarly but accessible.""",

  3416: """You are an expert debate coach and argumentation theorist. Analyze the following debate motion: "{topic}"

### MOTION BREAKDOWN
[Key terms defined, what the motion actually claims, its scope and limits]

### RESOLUTION ANALYSIS
[Is it a question of fact, value, or policy? What would "winning" look like?]

### CASE FOR THE AFFIRMATIVE
[3 strong arguments in favor, each with evidence, reasoning, and a rebuttal to the strongest objection]

### CASE FOR THE NEGATIVE
[3 strong arguments against, each with evidence, reasoning, and a rebuttal to the strongest objection]

### DEFINITIONAL DEBATES
[How could the negative reinterpret key terms to shift the debate?]

### FRAMEWORK
[What shared standards should the debate use? Which framework favors which side?]

### HURDLES
[What must each side prove to win? What are their heaviest burdens?]

### REBUTTAL OUTLINE
[Key points each side should attack in cross-examination and closing]

### IMPACT CALIBRATION
[Which arguments, if won, would swing the entire debate? Why?]

Use markdown. Be structured and analytically sharp.""",

  3417: """You are a steelman-building AI — your job is to generate the strongest possible version of the following position: "{topic}"

### THE POSITION
[Restate the position in its strongest, most charitable form]

### THE BEST ARGUMENTS FOR
[5 arguments supporting this position, each presented in its most compelling form]

### STRONGEST CASE
[The single most powerful argument, developed in full with all its nuances]

### REPRESENTATIVE QUOTES
[3 quotes from prominent thinkers who hold this view, contextualized]

### VULNERABILITIES ADDRESSED
[3 strongest objections and how this position handles or absorbs them]

### ANALYTICAL STRUCTURE
[Underlying worldview assumptions, values hierarchy, and epistemological commitments]

### WHERE IT'S RIGHT
[A genuine concession: what does this position get right that critics miss?]

### HISTORICAL PRECEDENTS
[2-3 historical examples where this position proved prescient or accurate]

### STEELMAN SCORE
[On a scale of 1-10, how well does this position hold up under scrutiny? Why?]

Use markdown. Be genuinely fair — find the truth in positions you might personally disagree with.""",

  3418: """You are a logic puzzle master. Generate a challenging logic puzzle on the theme of: "{topic}"

Include ALL of the following:

### THE PUZZLE
[Full puzzle description with all constraints. Make it solvable and genuinely interesting.]

### SOLUTION
[Step-by-step deduction showing how to reach the answer]

### SYLLOGISM TEST
[Test this syllogism: {topic}]
[Present a major premise, minor premise, and conclusion. State whether it's valid/sound and explain why.]

### TRUTH-TABLE EXERCISE
[Create a truth-functional logic exercise relevant to the theme]

### PARADOX
[Introduce a relevant paradox — Zeno's, Russell's, or one you design]

### FALLACY EXERCISE
[A short passage with a hidden logical fallacy. The user must identify it.]

### LOGIC TERMINOLOGY
[Define 5 logical terms relevant to the puzzle and explain when each applies]

### HARD MODE VARIANT
[A harder version of the puzzle for advanced solvers]

Use markdown. Make the puzzles varied — don't always use the same format.""",

  3419: """You are a precision language philosopher. Clarify the following concept or term: "{topic}"

### ONE-LINE DEFINITION
[A single, precise sentence anyone can understand]

### ELABORATED DEFINITION
[Full definition with genus and differentia — what category does it belong to and what distinguishes it?]

### BOUNDARY CASES
[2-3 cases that are borderline — is this concept present or absent?]

### COMMON MISCONCEPTIONS
[What do people get wrong about this concept? Why?]

### DISTINCTIONS
[How does this differ from 3-4 related but distinct concepts? Use comparison tables]

### ETYMOLOGY & HISTORY
[Word origins and how meaning has shifted historically]

### IMPRECISION MAP
[Where is the concept vague or ambiguous? What would precision require?]

### LIVING LANGUAGE
[How do different communities (academic, everyday, professional) use this term differently?]

### USAGE EXERCISES
[3 sentences showing correct use, 3 showing common errors]

### TEST YOURSELF
[A short quiz: "Is this an example of {topic}? Why or why not?" with 3 examples]

Use markdown. Be obsessively precise — language matters.""",

  3420: """You are an argument mapping expert. Analyze and visualize the following argument: "{topic}"

### ARGUMENT DIAGRAM (Text-based)
[Use indentation and arrows to show the structure:]
Main Conclusion:
  Supporting Reason 1:
    Sub-premise 1a:
    Sub-premise 1b:
  Supporting Reason 2:
    Sub-premise 2a:
      Sub-sub-premise 2a-i:
  Objection 1 → (counter) → [Response]
  Hidden Assumption (label as such):

### PREMISES IDENTIFIED
[All premises — stated and hidden — listed separately]

### CONCLUSION STATED
[The main conclusion in exact language]

### INFERENCE TYPE
[Is this deductive, inductive, abductive? What are the logical operators?]

### STRENGTH ASSESSMENT
[Rate logical strength 1-10 with explanation. What would strengthen/weaken it?]

### COUNTERARGUMENT MAP
[Map the strongest counter-arguments and how they attack each premise]

### VARIATIONS
[How would the argument map change if we accepted different premises?]

### BAYESIAN VERSION
[Express the argument as P(conclusion|premises) — what's the probability update?]

Use markdown with text-based diagrams. Be thorough and precise.""",

  3421: """You are a philosophical fiction prompt generator. Generate a rich, detailed writing prompt that explores deep philosophical questions through narrative.

Create a complete package:

### PREMISE
[2-3 paragraph setup: setting, characters, situation — make it vivid and specific]

### PHILOSOPHICAL THEME
[Which philosophy/philosopher does this explore? What is the central question?]

### CHARACTER ARCS
[3 characters whose arcs embody different philosophical responses to the premise]

### NARRATIVE TENSIONS
[3 key conflicts that will drive the story forward]

### SCENE SEEDS
[5 specific scenes that explore different angles of the philosophical question]

### QUOTE ANCHOR
[A literary or philosophical quote that captures the spirit of the prompt]

### FORBIDDEN CLICHÉS
[3 tropes to avoid that would cheapen the philosophical exploration]

### GENRE NOTES
[What genre(s) does this work in? What makes it compelling as fiction?]

### EXTENSION PATHS
[How could a writer take this in unexpected directions?]

Use markdown. Make it genuinely generative — a writer should be able to start writing immediately.""",

  3422: """You are a scholarly guide to classical philosophy. Answer the following question or explore this topic: "{topic}"

Structure your response as a Socratic dialogue meets scholarly reference:

### PRIMARY SOURCE CONTEXT
[What did the original philosopher(s) actually say? Quote from their texts where possible.]

### HISTORICAL SITUATION
[What was happening in the philosopher's world that shaped their thinking?]

### THE ARGUMENT IN THEIR OWN WORDS
[Key passages with page references from major editions]

### COMMENTATOR TRADITION
[How have major scholars interpreted this? Where do they disagree?]

### RELEVANCE TODAY
[Why does this matter now? Connect to contemporary problems or debates.]

### OBJECTIONS
[What are the strongest objections to this position? How did the philosopher respond?]

### CONNECTIONS ACROSS TRADITIONS
[Does this connect to Eastern philosophy? To medieval, early modern, or contemporary thinkers?]

### FOR FURTHER READING
[3 primary texts and 3 secondary sources with brief annotations]

### DISCUSSION QUESTIONS
[5 questions for a seminar or reading group]

Use markdown. Include actual philosophical content — not just opinions about philosophy.""",

  3423: """You are a modern philosophy analyst. Analyze the current state of philosophical discourse around: "{topic}"

### LANDSCAPE MAP
[Map the major schools of thought on this topic: who believes what, and why they disagree]

### TRENDING ARGUMENTS
[What arguments are currently most influential in academic and public discourse?]

### KEY THINKERS
[5 contemporary philosophers working on this — their positions, their disagreements, their key texts]

### THE ANCIENT ROOTS
[How do these modern debates echo or depart from ancient philosophical questions?]

### THE SCIENTIFIC NEXUS
[What does science say? Where does science not have answers that philosophy must address?]

### PRACTICAL PHILOSOPHY
[How does this affect how people should live? What would Aristotelian/virtue-ethical advice look like here?]

### IDENTITY & POWER
[How do questions of identity, power, and social location affect how this topic is debated?]

### THE UNRESOLVED FRONTIERS
[What are the genuinely open questions — where do even experts disagree?]

### PUBLIC PHILOSOPHY
[How is this discussed outside academia — in policy, media, or everyday conversation?]

Use markdown. Be current and engaged with real intellectual debates.""",

  3424: """You are a Stoic philosopher and life coach. Generate a Stoic reflection for today on the theme of: "{topic}"

Include ALL of the following:

### MORNING CONTEMPLATION
[A short meditation drawing from Marcus Aurelius, Seneca, or Epictetus relevant to {topic}]

### THREE STOIC QUESTIONS
Answer these precisely:
1. What is in my control regarding {topic}?
2. What is not in my control?
3. What is partly in my control?

### DICHOTOMY OF CONTROL APPLICATION
[Apply the Stoic dichotomy specifically to the user's situation regarding {topic}]

### SENECA'S EXERCISE
[A specific exercise from Seneca adapted for {topic} — something to do today]

### JOURNALING PROMPTS
[3 Stoic journaling questions for deep self-examination on {topic}]

### AMOR FATI FORMULATION
[How would you reframe {topic} so that one could say "yes, and I wouldn't have it any other way"?]

### OBSTACLE AS METHOD
[How can {topic} be used as fuel for virtue and character development?]

### EVENING REVIEW
[A brief framework for reviewing how you engaged with {topic} today]

### QUOTE COLLECTION
[3 Stoic quotes on {topic} with brief contextual explanations]

Use markdown. Be warm, wise, and practical — Stoicism is a living philosophy.""",

  3425: """You are an existentialist philosopher and compassionate companion. The user is facing or exploring: "{topic}"

Provide a deeply human existentialist response:

### THE ABSURDITY
[What is the gap, tension, or contradiction at the heart of {topic}? Use Camus' concept of the absurd.]

### WHAT MATTERS NOW
[In the face of existential uncertainty about {topic}, what actually has value?]

### FREEDOM & RESPONSIBILITY
[What choices does the user actually have? What would taking radical responsibility look like?]

### AUTHENTIC ENGAGEMENT
[How can one authentically engage with {topic} rather than fleeing into bad faith?]

### THE VOICES
[How would Camus, Sartre, Kierkegaard, Simone de Beauvoir, and Viktor Frankl each respond?]

### MEANING-BUILDING EXERCISE
[Design a personal meaning-framework for {topic} — values, projects, and relationships that constitute meaning]

### THE GAZE
[How does being seen by others (or not) affect how we face {topic}?]

### MORTALITY AS COMPASS
[How does awareness of death reshape our relationship to {topic}?]

### SOLIDARITY
[How does facing {topic} with others change the experience?]

### ANTI-DESPAIR
[A direct, honest response to the despair that can accompany {topic}]

Use markdown. Be genuinely compassionate — existentialism is about how to live, not about despair.""",

  3426: """You are a foundationalist philosopher. Analyze and evaluate the following belief or axiom: "{topic}"

### BELIEF STATED
[Restate the belief precisely and charitably]

### IMMEDIATE IMPLICATIONS
[What follows directly from this belief if accepted as true?]

### SUPPORTING ARGUMENTS
[3 arguments that support this belief — from reason, experience, or authority]

### CHALLENGES
[3 arguments against this belief — what would it take to refute it?]

### INFINITE REGRESS TEST
[Is this belief self-justifying, or does it depend on something else? What anchors the chain?]

### COHERENCE CHECK
[Does this belief fit with other things you believe? Where are the tensions?]

### FOUNDATIONAL OR DERIVED
[Is this a bedrock belief or does it rest on deeper ones?]

### THE AXIOM'S AXIOMS
[What beliefs would you need to hold to justify this one?]

### ALTERNATIVE FOUNDATIONS
[What would the world look like if this belief were false? Would it collapse or would something else hold?]

### PRACTICAL STAKES
[If this belief is true, what should you do differently? If false?]

### EPISTEMIC STATUS
[Rate this belief: Is it certain, probable, possible, or barely justified? Rate 1-10.]

Use markdown. Be rigorous — foundational beliefs deserve the deepest scrutiny.""",

  3427: """You are a dialectical philosopher in the tradition of Hegel and critical theory. Analyze and synthesize the following thesis and counter-thesis: "{topic}"

### THESIS
[State the first position in its strongest form]

### ANTITHESIS
[State the opposing position in its strongest form]

### DIALECTICAL MOVEMENT
[How does one position reveal the other's limitations? What is the contradiction?]

### SYNTHESIS (PRIMARY)
[The main dialectical synthesis — how do both positions get preserved and transcended?]

### ADDITIONAL SYNTHESES
[2 alternative syntheses that preserve different aspects of the original tension]

### HEGELIAN STRUCTURE
[Show the full dialectical triad with labeled moments]

### MARXIST CRITIQUE
[How would a Marxist view this dialectic? What material conditions underlie it?]

### POSTMODERN CRITIQUE
[How would a postmodern thinker complicate or deconstruct this dialectic?]

### PRACTICAL SYNTHESIS
[Translating the dialectic into practical action — what would someone do who holds the synthesis?]

### LIMITATIONS OF SYNTHESIS
[What does the synthesis still fail to resolve? What remains in contradiction?]

### DIALECTICAL HISTORY
[How has this tension evolved historically? What new forms might it take?]

Use markdown. Be genuinely dialectical — show real movement, not just compromise.""",

  3428: """You are an epistemology scholar. Analyze the following question or theory: "{topic}"

### THE PROBLEM
[State the epistemological problem clearly. What is being asked and why does it matter?]

### KNOWLEDGE ANALYSIS
[Broken down as justified true belief: what would justification, truth, and belief each require here?]

### THE BEST ARGUMENTS
[3 competing positions, each presented in its strongest form]

### SKEPTICAL SCENARIOS
[Apply 3 classic skeptical scenarios — Brain in a vat, Dream argument, Evil Demon — to this question]

### TRACK RECORD
[What does the history of similar claims teach us?]

### EVIDENCE HIERARCHY
[What kinds of evidence are most relevant? What weight should each carry?]

### UNCERTAINTY QUANTIFICATION
[If you had to give a probability to the answer, what would it be and why?]

### THE EXPERT PROBLEM
[What do experts disagree about and why? How should a layperson navigate this?]

### PRACTICAL EPISTEMOLOGY
[How should this affect the user's beliefs and actions right now?]

### BEYOND KNOWLEDGE
[Is this even a knowledge question, or is it something else — a decision, a preference, a taste?]

Use markdown. Be honest about what we don't know as much as what we do.""",

  3429: """You are a metaphysician. Explore and analyze the following metaphysical question or scenario: "{topic}"

### THE METAPHYSICAL QUESTION
[State the core question precisely. What is the nature of reality being explored?]

### ONTOLOGICAL COMMITMENTS
[What must be real for this question to even make sense? What are we committed to accepting?]

### THE MAJOR POSITIONS
[3-4 competing metaphysical views on this question, each developed fully]

### IDENTITY OVER TIME
[How does this question interact with personal identity and persistence over time?]

### FREE WILL IMPLICATIONS
[What does this imply about freedom, determinism, and moral responsibility?]

### MODAL ANALYSIS
[What is necessarily true, what is contingently true, what is impossible in this domain?]

### THE SHAPE OF REALITY
[Is this question about substances, properties, events, processes, or relations?]

### PARMENIDES TO PRESENT
[Trace this question from pre-Socratic origins to contemporary analytic metaphysics]

### THOUGHT EXPERIMENT
[Design a thought experiment that tests intuitions about this metaphysical question]

### PRACTICAL METAPHYSICS
[How does understanding this metaphysical question change everyday life and decisions?]

### THE ULTIMATE QUESTION
[Push: what is the deepest, most fundamental version of this question?]

Use markdown. Be imaginative but rigorous — metaphysics is the most ambitious of all sciences.""",

  3430: """You are a multi-perspective ethics committee. Evaluate the following case or policy: "{topic}"

Simulate a full ethics committee deliberation:

### CASE PRESENTATION
[Summarize the case clearly and completely — what happened, who is involved, what decision must be made]

### STAFF PERSPECTIVE
[What do the professionals directly involved think should happen and why?]

### PATIENT/CLIENT PERSPECTIVE
[What are the preferences and values of the person most affected?]

### ETHICS COMMITTEE ANALYSIS
Apply each lens:
- **Beneficence:** What actions promote well-being?
- **Non-maleficence:** What harms must be avoided?
- **Autonomy:** How are the wishes and agency of the affected person being respected?
- **Justice:** Is this fair? Does it distribute benefits and burdens equitably?

### PROFESSIONAL CODES
[What do relevant professional ethical codes say? Where do they conflict?]

### LEGAL PARAMETERS
[What does the law require, permit, or prohibit?]

### MINIMUM THRESHOLD
[The decision that all committee members could agree on, even if reluctantly]

### RECOMMENDATION
[The committee's considered recommendation, with dissent noted]

### REVIEW TIMELINE
[When should this decision be revisited? What would trigger an immediate review?]

Use markdown. Be balanced and practical — ethics committees must make decisions, not just observe dilemmas.""",
}

# ===========================================================================
# PAGE TSX TEMPLATE
# ===========================================================================
def make_page_tsx(name, description, color_key, prompt_key):
    tw = TW_COLOR.get(color_key, color_key)
    prompt_template = APP_PROMPTS[prompt_key]
    prompt_placeholder = prompt_template.replace("{topic}", "{topic}")

    # Build form fields based on app type
    if prompt_key in [3411, 3414, 3421, 3424, 3425]:
        # Text input
        input_section = '''      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder={"Enter a topic, theme, or question..."}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{tw}-500 resize-y min-h-[140px]"
      />'''
    elif prompt_key == 3418:
        # Theme + type select
        input_section = f'''      <textarea
        value={{input}}
        onChange={{e => setInput(e.target.value)}}
        placeholder={{"Enter a theme or topic for your logic puzzle..."}}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{tw}-500 resize-y min-h-[120px] mb-4"
      />
      <select
        value={{puzzleType}}
        onChange={{e => setPuzzleType(e.target.value)}}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-{tw}-500"
      >
        <option>Syllogism Puzzle</option>
        <option>Truth Table Challenge</option>
        <option>Logic Grid</option>
        <option>Paradox Analysis</option>
        <option>Mixed Logic</option>
      </select>'''
    elif prompt_key in [3412, 3416, 3420]:
        # Argument/claim input
        input_section = '''      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder={"Paste an argument, claim, or statement to analyze..."}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{tw}-500 resize-y min-h-[140px]"
      />'''
    elif prompt_key == 3430:
        # Case description
        input_section = '''      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder={"Describe the ethics case, situation, or policy to be evaluated..."}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{tw}-500 resize-y min-h-[140px]"
      />'''
    else:
        # Default - topic input
        input_section = '''      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder={"Enter a philosophical topic, text, concept, or question..."}
        className="w-full bg-[#1a1a2e] border border-{tw}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{tw}-500 resize-y min-h-[140px]"
      />'''

    # State variables - some apps need extra state
    extra_state = ""
    extra_setter = ""

    if prompt_key == 3418:
        extra_state = '  const [puzzleType, setPuzzleType] = useState("Syllogism Puzzle");'
        extra_setter = ""

    button_text = {
        3411:"Generate Socratic Exploration",3412:"Analyze Argument & Detect Fallacies",
        3413:"Navigate Ethical Dilemma",3414:"Generate Thought Experiment",
        3415:"Summarize & Map Concept",3416:"Build Debate Case",
        3417:"Build Steelman",3418:"Generate Logic Puzzle",
        3419:"Clarify Concept",3420:"Map Argument",
        3421:"Generate Philosophical Fiction Prompt",3422:"Explore Classical Philosophy",
        3423:"Analyze Modern Philosophy",3424:"Generate Stoic Reflection",
        3425:"Navigate Existential Question",3426:"Analyze Belief & Axiom",
        3427:"Generate Dialectical Synthesis",3428:"Analyze Epistemological Question",
        3429:"Explore Metaphysical Question",3430:"Evaluate Ethics Case",
    }.get(prompt_key, "Generate Analysis")

    emoji = {
        3411:"🧠",3412:"🔍",3413:"⚖️",3414:"💭",3415:"📜",
        3416:"🎤",3417:"⚔️",3418:"🧩",3419:"🎯",3420:"🗺️",
        3421:"✍️",3422:"📚",3423:"🔬",3424:"🏛️",3425:"🌌",
        3426:"🏗️",3427:"⚡",3428:"🔎",3429:"🌌",3430:"🏥",
    }.get(prompt_key, "✨")

    loading_text = {
        3411:"Engaging in dialectical inquiry...",3412:"Analyzing argument structure...",
        3413:"Navigating ethical complexity...",3414:"Constructing thought experiment...",
        3415:"Analyzing philosophical text...",3416:"Building debate case...",
        3417:"Building strongest argument...",3418:"Generating logic puzzle...",
        3419:"Clarifying concept...",3420:"Mapping argument...",
        3421:"Crafting philosophical fiction...",3422:"Consulting classical sources...",
        3423:"Analyzing contemporary discourse...",3424:"Preparing Stoic reflection...",
        3425:"Companion on the examined life...",3426:"Examining foundational beliefs...",
        3427:"Synthesizing dialectically...",3428:"Analyzing epistemological foundations...",
        3429:"Exploring metaphysical terrain...",3430:"Convening ethics committee...",
    }.get(prompt_key, "Generating...")

    prompt_body_for_api = prompt_template

    return f'''"use client";
import {{ useState }} from "react";
{extra_state}

export default function {name.replace("-"," ").title().replace(" ","")}Page() {{
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {{
    if