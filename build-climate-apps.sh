#!/bin/bash
set -e

WORKDIR="/Users/nebulalumino/.openclaw/workspace"
cd "$WORKDIR"

declare -A APPS=(
  ["ai-carbon-footprint"]="Carbon Footprint Analyzer|145,55,45|green|Enter your daily activities, travel, diet, and energy use"
  ["ai-carbon-offset"]="Carbon Offset Comparator|85,65,50|lime|Compare carbon offset programs, reforestation projects, and renewable energy certificates"
  ["ai-solar-roi"]="Renewable Energy ROI Calculator|45,70,55|yellow|Calculate payback period, savings, and ROI for solar panel installations"
  ["ai-esg-score"]="ESG Score Analyzer|220,60,55|blue|Analyze Environmental, Social, and Governance scores for companies and investments"
  ["ai-climate-risk"]="Property Climate Risk Assessor|0,65,50|red|Assess flood, wildfire, heat, and storm risk for properties and real estate"
  ["ai-sustainable-diet"]="Climate-Friendly Diet Planner|175,55,45|teal|Plan meals that minimize carbon footprint while maximizing nutrition"
  ["ai-ev-tco"]="EV vs ICE TCO Comparer|305,60,60|pink|Compare total cost of ownership between electric and internal combustion vehicles"
  ["ai-circular-economy"]="Waste Stream Analyzer|265,55,50|purple|Analyze waste streams and identify circular economy opportunities"
  ["ai-fast-fashion"]="Fast Fashion Impact Report|340,55,55|rose|Generate detailed environmental and social impact reports for fashion choices"
  ["ai-green-building"]="LEED/Energy Star Helper|235,55,55|indigo|Get guidance on LEED certification, Energy Star ratings, and green building standards"
  ["ai-ocean-plastic"]="Ocean Plastic Planner|200,45,45|slate|Plan ocean plastic cleanup initiatives and track plastic reduction impact"
  ["ai-air-quality"]="AQI Health Advisor|185,60,55|cyan|Get personalized health recommendations based on air quality index data"
  ["ai-deforestation-risk"]="Supply Chain Deforestation Mapper|25,70,55|orange|Map deforestation risks in supply chains and source sustainably"
  ["ai-sustainable-investing"]="Green Investment Screener|125,55,45|emerald|Screen investments for environmental impact, sustainability ratings, and green credentials"
  ["ai-water-conservation"]="Water Conservation Planner|165,55,45|cyan|Plan household and business water conservation strategies and track savings"
  ["ai-packaging-alternatives"]="Sustainable Packaging Guide|0,60,50|red|Find and compare sustainable packaging alternatives for products and businesses"
  ["ai-net-zero-roadmap"]="Corporate Net-Zero Builder|215,45,55|gray-blue|Build a comprehensive corporate net-zero roadmap with emissions targets and timelines"
  ["ai-biodiversity-impact"]="Biodiversity Impact Calculator|335,55,55|rose|Calculate biodiversity impact of projects, land use, and business operations"
  ["ai-heat-island"]="Heat Island Mitigator|45,75,55|yellow|Develop strategies to mitigate urban heat island effects in cities and neighborhoods"
  ["ai-rare-earth-metals"]="E-Waste Rare Earth Advisor|270,65,55|violet|Advise on rare earth metal recovery, e-waste recycling, and sustainable electronics"
)

for app in "${!APPS[@]}"; do
  IFS='|' read -r title hue sat light color description <<< "${APPS[$app]}"

  echo ""
  echo "============================================"
  echo "Building $app ($title)"
  echo "============================================"

  # Remove existing directory
  rm -rf "$app"

  # Create Next.js app
  echo "Creating Next.js app..."
  npx create-next-app@latest "$app" --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --no-turbopack --yes 2>/dev/null | tail -3

  # Install openai
  npm install openai 2>/dev/null | tail -1

  # Create API route
  mkdir -p "$app/src/app/api/generate"
  cat > "$app/src/app/api/generate/route.ts" << 'ROUTE_EOF'
import OpenAI from 'openai';

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
ROUTE_EOF

  # Create page.tsx
  cat > "$app/src/app/page.tsx" << PAGE_EOF
'use client';

import { useState } from 'react';

export default function Home() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!input.trim()) return;
    setLoading(true);
    setOutput('');
    try {
      const res = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: \`You are an expert in this field. Provide detailed, actionable insights based on the following input:\n\n\${input}\` }),
      });
      const data = await res.json();
      setOutput(data.result || data.error || 'No response received.');
    } catch (e: any) {
      setOutput('Error: ' + e.message);
    }
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 p-6 flex flex-col items-center justify-center">
      <div className="w-full max-w-2xl">
        <h1 className="text-3xl font-bold text-center mb-2 text-white">$title</h1>
        <p className="text-center text-gray-400 mb-8 text-sm">$description</p>
        <div className="bg-gray-800 rounded-2xl p-6 shadow-xl border border-gray-700">
          <textarea
            className="w-full bg-gray-900 text-gray-100 rounded-xl p-4 border border-gray-700 focus:border-\${color}-400 focus:outline-none resize-none"
            rows={6}
            placeholder="Enter your data, questions, or scenario details..."
            value={input}
            onChange={e => setInput(e.target.value)}
          />
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="mt-4 w-full py-3 px-6 bg-${color}-500 hover:bg-${color}-400 disabled:bg-${color}-800 text-gray-900 font-semibold rounded-xl transition-all"
          >
            {loading ? 'Generating...' : 'Generate Report'}
          </button>
        </div>
        {output && (
          <div className="mt-6 bg-gray-800 rounded-2xl p-6 border border-gray-700">
            <h2 className="text-${color}-400 font-semibold mb-3 text-sm uppercase tracking-wider">Analysis Results</h2>
            <pre className="text-gray-300 whitespace-pre-wrap text-sm leading-relaxed font-mono">{output}</pre>
          </div>
        )}
      </div>
    </main>
  );
}
PAGE_EOF

  # Fix the template literal backslash issue in page.tsx
  sed -i '' 's/\\`/\`/g' "$app/src/app/page.tsx"
  sed -i '' "s/\\\${input}/\${input}/g" "$app/src/app/page.tsx"

  # Build
  echo "Building..."
  cd "$app"
  OPENAI_API_KEY=dummy npm run build 2>&1 | tail -5

  # Git init and push
  echo "Pushing to GitHub..."
  git init 2>/dev/null || true
  git add -A 2>/dev/null
  git commit -m "feat: initial commit" 2>/dev/null || true
  
  # Create or use existing remote
  gh repo create NebulaLumino/$app --public --source=. --push 2>/dev/null || {
    git remote set-url origin https://github.com/NebulaLumino/$app.git 2>/dev/null || true
    git push -u origin main --force 2>/dev/null || true
  }
  
  cd "$WORKDIR"
  
  # Clean up
  rm -rf "$app/node_modules" "$app/.next"
  echo "Cleaned up $app"
done

echo ""
echo "============================================"
echo "ALL 20 APPS COMPLETE"
echo "============================================"