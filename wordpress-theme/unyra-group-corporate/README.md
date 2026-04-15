# Unyra Group Corporate WordPress Theme

Tema WordPress premium e multilíngue baseado na versão oficial desktop/mobile do site da Unyra Group LLC.

## Instalação

1. Copie a pasta `unyra-group-corporate` para `wp-content/themes/`.
2. Ative o tema em `Appearance > Themes`.
3. Vá em `Settings > Reading` e defina uma página estática como Home, usando a página inicial do site.
4. Crie as páginas com os slugs esperados para o conteúdo institucional renderizar automaticamente.

## Slugs recomendados

### Inglês
- `about`
- `markets-global-network`
- `solutions`
- `for-buyers`
- `for-producers-exporters`
- `contact`
- `privacy-policy`
- `thank-you`

### Português
- `sobre`
- `mercados-rede-global`
- `solucoes`
- `para-compradores`
- `para-produtores-exportadores`
- `contato`
- `politica-de-privacidade`
- `obrigado`

### Español
- `nosotros`
- `mercados-red-global`
- `soluciones`
- `para-compradores`
- `para-productores-exportadores`
- `contacto`
- `politica-de-privacidad`
- `gracias`

## Idiomas

- O tema funciona sozinho com fallback por `?unyra_lang=en|pt|es`.
- Se quiser uma estrutura multilíngue mais robusta dentro do WordPress, instale o Polylang.

## Formulário

- O envio usa `wp_mail()`.
- Configure o envio de e-mail do WordPress com um plugin SMTP para produção.
- Os e-mails de destino ficam no Customizer:
  - `Appearance > Customize > Unyra Contact Details`

## Logo e contatos

Você pode alterar:
- logo pelo recurso padrão `Custom Logo`
- email, telefone, localização e tagline no Customizer

## Observação

Este tema foi pensado para manter o visual institucional premium da versão em Next.js, mas no formato nativo de WordPress, com instalação simples e sem depender de React/App Router.
