**Nível alvo (CEFR):** B1  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 12` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Escrever um texto de 300 a 500 palavras com estrutura e um trecho de código.

## Leia antes

- `content/m12/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m12/README.md`
- [ ] Escrever `work/m12/article.md`
- [ ] Pedir ao tutor para marcar problemas SEM reescrever; corrigir você mesmo
- [ ] Rodar `python scripts/validate_module.py 12`

## Critério de pronto

- [ ] `python scripts/validate_module.py 12` termina com "✔ Module 12 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Publique o artigo (dev.to, blog ou GitHub Pages) depois da revisão.

## Como entregar

```bash
git switch -c modulo/12-artigo-tecnico
python scripts/validate_module.py 12
git push -u origin modulo/12-artigo-tecnico
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
