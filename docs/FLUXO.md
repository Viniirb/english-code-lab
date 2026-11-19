# Fluxo de estudo

A issue #N é o módulo N-1 (#1 = módulo 00).

1. Abra a issue do módulo e leia as tarefas.
2. Leia `content/mNN/README.md` (instruções em inglês simples) e os materiais da pasta.
3. Crie a branch: `git switch -c modulo/NN-nome` (o prefixo `modulo/NN-` é obrigatório).
4. Escreva em `work/mNN/` (e `journal/`). Peça correção ao tutor, mas **você** edita.
5. Valide: `.venv/bin/python scripts/validate_module.py NN`. Repita até aparecer `✔ Module NN done.`
6. Commit **em inglês** (módulo 04 em diante, no padrão `type: subject`) e push.
7. Abra o PR para `main` com `Closes #N`. Escreva a descrição do PR em inglês.
8. Espere o check **Validate module** ficar verde. Faça o merge (squash). A issue fecha.

## O que o CI confere

| Verificação | O que bloqueia |
|-------------|----------------|
| Integridade | PR que modifica ou apaga arquivos fora de `work/`, `journal/` e `srs/` (gabaritos, scripts, testes, workflows). Arquivos novos são aceitos. |
| Validação do módulo | O mesmo `validate_module.py NN` que você roda local. |
| Autotestes | `pytest tests` (garante que os validadores funcionam). |

## Observações

- Repositório privado no plano gratuito não tem proteção de branch obrigatória: só faça merge com o check verde.
- O gabarito dos quizzes é guardado em hash (`quiz.keys`): impede espiar sem querer. A branch `reference` tem as respostas; não olhe.
- O CI instala `pyspellchecker` e roda em Linux. Se o validador passar local e falhar no CI (ou vice-versa), abra uma issue.
