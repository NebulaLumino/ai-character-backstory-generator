#!/bin/bash
# Build script for Cycle 108 apps - Pets, Animals & Veterinary Care

set -e
WORKSPACE="/Users/nebulalumino/.openclaw/workspace"
TEMPLATE="$WORKSPACE/ai-zookeeping"
DEEPSEEK_KEY="${DEEPSEEK_API_KEY}"

mkapp() {
  local NUM=$1
  local NAME=$2
  local ACCENT=$3
  local TITLE=$4
  local DESC=$5
  local COPYFROM="${6:-$TEMPLATE}"
  local DEST="$WORKSPACE/ai-$NAME"

  echo ">>> Building ai-$NAME (task $NUM)..."

  # Copy template
  cp -r "$COPYFROM" "$DEST"

  # Update package.json
  node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('$DEST/package.json','utf8'));
pkg.name = 'ai-$NAME';
pkg.version = '0.1.0';
fs.writeFileSync('$DEST/package.json', JSON.stringify(pkg, null, 2));
"

  # Build page.tsx
  cat > "$DEST/app/page.tsx" << 'PAGEEOF'
"use client";
import { useState } from "react";
const ACCENT = "hsl([[HSL]], 70%, 55%)";
export default function Page() {
  const [[VARS]] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true); setOutput("");
    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ [[FIELDS]] }),
      });
      const data = await res.json();
      setOutput(data.output || "No response.");
    } catch { setOutput("Error."); }
    finally { setLoading(false); }
  };
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-gray-900 text-white px-4 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="mb-8 text-center">
          <h1 className="text-4xl font-bold mb-2" style={{ color: ACCENT }}>[[TITLE]]</h1>
          <p className="text-gray-400">[[DESC]]</p>
        </div>
        <div className="bg-gray-900/60 border border-gray-700 rounded-2xl p-6 mb-8">
          <h2 className="text-xl font-semibold mb-4" style={{ color: ACCENT }}>[[FORM_TITLE]]</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            [[FIELDS_HTML]]
            <button type="submit" disabled={loading}
              className="w-full py-3 rounded-lg font-semibold text-white transition hover:opacity-90 disabled:opacity-50"
              style={{ backgroundColor: ACCENT }}>
              {loading ? "Generating..." : "[[BTN_TEXT]]"}
            </button>
          </form>
        </div>
        {output && (
          <div className="bg-gray-900/60 border border-gray-700 rounded-2xl p-6">
            <h2 className="text-xl font-semibold mb-4" style={{ color: ACCENT }}>[[OUTPUT_TITLE]]</h2>
            <div className="prose prose-invert prose-sm max-w-none text-gray-300 whitespace-pre-wrap">{output}</div>
          </div>
        )}
      </div>
    </div>
  );
}
PAGEEOF
}

# Check disk space before starting
check_disk() {
  local avail=$(df / | tail -1 | awk '{print $4}')
  echo "Available space: ${avail} blocks"
  if [ "$avail" -lt 6000000 ]; then
    echo "WARNING: Less than 3GB available!"
  fi
}

check_disk
echo "Template ready. Starting app builds..."
echo "Will build in batches of 5."
