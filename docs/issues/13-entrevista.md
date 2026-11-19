**Nível alvo (CEFR):** B1  
**Habilidades:** Escrita, fala  
**Validação automática:** `python scripts/validate_module.py 13` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Contar experiências reais com estrutura (Situation, Task, Action, Result).

## Leia antes

- `content/m13/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Ler `content/m13/README.md` e `content/m13/questions.md`
- [ ] Escrever `work/m13/answers.md`
- [ ] Rodar `python scripts/validate_module.py 13`
- [ ] Gravar áudio respondendo a cada pergunta em 90 segundos (opcional, mas recomendado)

## Critério de pronto

- [ ] `python scripts/validate_module.py 13` termina com "✔ Module 13 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Faça uma simulação de 15 minutos com um amigo ou com um assistente de voz de IA.

## Como entregar

```bash
git switch -c modulo/13-entrevista
python scripts/validate_module.py 13
git push -u origin modulo/13-entrevista
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
