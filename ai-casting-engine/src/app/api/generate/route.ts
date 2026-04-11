import OpenAI from "openai";

export async function POST(req: Request) {
  const { prompt } = await req.json();
  const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY!,
    baseURL: "https://api.deepseek.com/v1",
  });
  const completion = await openai.chat.completions.create({
    model: "deepseek-chat",
    messages: [{ role: "user", content: prompt }],
    temperature: 0.7,
  });
  return Response.json({ result: completion.choices[0].message.content });
}
