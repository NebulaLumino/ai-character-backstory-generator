#!/usr/bin/env python3
"""Update task files for Cycle 110 completion"""
import re
from pathlib import Path

WORKSPACE = Path("/Users/nebulalumino/.openclaw/workspace")
GITHUB_BASE = "https://github.com/NebulaLumino"

TASK_APPS = {
    3291: "ai-sermon-generator",
    3292: "ai-scripture-commentary",
    3293: "ai-meditation-guide-generator",
    3294: "ai-interfaith-dialogue",
    3295: "ai-spiritual-retreat-planner",
    3296: "ai-buddhist-dharma-talk",
    3297: "ai-jewish-halakha-responsa",
    3298: "ai-islamic-fiqh-fatwa",
    3299: "ai-hindu-puranic-story",
    3300: "ai-interfaith-wedding-ceremony",
    3301: "ai-prayer-request-tracker",
    3302: "ai-chapel-wedding-planner",
    3303: "ai-pilgrimage-itinerary",
    3304: "ai-ritual-crafting-guide",
    3305: "ai-faith-nonprofit-grant",
    3306: "ai-spiritual-assessment",
    3307: "ai-scripture-memory-tracker",
    3308: "ai-faith-budget-planner",
    3309: "ai-youth-group-activity",
    3310: "ai-church-health-report",
}

TASK_DOCS = {
    3311: "Faith-Based Crisis Counseling & Pastoral Care AI",
    3312: "Sacred Text Translation & Preservation AI",
    3313: "Interfaith Theological Debate AI",
    3314: "Pilgrimage Route Planning & Sacred Site AI",
    3315: "Funerary Rites AI",
    3316: "Religious Education Curriculum Generation AI",
    3317: "Sacred Music Composition & Hymn Generation AI",
    3318: "Sacred Architecture AI",
    3319: "Charitable Giving / Zakat Optimization AI",
    3320: "Religious Dietary Law Compliance AI (Kosher/Halal)",
}

def update_task_file(task_num, github_url=None):
    task_file = WORKSPACE / "tasks" / f"task-{task_num}.md"
    if not task_file.exists():
        print(f"  [MISSING] {task_file}")
        return False
    
    content = task_file.read_text()
    
    # Update status
    content = re.sub(r'\*\*Status:\*\*.*', f'**Status:** ✅ Complete', content)
    
    # Add GitHub URL if provided
    if github_url:
        if "**GitHub:**" in content:
            content = re.sub(r'\*\*GitHub:\*\*.*', f'**GitHub:** {github_url}', content)
        else:
            # Find the last line and append
            content = content.rstrip() + f"\n- **GitHub:** {github_url}\n"
    
    # Add completion entry
    if "**Completed:**" not in content:
        content = content.rstrip() + f"\n- **Completed:** 2026-04-11\n"
    
    task_file.write_text(content)
    return True

print("Updating HIGH priority app task files (3291-3300)...")
for task_num, app_name in TASK_APPS.items():
    url = f"{GITHUB_BASE}/{app_name}"
    result = update_task_file(task_num, url)
    if result:
        print(f"  ✅ {task_num}: {app_name}")

print("\nUpdating LOW priority doc task files (3311-3320)...")
for task_num, doc_title in TASK_DOCS.items():
    result = update_task_file(task_num)
    if result:
        print(f"  ✅ {task_num}: {doc_title}")

# Update TASKS.md
print("\nUpdating TASKS.md...")
tasks_md = WORKSPACE / "TASKS.md"
if tasks_md.exists():
    content = tasks_md.read_text()
    for task_num in list(TASK_APPS.keys()) + list(TASK_DOCS.keys()):
        # Mark as complete in TASKS.md
        pattern = rf'(\d{{4}})\.\s+\[([ x])\]'
        def replacer(m):
            num = int(m.group(1))
            if num == task_num:
                return m.group(1) + ". [x]"
            return m.group(0)
        content = re.sub(pattern, replacer, content)
    tasks_md.write_text(content)
    print("  ✅ TASKS.md updated")
else:
    print("  ⚠️ TASKS.md not found")

# Update HEARTBEAT.md
print("\nUpdating HEARTBEAT.md...")
heartbeat_md = WORKSPACE / "HEARTBEAT.md"
completion_entry = """## Cycle 110 Complete — 2026-04-11

### AI × Religion, Spirituality, Theology & Faith-Based Organizations

**HIGH Priority Apps (3291-3300):** ✅ All 10 apps built, deployed to GitHub
- 3291: ai-sermon-generator (Red)
- 3292: ai-scripture-commentary (Orange)
- 3293: ai-meditation-guide-generator (Yellow)
- 3294: ai-interfaith-dialogue (Lime)
- 3295: ai-spiritual-retreat-planner (Green)
- 3296: ai-buddhist-dharma-talk (Teal)
- 3297: ai-jewish-halakha-responsa (Cyan)
- 3298: ai-islamic-fiqh-fatwa (Blue)
- 3299: ai-hindu-puranic-story (Indigo)
- 3300: ai-interfaith-wedding-ceremony (Violet)

**MEDIUM Priority Apps (3301-3310):** ✅ All 10 apps built, deployed to GitHub
- 3301: ai-prayer-request-tracker (Pink)
- 3302: ai-chapel-wedding-planner (Rose)
- 3303: ai-pilgrimage-itinerary (Orange)
- 3304: ai-ritual-crafting-guide (Yellow)
- 3305: ai-faith-nonprofit-grant (Lime)
- 3306: ai-spiritual-assessment (Green)
- 3307: ai-scripture-memory-tracker (Cyan)
- 3308: ai-faith-budget-planner (Blue)
- 3309: ai-youth-group-activity (Indigo)
- 3310: ai-church-health-report (Violet)

**LOW Priority Docs (3311-3320):** ✅ All 10 curiosity docs written
- 3311: Faith-Based Crisis Counseling & Pastoral Care AI
- 3312: Sacred Text Translation & Preservation AI
- 3313: Interfaith Theological Debate AI
- 3314: Pilgrimage Route Planning & Sacred Site AI
- 3315: Funerary Rites AI
- 3316: Religious Education Curriculum Generation AI
- 3317: Sacred Music Composition & Hymn Generation AI
- 3318: Sacred Architecture AI
- 3319: Charitable Giving / Zakat Optimization AI
- 3320: Religious Dietary Law Compliance AI (Kosher/Halal)

**GitHub:** All 20 apps pushed to NebulaLumino GitHub org
"""
if heartbeat_md.exists():
    existing = heartbeat_md.read_text()
    heartbeat_md.write_text(existing + "\n" + completion_entry)
    print("  ✅ HEARTBEAT.md appended")
else:
    heartbeat_md.write_text(completion_entry)
    print("  ✅ HEARTBEAT.md created")

print("\n✅ All task files updated!")
