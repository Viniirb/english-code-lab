**Nível alvo (CEFR):** A2  
**Habilidades:** Leitura, escrita  
**Validação automática:** `python scripts/validate_module.py 03` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Ler um README completo sem traduzir tudo e resumir com suas palavras.

## Leia antes

- `content/m03/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m03/readme-sample.md` marcando palavras novas (traduza só essas)
- [ ] Fazer o quiz em `work/m03/answers.txt`
- [ ] Escrever `work/m03/summary.md` (25 a 70 palavras)
- [ ] Rodar `python scripts/validate_module.py 03`

## Critério de pronto

- [ ] `python scripts/validate_module.py 03` termina com "✔ Module 03 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Pegue o README de uma biblioteca que você usa e escreva um resumo de 5 linhas em inglês.

## Como entregar

```bash
git switch -c modulo/03-lendo-documentacao
python scripts/validate_module.py 03
git push -u origin modulo/03-lendo-documentacao
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
