**Nível alvo (CEFR):** B1+  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 14` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Usar o inglês no mundo real: uma issue ou PR em projeto aberto e 14 dias de diário.

## Leia antes

- `content/m14/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m14/README.md`
- [ ] Abrir uma issue ou um PR pequeno, em inglês, em um projeto aberto que você usa
- [ ] Escrever `work/m14/evidence.md` (link + reflexão de 120+ palavras)
- [ ] Escrever `journal/AAAA-MM-DD.md` por 14 dias seguidos (25+ palavras cada)
- [ ] Rodar `python scripts/validate_module.py 14`

## Critério de pronto

- [ ] `python scripts/validate_module.py 14` termina com "✔ Module 14 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Responda a uma issue de outra pessoa em inglês.

## Como entregar

```bash
git switch -c modulo/14-capstone
python scripts/validate_module.py 14
git push -u origin modulo/14-capstone
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
