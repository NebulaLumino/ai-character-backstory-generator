'use client';

import { useState } from 'react';

export default function Home() {
  const [result, setResult] = useState<{ success: boolean; prompt?: string; error?: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    const formData = new FormData(e.currentTarget);

    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ success: false, error: 'Failed to generate music prompt' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-cyan-500/10 via-transparent to-transparent" />
        <div className="max-w-4xl mx-auto px-6 py-16 relative">
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-4 tracking-tight">
            AI Music <span className="text-cyan-400">Composer</span>
          </h1>
          <p className="text-xl text-slate-300 mb-8 max-w-2xl">
            Generate custom music prompts, melodies, and compositions. Create unique soundscapes for your projects.
          </p>
        </div>
      </div>

      {/* Composition Form */}
      <div className="max-w-4xl mx-auto px-6 pb-20">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Main Input */}
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
            <label htmlFor="description" className="block text-sm font-medium text-slate-300 mb-3">
              Describe your music
            </label>
            <textarea
              id="description"
              name="description"
              rows={4}
              placeholder="e.g., Upbeat electronic dance track with driving bass, dreamy ambient synths, or melancholic piano ballad..."
              className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent resize-none"
            />
          </div>

          {/* Options Grid */}
          <div className="grid md:grid-cols-2 gap-6">
            {/* Genre */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
              <label htmlFor="genre" className="block text-sm font-medium text-slate-300 mb-3">
                Genre
              </label>
              <select
                id="genre"
                name="genre"
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              >
                <option value="electronic">Electronic / EDM</option>
                <option value="ambient">Ambient / Atmospheric</option>
                <option value="orchestral">Orchestral / Classical</option>
                <option value="rock">Rock / Alternative</option>
                <option value="jazz">Jazz / Blues</option>
                <option value="pop">Pop / R&B</option>
                <option value="hiphop">Hip Hop / Rap</option>
                <option value="folk">Folk / Acoustic</option>
                <option value="cinematic">Cinematic / Film Score</option>
                <option value="world">World / Ethnic</option>
              </select>
            </div>

            {/* Mood */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
              <label htmlFor="mood" className="block text-sm font-medium text-slate-300 mb-3">
                Mood
              </label>
              <select
                id="mood"
                name="mood"
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              >
                <option value="uplifting">Uplifting / Energetic</option>
                <option value="melancholic">Melancholic / Sad</option>
                <option value="dark">Dark / Intense</option>
                <option value="dreamy">Dreamy / Ethereal</option>
                <option value="peaceful">Peaceful / Calm</option>
                <option value="aggressive">Aggressive / Harsh</option>
                <option value="romantic">Romantic / Warm</option>
                <option value="mysterious">Mysterious / Enigmatic</option>
                <option value="playful">Playful / Quirky</option>
                <option value="heroic">Heroic / Epic</option>
              </select>
            </div>

            {/* Tempo */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
              <label htmlFor="tempo" className="block text-sm font-medium text-slate-300 mb-3">
                Tempo
              </label>
              <select
                id="tempo"
                name="tempo"
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              >
                <option value="slow">Slow (60-80 BPM)</option>
                <option value="moderate">Moderate (80-110 BPM)</option>
                <option value="medium">Medium (110-130 BPM)</option>
                <option value="fast">Fast (130-160 BPM)</option>
                <option value="veryfast">Very Fast (160+ BPM)</option>
              </select>
            </div>

            {/* Key */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
              <label htmlFor="key" className="block text-sm font-medium text-slate-300 mb-3">
                Musical Key
              </label>
              <select
                id="key"
                name="key"
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              >
                <option value="any">Any Key</option>
                <option value="c-major">C Major / A Minor</option>
                <option value="g-major">G Major / E Minor</option>
                <option value="d-major">D Major / B Minor</option>
                <option value="a-major">A Major / F# Minor</option>
                <option value="e-major">E Major / C# Minor</option>
                <option value="b-major">B Major / G# Minor</option>
                <option value="f-major">F Major / D Minor</option>
                <option value="bb-major">Bb Major / G Minor</option>
                <option value="eb-major">Eb Major / C Minor</option>
                <option value="ab-major">Ab Major / F Minor</option>
                <option value="db-major">Db Major / Bb Minor</option>
              </select>
            </div>

            {/* Instruments */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6 md:col-span-2">
              <label htmlFor="instruments" className="block text-sm font-medium text-slate-300 mb-3">
                Preferred Instruments
              </label>
              <select
                id="instruments"
                name="instruments"
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              >
                <option value="synth">Synthesizers / Electronic</option>
                <option value="piano">Piano / Keys</option>
                <option value="guitar">Guitar (Acoustic/Electric)</option>
                <option value="strings">Strings (Orchestral)</option>
                <option value="drums">Drums / Percussion</option>
                <option value="bass">Bass (Synth/Bass Guitar)</option>
                <option value="brass">Brass / Horns</option>
                <option value="woodwind">Woodwind / Flute</option>
                <option value="vocals">Vocals / Choir</option>
                <option value="hybrid">Hybrid / Mixed</option>
              </select>
            </div>
          </div>

          {/* Duration */}
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-2xl p-6">
            <label htmlFor="duration" className="block text-sm font-medium text-slate-300 mb-3">
              Duration
            </label>
            <select
              id="duration"
              name="duration"
              className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
            >
              <option value="short">Short (30-60 seconds)</option>
              <option value="medium">Medium (1-2 minutes)</option>
              <option value="long">Long (2-4 minutes)</option>
              <option value="extended">Extended (4+ minutes)</option>
            </select>
          </div>

          {/* Result Display */}
          {result && (
            <div className={`rounded-2xl p-6 ${result.success ? 'bg-cyan-900/30 border border-cyan-500/50' : 'bg-red-900/30 border border-red-500/50'}`}>
              {result.success ? (
                <div>
                  <h3 className="text-lg font-semibold text-cyan-400 mb-3">Generated Music Prompt</h3>
                  <pre className="text-slate-200 whitespace-pre-wrap font-mono text-sm">{result.prompt}</pre>
                </div>
              ) : (
                <p className="text-red-400">{result.error}</p>
              )}
            </div>
          )}

          {/* Submit Button */}
          <button
            type="submit"
            disabled={loading}
            className="w-full py-4 px-8 bg-gradient-to-r from-cyan-500 to-cyan-600 hover:from-cyan-400 hover:to-cyan-500 text-white font-semibold rounded-xl transition-all duration-200 shadow-lg shadow-cyan-500/25 hover:shadow-cyan-500/40 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? 'Composing...' : 'Compose Music Prompt'}
          </button>
        </form>
      </div>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-8">
        <div className="max-w-4xl mx-auto px-6 text-center text-slate-500 text-sm">
          <p>Powered by DeepSeek AI • Music Prompt Generator</p>
        </div>
      </footer>
    </main>
  );
}