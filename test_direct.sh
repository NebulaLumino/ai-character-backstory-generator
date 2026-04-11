#!/bin/bash
WORKDIR="/Users/nebulalumino/.openclaw/workspace"
cd "$WORKDIR"
for app in ai-carbon-footprint ai-carbon-offset ai-esg-score ai-climate-risk ai-sustainable-diet ai-fast-fashion ai-green-building ai-ocean-plastic ai-air-quality ai-deforestation-risk ai-water-conservation ai-biodiversity-impact; do
    echo "=== $app ==="
    rm -rf "$app"
    npx create-next-app@latest "$app" --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --no-turbopack --yes 2>/dev/null | tail -1
    npm install openai 2>/dev/null | tail -1
    mkdir -p "$app/src/app/api/generate"
    cat > "$app/src/app/api/generate/route.ts" << 'ROUTE'
import OpenAI from 'openai';
export async function POST(req: Request) {
  try {
    const { prompt } = await req.json();
    const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY, baseURL: 'https://api.deepseek.com/v1' });
    const completion = await client.chat.completions.create({ model: 'deepseek-chat', messages: [{ role: 'user', content: prompt }], temperature: 0.7 });
    return Response.json({ result: completion.choices[0]?.message?.content || '' });
  } catch (e: any) { return Response.json({ error: e.message }, { status: 500 }); }
}
ROUTE
    echo "'use client';import{useState}from'react';export default function Home(){const[i,s,o]=useState(''),[l,g]=useState(false);const t=async()=>{if(!i.trim())return;g(true),s('');try{const e=await fetch('/api/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:\`You are an expert. Provide detailed insights based on:\n\n\${i}\`})}),n=await e.json();s(n.result||n.error||'No response')}catch(e){s('Error: '+e.message)}g(false)};return(<main className='min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 p-6 flex flex-col items-center justify-center'><div className='w-full max-w-2xl'><h1 className='text-3xl font-bold text-center mb-2 text-white'>AI Climate Tool</h1><p className='text-center text-gray-400 mb-8 text-sm'>Enter your data for analysis</p><div className='bg-gray-800 rounded-2xl p-6 shadow-xl border border-gray-700'><textarea className='w-full bg-gray-900 text-gray-100 rounded-xl p-4 border border-gray-700 focus:border-green-400 focus:outline-none resize-none' rows={6} placeholder='Enter data...' value={i} onChange={e=>s(e.target.value)}/>{l?<p className='mt-4 text-green-400'>Generating...</p>:<button onClick={t} className='mt-4 w-full py-3 px-6 bg-green-500 hover:bg-green-400 text-gray-900 font-semibold rounded-xl'>Generate Report</button>}</div>{o&&<div className='mt-6 bg-gray-800 rounded-2xl p-6 border border-gray-700'><h2 className='text-green-400 font-semibold mb-3'>Results</h2><pre className='text-gray-300 whitespace-pre-wrap text-sm'>{o}</pre></div>}</div></main>);}" > "$app/src/app/page.tsx"
    OPENAI_API_KEY=dummy npm run build --prefix "$app" 2>/dev/null | tail -2
    (cd "$app" && git init && git add -A && git commit -m "feat: initial commit" && git remote add origin https://github.com/NebulaLumino/$app.git && git push -u origin main --force 2>&1 | tail -2)
    rm -rf "$app/node_modules" "$app/.next"
    echo "Done: $app"
done
echo "ALL DONE"
