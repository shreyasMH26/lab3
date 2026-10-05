#!/usr/bin/env python3
"""
Lab 3 Creative Terminal Showcase: Git Stashing & Context Switching
Student: Shreyas M H
Experiment: Creating and Managing Branches (Stashing)
"""

import sys
import subprocess
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{MAGENTA}{BOLD}
  ____ ___ _____   _        _    ____     _____ 
 / ___|_ _|_   _| | |      / \\  | __ )   |___ / 
| |  _ | |  | |   | |     / _ \\ |  _ \\     |_ \\ 
| |_| || |  | |   | |___ / ___ \\| |_) |   ___) |
 \\____|___| |_|   |_____/_/   \\_\\____/   |____/ 
{RESET}{CYAN}>> Experiment 3: Git Stash & Frictionless Branch Switching <<{RESET}
"""

def show_stash_concept():
    print(f"\n{BOLD}{YELLOW}[*] Git Stashing Architecture (Temporary Clipboard):{RESET}")
    print(f"""{CYAN}
┌───────────────────────────────┐
│       Working Directory       │
│  (Dirty: unfinished.txt)     │
└───────────────┬───────────────┘
                │ git stash push -m "..."
                ▼
┌───────────────────────────────┐        ┌───────────────────────────────┐
│         Clean State           │        │         Stash Stack           │
│   (Ready to switch branch)    │        │  stash@{{0}}: "Working on..."   │
└───────────────┬───────────────┘        └───────────────┬───────────────┘
                │ git checkout bug-fix                   │
                ▼                                        │ git stash pop
┌───────────────────────────────┐                        ▼
│      bug-fix branch work      │──────────> ┌───────────────────────────┐
│     (Hotfix committed)        │            │  Restored Working State   │
└───────────────────────────────┘            └───────────────────────────┘
    {RESET}""")

def show_pop_vs_apply():
    print(f"{BOLD}{GREEN}[*] Core Tip from Manual — 'stash pop' vs 'stash apply':{RESET}")
    print(f"  • {BOLD}git stash pop{RESET}   : Restores modifications AND deletes the entry from stash history.")
    print(f"  • {BOLD}git stash apply{RESET} : Restores modifications BUT KEEPS the backup in the stash stack.\n")

def run_git_inspection():
    print(f"{BOLD}{MAGENTA}[*] Live Git Branch & Commit Status:{RESET}")
    try:
        branches = subprocess.check_output(["git", "branch", "-a"], text=True)
        print(f"{CYAN}Active Branches:\n{branches.strip()}{RESET}\n")
        
        log = subprocess.check_output(["git", "log", "--graph", "--oneline", "--all", "-n", "6"], text=True)
        print(f"{YELLOW}Commit History Across Branches:\n{log.strip()}{RESET}")
    except Exception as e:
        print(f"Git inspection error: {e}")

def run_quiz():
    print(f"\n{BOLD}{GREEN}--- Git Stash Knowledge Check (For Lab Evaluation) ---{RESET}")
    questions = [
        ("What command saves dirty uncommitted changes to temporary storage?", "git stash"),
        ("What command lists all existing stashes in the stash stack?", "git stash list"),
        ("Which stash restore command removes the stash after applying it?", "git stash pop")
    ]
    score = 0
    for q, ans in questions:
        print(f"\n{BOLD}Q: {q}{RESET}")
        user_ans = input(f"{YELLOW}Your Answer: {RESET}").strip()
        if ans.lower() in user_ans.lower():
            print(f"{GREEN}✓ Correct!{RESET}")
            score += 1
        else:
            print(f"\033[91m✗ Expected: {ans}{RESET}")
    print(f"\n{BOLD}{CYAN}Final Score: {score}/{len(questions)}{RESET}\n")

def main():
    print(BANNER)
    print(f"{GREEN}✓ Student: Shreyas M H (@shreyasMH26){RESET}")
    print(f"{GREEN}✓ Lab Activity: Experiment 3 (Stashing) Completed Successfully!{RESET}")
    show_stash_concept()
    show_pop_vs_apply()
    run_git_inspection()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--quiz":
        run_quiz()
    else:
        print(f"\n{BOLD}Tip:{RESET} Run {YELLOW}python3 stash_demo.py --quiz{RESET} for the interactive viva quiz!\n")

if __name__ == "__main__":
    main()
