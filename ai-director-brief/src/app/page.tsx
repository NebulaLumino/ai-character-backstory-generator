"use client";
import { useState } from "react";

export default function Home() {
  const [form, setForm] = useState({ concept: "", vision: "", style: "", mood: "" });
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    const prompt = `You are an experienced film director. Create a comprehensive director's brief for the following film:\n\nConcept: ${form.concept}\nVision: ${form.vision}\nVisual Style: ${form.style}\nMood/Atmosphere: ${form.mood}\n\nInclude: director's intent statement, visual references, lighting approach, casting philosophy, pacing notes, thematic anchors, and key scenes that define the film.`;
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
        <h1 className="text-4xl font-bold mb-2 text-center" style={{ color: "hsl(90, 70%, 55%)" }}>
          🎬 AI Director's Brief
        </h1>
        <p className="text-gray-400 text-center mb-8">Articulate your directorial vision with precision</p>

        <form onSubmit={handleSubmit} className="space-y-4 mb-6">
          <textarea
            className="w-full bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-lime-400 resize-none"
            placeholder="Film concept — what is the story?"
            value={form.concept}
            onChange={(e) => setForm({ ...form, concept: e.target.value })}
          />
          <textarea
            className="w-full bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-lime-400 resize-none"
            placeholder="Your vision — what do you want the audience to feel?"
            value={form.vision}
            onChange={(e) => setForm({ ...form, vision: e.target.value })}
          />
          <div className="grid grid-cols-2 gap-4">
            <input
              className="bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-lime-400"
              placeholder="Visual Style (e.g. Neo-noir, naturalistic)"
              value={form.style}
              onChange={(e) => setForm({ ...form, style: e.target.value })}
            />
            <input
              className="bg-gray-800/60 border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-lime-400"
              placeholder="Mood (e.g. Haunting, exhilarating)"
              value={form.mood}
              onChange={(e) => setForm({ ...form, mood: e.target.value })}
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-lg font-semibold text-black transition-all disabled:opacity-50"
            style={{ background: "hsl(90, 70%, 55%)" }}
          >
            {loading ? "Crafting brief..." : "Generate Director's Brief"}
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
