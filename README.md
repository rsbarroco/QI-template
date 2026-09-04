# QI — Quality Intelligence

Scaffold an AI-assisted QA project in seconds.

QI generates a **Claude-first QA constitution** — CLAUDE.md, rules, skills, scripts, and
CI config — customized to your team's stack. The generated project is ready to use with
[Claude Code](https://claude.ai/code) from day one, with proven patterns for evidence-based
QA, assertion validity, coverage tracking, and AI-usage reporting.

## Install

```bash
pip install git+https://github.com/rodrigobarroco/QI
# or: pipx install git+https://github.com/rodrigobarroco/QI
```

## Usage

```bash
qi my-project-tests
```

QI asks 10 questions about your stack and generates a project directory with everything
configured for your choices.

```
$ qi acme-qa
  ╭────────────────────────────────────────╮
  │  QI — Quality Intelligence             │
  │  Scaffold an AI-assisted QA project.  │
  ╰────────────────────────────────────────╯

  Project name? Acme QA
  Task tracker? Jira
  Jira project key? ACME
  Documentation platform? Confluence
  SQL databases? PostgreSQL
  NoSQL databases? MongoDB
  UI surfaces? Web (browser)
  Test framework? Playwright
  Cloud provider? AWS
  Async queues? SQS
  CI/CD? GitHub Actions

  create  CLAUDE.md
  create  .claude/rules/assertion-validity.md
  create  .claude/skills/ticket-intake.md
  create  .claude/skills/sql-query.md
  create  .claude/skills/web-ui.md
  create  .claude/skills/queue-testing.md
  create  .github/workflows/tests.yml
  ... (24 files total)

  ╭──────────────────────────────────────────────────────╮
  │  Done! Project created at acme-qa/                  │
  │                                                      │
  │  Next steps:                                         │
  │    cd acme-qa                                        │
  │    git init                                          │
  │    # Open in Claude Code and read CLAUDE.md          │
  ╰──────────────────────────────────────────────────────╯
```

## What gets generated

### Always generated (every project)

| File | Purpose |
|---|---|
| `CLAUDE.md` | AI constitution — rules, constraints, workflow |
| `COVERAGE.md` | Coverage tracker template |
| `.claude/rules/assertion-validity.md` | 6 principles for valid QA assertions |
| `.claude/rules/evidence-based-qa.md` | What counts as evidence |
| `.claude/rules/environment-safety.md` | Dev/staging OK, prod never |
| `.claude/rules/connection-validation.md` | Pre-flight connector checklist |
| `.claude/rules/coverage-sync.md` | Keeping coverage numbers in sync |
| `.claude/rules/feedback-loop.md` | Post-session debrief process |
| `.claude/skills/ticket-intake.md` | 8-step QA intake workflow |
| `.claude/skills/verify-ticket.md` | Verification loop (RTM → evidence → transition) |
| `.claude/skills/gap-analysis.md` | Coverage gap analysis |
| `.claude/skills/sprint-report.md` | End-of-sprint AI-usage report |
| `.claude/skills/json-schema.md` | Payload validation + silent no-op detection |
| `scripts/qa_track.py` | AI-usage activity tracker |
| `scripts/coverage_report.py` | Recomputes COVERAGE.md from specs |
| `specs/README.md` | How to write domain specs |

### Generated conditionally (based on your stack)

| Condition | File |
|---|---|
| SQL database selected | `.claude/skills/sql-query.md` |
| NoSQL database selected | `.claude/skills/nosql-query.md` |
| Web UI selected | `.claude/skills/web-ui.md` |
| Mobile (iOS/Android) selected | `.claude/skills/mobile.md` |
| Cloud provider selected | `.claude/skills/cloud-logs.md` |
| Async queue selected | `.claude/skills/queue-testing.md` |
| GitHub Actions CI | `.github/workflows/tests.yml` |
| GitLab CI | `.gitlab-ci.yml` |

## Options

```
qi [OUTPUT_DIR] [--dry-run]

  OUTPUT_DIR    Where to create the project (default: ./<project-slug>)
  --dry-run     Print the file list without writing anything
```

## Design principles

- **Claude-first, declared** — designed for Claude Code; works with any AI that reads markdown
- **Framework-agnostic** — delivers process and AI prompts, not a test framework
- **Conditional output** — only the skills/rules relevant to your stack are generated
- **Proven patterns** — rules and skills derived from real QA work, not theory
- **Portable** — install from git anywhere; no registry account needed

## Development

```bash
git clone https://github.com/rodrigobarroco/QI
cd QI
pip install -e ".[dev]"
pytest tests/ -v
```

## License

MIT
