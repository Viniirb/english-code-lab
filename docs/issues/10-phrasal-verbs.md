**Nível alvo (CEFR):** B1  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 10` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Aprender os phrasal verbs mais usados em times de software.

## Leia antes

- `content/m10/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m10/README.md`
- [ ] Fazer o cloze em `work/m10/answers.txt`
- [ ] Escrever 8 frases em `work/m10/sentences.md`
- [ ] Rodar `python scripts/validate_module.py 10`

## Critério de pronto

- [ ] `python scripts/validate_module.py 10` termina com "✔ Module 10 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Crie cartões para 10 phrasal verbs que você achou em documentação real.

## Como entregar

```bash
git switch -c modulo/10-phrasal-verbs
python scripts/validate_module.py 10
git push -u origin modulo/10-phrasal-verbs
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
