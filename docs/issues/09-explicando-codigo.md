**Nível alvo (CEFR):** B1  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 09` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Explicar o que uma função faz com frases curtas e conectores (first, then, because).

## Leia antes

- `content/m09/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m09/README.md` e `content/m09/functions.py`
- [ ] Escrever `work/m09/explanations.md`
- [ ] Rodar `python scripts/validate_module.py 09`

## Critério de pronto

- [ ] `python scripts/validate_module.py 09` termina com "✔ Module 09 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Explique em voz alta, em inglês, uma função sua (grave 1 minuto).

## Como entregar

```bash
git switch -c modulo/09-explicando-codigo
python scripts/validate_module.py 09
git push -u origin modulo/09-explicando-codigo
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
