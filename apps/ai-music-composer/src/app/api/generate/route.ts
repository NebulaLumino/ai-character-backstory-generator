import { NextRequest, NextResponse } from 'next/server';
import OpenAI from 'openai';

const deepseek = new OpenAI({
  apiKey: process.env.DEEPSEEK_API_KEY || '',
  baseURL: 'https://api.deepseek.com/v1',
});

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const description = formData.get('description') as string;
    const genre = formData.get('genre') as string;
    const mood = formData.get('mood') as string;
    const tempo = formData.get('tempo') as string;
    const key = formData.get('key') as string;
    const instruments = formData.get('instruments') as string;
    const duration = formData.get('duration') as string;

    const instrumentMap: Record<string, string> = {
      synth: 'synthesizers and electronic instruments',
      piano: 'piano and keyboard instruments',
      guitar: 'acoustic and electric guitars',
      strings: 'orchestral strings (violin, cello, etc.)',
      drums: 'drums and percussion',
      bass: 'bass (synth bass or bass guitar)',
      brass: 'brass instruments (horn, trumpet, etc.)',
      woodwind: 'woodwind instruments (flute, saxophone, etc.)',
      vocals: 'vocals and choir',
      hybrid: 'mixed/hybrid instrumentation',
    };

    const tempoMap: Record<string, string> = {
      slow: '60-80 BPM, slow and relaxed',
      moderate: '80-110 BPM, moderate pace',
      medium: '110-130 BPM, medium energy',
      fast: '130-160 BPM, fast and energetic',
      veryfast: '160+ BPM, very fast and intense',
    };

    const durationMap: Record<string, string> = {
      short: '30-60 seconds',
      medium: '1-2 minutes',
      long: '2-4 minutes',
      extended: '4+ minutes',
    };

    const systemPrompt = `You are a professional music composer and producer. Generate detailed, creative music prompts for AI music generation tools. Create prompts that are specific, evocative, and will yield high-quality results.`;

    const userPrompt = `Create a detailed music prompt based on the following parameters:

Description: ${description || 'Create an original composition'}

Genre: ${genre}
Mood: ${mood}
Tempo: ${tempoMap[tempo] || 'any tempo'}
Key: ${key === 'any' ? 'any musical key' : key.replace('-', ' ')}
Instruments: ${instrumentMap[instruments] || 'varied instruments'}
Duration: ${durationMap[duration] || 'medium length'}

Generate a detailed prompt that includes:
1. Musical structure and arrangement
2. Specific instrumentation details
3. Production style and sound design
4. Emotional arc and progression
5. Any specific techniques or effects

Return ONLY the prompt text, nothing else.`;

    const result = await deepseek.chat.completions.create({
      model: 'deepseek-chat',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      max_tokens: 800,
    });

    const prompt = result.choices?.[0]?.message?.content || 'Failed to generate prompt';

    return NextResponse.json({ success: true, prompt });
  } catch (error) {
    console.error('Error generating music prompt:', error);
    return NextResponse.json(
      { success: false, error: 'Failed to generate music prompt. Please try again.' },
      { status: 500 }
    );
  }
}