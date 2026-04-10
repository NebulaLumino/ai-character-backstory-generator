#!/usr/bin/env python3
tasks = {
    3240: ("AI Service Animal Task Trainer", "HIGH", "Generate training curricula for service animals based on handler disability needs and task requirements."),
    3241: ("AI Exotic Pet Species Care Guide", "MEDIUM", "Generate comprehensive care guides for exotic pets including reptiles, amphibians, and small mammals."),
    3242: ("AI Pet Birthday Party Planner", "MEDIUM", "Create pet birthday party plans including themes, decorations, games, and treat recipes."),
    3243: ("AI Horse Care & Riding Log", "MEDIUM", "Generate horse care routines and riding session logs with health tracking and training progress."),
    3244: ("AI Aquarium Setup & Fish Care", "MEDIUM", "Create aquarium setup guides with species compatibility, water chemistry, and maintenance schedules."),
    3245: ("AI Pet Travel Documents Generator", "MEDIUM", "Generate travel documentation for pets including health certificates, vaccination records, and import permits."),
    3246: ("AI Wildlife Camera Trap Analyzer", "MEDIUM", "Analyze wildlife camera trap images to identify species, count animals, and estimate population."),
    3247: ("AI Pet Product Review Summarizer", "MEDIUM", "Summarize and compare pet product reviews to help pet owners make informed purchasing decisions."),
    3248: ("AI Stray Animal Triage Prioritizer", "MEDIUM", "Generate triage priority scores for stray animals based on health, age, and adoptability factors."),
    3249: ("AI Pet Costume & Enrichment Ideas", "MEDIUM", "Generate creative pet costume ideas and environmental enrichment activities for mental stimulation."),
    3250: ("AI Dairy & Livestock Health Monitor", "MEDIUM", "Create livestock health monitoring plans with vaccination schedules, nutrition programs, and welfare checks."),
    3251: ("Explore AI Agents in Animal Cognition & Interspecies Communication AI", "LOW", "Research how AI agents are being used to decode animal communication, study cognition, and bridge interspecies understanding."),
    3252: ("Explore AI Agents in Veterinary Radiology & Diagnostic Imaging AI", "LOW", "Research AI in veterinary imaging: X-ray, MRI, CT interpretation, and diagnostic decision support for animals."),
    3253: ("Explore AI Agents in Animal Shelter Management & Adoption Prediction AI", "LOW", "Research AI in shelters: intake optimization, behavioral assessment, and matching algorithms to improve adoption rates."),
    3254: ("Explore AI Agents in Service Animal Training & Detection Dog AI", "LOW", "Research AI in training service animals: task optimization, health monitoring, and behavior analysis for detection dogs."),
    3255: ("Explore AI Agents in Wildlife Conservation & Poaching Detection AI", "LOW", "Research AI for conservation: species ID, anti-poaching sensors, habitat monitoring, and population estimation."),
    3256: ("Explore AI Agents in Animal Testing Alternatives & Ethical AI", "LOW", "Research AI alternatives to animal testing: organ-on-chip, in silico models, and ethical review automation."),
    3257: ("Explore AI Agents in Zoo Operations & Animal Welfare Monitoring AI", "LOW", "Research AI in zoos: welfare scoring, enclosure optimization, breeding programs, and visitor engagement."),
    3258: ("Explore AI Agents in Emotional Support Animals & Therapy Pets AI", "LOW", "Research AI in ESA/therapy animals: matching algorithms, handler training, and certification verification."),
    3259: ("Explore AI Agents in Livestock Facial Recognition & Herd Management AI", "LOW", "Research AI for livestock: individual animal ID, health monitoring, behavior tracking, and herd analytics."),
    3260: ("Explore AI Agents in Exotic Pet Trade Monitoring & Wildlife Trafficking AI", "LOW", "Research AI to detect illegal wildlife trade: species identification from images, supply chain monitoring, and enforcement support."),
}

for num, (name, pri, desc) in tasks.items():
    slug = name.lower().replace(" & ", "-").replace(" ", "-").replace("'", "").replace("(", "").replace(")", "").replace("ai-", "ai-").replace("--", "-")
    if slug.startswith("explore-ai-agents-in"):
        slug = slug.replace("explore-ai-agents-in-", "")
    slug = slug[:50]
    
    content = f"""# Task {num}: {name}

- **Task Number:** {num}
- **Status:** ⏳ Pending
- **Priority:** {pri}
- **Theme:** AI x Pets, Animals & Veterinary Care
- **Date Generated:** 2026-04-08

## Description
{desc}

## Technical Requirements
- Framework: Next.js 16 (App Router)
- Language: TypeScript
- Styling: Tailwind CSS with dark gradient background (from-gray-900 via-gray-950 to-gray-900)
- API: DeepSeek API via OpenAI SDK (baseURL: https://api.deepseek.com/v1, model: deepseek-chat)
- Pattern: Form input → /api/generate → DeepSeek API → Markdown output panel

## App Directory
`ai-{slug.replace("ai-", "")}`

## Accent Color
HSL hue: {((num - 3231) * 15) % 360}°
"""
    with open(f"/Users/nebulalumino/.openclaw/workspace/tasks/task-{num}.md", "w") as f:
        f.write(content)
    print(f"Created task-{num}.md: {name[:40]}")
