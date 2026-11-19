**Nível alvo (CEFR):** A2  
**Habilidades:** Leitura, escrita, código  
**Validação automática:** `python scripts/validate_module.py 05` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Traduzir um código legado em português para nomes, comentários e mensagens em inglês, mantendo o comportamento.

## Leia antes

- `content/m05/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m05/README.md`, `content/m05/legacy/pedidos.py` e `content/m05/test_orders.py`
- [ ] Criar `work/m05/orders.py` com nomes, comentários, docstrings e mensagens em inglês
- [ ] Rodar `python scripts/validate_module.py 05` (roda os testes e procura palavras em português)

## Critério de pronto

- [ ] `python scripts/validate_module.py 05` termina com "✔ Module 05 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Faça o mesmo em um arquivo real de um projeto seu e abra um PR de refatoração em inglês.

## Como entregar

```bash
git switch -c modulo/05-codigo-em-ingles
python scripts/validate_module.py 05
git push -u origin modulo/05-codigo-em-ingles
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
