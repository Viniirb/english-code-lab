**Nível alvo (CEFR):** A2  
**Habilidades:** Escrita  
**Validação automática:** `python scripts/validate_module.py 00` (o mesmo que o GitHub Actions roda no seu PR)

## Objetivo

Preparar o ambiente (Python, venv, validador) e escrever sua primeira apresentação em inglês.

## Leia antes

- `content/m00/README.md` (as instruções do módulo, em inglês simples: faz parte do treino)
- `docs/METODO.md` e, se travar, `docs/TUTOR.md`

## Tarefas

- [ ] Criar o venv e instalar: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
- [ ] Rodar `.venv/bin/python -m pytest tests` (os testes dos validadores devem passar)
- [ ] Ler `docs/METODO.md` e `docs/TUTOR.md`
- [ ] Escrever `work/m00/about-me.md` (40 a 150 palavras) seguindo `content/m00/README.md`
- [ ] Pedir ao tutor (IA) para corrigir o texto e anotar 3 erros que você cometeu
- [ ] Colocar o editor, o terminal e as mensagens do git em inglês (se ainda não estiverem)

## Critério de pronto

- [ ] `python scripts/validate_module.py 00` termina com "✔ Module 00 done."
- [ ] PR aberto com `Closes #<número desta issue>` e check **Validate module** verde
- [ ] Escrevi no PR, em inglês, 2 frases sobre o que foi difícil

## Desafio extra (opcional)

- Gravar 1 minuto lendo seu texto em voz alta e ouvir de volta.

## Como entregar

```bash
git switch -c modulo/00-setup
python scripts/validate_module.py 00
git push -u origin modulo/00-setup
# abra o PR para a main com Closes #N
```

> Só seus arquivos em `work/`, `journal/` e `srs/` podem ser alterados. O CI recusa mudanças em `content/`, `scripts/`, `tests/` e `.github/`.
