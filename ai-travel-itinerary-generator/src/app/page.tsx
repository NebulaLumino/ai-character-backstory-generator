"use client";

import { useState } from "react";

interface FormData {
  destination: string;
  travelDates: string;
  duration: string;
  travelers: string;
  budget: string;
  travelStyle: string;
  interests: string;
  dietaryRestrictions: string;
}

interface Itinerary {
  overview: string;
  days: { day: string; activities: string[] }[];
  tips: string[];
  estimatedCost: string;
}

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Itinerary | null>(null);
  const [error, setError] = useState("");
  const [formData, setFormData] = useState<FormData>({
    destination: "",
    travelDates: "",
    duration: "",
    travelers: "",
    budget: "",
    travelStyle: "balanced",
    interests: "",
    dietaryRestrictions: "",
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Failed to generate");
      setResult(data.itinerary);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
      <div className="container mx-auto px-4 py-12">
        <div className="mx-auto max-w-4xl">
          <h1 className="mb-2 text-center text-4xl font-bold tracking-tight">
            🧭 Travel Itinerary Generator
          </h1>
          <p className="mb-8 text-center text-lg text-purple-200">
            AI-powered travel planning tailored to your style and interests
          </p>

          <form onSubmit={handleSubmit} className="mb-8 rounded-2xl bg-white/10 p-6 backdrop-blur-md">
            <div className="grid gap-6 md:grid-cols-2">
              <div>
                <label className="mb-2 block text-sm font-medium">Destination *</label>
                <input
                  type="text"
                  required
                  placeholder="e.g., Japan, Tuscany, Bali"
                  value={formData.destination}
                  onChange={(e) => setFormData({ ...formData, destination: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white placeholder:text-white/50 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium">Travel Dates</label>
                <input
                  type="text"
                  placeholder="e.g., June 15-22, 2026"
                  value={formData.travelDates}
                  onChange={(e) => setFormData({ ...formData, travelDates: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white placeholder:text-white/50 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium">Duration</label>
                <select
                  value={formData.duration}
                  onChange={(e) => setFormData({ ...formData, duration: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                >
                  <option value="">Select days</option>
                  <option value="3">3 days</option>
                  <option value="5">5 days</option>
                  <option value="7">7 days</option>
                  <option value="10">10 days</option>
                  <option value="14">14 days</option>
                </select>
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium">Number of Travelers</label>
                <input
                  type="text"
                  placeholder="e.g., 2, couple / family of 4"
                  value={formData.travelers}
                  onChange={(e) => setFormData({ ...formData, travelers: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white placeholder:text-white/50 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium">Budget Level</label>
                <select
                  value={formData.budget}
                  onChange={(e) => setFormData({ ...formData, budget: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                >
                  <option value="">Select budget</option>
                  <option value="budget">Budget ($50-100/day)</option>
                  <option value="moderate">Moderate ($100-200/day)</option>
                  <option value="luxury">Luxury ($200-400/day)</option>
                  <option value="ultra-luxury">Ultra Luxury ($400+/day)</option>
                </select>
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium">Travel Style</label>
                <select
                  value={formData.travelStyle}
                  onChange={(e) => setFormData({ ...formData, travelStyle: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                >
                  <option value="balanced">Balanced (mix of sight-seeing & relaxation)</option>
                  <option value="adventure">Adventure & Outdoor</option>
                  <option value="cultural">Cultural & Historical</option>
                  <option value="relaxation">Relaxation & Wellness</option>
                  <option value="foodie">Food & Culinary</option>
                  <option value="nightlife">Nightlife & Entertainment</option>
                </select>
              </div>

              <div className="md:col-span-2">
                <label className="mb-2 block text-sm font-medium">Interests & Activities</label>
                <input
                  type="text"
                  placeholder="e.g., museums, hiking, local cuisine, art, wildlife"
                  value={formData.interests}
                  onChange={(e) => setFormData({ ...formData, interests: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white placeholder:text-white/50 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                />
              </div>

              <div className="md:col-span-2">
                <label className="mb-2 block text-sm font-medium">Dietary Restrictions / Preferences</label>
                <input
                  type="text"
                  placeholder="e.g., vegetarian, gluten-free, no seafood"
                  value={formData.dietaryRestrictions}
                  onChange={(e) => setFormData({ ...formData, dietaryRestrictions: e.target.value })}
                  className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-white placeholder:text-white/50 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="mt-6 w-full rounded-xl bg-gradient-to-r from-purple-500 to-pink-500 py-4 text-lg font-semibold transition-all hover:from-purple-600 hover:to-pink-600 disabled:opacity-50"
            >
              {loading ? "✨ Generating Itinerary..." : "🌍 Generate My Itinerary"}
            </button>
          </form>

          {error && (
            <div className="mb-6 rounded-xl border border-red-500/50 bg-red-500/10 p-4 text-red-200">
              {error}
            </div>
          )}

          {result && (
            <div className="rounded-2xl bg-white/10 p-6 backdrop-blur-md">
              <h2 className="mb-4 text-2xl font-bold">{result.overview}</h2>
              
              {result.estimatedCost && (
                <div className="mb-6 rounded-xl bg-green-500/20 p-4">
                  <span className="font-semibold">💰 Estimated Cost: </span>
                  {result.estimatedCost}
                </div>
              )}

              <div className="space-y-6">
                {result.days.map((dayObj, idx) => (
                  <div key={idx} className="rounded-xl bg-white/5 p-5">
                    <h3 className="mb-3 text-lg font-semibold text-purple-300">{dayObj.day}</h3>
                    <ul className="space-y-2">
                      {dayObj.activities.map((activity, actIdx) => (
                        <li key={actIdx} className="flex items-start gap-2">
                          <span className="mt-1.5 text-purple-400">•</span>
                          <span>{activity}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>

              {result.tips && result.tips.length > 0 && (
                <div className="mt-6 rounded-xl bg-amber-500/20 p-5">
                  <h3 className="mb-3 text-lg font-semibold">💡 Travel Tips</h3>
                  <ul className="space-y-2">
                    {result.tips.map((tip, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <span className="mt-1.5 text-amber-400">✓</span>
                        <span>{tip}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}