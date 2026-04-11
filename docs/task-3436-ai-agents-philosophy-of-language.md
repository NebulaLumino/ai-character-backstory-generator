# Philosophy of Language & Symbolic Reasoning

## Introduction

Language is humanity's most powerful tool. It is also one of philosophy's most contested domains. What is meaning? How do words connect to the world? And can machines truly understand language, or are they brilliant mimics? These questions sit at the heart of both philosophy of language and modern AI.

## Classical Theories of Meaning

### The Reference Theory (Millianism)

John Stuart Mill: The meaning of a word is its referent. "Water" means H₂O. This gives us extensional accuracy but struggles with concepts like "unicorn" (which refers to nothing yet has meaning).

### Frege's Sense and Reference

Gottlob Frege distinguished:
- **Reference (Bedeutung)**: The object in the world the term picks out
- **Sense (Sinn)**: The mode of presentation, the way the referent is conceived

"Superman" and "Clark Kent" refer to the same person but have different senses. This explains why "Superman is Superman" is trivial while "Superman is Clark Kent" is informative.

### The Use Theory (Wittgenstein)

> "Meaning is use." — Ludwig Wittgenstein, *Philosophical Investigations*

Words don't primarily refer to things in the world; they get their meaning from their role in the language game, the practices and contexts in which they're used.

This has profound implications for AI: if meaning = use, then a language model trained on millions of language practices might genuinely have something like meaning — not just pattern-matching.

## Searle's Chinese Room Argument

John Searle (1980) posed a devastating objection to the idea that symbol manipulation = understanding:

Imagine a person in a room who follows English rules to manipulate Chinese symbols, outputting appropriate Chinese responses — without understanding Chinese at all. The room (like a computer) manipulates symbols but has no understanding.

**The conclusion**: Syntax (symbol manipulation) is not sufficient for semantics (meaning/understanding).

**Responses**:
- **Systems reply**: Understanding is a property of the whole system, not any single component
- **Robot reply**: Put the room in a robot with sensors — then it would understand
- **Emergence reply**: Large enough syntax might spontaneously produce semantics

This debate is far from settled and remains central to AI consciousness discussions.

## Language Models: What's Actually Happening

Modern LLMs (GPT-4, Claude, etc.) are trained to predict the next token given context. Their remarkable capabilities have reignited old debates:

| Theory | LLMs as...? |
|--------|-------------|
| Millian | Complex referential machines |
| Fregean | Encoding multiple senses in weights |
| Use theorist | Learning language games from data |
| Searlean | Sophisticated Chinese rooms |

## Grounding and Symbol Grounding Problem

How do words get their meaning if not directly connected to the world? Stevan Harnad's **Symbol Grounding Problem**: symbols must be grounded in something non-symbolic (sensory experience, motor actions) to have meaning.

LLMs trained purely on text are **not grounded** — they have never seen a cat, only texts about cats. This makes them vulnerable to errors a grounded agent wouldn't make.

## Wittgenstein on Rules and Private Language

Wittgenstein's rule-following considerations: When you follow a rule, you think you're tracking something objective. But there could always be another interpretation. This leads to the famous private language argument: a language that could only be understood by one person isn't really a language at all.

This poses challenges for AI trained in isolation: how do we know the AI "understands" rules the way we do?

## Formal Tools: Montague Grammar & Beyond

Richard Montague showed that natural language and formal language could be given identical semantics. This was revolutionary — it suggested that the formality required for computational semantics wasn't a limitation but a feature.

Modern semantic parsing, Abstract Meaning Representation (AMR), and formal ontology work build directly on this insight.

## Practical AI Applications

| Concept | AI Application |
|---------|--------------|
| Compositionality | Systematic generalization to novel sentences |
| Pragmatics | Context-dependent meaning in dialog systems |
| Grounding | Vision-language models linking images to text |
| Common sense | Knowledge graphs, world models |
| Ambiguity | WSD (Word Sense Disambiguation) systems |

## Resources

- Gottlob Frege, "On Sense and Reference" (1892)
- Ludwig Wittgenstein, *Philosophical Investigations* (1953)
- John Searle, "Minds, Brains, and Programs" (1980)
- David Lewis, *Convention* (1969)
- Jerry Fodor, *The Language of Thought* (1975)
