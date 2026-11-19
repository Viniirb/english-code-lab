# Método: 20 minutos por dia

Consistência vence intensidade. 20 minutos por dia ganham de 3 horas no domingo.

## Rotina diária

| Minutos | O quê | Como |
|---------|-------|------|
| 5 | Cartões | `python scripts/srs.py review` |
| 5 | Leitura real | Um README, uma issue ou um PR em inglês. Sublinhe só o que não entendeu |
| 8 | Escrita | O exercício do módulo atual, ou o diário (`journal/AAAA-MM-DD.md`) |
| 2 | Revisão | Cole seu texto no tutor (docs/TUTOR.md) e anote 1 erro novo |

## Regras que aceleram

1. **Leia antes de escrever.** Para escrever um commit ou um bug report, leia 5 exemplos bons de um projeto que você admira.
2. **Não traduza texto inteiro.** Leia a frase toda, adivinhe pelo contexto, só então consulte a palavra desconhecida.
3. **Escreva você primeiro, a IA corrige depois.** Se a IA escreve, você não aprende. Peça que ela **aponte** os erros, não que reescreva.
4. **Ponha seu ambiente em inglês**: editor, terminal, git, navegador de desenvolvimento. É exposição gratuita.
5. **Erros viram cartões.** Cada erro que o tutor apontar vira um cartão em `work/m01/glossary.md` ou uma linha em um arquivo `work/erros.md`.
6. **Fale em voz alta.** Leia seus textos em voz alta. Grave 1 minuto por semana e compare.
7. **Use inglês real no trabalho.** Commits, PRs e comentários de código novos já saem em inglês.

## Como ler documentação sem travar

1. Leia o título e os subtítulos primeiro (mapa).
2. Leia os exemplos de código: eles contam o que o texto explica.
3. Leia o texto em volta. Sublinhe no máximo 5 palavras desconhecidas por página.
4. Consulte só essas. Escreva a frase com suas palavras.

## Níveis (CEFR) em uma linha

- **A2**: entende frases simples e comuns, escreve mensagens curtas.
- **B1**: entende os pontos principais de textos técnicos claros, escreve textos simples e conectados.
- **B2**: lê textos técnicos complexos, escreve com precisão e tom adequado.

## Quando o validador reclama

O validador é uma heurística. Se você acha que o seu texto está correto e ele reclama:
1. Releia a mensagem: ela diz o que verificou.
2. Peça ao tutor uma segunda opinião.
3. Se for um termo técnico legítimo, ele pode entrar em `scripts/allowlist.txt` (via PR separado, fora de um módulo).
