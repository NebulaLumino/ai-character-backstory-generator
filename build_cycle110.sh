#!/bin/bash
set -e
WORKSPACE="/Users/nebulalumino/.openclaw/workspace"
cd "$WORKSPACE"

# Colors for output
RED='\033[0;31m'; ORANGE='\033[0;33m'; YELLOW='\033[1;33m'; LIME='\033[0;32m'
GREEN='\033[0;32m'; TEAL='\033[0;36m'; CYAN='\033[0;36m'; BLUE='\033[0;34m'
INDIGO='\033[0;94m'; VIOLET='\033[0;35m'; PINK='\033[0;35m'; ROSE='\033[0;35m'
NC='\033[0m'

log() { echo -e "${NC}[$(date '+%H:%M:%S')] $1${NC}"; }

# HIGH apps accent colors (Tailwind hsl values)
declare -A ACCENT_HSL
ACCENT_HSL["red"]="0 84% 60%"
ACCENT_HSL["orange"]="25 95% 53%"
ACCENT_HSL["yellow"]="48 96% 53%"
ACCENT_HSL["lime"]="142 76% 42%"
ACCENT_HSL["green"]="142 71% 45%"
ACCENT_HSL["teal"]="174 65% 40%"
ACCENT_HSL["cyan"]="188 78% 51%"
ACCENT_HSL["blue"]="217 91% 53%"
ACCENT_HSL["indigo"]="239 84% 67%"
ACCENT_HSL["violet"]="262 83% 58%"
ACCENT_HSL["pink"]="350 89% 60%"
ACCENT_HSL["rose"]="330 81% 60%"

# ========================
# PHASE 1: Build HIGH apps 3291-3300
# ========================

build_app() {
    local task_num=$1
    local app_name=$2
    local accent_key=$3
    local hsl="${ACCENT_HSL[$accent_key]}"

    log "${GREEN}=== Building app $task_num: $app_name (accent: $accent_key) ===${NC}"

    local app_dir="$WORKSPACE/$app_name"

    # Scaffold if missing
    if [ ! -d "$app_dir" ]; then
        log "  [SCAFFOLD] Creating $app_name..."
        npx create-next-app@latest "$app_name" --typescript --tailwind --app --no-src-dir --import-alias "@/*" --yes --no-turbopack 2>&1 | tail -5
    else
        log "  [SKIP] $app_name already exists"
    fi

    # Ensure directory
    mkdir -p "$app_dir/app/api/generate"

    # ====== globals.css ======
    cat > "$app_dir/app/globals.css" << 'CSSEOF'
@import "tailwindcss";
:root { --background: #030712; --foreground: #f3f4f6; }
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: system-ui, -apple-system, sans-serif;
}
body { background: var(--background); color: var(--foreground); }
CSSEOF

    # Add accent border
    cat >> "$app_dir/app/globals.css" << EOF

/* Accent color: ${accent_key} */
.app-header {
  border-bottom: 3px solid hsl(${hsl});
}
.accent-text { color: hsl(${hsl}); }
.accent-bg { background-color: hsl(${hsl}); }
.accent-border { border-color: hsl(${hsl}); }
.accent-ring:focus { --tw-ring-color: hsl(${hsl}); }
.accent-bg-hover:hover { background-color: hsl(${hsl} / 0.15); }
.accent-text-hover:hover { color: hsl(${hsl}); }
.generate-btn {
  background-color: hsl(${hsl});
  color: white;
}
.generate-btn:hover { filter: brightness(1.1); }
.generate-btn:disabled { opacity: 0.5; cursor: not-allowed; }
CSSEOF

    # ====== package.json add openai ======
    if ! grep -q '"openai"' "$app_dir/package.json" 2>/dev/null; then
        log "  [PATCH] Adding openai dependency..."
        (cd "$app_dir" && npm install openai@^4.0.0 --save 2>&1 | tail -3)
    fi

    # ====== API route ======
    cat > "$app_dir/app/api/generate/route.ts" << 'ROUTEEOF'
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { prompt } = await req.json();
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      return NextResponse.json({ error: "OPENAI_API_KEY not set in .env.local" }, { status: 500 });
    }
    const response = await fetch("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${apiKey}` },
      body: JSON.stringify({ model: "deepseek-chat", messages: [
        { role: "system", content: "You are a helpful AI assistant." },
        { role: "user", content: prompt }
      ], stream: false }),
    });
    if (!response.ok) {
      const err = await response.text();
      return NextResponse.json({ error: `API error: ${response.status} - ${err}` }, { status: 500 });
    }
    const data = await response.json();
    const content = data.choices?.[0]?.message?.content ?? "";
    return NextResponse.json({ content });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : String(err);
    return NextResponse.json({ error: `Server error: ${msg}` }, { status: 500 });
  }
}
ROUTEEOF

    # ====== page.tsx ======
    cat > "$app_dir/app/page.tsx" << "PAGEEOF"
"use client";
import { useState } from "react";

export default function Home() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    if (!input.trim()) return;
    setLoading(true);
    setOutput("");
    setError("");
    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input }),
      });
      const data = await res.json();
      if (!res.ok) { setError(data.error || "Generation failed"); }
      else { setOutput(data.content || "No content generated."); }
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <header className="app-header bg-gray-900 px-6 py-5 mb-8">
        <h1 className="text-2xl font-bold accent-text">AI Sermon Generator</h1>
        <p className="text-gray-400 text-sm mt-1">Spirit-filled sermons & weekly homilies</p>
      </header>
      <main className="max-w-3xl mx-auto px-6 pb-16">
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Describe your sermon topic, scripture, and preferences</label>
            <textarea
              value={input}
              onChange={e => setInput(e.target.value)}
              placeholder="e.g., Write a 20-minute inspirational sermon on forgiveness for a general congregation based on Luke 15:11-32"
              rows={6}
              className="w-full bg-gray-800 border border-gray-700 rounded-xl px-4 py-3 text-gray-100 placeholder-gray-500 focus:outline-none focus:ring-2 accent-ring resize-none"
            />
          </div>
          <button
            onClick={handleGenerate}
            disabled={loading || !input.trim()}
            className="generate-btn w-full py-3 rounded-xl font-semibold text-lg transition-all"
          >
            {loading ? "Generating..." : "Generate Sermon"}
          </button>
          {error && (
            <div className="bg-red-900/30 border border-red-700 text-red-300 rounded-xl p-4 text-sm">{error}</div>
          )}
          {output && (
            <div className="bg-gray-900 border border-gray-700 rounded-xl p-6">
              <h3 className="text-sm font-semibold text-gray-400 mb-3">Generated Sermon</h3>
              <div className="prose prose-invert prose-sm max-w-none whitespace-pre-wrap text-gray-200">{output}</div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
PAGEEOF

    # ====== layout.tsx update ======
    cat > "$app_dir/app/layout.tsx" << 'LAYOUTEOF'
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI App",
  description: "AI-powered application",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
LAYOUTEOF

    # ====== Install & Build ======
    log "  [BUILD] Installing dependencies..."
    cd "$app_dir"
    npm install 2>&1 | tail -3
    log "  [BUILD] Building..."
    npm run build 2>&1 | tail -10

    # ====== Git push ======
    log "  [GIT] Committing..."
    if [ ! -d "$app_dir/.git" ]; then
        git init -q
        git add -A
        git commit -m "$app_name"
        git remote add origin "https://github.com/NebulaLumino/${app_name}.git" 2>/dev/null || true
        git branch -M main 2>/dev/null || true
        gh repo create "${app_name}" --public --push 2>&1 | tail -3 || log "  [GIT] Repo may already exist"
    else
        cd "$app_dir"
        git add -A
        git commit -m "$app_name" 2>/dev/null || log "  [GIT] Nothing to commit"
        git push origin main 2>&1 | tail -3 || log "  [GIT] Push may have failed"
    fi

    cd "$WORKSPACE"
    # Clean up
    rm -rf "$app_dir/node_modules" "$app_dir/.next"
    log "  [CLEAN] node_modules and .next removed"

    log "${GREEN}✓ $app_name done${NC}\n"
}

# Run all HIGH apps
for entry in "3291:ai-sermon-generator:red" "3292:ai-scripture-commentary:orange" "3293:ai-meditation-guide-generator:yellow" "3294:ai-interfaith-dialogue:lime" "3295:ai-spiritual-retreat-planner:green" "3296:ai-buddhist-dharma-talk:teal" "3297:ai-jewish-halakha-responsa:cyan" "3298:ai-islamic-fiqh-fatwa:blue" "3299:ai-hindu-puranic-story:indigo" "3300:ai-interfaith-wedding-ceremony:violet"; do
    task=$(echo $entry | cut -d: -f1)
    app=$(echo $entry | cut -d: -f2)
    accent=$(echo $entry | cut -d: -f3)
    build_app $task $app $accent
done

log "${GREEN}All HIGH apps complete!${NC}"
