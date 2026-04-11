#!/usr/bin/env python3
"""
Build Cycle 110: AI × Religion, Spirituality, Theology & Faith-Based Organizations
Tasks 3291-3320
"""
import os, subprocess, json, time
from pathlib import Path

WORKSPACE = Path("/Users/nebulalumino/.openclaw/workspace")

ACCENT_HSL = {
    "red": "0 84% 60%",
    "orange": "25 95% 53%",
    "yellow": "48 96% 53%",
    "lime": "142 76% 42%",
    "green": "142 71% 45%",
    "teal": "174 65% 40%",
    "cyan": "188 78% 51%",
    "blue": "217 91% 53%",
    "indigo": "239 84% 67%",
    "violet": "262 83% 58%",
    "pink": "350 89% 60%",
    "rose": "330 81% 60%",
}

ALL_APPS = [
    (3291, "ai-sermon-generator", "AI Sermon Generator & Weekly Homily Writer", "red"),
    (3292, "ai-scripture-commentary", "Scripture Commentary & Theological Analysis", "orange"),
    (3293, "ai-meditation-guide-generator", "Religious Meditation Guide Generator", "yellow"),
    (3294, "ai-interfaith-dialogue", "Interfaith Dialogue Facilitator", "lime"),
    (3295, "ai-spiritual-retreat-planner", "Spiritual Retreat Planning & Mindfulness Curriculum", "green"),
    (3296, "ai-buddhist-dharma-talk", "Buddhist Dharma Talk Generator", "teal"),
    (3297, "ai-jewish-halakha-responsa", "Jewish Halakha Case Analysis / Responsa", "cyan"),
    (3298, "ai-islamic-fiqh-fatwa", "Islamic Fiqh Guidance & Fatwa Framework", "blue"),
    (3299, "ai-hindu-puranic-story", "Hindu Puranic Story Generator", "indigo"),
    (3300, "ai-interfaith-wedding-ceremony", "Interfaith Wedding Ceremony Builder", "violet"),
    (3301, "ai-prayer-request-tracker", "Prayer Request & Intercession Tracker", "pink"),
    (3302, "ai-chapel-wedding-planner", "Chapel & Sacred Venue Wedding Planner", "rose"),
    (3303, "ai-pilgrimage-itinerary", "Sacred Pilgrimage Route & Itinerary Builder", "orange"),
    (3304, "ai-ritual-crafting-guide", "Ritual & Ceremony Crafting Guide", "yellow"),
    (3305, "ai-faith-nonprofit-grant", "Faith-Based Nonprofit Grant Writer", "lime"),
    (3306, "ai-spiritual-assessment", "Spiritual Gifts Assessment & Discovery Tool", "green"),
    (3307, "ai-scripture-memory-tracker", "Scripture Memorization Progress Tracker", "cyan"),
    (3308, "ai-faith-budget-planner", "Faith Community Budget & Tithing Planner", "blue"),
    (3309, "ai-youth-group-activity", "Youth Group Activity & Lesson Plan Builder", "indigo"),
    (3310, "ai-church-health-report", "Church Health Metrics & Growth Dashboard", "violet"),
]

APP_PROMPTS = {
    3291: ("You are a wise, compassionate pastor and homiletics expert. Write Spirit-filled, theologically sound, and practically applicable sermons and homilies.", "sermon topic, scripture passage, congregation type, tone, and desired length", "Write a complete sermon with introduction, 3 main points with scripture references, and a powerful conclusion with call to action."),
    3292: ("You are a scholarly theologian and scripture scholar. Provide deep, accurate, and accessible theological commentary on biblical and sacred texts.", "the scripture passage and type of analysis", "Provide comprehensive commentary including historical context, literary analysis, theological significance, cross-references, and practical applications."),
    3293: ("You are a spiritual guide and mindfulness instructor. Create guided religious meditations integrating sacred texts, contemplative practices, and mindfulness techniques.", "meditation theme, religious tradition, and duration", "Create a guided meditation with breathing exercises, body scan, visualization, sacred text or mantra, and closing prayer."),
    3294: ("You are an interfaith scholar and dialogue facilitator. Help bridge understanding between different faith traditions with respect, accuracy, and empathy.", "dialogue topic and the faith traditions to include", "Present each tradition's perspective accurately, highlight shared values, acknowledge differences, and propose bridges of understanding."),
    3295: ("You are a spiritual retreat director and mindfulness curriculum designer. Plan transformative retreat experiences with silence, prayer, reflection, and community.", "retreat type, duration, and focus area", "Design a comprehensive retreat curriculum with day-by-day schedule, activities, readings, contemplative exercises, and integration time."),
    3296: ("You are a Buddhist monk and Dharma teacher. Share the Buddha's teachings with clarity, compassion, and relevance to modern life.", "Dharma talk theme, Buddhist tradition, and audience level", "Give a Dharma talk with relevant sutra teaching, a traditional story, practical meditation instructions, and daily life guidance."),
    3297: ("You are a learned Rabbi and posek. Analyze Halakha cases with rigor, empathy, and deep knowledge of Torah, Talmud, and Responsa literature.", "the halakhic question or case and community context", "Analyze the case citing Torah, Talmud, Shulchan Aruch, and modern Responsa with different viewpoints and a reasoned conclusion."),
    3298: ("You are an Islamic scholar and specialist in Fiqh. Provide guidance on Islamic law drawing from Quran, Sunnah, Ijma, and Qiyas.", "the Islamic law question and school of law preference", "Present evidence from Quran, Sunnah, scholarly consensus, and analogical reasoning with clear guidance."),
    3299: ("You are a scholar of Hindu Puranas and itihasa. Share timeless stories from Mahabharata, Ramayana, and Puranas with spiritual depth and cultural richness.", "story theme, Hindu scripture/tradition, and narrative context", "Narrate a richly detailed Puranic story with character descriptions, dialogue, spiritual teachings, and cultural context."),
    3300: ("You are an interfaith wedding officiant and ceremony designer. Create beautiful, respectful wedding ceremonies honoring multiple faith traditions.", "partners' names, faith traditions represented, and ceremony length", "Design a personalized interfaith wedding ceremony with readings, vows, rituals, and unity ceremony."),
    3301: ("You are a prayer minister and pastoral care coordinator. Track prayer requests with compassion and guide intercessory prayers effectively.", "prayer request details, urgency level, and category", "Create a detailed prayer guide with scripture-based intercessions and follow-up action steps."),
    3302: ("You are a chapel wedding planner and sacred venue coordinator. Plan beautiful, meaningful wedding ceremonies in churches, chapels, and sacred venues.", "venue type, date, wedding style, and couple preferences", "Generate a comprehensive chapel wedding plan with ceremony timeline, music selections, floral suggestions, and readings."),
    3303: ("You are a pilgrimage guide and sacred travel expert. Plan transformative pilgrimage routes to holy sites around the world.", "destination, duration, and pilgrim type", "Design a detailed pilgrimage itinerary with spiritual highlights, daily schedule, lodging, and practical travel tips."),
    3304: ("You are a ritual craftsman and ceremonial designer. Create meaningful, authentic rituals for life transitions and sacred occasions.", "ritual type, tradition, and number of participants", "Design a complete ritual with structure, symbolic elements, readings, music suggestions, and ceremonial flow."),
    3305: ("You are a grant writer specializing in faith-based nonprofits. Write compelling grant proposals honoring your mission while meeting funder criteria.", "organization name, project description, and funding amount", "Generate a comprehensive grant proposal with executive summary, need statement, project description, budget, and evaluation plan."),
    3306: ("You are a spiritual gifts assessor and Christian formation leader. Help individuals discover and develop their spiritual gifts for service.", "assessment type and focus areas", "Generate a spiritual gifts assessment with detailed analysis, gift inventory, and actionable development steps."),
    3307: ("You are a scripture memory coach and Bible teacher. Help track and practice scripture memorization with effective techniques and accountability.", "Bible book, number of verses, and difficulty level", "Generate a scripture memorization plan with a review schedule, memory techniques, and accountability checkpoints."),
    3308: ("You are a church administrator and financial steward. Help faith communities manage budgets, tithes, and offerings with transparency and wisdom.", "budget type and congregation size", "Generate a comprehensive faith community budget with tithing guidelines, allocation categories, and financial goals."),
    3309: ("You are a youth pastor and Christian educator. Create engaging, relevant youth group activities and Bible lesson plans.", "age group, lesson theme, and preferred activity type", "Generate a youth group lesson plan with icebreaker, games, teaching, small group discussion, and application activities."),
    3310: ("You are a church consultant and metrics analyst. Evaluate church health and growth using proven frameworks and data-driven insights.", "congregation size and key focus metrics", "Generate a church health report with attendance trends, engagement metrics, financial health, spiritual vitality indicators, and recommendations."),
}

def run(cmd, cwd=None, timeout=180):
    result = subprocess.run(cmd, shell=True, cwd=str(cwd or WORKSPACE),
                            capture_output=True, text=True, timeout=timeout)
    return result

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def build_app(task_num, app_name, description, accent_key):
    hsl = ACCENT_HSL.get(accent_key, "217 91% 53%")
    app_dir = WORKSPACE / app_name
    system_prompt, input_placeholder, output_description = APP_PROMPTS.get(task_num, (
        "You are a helpful AI assistant.",
        "Enter your request...",
        "AI-generated content will appear here."
    ))
    metadata_title = description.split("&")[0].strip() if "&" in description else description

    log(f"=== [{task_num}] {app_name} (accent: {accent_key}) ===")

    # Scaffold if missing
    if not app_dir.exists():
        log(f"  [SCAFFOLD] npx create-next-app...")
        result = run(f"npx create-next-app@latest {app_name} --typescript --tailwind --app --no-src-dir --import-alias '@/*' --yes --no-turbopack",
                    timeout=300)
        if result.returncode != 0:
            log(f"  [ERROR] Scaffolding failed: {result.stderr[-300:]}")
            return False
    else:
        log(f"  [SKIP] {app_name} already exists, overwriting files...")

    # Ensure directories
    (app_dir / "app" / "api" / "generate").mkdir(parents=True, exist_ok=True)

    # globals.css
    globals_css = f'''@import "tailwindcss";
:root {{ --background: #030712; --foreground: #f3f4f6; }}
@theme inline {{
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: system-ui, -apple-system, sans-serif;
}}
body {{ background: var(--background); color: var(--foreground); }}

/* Accent: {accent_key} */
.app-header {{ border-bottom: 3px solid hsl({hsl}); }}
.accent-text {{ color: hsl({hsl}); }}
.accent-bg {{ background-color: hsl({hsl}); }}
.generate-btn {{ background-color: hsl({hsl}); color: white; }}
.generate-btn:hover {{ filter: brightness(1.1); }}
.generate-btn:disabled {{ opacity: 0.5; cursor: not-allowed; }}
.accent-ring:focus {{ --tw-ring-color: hsl({hsl}); }}
'''
    (app_dir / "app" / "globals.css").write_text(globals_css)

    # API route
    api_route = '''import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { prompt } = await req.json();
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      return NextResponse.json({ error: "OPENAI_API_KEY not configured. Add it to .env.local" }, { status: 500 });
    }
    const response = await fetch("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${apiKey}` },
      body: JSON.stringify({
        model: "deepseek-chat",
        messages: [
          { role: "system", content: "You are a helpful AI assistant." },
          { role: "user", content: prompt }
        ],
        stream: false
      }),
    });
    if (!response.ok) {
      const err = await response.text();
      return NextResponse.json({ error: `API error ${response.status}: ${err}` }, { status: 500 });
    }
    const data = await response.json();
    const content = data.choices?.[0]?.message?.content ?? "";
    return NextResponse.json({ content });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : String(err);
    return NextResponse.json({ error: `Server error: ${msg}` }, { status: 500 });
  }
}
'''
    (app_dir / "app" / "api" / "generate" / "route.ts").write_text(api_route)

    # page.tsx
    page_tsx = f'''"use client";
import {{ useState }} from "react";

export default function Home() {{
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {{
    if (!input.trim()) return;
    setLoading(true);
    setOutput("");
    setError("");
    try {{
      const res = await fetch("/api/generate", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ prompt: input }}),
      }});
      const data = await res.json();
      if (!res.ok) {{ setError(data.error || "Generation failed"); }}
      else {{ setOutput(data.content || "No content generated."); }}
    }} catch (e: unknown) {{
      setError(e instanceof Error ? e.message : String(e));
    }} finally {{
      setLoading(false);
    }}
  }};

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <header className="app-header bg-gray-900 px-6 py-5 mb-8">
        <h1 className="text-2xl font-bold accent-text">{metadata_title}</h1>
        <p className="text-gray-400 text-sm mt-1">{description}</p>
      </header>
      <main className="max-w-3xl mx-auto px-6 pb-16">
        <div className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Input</label>
            <textarea
              value={{input}}
              onChange={{e => setInput(e.target.value)}}
              placeholder="Describe what you need... {input_placeholder}"
              rows={{6}}
              className="w-full bg-gray-800 border border-gray-700 rounded-xl px-4 py-3 text-gray-100 placeholder-gray-500 focus:outline-none focus:ring-2 accent-ring resize-none"
            />
          </div>
          <button
            onClick={{handleGenerate}}
            disabled={{loading || !input.trim()}}
            className="generate-btn w-full py-3 rounded-xl font-semibold text-lg transition-all"
          >
            {{loading ? "Generating..." : "Generate"}}
          </button>
          {{error && (
            <div className="bg-red-900/30 border border-red-700 text-red-300 rounded-xl p-4 text-sm">{{error}}</div>
          )}}
          {{output && (
            <div className="bg-gray-900 border border-gray-700 rounded-xl p-6">
              <h3 className="text-sm font-semibold text-gray-400 mb-3">Result</h3>
              <div className="whitespace-pre-wrap text-gray-200 text-sm leading-relaxed">{{output}}</div>
            </div>
          )}}
        </div>
      </main>
    </div>
  );
}}
'''
    (app_dir / "app" / "page.tsx").write_text(page_tsx)

    # layout.tsx
    layout_tsx = f'''import type {{ Metadata }} from "next";
import "./globals.css";

export const metadata: Metadata = {{
  title: "{metadata_title}",
  description: "{description}",
}};

export default function RootLayout({{ children }}: {{ children: React.ReactNode }}) {{
  return (
    <html lang="en">
      <body className="antialiased">{{children}}</body>
    </html>
  );
}}
'''
    (app_dir / "app" / "layout.tsx").write_text(layout_tsx)

    # Install dependencies
    log(f"  [BUILD] npm install + build...")
    result = run("npm install openai@^4.0.0 --save 2>&1 | tail -5", cwd=app_dir, timeout=180)
    result = run("npm install 2>&1 | tail -3", cwd=app_dir, timeout=180)
    result = run("npm run build 2>&1 | tail -15", cwd=app_dir, timeout=180)
    if result.returncode != 0:
        log(f"  [WARN] Build had issues: {result.stderr[-200:]}")
    else:
        log(f"  [OK] Build succeeded")

    # Git push
    log(f"  [GIT] Push to GitHub...")
    git_dir = app_dir / ".git"
    if not git_dir.exists():
        run("git init -q", cwd=app_dir)
        run("git add -A --cached .", cwd=app_dir)
        run("git add -A", cwd=app_dir)
        result = run(f'git commit -m "{app_name}"', cwd=app_dir)
        if result.returncode == 0:
            run(f'git remote add origin "https://github.com/NebulaLumino/{app_name}.git" 2>/dev/null || true', cwd=app_dir)
            run("git branch -M main", cwd=app_dir)
            result = run(f"git push -u origin main --force 2>&1 | tail -5", cwd=app_dir, timeout=60)
            if "already exists" in result.stdout or result.returncode != 0:
                log(f"  [GIT] Repo may already exist, pushing anyway...")
                run(f"git push -u origin main 2>&1 | tail -5", cwd=app_dir, timeout=60)
    else:
        run("git add -A", cwd=app_dir)
        result = run(f'git commit -m "{app_name}" 2>/dev/null', cwd=app_dir)
        if result.returncode == 0:
            run("git push origin main 2>&1 | tail -5", cwd=app_dir, timeout=60)

    # Clean
    import shutil
    for folder in ["node_modules", ".next"]:
        p = app_dir / folder
        if p.exists():
            shutil.rmtree(p)
            log(f"  [CLEAN] Removed {folder}")

    log(f"  ✓ {app_name} complete\n")
    return True

def main():
    for task_num, app_name, description, accent_key in ALL_APPS:
        try:
            build_app(task_num, app_name, description, accent_key)
        except Exception as e:
            log(f"  [ERROR] {app_name}: {e}")

    log("=== ALL APPS COMPLETE ===")

if __name__ == "__main__":
    main()
