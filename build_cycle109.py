#!/usr/bin/env python3
"""Build script for Cycle 109 Film AI apps — v2 fixed."""
import subprocess, os, sys

WORKDIR = "/Users/nebulalumino/.openclaw/workspace"


def title_case(s):
    return " ".join(w.capitalize() for w in s.replace("_", " ").split())


# (app_dir, title, hue, prompt_keys, prompt_template, uses_src)
APPS = [
    ("ai-ai-film-script-generator-screenplay-writer",
     "AI Film Script Generator & Screenplay Writer", 0,
     ["genre","logline","tone","protagonist","antagonist","setting","audience","runtime"],
     """You are a professional screenplay writer. Write a complete, production-ready film script based on this brief:

- Genre: {genre}
- Logline: {logline}
- Tone: {tone}
- Protagonist: {protagonist}
- Antagonist: {antagonist}
- Setting: {setting}
- Target Audience: {audience}
- Approx Runtime: {runtime}

Format with proper scene headings (INT./EXT.), action lines, character names, dialogue, and parentheticals. Include a compelling opening, rising action, climax, and resolution. Use standard screenplay format.""",
     True),

    ("ai-ai-storyboard-artist-visual-narrative-designer",
     "AI Storyboard Artist & Visual Narrative Designer", 15,
     ["scene","style","camera","numPanels","pacing"],
     """You are a professional storyboard artist. Create a detailed storyboard plan:

- Scene: {scene}
- Visual Style: {style}
- Camera Movement: {camera}
- Number of Panels: {numPanels}
- Pacing Notes: {pacing}

For each panel provide: panel number, shot type (Wide/Medium/Close-up/Extreme Close-up), camera angle (Eye Level/High Angle/Low Angle/Dutch Angle), camera movement, visual description, character positioning, and transition suggestion.""",
     True),

    ("ai-ai-video-shot-list-shot-composition-planner",
     "AI Video Shot List & Shot Composition Planner", 30,
     ["scene","style","numShots","aspectRatio","equipment"],
     """You are a cinematography expert. Create a detailed shot list:

- Scene: {scene}
- Visual Style: {style}
- Number of Shots: {numShots}
- Aspect Ratio: {aspectRatio}
- Equipment Available: {equipment}

For each shot provide: shot number, shot type, camera angle, lens choice, movement, composition notes, duration estimate, and special considerations.""",
     True),

    ("ai-ai-directors-vision-brief-generator",
     "AI Director's Vision Brief Generator", 45,
     ["title","genre","tone","visualStyle","keyMoments","theme","referenceFilms"],
     """You are an acclaimed film director. Create a director's vision brief:

- Title: {title}
- Genre: {genre}
- Tone: {tone}
- Visual Style: {visualStyle}
- Key Moments: {keyMoments}
- Theme: {theme}
- Reference Films: {referenceFilms}

Include: directorial intent, visual language, color palette, key creative choices, and what makes this film unique.""",
     True),

    ("ai-ai-casting-recommendation-engine",
     "AI Casting Recommendation Engine", 60,
     ["title","format","genre","protagonist","antagonist","supporting","audience","union"],
     """You are a casting director. Create a detailed casting breakdown:

- Project: {title}
- Format: {format}
- Genre: {genre}
- Protagonist: {protagonist}
- Antagonist: {antagonist}
- Supporting Cast: {supporting}
- Target Audience: {audience}
- Union/Non-Union: {union}

Provide: character breakdown (name, age range, physical traits), top 5 casting recommendations per lead with rationale, and audition sides recommendations.""",
     True),

    ("ai-ai-location-scouting-report-generator",
     "AI Location Scouting Report Generator", 75,
     ["setting","era","season","budget","accessibility","climate","permits"],
     """You are a location manager. Generate a location scouting report:

- Setting: {setting}
- Era/Time Period: {era}
- Season/Time of Day: {season}
- Budget Tier: {budget}
- Accessibility: {accessibility}
- Climate/Weather: {climate}
- Permit Requirements: {permits}

Provide: location recommendations, real-world location ideas, pros/cons, logistical notes, permit requirements, and cost estimates.""",
     True),

    ("ai-ai-film-budget-production-schedule-builder",
     "AI Film Budget & Production Schedule Builder", 90,
     ["title","format","genre","runtime","locations","scope","budget","complexity"],
     """You are a line producer. Create a film budget and production schedule:

- Title: {title}
- Format: {format}
- Genre: {genre}
- Runtime: {runtime}
- Number of Locations: {locations}
- Production Scope: {scope}
- Budget Range: {budget}
- Complexity: {complexity}

Provide: pre-production budget breakdown, shooting schedule (days per scene), department costs, contingency, and key milestones.""",
     True),

    ("ai-ai-color-grading-preset-designer",
     "AI Color Grading Preset Designer", 105,
     ["film","genre","mood","referenceLooks","camera","deliverable","style"],
     """You are a colorist. Design color grading presets:

- Film/Project: {film}
- Genre: {genre}
- Mood: {mood}
- Reference Looks: {referenceLooks}
- Camera System: {camera}
- Deliverable: {deliverable}
- Style: {style}

Provide: LUT/preset recommendations with hue/saturation/lift values, color palette, reference stills, and DaVinci Resolve/Premiere Pro instructions.""",
     True),

    ("ai-ai-video-editing-transcript-assembly-editor",
     "AI Video Editing Transcript & Assembly Editor", 120,
     ["transcript","footage","pacing","tone","genre","music","transitions","cuts"],
     """You are an editor. Create an editing assembly plan:

- Transcript/Scene Description: {transcript}
- Available Footage: {footage}
- Desired Pacing: {pacing}
- Tone: {tone}
- Genre: {genre}
- Music Direction: {music}
- Transitions: {transitions}
- Cut Notes: {cuts}

Provide: scene-by-scene assembly plan, cut recommendations, transition points, music cues, and narrative flow.""",
     True),

    ("ai-ai-sound-design-foley-suggestion-generator",
     "AI Sound Design & Foley Suggestion Generator", 135,
     ["scene","genre","mood","era","setting","budget","atmosphere","dialogue"],
     """You are a sound designer. Create a sound design breakdown:

- Scene: {scene}
- Genre: {genre}
- Mood: {mood}
- Era/Setting: {era}
- Location: {setting}
- Budget for Sound: {budget}
- Atmosphere: {atmosphere}
- Dialogue Priority: {dialogue}

Provide: foley suggestions, ambience recommendations, sound effects list, music temp track ideas, and mixing priorities.""",
     True),

    ("ai-ai-visual-effects-shot-breakdown-compositor-brief",
     "AI Visual Effects Shot Breakdown & Compositor Brief", 150,
     ["scene","genre","complexity","budget","software","pipeline","scope"],
     """You are a VFX supervisor. Create a VFX shot breakdown:

- Scene Description: {scene}
- Genre: {genre}
- Complexity: {complexity}
- Budget for VFX: {budget}
- Software/Pipeline: {software}
- Pipeline: {pipeline}
- Scope: {scope}

Provide: shot-by-shot VFX breakdown, element lists, technical specs (resolution, frame rate), compositor notes, and render estimates.""",
     True),

    ("ai-ai-subtitle-closed-caption-generator",
     "AI Subtitle & Closed Caption Generator", 165,
     ["transcript","language","style","readingSpeed","speaker","format","dialect"],
     """You are a subtitling specialist. Generate subtitles/captions:

- Dialogue Transcript: {transcript}
- Target Language: {language}
- Style: {style}
- Max Reading Speed: {readingSpeed}
- Speaker: {speaker}
- Format: {format}
- Dialect: {dialect}

Provide: SRT-format subtitles with speaker labels, SDH annotations, and style guide notes.""",
     True),

    ("ai-ai-film-distribution-strategy-festival-roadmap",
     "AI Film Distribution Strategy & Festival Roadmap", 180,
     ["title","format","genre","premiere","budget","runtime","audience","platform"],
     """You are a film distribution strategist. Create a festival/distribution strategy:

- Title: {title}
- Format: {format}
- Genre: {genre}
- Premiere Level: {premiere}
- Budget: {budget}
- Runtime: {runtime}
- Target Audience: {audience}
- Platform Strategy: {platform}

Provide: festival roadmap (tier-1/2/3), theatrical vs VOD strategy, P&A budget, release windows, and international sales approach.""",
     True),

    ("ai-ai-movie-review-aggregator-sentiment-analyzer",
     "AI Movie Review Aggregator & Sentiment Analyzer", 195,
     ["film","critics","audience","platform","focus","language"],
     """You are a film critic and data analyst. Analyze review sentiment:

- Film: {film}
- Critics' Reviews: {critics}
- Audience Reviews: {audience}
- Platform: {platform}
- Focus Area: {focus}
- Language: {language}

Provide: sentiment score (positive/negative/neutral %), key praise, key criticisms, common terms, rating distribution, and film comparison.""",
     True),

    ("ai-ai-film-marketing-poster-concept-generator",
     "AI Film Marketing Poster Concept Generator", 210,
     ["title","genre","tone","audience","keyArt","tagline","platform","style"],
     """You are an art director. Create marketing poster concepts:

- Title: {title}
- Genre: {genre}
- Tone: {tone}
- Target Audience: {audience}
- Key Art Description: {keyArt}
- Tagline: {tagline}
- Platform: {platform}
- Style Direction: {style}

Provide: 3 distinct poster concepts with visual descriptions, typography, color palette, layout sketches, and messaging hierarchy.""",
     True),

    ("ai-ai-deleted-scene-justification-report",
     "AI Deleted Scene Justification Report", 225,
     ["scene","context","script","reason","sceneNumber","duration","budget"],
     """You are a producer. Create a deleted scene justification report:

- Scene Description: {scene}
- Story Context: {context}
- Script Context: {script}
- Reason for Deletion: {reason}
- Scene Number: {sceneNumber}
- Duration: {duration}
- Budget Impact: {budget}

Provide: creative rationale, story contribution, budget/production impact analysis, and alternative use suggestions in memo format.""",
     True),

    ("ai-ai-continuity-checker-scene-consistency-analyzer",
     "AI Continuity Checker & Scene Consistency Analyzer", 240,
     ["scene","script","previousScene","characters","props","lighting","timeOfDay"],
     """You are a script supervisor. Analyze continuity and scene consistency:

- Scene Description: {scene}
- Script: {script}
- Previous Scene: {previousScene}
- Character Details: {characters}
- Prop List: {props}
- Lighting: {lighting}
- Time of Day: {timeOfDay}

Provide: continuity error report (flag discrepancies), consistency recommendations, prop tracking notes, and script issues found.""",
     True),

    ("ai-ai-film-noir-genre-deconstructor",
     "AI Film Noir Genre Deconstructor", 255,
     ["premise","setting","characters","tone","era","subgenre","tropes"],
     """You are a film noir expert. Deconstruct the film noir genre:

- Premise: {premise}
- Setting: {setting}
- Characters: {characters}
- Tone: {tone}
- Era/Period: {era}
- Subgenre: {subgenre}
- Tropes: {tropes}

Provide: noir genre analysis, key tropes and how to subvert/honor them, visual style guide, character archetypes, dialogue style, and structural outline.""",
     True),

    ("ai-ai-documentary-research-interview-question-generator",
     "AI Documentary Research & Interview Question Generator", 270,
     ["subject","thesis","format","interviewee","style","tone","audience","scope"],
     """You are a documentary filmmaker. Generate interview questions and research guide:

- Subject: {subject}
- Thesis: {thesis}
- Format: {format}
- Interviewee: {interviewee}
- Style: {style}
- Tone: {tone}
- Audience: {audience}
- Scope: {scope}

Provide: top 20 interview questions (by theme), follow-up questions, research sources, visual reference ideas, and B-roll suggestions.""",
     True),

    ("ai-ai-behindthescenes-content-generator",
     "AI Behind-the-Scenes Content Generator", 285,
     ["title","format","scenes","crew","behindTheScenes","platform","audience"],
     """You are a BTS content producer. Generate behind-the-scenes content:

- Title: {title}
- Format: {format}
- Key Scenes: {scenes}
- Crew Roles: {crew}
- BTS Content Type: {behindTheScenes}
- Platform: {platform}
- Audience: {audience}

Provide: BTS video concept (3-5 segments), interview questions for cast/crew, blooper reel ideas, making-of narrative arc, and social media calendar.""",
     True),

    # Standalone apps
    ("ai-film-script-generator",
     "AI Film Script Generator", 0,
     ["genre","logline","tone","protagonist","antagonist","setting","audience","runtime"],
     """You are a professional screenplay writer. Write a complete film script:

- Genre: {genre}
- Logline: {logline}
- Tone: {tone}
- Protagonist: {protagonist}
- Antagonist: {antagonist}
- Setting: {setting}
- Target Audience: {audience}
- Runtime: {runtime}

Format with INT./EXT. scene headings, action lines, character names, dialogue, parentheticals. Include opening, rising action, climax, resolution.""",
     True),

    ("ai-storyboard-artist",
     "AI Storyboard Artist", 15,
     ["scene","style","camera","numPanels","pacing"],
     """You are a storyboard artist. Create a storyboard plan:

- Scene: {scene}
- Visual Style: {style}
- Camera Movement: {camera}
- Number of Panels: {numPanels}
- Pacing: {pacing}

For each panel: number, shot type, camera angle, movement, visual description, character positioning, transition.""",
     True),

    ("ai-video-shot-list",
     "AI Video Shot List", 30,
     ["scene","style","numShots","aspectRatio","equipment"],
     """You are a cinematography expert. Create a shot list:

- Scene: {scene}
- Visual Style: {style}
- Number of Shots: {numShots}
- Aspect Ratio: {aspectRatio}
- Equipment: {equipment}

For each shot: number, shot type, camera angle, lens, movement, composition, duration, special notes.""",
     True),

    ("ai-director-vision",
     "AI Director's Vision Brief Generator", 45,
     ["title","genre","tone","visualStyle","keyMoments","theme","referenceFilms"],
     """You are an acclaimed film director. Create a director's vision brief:

- Title: {title}
- Genre: {genre}
- Tone: {tone}
- Visual Style: {visualStyle}
- Key Moments: {keyMoments}
- Theme: {theme}
- Reference Films: {referenceFilms}

Include: directorial intent, visual language, color palette, key creative choices, and what makes this film unique.""",
     False),
]


def find_target_dir(app_path):
    """Find the correct target directory (src/app or app)."""
    src_dir = os.path.join(app_path, "src")
    if os.path.exists(os.path.join(src_dir, "app")):
        return src_dir  # src/app/ structure
    if os.path.exists(os.path.join(src_dir, "page.tsx")):
        return src_dir  # src/ structure (no app subdir)
    app_dir = os.path.join(app_path, "app")
    if os.path.exists(os.path.join(app_dir, "page.tsx")):
        return app_dir  # app/ structure
    return None


def process(name, title, hue, prompt_keys, prompt_template, uses_src):
    app_path = os.path.join(WORKDIR, name)
    print("  [INFO] %s (src=%s)" % (name, uses_src))

    target_dir = find_target_dir(app_path)
    if not target_dir:
        print("  [SKIP] %s: no target directory found" % name)
        return

    page_path = os.path.join(target_dir, "page.tsx")
    css_path = os.path.join(target_dir, "globals.css")
    api_dir = os.path.join(target_dir, "api", "generate")
    api_path = os.path.join(api_dir, "route.ts")

    accent = "hsl(%d, 70%%, 55%%)" % hue
    accent_border = "hsl(%d, 70%%, 45%%)" % hue

    # ── globals.css ──
    with open(css_path, "w") as f:
        f.write(
            '@import "tailwindcss";\n\n'
            ':root { --background: #000000; --foreground: #ffffff; }\n'
            '@theme inline {\n'
            '  --color-background: var(--background);\n'
            '  --color-foreground: var(--foreground);\n'
            '  --font-sans: var(--font-geist-sans);\n'
            '  --font-mono: var(--font-geist-mono);\n'
            '}\n'
            'body { background: var(--background); color: var(--foreground); font-family: Arial, Helvetica, sans-serif; }\n'
        )

    # ── page.tsx ──
    field_parts = []
    for key in prompt_keys:
        label = title_case(key)
        field_parts.append(
            '          <div>\n'
            '            <label className="block text-sm text-gray-400 mb-1 capitalize">' + label + '</label>\n'
            '            <input\n'
            '              type="text"\n'
            '              placeholder="' + label + '"\n'
            '              value={form["' + key + '"] || ""}\n'
            '              onChange={e => setForm(f => ({ ...f, "' + key + '": e.target.value }))}\n'
            '              className="w-full bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-0"\n'
            '            />\n'
            '          </div>'
        )
    fields_html = '\n'.join(field_parts)

    page_code = (
        '"use client";\n'
        'import { useState } from "react";\n\n'
        'type FormData = Record<string, string>;\n\n'
        'export default function Home() {\n'
        '  const [form, setForm] = useState<FormData>({});\n'
        '  const [output, setOutput] = useState("");\n'
        '  const [loading, setLoading] = useState(false);\n'
        '  const [error, setError] = useState("");\n\n'
        '  const handleSubmit = async (e: React.FormEvent) => {\n'
        '    e.preventDefault();\n'
        '    setLoading(true);\n'
        '    setOutput("");\n'
        '    setError("");\n'
        '    const res = await fetch("/api/generate", {\n'
        '      method: "POST",\n'
        '      headers: { "Content-Type": "application/json" },\n'
        '      body: JSON.stringify({ formData: form }),\n'
        '    });\n'
        '    const data = await res.json();\n'
        '    setOutput(data.result || data.error || "No output generated.");\n'
        '    setLoading(false);\n'
        '  };\n\n'
        '  return (\n'
        '    <div className="min-h-screen bg-gradient-to-br from-gray-950 via-gray-900 to-black text-white">\n'
        '      <div className="max-w-4xl mx-auto px-6 py-12">\n'
        '        <div className="mb-8 pb-6" style={{ borderBottom: "2px solid ' + accent_border + '" }}>\n'
        '          <h1 className="text-4xl font-bold mb-2" style={{ color: "' + accent + '" }}>' + title + '</h1>\n'
        '        </div>\n'
        '        <form onSubmit={handleSubmit} className="space-y-4 mb-6">\n'
        + fields_html + '\n'
        '          <button type="submit" disabled={loading}\n'
        '            className="w-full py-3 rounded-lg font-semibold text-white transition-all disabled:opacity-50"\n'
        '            style={{ backgroundColor: "' + accent + '" }}>\n'
        '            {loading ? "Generating..." : "Generate"}\n'
        '          </button>\n'
        '        </form>\n'
        '        {error && <div className="bg-red-900/30 border border-red-800 text-red-300 rounded-lg px-4 py-3 mb-4">{error}</div>}\n'
        '        {output && <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">\n'
        '          <pre className="text-gray-300 whitespace-pre-wrap text-sm leading-relaxed">{output}</pre>\n'
        '        </div>}\n'
        '      </div>\n'
        '    </div>\n'
        '  );\n'
        '}\n'
    )
    with open(page_path, "w") as f:
        f.write(page_code)
    print("    Wrote page.tsx -> " + page_path)

    # ── API route ──
    os.makedirs(api_dir, exist_ok=True)
    route_code = (
        'import { NextRequest, NextResponse } from "next/server";\n'
        'import OpenAI from "openai";\n\n'
        'const openai = new OpenAI({\n'
        '  apiKey: process.env.OPENAI_API_KEY || "",\n'
        '  baseURL: "https://api.deepseek.com/v1",\n'
        '});\n\n'
        'export async function POST(req: NextRequest) {\n'
        '  try {\n'
        '    const { formData } = await req.json();\n'
        '    const systemPrompt = "You are a world-class expert in this domain. Provide detailed, well-structured, actionable output.";\n'
        '    const userPrompt = `' + prompt_template.replace('`', '\\`') + '`;\n'
        '    const completion = await openai.chat.completions.create({\n'
        '      model: "deepseek-chat",\n'
        '      messages: [\n'
        '        { role: "system", content: systemPrompt },\n'
        '        { role: "user", content: userPrompt },\n'
        '      ],\n'
        '      temperature: 0.7,\n'
        '      max_tokens: 2500,\n'
        '    });\n'
        '    return NextResponse.json({ result: completion.choices[0].message.content });\n'
        '  } catch (err: any) {\n'
        '    return NextResponse.json({ error: err.message }, { status: 500 });\n'
        '  }\n'
        '}\n'
    )
    with open(api_path, "w") as f:
        f.write(route_code)
    print("    Wrote route.ts -> " + api_path)

    # ── build ──
    print("    Building %s..." % name)
    env = os.environ.copy()
    env["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-dummy")
    r = subprocess.run(
        "npm install && npm run build",
        cwd=app_path, shell=True, capture_output=True, text=True, env=env, timeout=180
    )
    if r.returncode != 0:
        print("    BUILD FAILED for %s:" % name)
        print(r.stderr[-2000:])
        return
    print("    Build OK")

    # ── git push ──
    has_git = os.path.exists(os.path.join(app_path, ".git"))
    if has_git:
        subprocess.run(["git", "add", "."], cwd=app_path, check=True)
        subprocess.run(["git", "commit", "-m", name + ": initial implementation"], cwd=app_path, check=True)
        r = subprocess.run(["git", "push", "-u", "origin", "main"],
                          cwd=app_path, capture_output=True, text=True)
        if r.returncode == 0:
            print("    Pushed: " + name)
        elif "everything up-to-date" in r.stdout or "already up-to-date" in r.stdout:
            print("    Already up-to-date: " + name)
        else:
            print("    Push note: " + r.stdout[:200])
    else:
        subprocess.run(["git", "init"], cwd=app_path, check=True)
        subprocess.run(["git", "add", "."], cwd=app_path, check=True)
        subprocess.run(["git", "commit", "-m", name + ": initial implementation"], cwd=app_path, check=True)
        r = subprocess.run(
            ["gh", "repo", "create", name, "--public", "--push", "--source", app_path],
            capture_output=True, text=True
        )
        if r.returncode == 0:
            print("    Created repo: " + name)
        elif "already exists" in r.stderr:
            print("    Repo exists: " + name)
        else:
            print("    gh note: " + r.stderr[:300])

    # ── cleanup ──
    for d in ["node_modules", ".next"]:
        p = os.path.join(app_path, d)
        if os.path.exists(p):
            subprocess.run(["rm", "-rf", p], check=False)
    print("    Done: " + name)


# ── git identity ──
subprocess.run(["git", "config", "--global", "user.email", "nebula.lumino@example.com"], check=True)
subprocess.run(["git", "config", "--global", "user.name", "Nebula Lumino"], check=True)

# ── main loop ──
done = []
failed = []

for app in APPS:
    name = app[0]
    print("\n>>> " + name)
    try:
        process(name, app[1], app[2], app[3], app[4], app[5])
        done.append(name)
    except Exception as e:
        import traceback
        print("  ERROR: " + str(e))
        traceback.print_exc()
        failed.append(name)

print("\n\n=== COMPLETE ===")
print("Done: %d" % len(done))
print("Failed: %d" % len(failed))
if failed:
    print("Failed:", ", ".join(failed))
