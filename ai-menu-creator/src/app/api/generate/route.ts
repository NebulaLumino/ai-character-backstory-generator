import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { restaurantName, cuisine, priceRange, vibe, targetAudience } = body;

    if (!restaurantName || !cuisine) {
      return NextResponse.json({ error: "Restaurant name and cuisine type are required" }, { status: 400 });
    }

    const { OpenAI } = await import("openai");
    const client = new OpenAI({
      baseURL: "https://api.deepseek.com/v1",
      apiKey: process.env.OPENAI_API_KEY,
    });

    const prompt = `You are an expert restaurant consultant and menu designer. Create a professional, profit-optimized restaurant menu for the following establishment:

**Restaurant Name:** ${restaurantName}
**Cuisine Type:** ${cuisine}
**Price Range:** ${priceRange || "$$"}
**Vibe / Ambiance:** ${vibe || "Casual"}
**Target Audience:** ${targetAudience || "General public"}

Please provide a complete restaurant menu including:
1. Creative restaurant name and tagline
2. Menu categories (e.g., Starters, Mains, Desserts, Drinks)
3. Dish names and appetizing descriptions for each category
4. Strategic pricing aligned with the ${priceRange || "$$"} price point
5. Signature house dishes or specialty items
6. Pairing suggestions or chef's notes where appropriate

Format with clear headings, realistic prices, and evocative dish descriptions that drive appetite.`;

    const completion = await client.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are an expert restaurant consultant and menu designer with deep knowledge of culinary arts, food costing, and customer psychology." },
        { role: "user", content: prompt },
      ],
      temperature: 0.8,
      max_tokens: 2500,
    });

    const result = completion.choices[0]?.message?.content || "No menu generated.";

    return NextResponse.json({ result });
  } catch (error: unknown) {
    console.error("Generate error:", error);
    const message = error instanceof Error ? error.message : "Generation failed";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
