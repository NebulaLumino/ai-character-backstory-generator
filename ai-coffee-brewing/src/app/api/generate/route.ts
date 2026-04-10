import { NextRequest, NextResponse } from "next/server";
export async function POST(req: NextRequest) {
  try {
    const { brewMethod, beanOrigin, roastLevel, strengthPreference, grindSize, waterQuality, cupCount } = await req.json();
    if (!brewMethod) return NextResponse.json({ error: "Brewing method is required" }, { status: 400 });
    const { OpenAI } = await import("openai");
    const client = new OpenAI({ baseURL: "https://api.deepseek.com/v1", apiKey: process.env.OPENAI_API_KEY });
    const prompt = `You are a specialty coffee expert and barista. Create a detailed brewing guide.

Method: ${brewMethod}
Bean Origin: ${beanOrigin || "Any origin"}
Roast Level: ${roastLevel || "Medium"}
Strength Preference: ${strengthPreference || "Medium"}
Grind Size Available: ${grindSize || "Medium"}
Water Quality: ${waterQuality || "Filtered tap water"}
Number of Cups: ${cupCount || "1-2 cups"}

Include:
1. Coffee-to-water ratio (grams of coffee per ml of water)
2. Optimal grind size for your method
3. Water temperature range
4. Total brew time and pour/steep sequence
5. Step-by-step technique (numbered steps)
6. Common mistakes to avoid
7. How to adjust for strength
8. Tips for your specific bean origin
9. Variations to try

Format with clear markdown and numbered steps. Be precise with measurements.`;
    const completion = await client.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are a specialty coffee expert with deep knowledge of extraction science, bean origins, roast profiles, and brewing techniques for all methods." },
        { role: "user", content: prompt },
      ],
      temperature: 0.7, max_tokens: 2000,
    });
    return NextResponse.json({ output: completion.choices[0]?.message?.content || "No guide generated." });
  } catch (error: unknown) {
    return NextResponse.json({ error: error instanceof Error ? error.message : "Generation failed" }, { status: 500 });
  }
}