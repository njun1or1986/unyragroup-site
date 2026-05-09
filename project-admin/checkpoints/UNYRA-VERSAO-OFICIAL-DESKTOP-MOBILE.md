# Unyra Versao Oficial Desktop e Mobile

Esta e a versao oficial aprovada do site da Unyra Group LLC no estado atual, com base validada para desktop, celular e tablet.

Status:
- Snapshot oficial principal salvo em `snapshots/unyra-oficial-desktop-mobile.tar.gz`
- Copia historica desta versao salva em `snapshots/unyra-oficial-desktop-mobile-2026-04-14-233500.tar.gz`
- Script de restauracao rapida em `./project-admin/scripts/restore-unyra-oficial-desktop-mobile.sh`

Projeto ativo:
- Pasta: `/Users/ninglobalservices/Documents/Unyra Group LLC`

Links locais:
- `http://localhost:3000`
- `http://localhost:3000/pt`
- `http://localhost:3000/en`
- `http://localhost:3000/es`

Como voltar exatamente para esta versao oficial:
1. Abra o terminal na pasta do projeto.
2. Rode `./project-admin/scripts/restore-unyra-oficial-desktop-mobile.sh`
3. Depois rode `npm run dev`

Observacoes:
- O script cria automaticamente um backup do estado atual antes de restaurar esta versao oficial.
- Assim voce pode testar novos ajustes sem perder este ponto aprovado.
- Esta versao fica preservada como referencia oficial de desktop e mobile.
