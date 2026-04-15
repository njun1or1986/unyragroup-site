# Unyra Base Padrao

Esta e a base padrao aprovada do site da Unyra Group LLC neste momento.

Status:
- Base ativa salva em `snapshots/unyra-base-padrao.tar.gz`
- Copia historica desta base salva em `snapshots/unyra-base-padrao-2026-04-14-215143.tar.gz`
- Script de restauracao rapida em `./restore-unyra-base-padrao.sh`

Projeto ativo:
- Pasta: `/Users/ninglobalservices/Documents/Unyra Group LLC`

Links locais:
- `http://localhost:3000`
- `http://localhost:3000/pt`
- `http://localhost:3000/en`
- `http://localhost:3000/es`

Como voltar exatamente para esta base:
1. Abra o terminal na pasta do projeto.
2. Rode `./restore-unyra-base-padrao.sh`
3. Depois rode `npm run dev`

Observacao:
- O script cria automaticamente um backup do estado atual antes de restaurar a base padrao.
- Assim voce pode sempre voltar para esta versao sem perder um trabalho mais recente.
