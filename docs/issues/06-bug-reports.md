**Nível alvo (CEFR):** A2  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 06` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Escrever um bug report que um desconhecido consegue reproduzir em um minuto.

## Leia antes

- `content/m06/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m06/README.md`, `content/m06/scenarios.md` e `content/m06/TEMPLATE.md`
- [ ] Escrever `work/m06/bug-1.md`, `bug-2.md` e `bug-3.md`
- [ ] Rodar `python scripts/validate_module.py 06`

## Critério de pronto

- [ ] `python scripts/validate_module.py 06` termina com "✔ Module 06 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Troque seus reports com o tutor e peça para ele tentar "reproduzir" só lendo.

## Como entregar

```bash
git switch -c modulo/06-bug-reports
python scripts/validate_module.py 06
git push -u origin modulo/06-bug-reports
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
