# Tutor de IA (Claude Code, ChatGPT, Codex, qualquer um)

Use um assistente de IA como **tutor**, não como escritor. O objetivo é que VOCÊ escreva.

## Prompt base (cole no início da conversa)

```text
You are my English tutor for software developers. My level is A2 (beginner) and my goal is B1.
Rules:
1. I will paste a short text that I wrote. Do NOT rewrite the whole text.
2. List my mistakes in a table: "my text" | "problem" | "better version" | "rule in simple English".
3. Explain each rule in very simple English, and add one short note in Portuguese (pt-BR) when the rule is hard.
4. Give me at most 5 mistakes per text. Choose the ones that are most important and most repeated.
5. After the table, ask me to rewrite ONE sentence, and wait for my answer.
6. Keep your sentences short. Use words from software development.
```

## Prompt para revisar commit, PR ou bug report

```text
Review this {commit message | pull request description | bug report} written by a developer with A2 English.
Check: clarity, grammar, tone, and whether a stranger can understand it. Follow the tutor rules above.
Do not change technical meaning.
```

## Prompt para conversa (fala/escrita)

```text
Act as a teammate in a daily stand-up. Ask me 3 short questions about my work yesterday and today.
Wait for each answer. After my answers, correct only the 3 most important mistakes.
```

## Usando um agente de código (Claude Code, Codex)

Abra o terminal no repositório e peça:

```text
Read work/m07/pr-1.md and act as my English tutor (rules in docs/TUTOR.md). Do NOT edit any file.
Show the 5 most important mistakes and explain them simply.
```

Regra de ouro: **o agente não edita seus arquivos de `work/`**. Você aplica as correções com as suas mãos.

## O que NÃO fazer

- Pedir "traduza e escreva isso por mim".
- Colar segredos, senhas, dados de clientes ou código confidencial da empresa.
- Aceitar uma correção sem entender a regra. Se não entendeu, pergunte "why?".
