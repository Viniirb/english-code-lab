**Nível alvo (CEFR):** B1  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 11` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Relatar seu trabalho no passado, o plano no futuro e os bloqueios.

## Leia antes

- `content/m11/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m11/README.md` e `content/m11/TEMPLATE.md`
- [ ] Escrever 5 updates em `work/m11/updates.md`
- [ ] Rodar `python scripts/validate_module.py 11`

## Critério de pronto

- [ ] `python scripts/validate_module.py 11` termina com "✔ Module 11 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Escreva seu update real do dia em inglês por uma semana (mesmo que só para você).

## Como entregar

```bash
git switch -c modulo/11-updates-assincronos
python scripts/validate_module.py 11
git push -u origin modulo/11-updates-assincronos
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
