# english-code-lab

Aprenda inglês **usando o que você já faz todo dia: código**. Você lê documentação, mensagens de erro e code reviews reais,
e escreve commits, bug reports, PRs, artigos e respostas de entrevista. Cada módulo é uma **issue** e é validado
automaticamente por scripts e pelo GitHub Actions.

Ponto de partida: **A2** (lê documentação com ajuda). Meta do laboratório: **B1 sólido em escrita técnica e leitura**.

## Por que isso funciona

1. **Contexto que você já domina.** Você entende o código, então só o inglês é novo. Isso acelera a leitura.
2. **Escrita com feedback imediato.** Validadores checam idioma, ortografia, estrutura e legibilidade em segundos.
3. **Repetição espaçada.** Seu glossário vira cartões (`scripts/srs.py`), revistos em intervalos crescentes.
4. **Uso real.** O capstone é uma contribuição de verdade em um projeto aberto e 14 dias seguidos de diário.
5. **Hábito visível.** Seu histórico de commits e `journal/` mostram a sequência de dias.

Os validadores são **heurísticas**: pegam erros comuns, mas não provam que seu inglês é bom. Para feedback de verdade, use o
tutor de IA (`docs/TUTOR.md`) como parte do processo.

## Como funciona

- **15 módulos** (00 a 14), cada um uma **issue** (issue #N = módulo N-1).
- As instruções e os exercícios de cada módulo estão em `content/mNN/` (em inglês simples, de propósito: leitura é treino).
- Seu trabalho vai em `work/mNN/` e `journal/`. Mais nada pode ser alterado.
- Fluxo: branch `modulo/NN-nome`, valide com `python scripts/validate_module.py NN`, abra um PR com `Closes #N`.
- A solução de exemplo fica na branch `reference`. Consulte só depois de tentar.

Detalhes: [`docs/FLUXO.md`](docs/FLUXO.md), [`docs/METODO.md`](docs/METODO.md), [`docs/TUTOR.md`](docs/TUTOR.md).

## Trilha

| # | Módulo | CEFR | Habilidades |
|---|--------|------|-------------|
| 00 | Setup e método | A2 | Escrita |
| 01 | Vocabulário de desenvolvedor | A2 | Leitura, escrita |
| 02 | Lendo mensagens de erro | A2 | Leitura, escrita |
| 03 | Lendo documentação | A2 | Leitura, escrita |
| 04 | Mensagens de commit | A2 | Escrita |
| 05 | Nomes e comentários em inglês (código) | A2 | Leitura, escrita, código |
| 06 | Relatórios de bug | A2 | Escrita |
| 07 | Descrições de pull request | B1 | Escrita |
| 08 | Code review (leitura e escrita) | B1 | Leitura, escrita |
| 09 | Explicando código | B1 | Escrita |
| 10 | Phrasal verbs de tecnologia | B1 | Leitura, escrita |
| 11 | Updates assíncronos (stand-up escrito) | B1 | Escrita |
| 12 | Artigo técnico curto | B1 | Escrita |
| 13 | Entrevista: respostas STAR | B1 | Escrita, fala |
| 14 | Capstone: contribuição real + 14 dias | B1+ | Leitura, escrita |

## Comece aqui (10 min)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests               # testes dos validadores
.venv/bin/python scripts/validate_module.py 00 # deve falhar: falta seu texto
```

Depois abra a issue #1 (Módulo 00) e siga as tarefas.

## Comandos

```bash
.venv/bin/python scripts/validate_module.py 03   # valida um módulo
.venv/bin/python scripts/progress.py             # quadro de progresso
.venv/bin/python scripts/srs.py review           # cartões do dia (5 min)
.venv/bin/python scripts/srs.py stats
```
