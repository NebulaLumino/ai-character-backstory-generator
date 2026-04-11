"use client";
import { useState } from "react";

export default function Home() {
  const [form, setForm] = useState({ role: "", description: "", look: "", personality: "" });
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    const prompt = `You are an expert casting director. For each role listed, generate ideal casting recommendations:\n\nRole: ${form.role}\nCharacter Description: ${form.description}\nPhysical Look: ${form.look}\nPersonality Traits: ${form.personality}\n\nProvide: character breakdown, ideal age range, physical attributes, ethnicity range, personality essence, sample reference actors (with diversity), and chemistry read suggestions.`;
    const res = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setOutput(data.result || "No output generated.");
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-950 via-gray-900 to-black text-white flex flex-col items-center justify-center p-8">
      <div className="w-full max-w-3xl">
        <h1 className="text-4xl font-bold mb-2 text-center" style={{ color: "hsl(120, 70%, 55%)" }}>
          🎭 AI Casting Engine
        </h1>
        <p className="text-gray-400 text-center mb-8">Find the perfect cast for your characters</p>

        <form onSubmit={handleSubmit} className="space-y-4 mb-6">
          <input
            className="w-full bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400"
            placeholder="Character role (e.g. LEAD: Marcus, SUPPORTING: Elena)"
            value={form.role}
            onChange={(e) => setForm({ ...form, role: e.target.value })}
          />
          <textarea
            className="w-full bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400 resize-none"
            placeholder="Character description — background, arc, motivation"
            value={form.description}
            onChange={(e) => setForm({ ...form, description: e.target.value })}
          />
          <div className="grid grid-cols-2 gap-4">
            <input
              className="bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400"
              placeholder="Physical Look (e.g. Rugged, elegant, androgynous)"
              value={form.look}
              onChange={(e) => setForm({ ...form, look: e.target.value })}
            />
            <input
              className="bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400"
              placeholder="Personality (e.g. Charismatic, brooding, unpredictable)"
              value={form.personality}
              onChange={(e) => setForm({ ...form, personality: e.target.value })}
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-lg font-semibold text-black transition-all disabled:opacity-50"
            style={{ background: "hsl(120, 70%, 55%)" }}
          >
            {loading ? "Finding cast..." : "Generate Casting Breakdown"}
          </button>
        </form>

        {output && (
          <div className="bg-gray-900/80 border border-gray-700 rounded-xl p-6">
            <pre className="text-gray-300 whitespace-pre-wrap font-mono text-sm">{output}</pre>
          </div>
        )}
      </div>
    </main>
  );
}
