# Exam Agent Skills

This repository contains a reusable `skills/` folder for exam-solving and Python-to-LaTeX exam generation agents.

The expected project layout is:

```text
<project>/
  .agents/
    skills/
      python-latex-exam-master/
      python-latex-exam-ds-solver/
      python-latex-exam-gt-solver/
      python-latex-exam-hh-co-dien-solver/
      python-latex-exam-hh-gan-truc-solver/
      python-latex-exam-sp-xac-suat-co-dien-solver/
      python-latex-exam-sp-xac-suat-co-dieu-kien-solver/
```

## Fresh Setup

Start inside your project folder, for example `ThanhDanh`.

```powershell
cd <project>
```

Create a folder named `.agents` inside the project.

Clone this repository into `.agents`:

```powershell
cd .agents
git clone <repo-link> .
```

The final `.` means "clone the repository contents into the current `.agents` folder".

## Check The Install

Go back to the project folder:

```powershell
cd ..
```

Check that the skills exist:

```powershell
Get-ChildItem ".agents\skills"
```

You should see `python-latex-exam-master` plus the domain solver skills.

## Update Later

Run:

```powershell
cd <project>\.agents
git pull
```

## Before Using The Skills

Always start the agent from the project folder that contains `.agents`.

```powershell
cd <project>
```

For example:

```powershell
cd <path-to>\ThanhDanh
```

Then open or run your agent from that folder. If the agent starts from another directory, it may not discover `.agents/skills`.

## Usage Notes

- `python-latex-exam-master` contains shared LaTeX, style, randomization, validation, and house-style rules.
- The `*-solver` skills contain domain-specific solving strategies.
- For best results, provide the problem image, solution-reference image, question code, topic type, and expected output format.
