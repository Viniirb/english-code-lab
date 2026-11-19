**Nível alvo (CEFR):** A2  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 02` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Perder o medo de mensagens de erro: entender o que acontece e dizer em inglês o que tentar.

## Leia antes

- `content/m02/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m02/errors.md`
- [ ] Fazer o quiz de `content/m02/quiz.md` em `work/m02/answers.txt`
- [ ] Escrever `work/m02/explanations.md` (um parágrafo por erro, 8+ palavras cada)
- [ ] Rodar `python scripts/validate_module.py 02`

## Critério de pronto

- [ ] `python scripts/validate_module.py 02` termina com "✔ Module 02 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Cole 3 erros reais que você viu no trabalho, explique cada um em inglês e como resolveu.

## Como entregar

```bash
git switch -c modulo/02-mensagens-de-erro
python scripts/validate_module.py 02
git push -u origin modulo/02-mensagens-de-erro
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
