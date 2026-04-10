import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { productName, servingSize, calories, fat, carbs, protein, fiber, sugar, sodium } = await req.json();

    if (!productName) {
      return NextResponse.json({ error: "Product name is required" }, { status: 400 });
    }

    const { OpenAI } = await import("openai");
    const client = new OpenAI({
      baseURL: "https://api.deepseek.com/v1",
      apiKey: process.env.OPENAI_API_KEY,
    });

    const prompt = `You are a nutrition expert analyzing a food product label. Analyze the following nutrition information:

**Product:** ${productName}
**Serving Size:** ${servingSize || "Not specified"}
**Nutrition per serving:**
- Calories: ${calories || "N/A"}
- Total Fat: ${fat || "N/A"}g
- Total Carbohydrates: ${carbs || "N/A"}g
- Protein: ${protein || "N/A"}g
- Dietary Fiber: ${fiber || "N/A"}g
- Total Sugars: ${sugar || "N/A"}g
- Sodium: ${sodium || "N/A"}mg

Please provide:
1. **Overall Health Score** (1-10 with explanation)
2. **Macro Breakdown** - balance of carbs/fat/protein, whether it's high-protein, low-carb, etc.
3. **Key Concerns** - anything to watch out for (high sodium, added sugars, saturated fat, etc.)
4. **Key Positives** - good aspects of the nutritional profile
5. **Who Should Consider** - best suited for what type of diet or person (athletes, keto, low-sodium diets, etc.)
6. **Better Alternatives** - suggestions for healthier options in the same category
7. **FDA Label Reading Guide** - how to interpret the % Daily Value for each nutrient

Format clearly with markdown headings. Be direct and practical in your assessment.`;

    const completion = await client.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are a registered dietitian and nutrition expert. You analyze food labels with scientific precision and give practical, actionable advice. Be honest — don't hype products that don't deserve it, and don't unfairly criticize good products." },
        { role: "user", content: prompt },
      ],
      temperature: 0.5,
      max_tokens: 2000,
    });

    const output = completion.choices[0]?.message?.content || "No analysis generated.";
    return NextResponse.json({ output });
  } catch (error: unknown) {
    console.error("Analyze error:", error);
    const message = error instanceof Error ? error.message : "Analysis failed";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}