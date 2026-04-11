#!/usr/bin/env python3
import os, json

APPS = [
    ("ai-socratic-question",      "red",       "🧠", "Socratic Question Generator",    "Generate deep Socratic questions on any topic",                                    "Enter a philosophical topic, question, or concept to explore...",                            "Engaging in dialectical inquiry..."),
    ("ai-logical-fallacy",         "orange",    "🔍", "Logical Fallacy Detector",         "Identify and explain logical fallacies in arguments",                               "Paste an argument or claim to analyze for logical fallacies...",                                 "Examining logical structures..."),
    ("ai-ethical-dilemma",         "yellow",    "⚖️", "Ethical Dilemma Simulator",        "Explore ethical dilemmas and moral reasoning scenarios",                             "Describe a ethical situation or dilemma to analyze...",                                          "Navigating moral complexity..."),
    ("ai-thought-experiment",      "lime",      "🧪", "Thought Experiment Engine",       "Design and analyze philosophical thought experiments",                              "Describe a philosophical scenario or concept for a thought experiment...",                       "Constructing thought experiment..."),
    ("ai-philosophy-summarizer",   "green",     "📚", "Philosophy Summarizer",           "Summarize philosophical texts, arguments, and schools of thought",                    "Paste a philosophical text, passage, or concept to summarize...",                               "Distilling philosophical wisdom..."),
    ("ai-debate-motion",           "teal",      "🎤", "Debate Motion Generator",         "Generate debate motions with arguments for and against",                            "Enter a topic, issue, or statement to generate debate motions...",                              "Preparing debate positions..."),
    ("ai-steelman-builder",        "cyan",      "🛡️", "Steel Man Argument Builder",      "Build the strongest version of an opposing argument",                                "Enter an argument or position to build a steel man for...",                                       "Forging strongest counterargument..."),
    ("ai-logic-puzzle",            "blue",      "🧩", "Logic Puzzle Generator",           "Generate logic puzzles, brain teasers, and deductive reasoning challenges",           "Enter a topic or puzzle type to generate a logic puzzle...",                                     "Designing logical challenge..."),
    ("ai-concept-clarifier",       "violet",    "💡", "Concept Clarifier",               "Clarify and disambiguate philosophical concepts and terms",                         "Enter a philosophical concept or term to clarify...",                                             "Illuminating conceptual distinctions..."),
    ("ai-argument-map",            "purple",    "🗺️", "Argument Mapper",                  "Map the structure of arguments showing premises, inferences, and conclusions",       "Enter an argument or claim to map its structure...",                                             "Mapping inferential pathways..."),
    ("ai-philosophy-fiction",      "pink",      "📖", "Philosophy Fiction Generator",    "Generate short philosophical fiction scenarios and vignettes",                       "Enter a theme, concept, or scenario for philosophical fiction...",                                "Weaving philosophy into narrative..."),
    ("ai-classic-philosophy",      "rose",      "🏛️", "Classic Philosophy Explorer",     "Explore major works, thinkers, and schools of classical philosophy",                    "Enter a philosopher, work, or school of classical thought to explore...",                         "Surveying ancient wisdom..."),
    ("ai-modern-philosophy",       "orange",    "🔬", "Modern Philosophy Explorer",      "Explore contemporary philosophical movements, thinkers, and debates",                   "Enter a modern philosopher, movement, or concept to explore...",                                "Navigating contemporary thought..."),
    ("ai-stoic-wisdom",            "amber",     "🏛️", "Stoic Wisdom Generator",          "Generate Stoic wisdom, practices, and guidance from Marcus Aurelius, Epictetus, Seneca", "Enter a challenge, concern, or situation for Stoic guidance...",                              "Consulting the Stoic masters..."),
    ("ai-existential-companion",   "lime",      "🌌", "Existential Companion",           "Explore existentialist themes, anxiety, meaning, and authenticity",                   "Enter a question about meaning, death, freedom, or existence...",                                "Confronting existential horizons..."),
    ("ai-axiom-checker",           "emerald",   "🔬", "Axiom Checker",                   "Examine, test, and challenge foundational axioms and self-evident truths",             "Enter an axiom, principle, or foundational claim to examine...",                                 "Probing foundational premises..."),
    ("ai-dialectical-synthesis",   "aqua",      "⚡", "Dialectical Synthesis Engine",    "Synthesize opposing theses through Hegelian dialectical reasoning",                   "Enter a thesis and antithesis to synthesize through dialectical reasoning...",                    "Resolving contradictions through synthesis..."),
    ("ai-epistemology",            "sky",       "🧠", "Epistemology Explorer",           "Explore theories of knowledge, belief, justification, and truth",                     "Enter a question about knowledge, belief, or truth to explore...",                               "Examining the foundations of knowing..."),
    ("ai-metaphysics",             "indigo",    "🌎", "Metaphysics Explorer",            "Explore the nature of reality, being, causation, and existence",                    "Enter a question about reality, being, or existence to explore...",                             "Probing the fabric of reality..."),
    ("ai-ethics-committee",        "violet",    "⚖️", "Ethics Committee Simulator",       "Simulate multi-perspective ethical deliberation and committee reasoning",             "Describe a case, scenario, or dilemma for ethical deliberation...",                              "Convening ethics committee..."),
]

# route.ts is identical for all apps
ROUTE_TS = '''import OpenAI from "openai";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { topic, puzzleType } = body;
    if (!topic?.trim()) {
      return NextResponse.json({ error: "Topic is required" }, { status: 400 });
    }
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      baseURL: "https://api.deepseek.com/v1",
    });
    const completion = await openai.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: topic }
      ],
    });
    return NextResponse.json({ result: completion.choices[0].message.content });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
'''

# Logic puzzle page has dropdown; others are standard
LOGIC_PUZZLE_PAGETSX = '''"use client"
import {{ useState }} from "react"

export default function Home() {{
  const [input, setInput] = useState("")
  const [puzzleType, setPuzzleType] = useState("syllogism")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const handleGenerate = async () => {{
    if (!input.trim()) return
    setLoading(true)
    setError("")
    setResult("")
    try {{
      const res = await fetch("/api/generate", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ topic: input, puzzleType }}),
      }})
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || "Generation failed")
      setResult(data.result)
    }} catch (e: any) {{
      setError(e.message)
    }} finally {{
      setLoading(false)
    }}
  }}

  const accent = "blue"
  const emoji = "🧩"
  const title = "Logic Puzzle Generator"
  const desc = "Generate logic puzzles, brain teasers, and deductive reasoning challenges"
  const placeholder = "Enter a topic or puzzle type to generate a logic puzzle..."
  const loadingText = "Designing logical challenge..."

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 text-white font-sans">
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div className="text-center mb-10">
          <div className="text-5xl mb-3">{{emoji}}</div>
          <h1 className="text-4xl font-bold mb-3 bg-gradient-to-r from-blue-400 to-blue-200 bg-clip-text text-transparent">
            {{title}}
          </h1>
          <p className="text-gray-400 text-lg">{{desc}}</p>
        </div>
        <select
          value={{puzzleType}}
          onChange={{e => setPuzzleType(e.target.value)}}
          className="w-full bg-[#1a1a2e] border border-blue-500/30 rounded-xl px-5 py-4 text-white focus:outline-none focus:border-blue-500 mb-4"
        >
          <option value="syllogism">Syllogism</option>
          <option value="truth-tellers">Truth-Tellers & Liars</option>
          <option value="logic-grid">Logic Grid</option>
          <option value="lateral-thinking">Lateral Thinking</option>
          <option value="deductive">Deductive Reasoning</option>
          <option value="paradox">Paradox</option>
        </select>
        <textarea
          value={{input}}
          onChange={{e => setInput(e.target.value)}}
          placeholder={{placeholder}}
          className="w-full bg-[#1a1a2e] border border-blue-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-blue-500 resize-y min-h-[140px] mb-4"
        />
        <button
          onClick={{handleGenerate}}
          disabled={{loading}}
          className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-blue-800 text-white font-semibold py-4 rounded-xl transition-all mb-6"
        >
          {{loading ? loadingText : "✨ Generate"}}
        </button>
        {{error && (
          <div className="bg-red-900/40 border border-red-500/50 rounded-xl p-4 text-red-300 mb-6">
            {{error}}
          </div>
        )}}
        {{result && (
          <div className="bg-[#111827] border border-blue-500/30 rounded-2xl p-8">
            <pre className="whitespace-pre-wrap text-sm leading-relaxed text-gray-300 font-sans">
              {{result}}
            </pre>
          </div>
        )}}
      </div>
    </div>
  )
}}
'''

# Standard page.tsx template (all apps except logic-puzzle)
def make_page_ts(emoji, title, desc, placeholder, loading_text, accent):
    return f'''"use client"
import {{ useState }} from "react"

export default function Home() {{
  const [input, setInput] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const handleGenerate = async () => {{
    if (!input.trim()) return
    setLoading(true)
    setError("")
    setResult("")
    try {{
      const res = await fetch("/api/generate", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ topic: input }}),
      }})
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || "Generation failed")
      setResult(data.result)
    }} catch (e: any) {{
      setError(e.message)
    }} finally {{
      setLoading(false)
    }}
  }}

  const accent = "{accent}"
  const emoji = "{emoji}"
  const title = "{title}"
  const desc = "{desc}"
  const placeholder = "{placeholder}"
  const loadingText = "{loading_text}"

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 text-white font-sans">
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div className="text-center mb-10">
          <div className="text-5xl mb-3">{{emoji}}</div>
          <h1 className="text-4xl font-bold mb-3 bg-gradient-to-r from-{{accent}}-400 to-{{accent}}-200 bg-clip-text text-transparent">
            {{title}}
          </h1>
          <p className="text-gray-400 text-lg">{{desc}}</p>
        </div>
        <textarea
          value={{input}}
          onChange={{e => setInput(e.target.value)}}
          placeholder={{placeholder}}
          className="w-full bg-[#1a1a2e] border border-{{accent}}-500/30 rounded-xl px-5 py-4 text-white placeholder-gray-600 focus:outline-none focus:border-{{accent}}-500 resize-y min-h-[140px] mb-4"
        />
        <button
          onClick={{handleGenerate}}
          disabled={{loading}}
          className={{"w-full bg-" + accent + "-600 hover:bg-" + accent + "-700 disabled:bg-" + accent + "-800 text-white font-semibold py-4 rounded-xl transition-all mb-6"}}
        >
          {{loading ? loadingText : "✨ Generate"}}
        </button>
        {{error && (
          <div className="bg-red-900/40 border border-red-500/50 rounded-xl p-4 text-red-300 mb-6">
            {{error}}
          </div>
        )}}
        {{result && (
          <div className="bg-[#111827] border border-{{accent}}-500/30 rounded-2xl p-8">
            <pre className="whitespace-pre-wrap text-sm leading-relaxed text-gray-300 font-sans">
              {{result}}
            </pre>
          </div>
        )}}
      </div>
    </div>
  )
}}
'''

APPS_DIR = "/Users/nebulalumino/.openclaw/workspace/apps"

for app_name, accent, emoji, title, desc, placeholder, loading_text in APPS:
    app_dir = os.path.join(APPS_DIR, app_name)
    api_dir = os.path.join(app_dir, "app", "api", "generate")
    os.makedirs(api_dir, exist_ok=True)

    # Write route.ts
    route_path = os.path.join(api_dir, "route.ts")
    with open(route_path, "w") as f:
        f.write(ROUTE_TS)
    print(f"Written: {route_path}")

    # Write page.tsx
    page_path = os.path.join(app_dir, "app", "page.tsx")
    if app_name == "ai-logic-puzzle":
        with open(page_path, "w") as f:
            f.write(LOGIC_PUZZLE_PAGETSX)
    else:
        with open(page_path, "w") as f:
            f.write(make_page_ts(emoji, title, desc, placeholder, loading_text, accent))
    print(f"Written: {page_path}")

print("\nAll files written!")
