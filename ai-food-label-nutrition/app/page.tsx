"use client";
import { useState } from "react";

function Page() {
  const [productName, setProductName] = useState("");
  const [servingSize, setServingSize] = useState("");
  const [calories, setCalories] = useState("");
  const [fat, setFat] = useState("");
  const [carbs, setCarbs] = useState("");
  const [protein, setProtein] = useState("");
  const [fiber, setFiber] = useState("");
  const [sugar, setSugar] = useState("");
  const [sodium, setSodium] = useState("");
  const accent = "green";
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    if (!productName.trim()) { setError("Please enter the product name."); return; }
    setLoading(true); setError(""); setOutput("");
    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ productName, servingSize, calories, fat, carbs, protein, fiber, sugar, sodium }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Analysis failed");
      setOutput(data.output);
    } catch (err: any) { setError(err.message); }
    finally { setLoading(false); }
  };

  return (
    <main className="max-w-5xl mx-auto px-4 py-12">
      <div className="text-center mb-10">
        <h1 className={`text-4xl font-bold mb-3 bg-gradient-to-r from-${accent}-400 to-${accent}-600 bg-clip-text text-transparent`}>AI Food Label Nutrition Analyzer</h1>
        <p className="text-gray-400 text-sm">Understand nutrition labels, interpret serving sizes, and evaluate food products</p>
      </div>
      <div className="bg-gray-800/50 border border-gray-700 rounded-xl p-6 mb-6">
        <h2 className="text-lg font-semibold mb-4 text-gray-200">Enter Nutrition Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="md:col-span-2">
            <label className="block text-sm font-medium mb-1">Product Name *</label>
            <input value={productName} onChange={e => setProductName(e.target.value)} placeholder="e.g., Chobani Greek Yogurt, Kind Bar Dark Chocolate" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" />
          </div>
          <div><label className="block text-sm font-medium mb-1">Serving Size</label><input value={servingSize} onChange={e => setServingSize(e.target.value)} placeholder="e.g., 1 cup (240ml)" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Calories per Serving</label><input type="number" value={calories} onChange={e => setCalories(e.target.value)} placeholder="e.g., 150" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Total Fat (g)</label><input type="number" value={fat} onChange={e => setFat(e.target.value)} placeholder="e.g., 8" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Total Carbohydrates (g)</label><input type="number" value={carbs} onChange={e => setCarbs(e.target.value)} placeholder="e.g., 22" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Protein (g)</label><input type="number" value={protein} onChange={e => setProtein(e.target.value)} placeholder="e.g., 12" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Dietary Fiber (g)</label><input type="number" value={fiber} onChange={e => setFiber(e.target.value)} placeholder="e.g., 3" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Total Sugars (g)</label><input type="number" value={sugar} onChange={e => setSugar(e.target.value)} placeholder="e.g., 14" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
          <div><label className="block text-sm font-medium mb-1">Sodium (mg)</label><input type="number" value={sodium} onChange={e => setSodium(e.target.value)} placeholder="e.g., 450" className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm focus:outline-none focus:border-green-500" /></div>
        </div>
      </div>
      <div className="flex justify-center mb-6">
        <button onClick={handleGenerate} disabled={loading} className={`px-8 py-3 rounded-lg font-semibold text-white ${loading ? 'bg-green-700 cursor-not-allowed' : 'bg-green-600 hover:bg-green-500 transition-all'}`}>
          {loading ? "Analyzing..." : "Analyze Nutrition Label"}
        </button>
      </div>
      {error && <div className="bg-red-900/30 border border-red-700 rounded-lg p-4 text-red-300 text-sm mb-6">{error}</div>}
      {output && (
        <div className="bg-gray-800/70 border border-gray-700 rounded-xl p-6">
          <h2 className="text-lg font-semibold mb-4 text-gray-200">Analysis</h2>
          <pre className="text-gray-300 text-sm whitespace-pre-wrap">{output}</pre>
        </div>
      )}
    </main>
  );
}
export default Page;