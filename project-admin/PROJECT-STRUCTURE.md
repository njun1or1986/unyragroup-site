# Project Structure

## Aplicacao ativa

- `app/`: rotas, metadata, sitemap, robots e endpoint de formulario
- `components/`: UI reutilizavel, shell do site e formulario
- `lib/`: config da marca, SEO, dicionarios e helpers
- `messages/`: copys em ingles, portugues e espanhol
- `public/`: logo, imagens e assets publicos

## Operacao do projeto

- `project-admin/`: centro administrativo e de retomada
- `snapshots/`: checkpoints compactados
- `.vercel/project.json`: vinculacao local com o projeto Vercel oficial

## Camadas paralelas

- `design/`: materiais de design e derivados
  ver `design/README.md`
- `research/`: pesquisa de apoio
  ver `research/README.md`
- `wordpress-theme/`: tema WordPress convertido
  ver `wordpress-theme/README.md`
- `unyra-ops-system/`: sistema operacional/documental paralelo da marca

## Arquivo legado arquivado

O antigo site estatico de raiz foi movido para:

- `project-admin/archive/legacy-static-site/`

Arquivos vazios de placeholder da raiz foram movidos para:

- `project-admin/archive/root-placeholders/`

## Checkpoints

- `snapshots/`: historico compactado do projeto
  ver `snapshots/README.md`
