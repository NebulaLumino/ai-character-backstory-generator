#!/usr/bin/env python3
import os, subprocess

WORKDIR = "/Users/nebulalumino/.openclaw/workspace"
os.chdir(WORKDIR)

FAILED = [
    "ai-carbon-footprint", "ai-carbon-offset", "ai-esg-score",
    "ai-climate-risk", "ai-sustainable-diet", "ai-fast-fashion",
    "ai-green-building", "ai-ocean-plastic", "ai-air-quality",
    "ai-deforestation-risk", "ai-water-conservation", "ai-biodiversity-impact",
]

ROUTE_TS = """import OpenAI from 'openai';

export async function POST(req: Request) {
  try {
    const { prompt } = await req.json();
    const client = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      baseURL: 'https://api.deepseek.com/v1',
    });
    const completion = await client.chat.completions.create({
      model: 'deepseek-chat',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.7,
    });
    return Response.json({ result: completion.choices[0]?.message?.content || '' });
  } catch (e: any) {
    return Response.json({ error: e.message }, { status: 500 });
  }
}
"""

APP_CONFIG = {
    "ai-carbon-footprint":    ("Carbon Footprint Analyzer",       "green",  "Enter your daily activities, travel, diet, and energy use for detailed analysis"),
    "ai-carbon-offset":       ("Carbon Offset Comparator",        "lime",   "Compare carbon offset programs, reforestation projects, and renewable energy certificates"),
    "ai-esg-score":           ("ESG Score Analyzer",              "blue",   "Analyze Environmental, Social, and Governance scores for companies and investments"),
    "ai-climate-risk":        ("Property Climate Risk Assessor", "red",    "Assess flood, wildfire, heat, and storm risk for properties and real estate"),
    "ai-sustainable-diet":    ("Climate-Friendly Diet Planner",   "teal",   "Plan meals that minimize carbon footprint while maximizing nutrition"),
    "ai-fast-fashion":        ("Fast Fashion Impact Report",      "rose",   "Generate detailed environmental and social impact reports for fashion choices"),
    "ai-green-building":      ("LEED/Energy Star Helper",         "indigo", "Get guidance on LEED certification, Energy Star ratings, and green building standards"),
    "ai-ocean-plastic":       ("Ocean Plastic Planner",           "slate",  "Plan ocean plastic cleanup initiatives and track plastic reduction impact"),
    "ai-air-quality":         ("AQI Health Advisor",               "cyan",   "Get personalized health recommendations based on air quality index data"),
    "ai-deforestation-risk":  ("Supply Chain Deforestation Mapper","orange","Map deforestation risks in supply chains and source sustainably"),
    "ai-water-conservation":  ("Water Conservation Planner",      "cyan",   "Plan household and business water conservation strategies"),
    "ai-biodiversity-impact":  ("Biodiversity Impact Calculator",  "rose",   "Calculate biodiversity impact of projects, land use, and business operations"),
}

def run(cmd, cwd=None, timeout=30):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return r.stdout, r.stderr, r.returncode

for app in FAILED:
    print(f"\nRepushing: {app}")
    
    title, color, desc = APP_CONFIG[app]
    
    # Recreate app
    print(f"  Recreating Next.js app...")
    run(f"rm -rf {app} && npx create-next-app@latest {app} --typescript --tailwind --eslint --app --src-dir --import-alias '@/*' --no-turbopack --yes", cwd=WORKDIR, timeout=120)
    
    # Install openai
    run(f"npm install openai 2>/dev/null", cwd=f"{WORKDIR}/{app}", timeout=60)
    
    # Write API route
    os.makedirs(f"{WORKDIR}/{app}/src/app/api/generate", exist_ok=True)
    with open(f"{WORKDIR}/{app}/src/app/api/generate/route.ts", "w") as f:
        f.write(ROUTE_TS)
    
    # Write page.tsx
    page = f"""'use client';

import {{ useState }} from 'react';

export default function Home() {{
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {{
    if (!input.trim()) return;
    setLoading(true);
    setOutput('');
    try {{
      const res = await fetch('/api/generate', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{
          prompt: `You are an expert in this field. Provide detailed, actionable insights based on the following input:\\n\\n${{input}}`
        }}),
      }});
      const data = await res.json();
      setOutput(data.result || data.error || 'No response received.');
    }} catch (e: any) {{
      setOutput('Error: ' + e.message);
    }}
    setLoading(false);
  }};

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 p-6 flex flex-col items-center justify-center">
      <div className="w-full max-w-2xl">
        <h1 className="text-3xl font-bold text-center mb-2 text-white">{title}</h1>
        <p className="text-center text-gray-400 mb-8 text-sm">{desc}</p>
        <div className="bg-gray-800 rounded-2xl p-6 shadow-xl border border-gray-700">
          <textarea
            className="w-full bg-gray-900 text-gray-100 rounded-xl p-4 border border-gray-700 focus:border-{color}-400 focus:outline-none resize-none"
            rows={{6}}
            placeholder="Enter your data, questions, or scenario details..."
            value={{input}}
            onChange={{e => setInput(e.target.value)}}
          />
          <button
            onClick={{handleGenerate}}
            disabled={{loading}}
            className="mt-4 w-full py-3 px-6 bg-{color}-500 hover:bg-{color}-400 disabled:bg-{color}-800 text-gray-900 font-semibold rounded-xl transition-all"
          >
            {{loading ? 'Generating...' : 'Generate Report'}}
          </button>
        </div>
        {{output && (
          <div className="mt-6 bg-gray-800 rounded-2xl p-6 border border-gray-700">
            <h2 className="text-{color}-400 font-semibold mb-3 text-sm uppercase tracking-wider">Analysis Results</h2>
            <pre className="text-gray-300 whitespace-pre-wrap text-sm leading-relaxed font-mono">{{output}}</pre>
          </div>
        )}}
      </div>
    </main>
  );
}}
"""
    with open(f"{WORKDIR}/{app}/src/app/page.tsx", "w") as f:
        f.write(page)
    
    # Build
    print(f"  Building...")
    out, err, rc = run("OPENAI_API_KEY=dummy npm run build", cwd=f"{WORKDIR}/{app}", timeout=120)
    if rc == 0:
        print(f"  Build: OK")
    else:
        print(f"  Build: ERROR - {err[-200:]}")
    
    # Git init and push
    print(f"  Pushing to GitHub...")
    run("git init 2>/dev/null || true", cwd=f"{WORKDIR}/{app}")
    run("git add -A && git commit -m 'feat: initial commit' 2>/dev/null || true", cwd=f"{WORKDIR}/{app}")
    
    run(f"git remote set-url origin https://github.com/NebulaLumino/{app}.git 2>/dev/null || true", cwd=f"{WORKDIR}/{app}")
    out, err, rc = run(f"git push -u origin main --force", cwd=f"{WORKDIR}/{app}", timeout=30)
    if rc == 0:
        print(f"  Pushed!")
    else:
        print(f"  Push error: {err[-200:]}")
    
    # Clean up
    run(f"rm -rf {WORKDIR}/{app}/node_modules {WORKDIR}/{app}/.next", timeout=10)
    print(f"  Cleaned: {app}")

print("\n\nAll re-pushes done!")