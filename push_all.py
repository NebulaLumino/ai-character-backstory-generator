#!/usr/bin/env python3
"""Re-push all 20 Cycle 110 apps to GitHub"""
import subprocess
from pathlib import Path

WORKSPACE = Path("/Users/nebulalumino/.openclaw/workspace")

APPS = [
    "ai-sermon-generator",
    "ai-scripture-commentary",
    "ai-meditation-guide-generator",
    "ai-interfaith-dialogue",
    "ai-spiritual-retreat-planner",
    "ai-buddhist-dharma-talk",
    "ai-jewish-halakha-responsa",
    "ai-islamic-fiqh-fatwa",
    "ai-hindu-puranic-story",
    "ai-interfaith-wedding-ceremony",
    "ai-prayer-request-tracker",
    "ai-chapel-wedding-planner",
    "ai-pilgrimage-itinerary",
    "ai-ritual-crafting-guide",
    "ai-faith-nonprofit-grant",
    "ai-spiritual-assessment",
    "ai-scripture-memory-tracker",
    "ai-faith-budget-planner",
    "ai-youth-group-activity",
    "ai-church-health-report",
]

def run(cmd, cwd=None):
    r = subprocess.run(cmd, shell=True, cwd=str(cwd or WORKSPACE),
                       capture_output=True, text=True, timeout=60)
    return r

for app in APPS:
    app_dir = WORKSPACE / app
    if not app_dir.exists():
        print(f"❌ {app}: directory missing!")
        continue
    
    # Check if .git exists
    has_git = (app_dir / ".git").exists()
    print(f"\n{'='*50}")
    print(f"App: {app} (has_git={has_git})")
    
    # Init git if missing
    if not has_git:
        r = run("git init", cwd=app_dir)
        print(f"  git init: {r.returncode}")
        r = run("git add -A", cwd=app_dir)
        print(f"  git add: {r.returncode}")
        r = run(f'git commit -m "{app}"', cwd=app_dir)
        print(f"  git commit: {r.returncode}")
        if r.returncode != 0:
            print(f"  COMMIT FAILED: {r.stderr[:200]}")
    
    # Try gh repo create
    r = run(f'gh repo create "{app}" --public --source=. --push 2>&1', cwd=app_dir)
    print(f"  gh repo create+push: {r.returncode}")
    if "already exists" in r.stdout or "already exists" in r.stderr:
        print("  Repo exists, pushing directly...")
        r = run(f'git remote add origin "https://github.com/NebulaLumino/{app}.git" 2>/dev/null || git remote set-url origin "https://github.com/NebulaLumino/{app}.git"', cwd=app_dir)
        r = run(f'git push -u origin main --force 2>&1', cwd=app_dir)
        print(f"  push: {r.returncode}")
        if r.returncode != 0:
            print(f"  PUSH FAILED: {r.stderr[:300]}")
        else:
            print(f"  ✓ Pushed {app}")
    elif r.returncode == 0:
        print(f"  ✓ Created and pushed {app}")
    else:
        print(f"  GH ERROR: {r.stderr[:200]}")
    
    # Also check if there's an existing remote
    r = run("git remote -v", cwd=app_dir)
    print(f"  remotes: {r.stdout.strip()}")

print("\nDone!")
