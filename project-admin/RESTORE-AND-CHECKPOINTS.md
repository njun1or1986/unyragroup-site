# Restore And Checkpoints

## Checkpoints historicos

- `project-admin/checkpoints/UNYRA-BASE-PADRAO.md`
- `project-admin/checkpoints/UNYRA-VERSAO-OFICIAL-DESKTOP-MOBILE.md`
- `project-admin/checkpoints/UNYRA-ANALYTICS-DEPLOY-READY.md`

## Checkpoint recomendado atual

- `project-admin/checkpoints/UNYRA-OFFICIAL-ORGANIZED-BASE-2026-05-09.md`
- `project-admin/checkpoints/UNYRA-LIVE-FORM-VALIDATED-2026-05-09.md`

## Scripts de restauracao

- `project-admin/scripts/restore-unyra-base-padrao.sh`
- `project-admin/scripts/restore-unyra-oficial-desktop-mobile.sh`
- `project-admin/scripts/restore-unyra-analytics-deploy-ready.sh`
- `project-admin/scripts/restore-unyra-live-form-validated.sh`
- `project-admin/scripts/restore-unyra-official-organized-base.sh`

## Snapshot recomendado atual

- `snapshots/unyra-official-organized-base-2026-05-09.tar.gz`
- `snapshots/unyra-live-form-validated-2026-05-09.tar.gz`

## Regra de uso

Antes de uma demanda mais sensivel ou experimental:

1. criar um novo snapshot se o ponto estiver muito valioso
2. trabalhar normalmente no codigo
3. se precisar voltar ao estado aprovado, usar o script correspondente

Todos os scripts criam backup automatico do estado atual antes da restauracao.
