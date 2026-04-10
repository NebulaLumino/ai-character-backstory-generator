"use client";
import { useState } from "react";

export default function Home() {
  const [form, setForm] = useState({ brewMethod: "", beanOrigin: "", roastLevel: "Medium", strengthPreference: "Medium", grindSize: "", waterQuality: "Filtered", cupCount: "2" });
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.brewMethod) { setError("Please select a brewing method."); return; }
    setLoading(true); setError(""); setOutput("");
    try {
      const res = await fetch("/api/generate", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Generation failed");
      setOutput(data.output || "");
    } catch (err: any) { setError(err.message); } finally { setLoading(false); }
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-900 via-gray-950 to-gray-900 text-white px-4 py-12">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-10">
          <div className="inline-flex items-center gap-2 mb-4 px-4 py-2 rounded-full bg-amber-500/10 border border-amber-500/30">
            <span className="text-amber-400 text-sm font-medium">☕ AI × Food & Cooking</span>
          </div>
          <h1 className="text-4xl font-bold text-white mb-3">AI Coffee Brewing Guide</h1>
          <p className="text-gray-400 text-lg">Personalized brewing guides with ratios, temperatures, and barista techniques</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-5 mb-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Brewing Method *</label>
              <select name="brewMethod" value={form.brewMethod} onChange={handleChange} required
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm">
                <option value="">Select method</option>
                <option>Pour-over (V60 / Chemex)</option><option>Espresso</option><option>French Press</option>
                <option>AeroPress</option><option>Cold Brew</option><option>Moka Pot</option>
                <option>Drip Coffee Maker</option><option>Siphon</option><option>Nespresso-style pods</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Bean Origin</label>
              <input type="text" name="beanOrigin" value={form.beanOrigin} onChange={handleChange} placeholder="e.g., Ethiopian Yirgacheffe, Colombian, Kenya AA"
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Roast Level</label>
              <select name="roastLevel" value={form.roastLevel} onChange={handleChange}
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm">
                <option>Light</option><option>Medium-Light</option><option>Medium</option><option>Medium-Dark</option><option>Dark</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Strength Preference</label>
              <select name="strengthPreference" value={form.strengthPreference} onChange={handleChange}
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm">
                <option>Mild</option><option>Medium</option><option>Strong</option><option>Extra Strong</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Grind Size Available</label>
              <select name="grindSize" value={form.grindSize} onChange={handleChange}
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm">
                <option value="">Not sure / adjustable</option><option>Extra Fine (espresso)</option><option>Fine</option><option>Medium-Fine</option><option>Medium</option><option>Medium-Coarse</option><option>Coarse (French Press)</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">Number of Cups</label>
              <input type="number" name="cupCount" value={form.cupCount} onChange={handleChange} min="1" max="12"
                className="w-full bg-gray-800/60 border border-gray-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition-all text-sm" />
            </div>
          </div>
          <button type="submit" disabled={loading}
            className="w-full bg-amber-600 hover:bg-amber-500 disabled:bg-amber-600/50 text-white font-semibold py-4 rounded-xl transition-all duration-200 text-base flex items-center justify-center gap-2">
            {loading ? (
              <><svg className="animate-spin h-5 w-5" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" /><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" /></svg>Brewing...</>
            ) : "☕ Generate Brewing Guide"}
          </button>
        </form>
        {error && <div className="bg-red-900/30 border border-red-700 rounded-xl p-4 text-red-300 text-sm mb-6">{error}</div>}
        {output && (
          <div className="bg-gray-800/50 border border-gray-700 rounded-2xl p-6 md:p-8">
            <h2 className="text-xl font-semibold text-amber-400 mb-4">Your Brewing Guide</h2>
            <div className="prose prose-invert prose-amber max-w-none text-gray-200 whitespace-pre-wrap text-sm leading-relaxed">{output}</div>
          </div>
        )}
      </div>
    </main>
  );
}