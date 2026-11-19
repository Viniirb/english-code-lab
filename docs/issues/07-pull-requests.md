**Nível alvo (CEFR):** B1  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 07` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Explicar mudanças para o revisor: o quê, por quê, como testar.

## Leia antes

- `content/m07/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m07/README.md`, `content/m07/scenarios.md` e `content/m07/TEMPLATE.md`
- [ ] Escrever `work/m07/pr-1.md` e `work/m07/pr-2.md`
- [ ] Rodar `python scripts/validate_module.py 07`
- [ ] Escrever o PR deste módulo em inglês, no mesmo formato

## Critério de pronto

- [ ] `python scripts/validate_module.py 07` termina com "✔ Module 07 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Reescreva a descrição de um PR real seu, em inglês.

## Como entregar

```bash
git switch -c modulo/07-pull-requests
python scripts/validate_module.py 07
git push -u origin modulo/07-pull-requests
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
