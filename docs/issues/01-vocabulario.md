**Nível alvo (CEFR):** A2  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 01` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Dominar as 40 palavras que aparecem em todo código e documentação.

## Leia antes

- `content/m01/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m01/README.md` e `content/m01/terms.md`
- [ ] Criar `work/m01/glossary.md` com pelo menos 25 palavras (significado em português + frase SUA em inglês)
- [ ] Treinar com `python scripts/srs.py review` por 5 dias seguidos
- [ ] Rodar `python scripts/validate_module.py 01`

## Critério de pronto

- [ ] `python scripts/validate_module.py 01` termina com "✔ Module 01 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Complete as 40 palavras. Escreva 3 frases que usem 2 palavras do glossário juntas.

## Como entregar

```bash
git switch -c modulo/01-vocabulario
python scripts/validate_module.py 01
git push -u origin modulo/01-vocabulario
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
