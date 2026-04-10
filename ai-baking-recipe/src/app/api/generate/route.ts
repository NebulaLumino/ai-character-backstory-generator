import { NextRequest, NextResponse } from "next/server";
export async function POST(req: NextRequest) {
  try {
    const { bakedGood, skillLevel, dietaryRestrictions, equipment, servingSize, timeAvailable } = await req.json();
    if (!bakedGood) return NextResponse.json({ error: "Baked good is required" }, { status: 400 });
    const { OpenAI } = await import("openai");
    const client = new OpenAI({ baseURL: "https://api.deepseek.com/v1", apiKey: process.env.OPENAI_API_KEY });
    const prompt = `You are an expert pastry chef and baking instructor. Create a detailed baking recipe for: ${bakedGood}

Skill Level: ${skillLevel || "Intermediate"}
Dietary Restrictions: ${dietaryRestrictions || "None"}
Equipment Available: ${equipment || "Standard home oven and basic tools"}
Serving Size: ${servingSize || "8"}
Time Available: ${timeAvailable || "2-3 hours"}

Include:
1. Recipe name and brief description
2. Complete ingredient list with weights (in grams and cups)
3. Step-by-step instructions with baker's notes
4. Temperature and timing (with fan oven adjustments if relevant)
5. Common failure points and how to avoid them
6. Ingredient substitutions for dietary needs
7. Pro tips for best results
8. Storage instructions

Format with clear markdown headings. Be precise with measurements.`;
    const completion = await client.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are an expert pastry chef with deep knowledge of baking chemistry, technique, and equipment." },
        { role: "user", content: prompt },
      ],
      temperature: 0.8, max_tokens: 2000,
    });
    return NextResponse.json({ output: completion.choices[0]?.message?.content || "No recipe generated." });
  } catch (error: unknown) {
    return NextResponse.json({ error: error instanceof Error ? error.message : "Generation failed" }, { status: 500 });
  }
}