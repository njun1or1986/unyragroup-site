# Deployment And Domains

## Projeto Vercel oficial

- Projeto oficial atual: `unyragroup-site`
- Vinculacao local atual: `.vercel/project.json`
- Dominio principal publicado: `https://www.unyragroup.com`

## Projeto Vercel secundario

- Projeto secundario/historico de apoio: `unyra-group-llc`
- URL util para comparacoes e fallback: `https://unyra-group-llc.vercel.app`

## Dominio com e sem www

- `https://www.unyragroup.com` serve o site oficial
- `https://unyragroup.com` funciona e redireciona para `https://www.unyragroup.com`

## Regra operacional

Para deploys futuros deste workspace:

1. confirmar que `.vercel/project.json` aponta para `unyragroup-site`
2. rodar `npm run build`
3. publicar com `vercel --prod`
4. testar:
   - `/en`
   - `/pt`
   - `/es`
   - `/api/contact`

## Variaveis criticas em producao

- `RESEND_API_KEY`
- `CONTACT_FORM_FROM`
- `CONTACT_FORM_TO`
- `CONTACT_SUBJECT_PREFIX`

Sem essas variaveis no projeto oficial, o formulario pode responder `ok` e cair em modo placeholder sem entregar email real.
