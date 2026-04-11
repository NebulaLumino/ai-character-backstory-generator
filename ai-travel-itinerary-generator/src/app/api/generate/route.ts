import { NextResponse } from "next/server";
import OpenAI from "openai";

function getOpenAI() {
  return new OpenAI({
    baseURL: "https://api.deepseek.com/v1",
    apiKey: process.env.DEEPSEEK_API_KEY,
  });
}

const SYSTEM_PROMPT = `You are an expert travel planner and destination specialist. Generate a detailed travel itinerary based on the user's preferences.

Respond with ONLY valid JSON (no markdown formatting), in this exact structure:
{
  "overview": "2-3 sentence trip summary",
  "estimatedCost": "budget breakdown with approximate daily costs",
  "days": [
    {
      "day": "Day 1: [Theme or focus]",
      "activities": ["activity 1 with time blocks", "activity 2", "lunch suggestion", "dinner recommendation"]
    }
  ],
  "tips": ["practical tip 1", "tip 2", "local customs"]
}

Guidelines:
- Each day should have 3-4 activities with approximate timing
- Include specific restaurant/café recommendations where meals are suggested
- Factor in travel time between locations
- Consider the travel style (adventure, cultural, relaxation, etc.)
- Account for dietary restrictions
- Include local insights and hidden gems
- Make it practical and doable`;

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const {
      destination,
      travelDates,
      duration,
      travelers,
      budget,
      travelStyle,
      interests,
      dietaryRestrictions,
    } = body;

    if (!destination) {
      return NextResponse.json({ error: "Destination is required" }, { status: 400 });
    }

    const prompt = `Create a ${duration || "7"}-day travel itinerary for ${destination}.

${travelDates ? `Travel dates: ${travelDates}` : ""}
${travelers ? `Travelers: ${travelers}` : ""}
${budget ? `Budget level: ${budget}` : ""}
Travel style: ${travelStyle}
Interests: ${interests || "general sightseeing"}
Dietary restrictions: ${dietaryRestrictions || "none"}

Generate a comprehensive day-by-day itinerary.`;

    const openai = getOpenAI();
    const completion = await openai.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: SYSTEM_PROMPT },
        { role: "user", content: prompt },
      ],
      response_format: { type: "json_object" },
      temperature: 0.8,
    });

    const content = completion.choices[0]?.message?.content;
    if (!content) {
      return NextResponse.json({ error: "Failed to generate itinerary" }, { status: 500 });
    }

    let itinerary;
    try {
      itinerary = JSON.parse(content);
    } catch {
      return NextResponse.json({ error: "Invalid AI response format" }, { status: 500 });
    }

    return NextResponse.json({ itinerary });
  } catch (error) {
    console.error("Itinerary generation error:", error);
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Generation failed" },
      { status: 500 }
    );
  }
}