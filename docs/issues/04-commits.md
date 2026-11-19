**Nível alvo (CEFR):** A2  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 04` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Escrever commits claros no imperativo, no estilo Conventional Commits.

## Leia antes

- `content/m04/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m04/README.md` e `content/m04/scenarios.md`
- [ ] Escrever 10 mensagens em `work/m04/commits.txt`
- [ ] Rodar `python scripts/validate_module.py 04`
- [ ] A partir de agora, escreva TODOS os seus commits deste repositório em inglês no mesmo padrão

## Critério de pronto

- [ ] `python scripts/validate_module.py 04` termina com "✔ Module 04 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Reescreva 10 commits antigos de um projeto seu (em um arquivo, sem reescrever o histórico).

## Como entregar

```bash
git switch -c modulo/04-commits
python scripts/validate_module.py 04
git push -u origin modulo/04-commits
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
