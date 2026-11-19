**Nível alvo (CEFR):** B1  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 08` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Entender os códigos do review (nit, LGTM, blocking) e escrever feedback gentil e específico.

## Leia antes

- `content/m08/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m08/README.md`
- [ ] Fazer o quiz em `work/m08/answers.txt`
- [ ] Escrever `work/m08/review.md` (5 comentários, um por trecho de código)
- [ ] Rodar `python scripts/validate_module.py 08`

## Critério de pronto

- [ ] `python scripts/validate_module.py 08` termina com "✔ Module 08 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Revise em inglês um PR real de um colega ou de um projeto aberto (comentando só se couber).

## Como entregar

```bash
git switch -c modulo/08-code-review
python scripts/validate_module.py 08
git push -u origin modulo/08-code-review
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
