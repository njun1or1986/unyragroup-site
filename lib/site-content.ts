export type Locale = "en" | "pt" | "es";

export const defaultLocale: Locale = "en";

export const localeOptions = [
  { code: "en" as const, label: "English", shortLabel: "EN" },
  { code: "pt" as const, label: "Português", shortLabel: "PT" },
  { code: "es" as const, label: "Español", shortLabel: "ES" }
];

export const siteSettings = {
  name: "UNYRA GROUP LLC",
  url: "https://unyragroup.com",
  email: "sales@unyragroup.com",
  phoneDisplay: "+1 888 789 8843",
  phoneHref: "+18887898843",
  location: "Orlando, Florida, USA",
  seoTitle:
    "UNYRA GROUP LLC | Global Trade, Commodity Sourcing & Cross-Border Business Development",
  seoDescription:
    "UNYRA GROUP LLC is an international trading and business development company based in Orlando, Florida, focused on commodity trading, global sourcing, garlic supply chains, and strategic cross-border execution."
};

type NavItem = {
  label: string;
  href: string;
};

type HeroStat = {
  value: string;
  label: string;
};

type InfoItem = {
  title: string;
  description: string;
};

type ServiceItem = {
  id: "sourcing" | "expansion" | "execution" | "coordination" | "partnerships";
  title: string;
  description: string;
};

type MapPoint = {
  id: string;
  label: string;
  x: number;
  y: number;
  kind: string;
};

type MapCard = {
  eyebrow: string;
  title: string;
  description: string;
};

type FaqItem = {
  question: string;
  answer: string;
};

type FormCopy = {
  labels: {
    name: string;
    company: string;
    email: string;
    message: string;
  };
  placeholders: {
    name: string;
    company: string;
    email: string;
    message: string;
  };
  submitLabel: string;
  disclaimer: string;
  successMessage: string;
  fallbackMessage: string;
};

type SiteCopy = {
  locationDisplay: string;
  header: {
    nav: NavItem[];
    cta: string;
    languageLabel: string;
    openMenu: string;
    closeMenu: string;
  };
  hero: {
    eyebrow: string;
    title: string;
    description: string;
    primaryCta: string;
    secondaryCta: string;
    trustLine: string;
    highlights: string[];
    stats: HeroStat[];
    visualTag: string;
    visualTitle: string;
    visualDescription: string;
  };
  about: {
    eyebrow: string;
    title: string;
    description: string;
    paragraphs: string[];
    markers: InfoItem[];
  };
  services: {
    eyebrow: string;
    title: string;
    description: string;
    items: ServiceItem[];
  };
  global: {
    eyebrow: string;
    title: string;
    description: string;
    metrics: HeroStat[];
    points: MapPoint[];
    cards: MapCard[];
  };
  products: {
    eyebrow: string;
    title: string;
    description: string;
    items: InfoItem[];
  };
  why: {
    eyebrow: string;
    title: string;
    description: string;
    items: InfoItem[];
  };
  contact: {
    eyebrow: string;
    title: string;
    description: string;
    trustPoints: string[];
    form: FormCopy;
  };
  footer: {
    description: string;
    legal: string;
    languageLabel: string;
  };
  faq: {
    items: FaqItem[];
  };
};

export const siteContent: Record<Locale, SiteCopy> = {
  en: {
    locationDisplay: "Orlando, Florida, USA",
    header: {
      nav: [
        { label: "About", href: "#about" },
        { label: "Services", href: "#services" },
        { label: "Global Presence", href: "#global-presence" },
        { label: "Products", href: "#products" },
        { label: "Why UNYRA", href: "#why-unyra" },
        { label: "Contact", href: "#contact" }
      ],
      cta: "Start a Partnership",
      languageLabel: "Language selector",
      openMenu: "Open navigation",
      closeMenu: "Close navigation"
    },
    hero: {
      eyebrow: "Orlando, Florida, USA | Global Trade | Commodity Sourcing | Cross-Border Execution",
      title: "Global Trade. Real Execution.",
      description:
        "Connecting suppliers and buyers across international markets with precision, trust, and strategic execution.",
      primaryCta: "Start a Partnership",
      secondaryCta: "Contact Us",
      trustLine:
        "Designed to inspire confidence with banks, global suppliers, large buyers, and strategic trade partners.",
      highlights: [
        "Institutional credibility",
        "Commodity expertise",
        "International execution"
      ],
      stats: [
        { value: "USA", label: "Headquartered in Orlando, Florida" },
        { value: "6 hubs", label: "Active sourcing and trade corridors" },
        { value: "3 languages", label: "English, Portuguese, and Spanish" }
      ],
      visualTag: "Strategic Global Operator",
      visualTitle: "An international bridge between supply, demand, and market expansion.",
      visualDescription:
        "UNYRA operates with the discipline of a strategic trading partner, aligning sourcing, execution, and long-term commercial relationships across borders."
    },
    about: {
      eyebrow: "About UNYRA",
      title: "A global trading and business development company built for serious counterparties.",
      description:
        "UNYRA GROUP LLC is based in Orlando, Florida and works internationally across commodity trading, global sourcing, and cross-border business development.",
      paragraphs: [
        "We connect reliable suppliers and qualified buyers with a focus on commercial clarity, disciplined execution, and long-term value creation.",
        "Our team combines market access, sourcing intelligence, and practical transaction support to move opportunities from initial conversation to dependable commercial flow.",
        "UNYRA brings strong expertise in agricultural products, especially garlic supply chains spanning the United States, Brazil, Argentina, China, Europe, and the Middle East."
      ],
      markers: [
        {
          title: "US-based, globally active",
          description:
            "We operate from Orlando with an international mandate and a cross-border commercial network."
        },
        {
          title: "Trade-first mindset",
          description:
            "We are positioned as an execution-focused partner, not a passive intermediary."
        },
        {
          title: "Agricultural depth",
          description:
            "Garlic and agricultural sourcing remain a core area of specialist experience."
        }
      ]
    },
    services: {
      eyebrow: "Core Services",
      title: "Five premium capabilities for international growth and trade execution.",
      description:
        "Each mandate is approached with commercial discipline, strategic thinking, and operational follow-through.",
      items: [
        {
          id: "sourcing",
          title: "Global Sourcing",
          description:
            "Identifying reliable supply partners across strategic origins with quality, timing, and pricing discipline."
        },
        {
          id: "expansion",
          title: "Market Expansion",
          description:
            "Opening qualified cross-border opportunities for companies seeking credible international growth."
        },
        {
          id: "execution",
          title: "Trade Execution",
          description:
            "Supporting the commercial process from negotiation alignment to practical transaction momentum."
        },
        {
          id: "coordination",
          title: "Supply Chain Coordination",
          description:
            "Helping counterparties stay aligned across sourcing, logistics, documentation, and delivery expectations."
        },
        {
          id: "partnerships",
          title: "Strategic Partnerships",
          description:
            "Building long-term relationships between serious buyers, suppliers, and global business operators."
        }
      ]
    },
    global: {
      eyebrow: "Global Presence",
      title: "Positioned across the corridors that shape agricultural trade.",
      description:
        "UNYRA is connected to sourcing, distribution, and strategic trade routes spanning the Americas, Europe, China, and the Middle East.",
      metrics: [
        { value: "6 regions", label: "sourcing and distribution touchpoints" },
        { value: "Agricultural", label: "product expertise with garlic at the core" },
        { value: "Cross-border", label: "trade and business development execution" }
      ],
      points: [
        { id: "usa", label: "USA", x: 20, y: 39, kind: "Distribution" },
        { id: "brazil", label: "Brazil", x: 31, y: 69, kind: "Sourcing" },
        { id: "argentina", label: "Argentina", x: 28, y: 82, kind: "Sourcing" },
        { id: "europe", label: "Europe", x: 51, y: 29, kind: "Distribution" },
        { id: "middle-east", label: "Middle East", x: 61, y: 40, kind: "Trade Route" },
        { id: "china", label: "China", x: 77, y: 36, kind: "Sourcing" }
      ],
      cards: [
        {
          eyebrow: "Sourcing Network",
          title: "Agricultural procurement across primary origin markets",
          description:
            "Structured around trusted supply relationships and product-driven market intelligence."
        },
        {
          eyebrow: "Distribution Reach",
          title: "Commercial flow connecting origin and demand centers",
          description:
            "Designed to support serious buyers, importers, and strategic counterparties."
        },
        {
          eyebrow: "Trade Routes",
          title: "Cross-border execution with commercial visibility",
          description:
            "Clear coordination across markets, expectations, and operational timing."
        }
      ]
    },
    products: {
      eyebrow: "Industries & Products",
      title: "Focused where quality, continuity, and market knowledge matter.",
      description:
        "UNYRA combines commercial positioning with hands-on awareness of agricultural supply realities.",
      items: [
        {
          title: "Fresh Produce",
          description:
            "Supply relationships aligned with timing, quality, and dependable commercial continuity."
        },
        {
          title: "Garlic Supply Chains",
          description:
            "Deep familiarity with international garlic flows, sourcing dynamics, and buyer requirements."
        },
        {
          title: "Agricultural Commodities",
          description:
            "Strategic support for agricultural products where market execution and trust are decisive."
        },
        {
          title: "Global Food Distribution",
          description:
            "Cross-border coordination for product movement, counterpart alignment, and long-term supply development."
        }
      ]
    },
    why: {
      eyebrow: "Why UNYRA",
      title: "Built to reduce friction, strengthen confidence, and move business forward.",
      description:
        "Our value is not only in introductions. It is in how we align market intelligence, execution discipline, and relationship quality.",
      items: [
        {
          title: "Global Network",
          description:
            "Relationships across multiple regions create access to qualified supply and demand conversations."
        },
        {
          title: "Reliable Execution",
          description:
            "We prioritize disciplined follow-through, responsiveness, and commercial clarity."
        },
        {
          title: "Market Intelligence",
          description:
            "Category knowledge and international perspective support better decision-making."
        },
        {
          title: "Long-Term Partnerships",
          description:
            "We focus on counterparties seeking durable alignment rather than isolated transactions."
        },
        {
          title: "Operational Efficiency",
          description:
            "A lean, structured approach helps opportunities advance with less noise and stronger coordination."
        }
      ]
    },
    contact: {
      eyebrow: "Contact",
      title: "Start a high-value conversation with UNYRA.",
      description:
        "Share your sourcing need, supply offer, or expansion objective. We review inbound opportunities with discretion and commercial seriousness.",
      trustPoints: [
        "Institutional positioning for banks, suppliers, and global counterparties",
        "Multilingual communication in English, Portuguese, and Spanish",
        "Based in Orlando, Florida with international commercial reach"
      ],
      form: {
        labels: {
          name: "Name",
          company: "Company",
          email: "Email",
          message: "Message"
        },
        placeholders: {
          name: "Your name",
          company: "Company name",
          email: "name@company.com",
          message: "Tell us about your sourcing, buying, supply, or market expansion objective."
        },
        submitLabel: "Contact UNYRA",
        disclaimer:
          "By submitting this form, you agree to be contacted by UNYRA GROUP LLC regarding your inquiry.",
        successMessage:
          "Your email draft is ready. If no email window opens, contact us directly at sales@unyragroup.com.",
        fallbackMessage:
          "This form currently opens a prefilled email so your inquiry reaches UNYRA immediately."
      }
    },
    footer: {
      description:
        "UNYRA GROUP LLC is a global trading and business development company connecting suppliers and buyers through sourcing intelligence, disciplined execution, and long-term partnership thinking.",
      legal: "UNYRA GROUP LLC. All rights reserved.",
      languageLabel: "Languages"
    },
    faq: {
      items: [
        {
          question: "What does UNYRA GROUP LLC do?",
          answer:
            "UNYRA GROUP LLC operates in commodity trading, global sourcing, and cross-border business development, connecting suppliers and buyers across international markets."
        },
        {
          question: "Where is UNYRA GROUP LLC based?",
          answer:
            "UNYRA GROUP LLC is based in Orlando, Florida, USA, and operates internationally."
        },
        {
          question: "Which products are part of UNYRA's expertise?",
          answer:
            "UNYRA has strong experience in garlic supply chains, fresh produce, agricultural commodities, and global food distribution."
        },
        {
          question: "Which regions does UNYRA work with?",
          answer:
            "UNYRA is active across the USA, Brazil, Argentina, China, Europe, and the Middle East."
        },
        {
          question: "How can I contact UNYRA?",
          answer:
            "You can reach UNYRA by email at sales@unyragroup.com, by phone at +1 888 789 8843, or through the website contact form."
        }
      ]
    }
  },
  pt: {
    locationDisplay: "Orlando, Flórida, EUA",
    header: {
      nav: [
        { label: "Sobre", href: "#about" },
        { label: "Serviços", href: "#services" },
        { label: "Presença Global", href: "#global-presence" },
        { label: "Produtos", href: "#products" },
        { label: "Por que UNYRA", href: "#why-unyra" },
        { label: "Contato", href: "#contact" }
      ],
      cta: "Iniciar Parceria",
      languageLabel: "Seletor de idioma",
      openMenu: "Abrir navegação",
      closeMenu: "Fechar navegação"
    },
    hero: {
      eyebrow: "Orlando, Flórida, EUA | Comércio Global | Abastecimento de Commodities | Execução Internacional",
      title: "Comércio Global. Execução Real.",
      description:
        "Conectando fornecedores e compradores em mercados internacionais com precisão, confiança e execução estratégica.",
      primaryCta: "Iniciar Parceria",
      secondaryCta: "Fale Conosco",
      trustLine:
        "Desenvolvido para transmitir confiança a bancos, fornecedores globais, grandes compradores e parceiros estratégicos.",
      highlights: [
        "Credibilidade institucional",
        "Especialização em commodities",
        "Execução internacional"
      ],
      stats: [
        { value: "EUA", label: "Base em Orlando, Flórida" },
        { value: "6 polos", label: "Corredores ativos de abastecimento e comércio" },
        { value: "3 idiomas", label: "Inglês, português e espanhol" }
      ],
      visualTag: "Operação Estratégica Global",
      visualTitle: "Uma ponte internacional entre oferta, demanda e expansão de mercado.",
      visualDescription:
        "A UNYRA atua com a disciplina de uma parceira estratégica de comércio internacional, alinhando abastecimento, execução e relacionamentos comerciais de longo prazo entre diferentes mercados."
    },
    about: {
      eyebrow: "Sobre a UNYRA",
      title: "Uma empresa global de comércio e desenvolvimento de negócios construída para contrapartes sérias.",
      description:
        "A UNYRA GROUP LLC está baseada em Orlando, Flórida, e atua internacionalmente em comércio de commodities, abastecimento global e desenvolvimento de negócios entre fronteiras.",
      paragraphs: [
        "Conectamos fornecedores confiáveis e compradores qualificados com foco em clareza comercial, execução disciplinada e geração de valor no longo prazo.",
        "Nossa atuação combina acesso a mercado, inteligência de abastecimento e suporte prático à transação para transformar conversas em fluxo comercial consistente.",
        "A UNYRA possui forte experiência em produtos agrícolas, especialmente nas cadeias globais de alho entre Estados Unidos, Brasil, Argentina, China, Europa e Oriente Médio."
      ],
      markers: [
        {
          title: "Base nos EUA, operação global",
          description:
            "Atuamos a partir de Orlando com mandato internacional e rede comercial transfronteiriça."
        },
        {
          title: "Mentalidade orientada a comércio",
          description:
            "Nos posicionamos como parceiro focado em execução, não como intermediário passivo."
        },
        {
          title: "Profundidade agrícola",
          description:
            "Alho e abastecimento agrícola seguem como área central de especialização."
        }
      ]
    },
    services: {
      eyebrow: "Serviços Principais",
      title: "Cinco capacidades premium para crescimento internacional e execução comercial.",
      description:
        "Cada mandato é conduzido com disciplina comercial, visão estratégica e acompanhamento operacional.",
      items: [
        {
          id: "sourcing",
          title: "Abastecimento Global",
          description:
            "Identificação de parceiros de fornecimento confiáveis em origens estratégicas com disciplina de qualidade, prazo e preço."
        },
        {
          id: "expansion",
          title: "Expansão de Mercado",
          description:
            "Abertura de oportunidades transfronteiriças qualificadas para empresas que buscam crescimento internacional com credibilidade."
        },
        {
          id: "execution",
          title: "Execução Comercial",
          description:
            "Apoio ao processo comercial desde o alinhamento da negociação até o avanço prático da transação."
        },
        {
          id: "coordination",
          title: "Coordenação da Cadeia de Suprimentos",
          description:
            "Alinhamento entre as partes em abastecimento, logística, documentação e expectativas de entrega."
        },
        {
          id: "partnerships",
          title: "Parcerias Estratégicas",
          description:
            "Construção de relacionamentos de longo prazo entre compradores sérios, fornecedores e operadores globais."
        }
      ]
    },
    global: {
      eyebrow: "Presença Global",
      title: "Posicionada nos corredores que moldam o comércio agrícola.",
      description:
        "A UNYRA está conectada a abastecimento, distribuição e rotas estratégicas de comércio entre Américas, Europa, China e Oriente Médio.",
      metrics: [
        { value: "6 regiões", label: "pontos de abastecimento e distribuição" },
        { value: "Agrícola", label: "expertise com alho no centro da operação" },
        { value: "Entre fronteiras", label: "execução em comércio e desenvolvimento de negócios" }
      ],
      points: [
        { id: "usa", label: "EUA", x: 20, y: 39, kind: "Distribuição" },
        { id: "brazil", label: "Brasil", x: 31, y: 69, kind: "Origem" },
        { id: "argentina", label: "Argentina", x: 28, y: 82, kind: "Origem" },
        { id: "europe", label: "Europa", x: 51, y: 29, kind: "Distribuição" },
        { id: "middle-east", label: "Oriente Médio", x: 61, y: 40, kind: "Rota Comercial" },
        { id: "china", label: "China", x: 77, y: 36, kind: "Origem" }
      ],
      cards: [
        {
          eyebrow: "Rede de Abastecimento",
          title: "Aquisição agrícola em mercados de origem estratégicos",
          description:
            "Estruturada sobre relações confiáveis de fornecimento e inteligência comercial orientada ao produto."
        },
        {
          eyebrow: "Alcance de Distribuição",
          title: "Fluxo comercial conectando origem e centros de demanda",
          description:
            "Desenhado para atender compradores sérios, importadores e contrapartes estratégicas."
        },
        {
          eyebrow: "Rotas Comerciais",
          title: "Execução internacional com visibilidade comercial",
          description:
            "Coordenação clara entre mercados, expectativas e ritmo operacional."
        }
      ]
    },
    products: {
      eyebrow: "Indústrias e Produtos",
      title: "Foco onde qualidade, continuidade e conhecimento de mercado fazem diferença.",
      description:
        "A UNYRA combina posicionamento comercial com visão prática sobre a realidade das cadeias agrícolas.",
      items: [
        {
          title: "Produtos Frescos",
          description:
            "Relações de fornecimento alinhadas com prazo, qualidade e continuidade comercial confiável."
        },
        {
          title: "Cadeias Globais de Alho",
          description:
            "Conhecimento profundo dos fluxos internacionais de alho, dinâmica de abastecimento e exigências de compradores."
        },
        {
          title: "Commodities Agrícolas",
          description:
            "Suporte estratégico para produtos agrícolas em que execução e confiança são decisivas."
        },
        {
          title: "Distribuição Global de Alimentos",
          description:
            "Coordenação transfronteiriça para movimentação de produtos, alinhamento entre contrapartes e desenvolvimento de fornecimento no longo prazo."
        }
      ]
    },
    why: {
      eyebrow: "Por que UNYRA",
      title: "Construída para reduzir atrito, reforçar confiança e fazer os negócios avançarem.",
      description:
        "Nosso valor não está apenas na conexão entre partes. Está em alinhar inteligência de mercado, disciplina de execução e qualidade relacional.",
      items: [
        {
          title: "Rede Global",
          description:
            "Relacionamentos em múltiplas regiões criam acesso a conversas qualificadas entre oferta e demanda."
        },
        {
          title: "Execução Confiável",
          description:
            "Priorizamos acompanhamento disciplinado, resposta ágil e clareza comercial."
        },
        {
          title: "Inteligência de Mercado",
          description:
            "Conhecimento de categoria e perspectiva internacional apoiam decisões mais sólidas."
        },
        {
          title: "Parcerias de Longo Prazo",
          description:
            "Focamos em contrapartes que buscam alinhamento duradouro, não transações isoladas."
        },
        {
          title: "Eficiência Operacional",
          description:
            "Uma estrutura enxuta e organizada ajuda as oportunidades a avançarem com menos ruído e melhor coordenação."
        }
      ]
    },
    contact: {
      eyebrow: "Contato",
      title: "Inicie uma conversa de alto valor com a UNYRA.",
      description:
        "Compartilhe sua necessidade de abastecimento, oferta de fornecimento ou objetivo de expansão. Avaliamos oportunidades com discrição e seriedade comercial.",
      trustPoints: [
        "Posicionamento institucional para bancos, fornecedores e contrapartes globais",
        "Comunicação multilíngue em inglês, português e espanhol",
        "Base em Orlando, Flórida, com alcance comercial internacional"
      ],
      form: {
        labels: {
          name: "Nome",
          company: "Empresa",
          email: "E-mail",
          message: "Mensagem"
        },
        placeholders: {
          name: "Seu nome",
          company: "Nome da empresa",
          email: "nome@empresa.com",
          message: "Conte sua necessidade de abastecimento, compra, fornecimento ou expansão de mercado."
        },
        submitLabel: "Falar com a UNYRA",
        disclaimer:
          "Ao enviar este formulário, você concorda em ser contatado pela UNYRA GROUP LLC sobre sua solicitação.",
        successMessage:
          "Seu rascunho de e-mail está pronto. Se nenhuma janela abrir, escreva diretamente para sales@unyragroup.com.",
        fallbackMessage:
          "No momento, este formulário abre um e-mail preenchido para que sua mensagem chegue imediatamente à UNYRA."
      }
    },
    footer: {
      description:
        "A UNYRA GROUP LLC é uma empresa global de comércio e desenvolvimento de negócios que conecta fornecedores e compradores por meio de inteligência de abastecimento, execução disciplinada e visão de parceria no longo prazo.",
      legal: "UNYRA GROUP LLC. Todos os direitos reservados.",
      languageLabel: "Idiomas"
    },
    faq: {
      items: [
        {
          question: "O que a UNYRA GROUP LLC faz?",
          answer:
            "A UNYRA GROUP LLC atua em comércio de commodities, abastecimento global e desenvolvimento de negócios entre fronteiras, conectando fornecedores e compradores em mercados internacionais."
        },
        {
          question: "Onde a UNYRA GROUP LLC está localizada?",
          answer:
            "A UNYRA GROUP LLC está baseada em Orlando, Flórida, EUA, e opera internacionalmente."
        },
        {
          question: "Quais produtos fazem parte da expertise da UNYRA?",
          answer:
            "A UNYRA possui forte experiência em cadeias globais de alho, produtos frescos, commodities agrícolas e distribuição internacional de alimentos."
        },
        {
          question: "Em quais regiões a UNYRA atua?",
          answer:
            "A UNYRA atua nos Estados Unidos, Brasil, Argentina, China, Europa e Oriente Médio."
        },
        {
          question: "Como posso entrar em contato com a UNYRA?",
          answer:
            "Você pode falar com a UNYRA pelo e-mail sales@unyragroup.com, pelo telefone +1 888 789 8843 ou pelo formulário do site."
        }
      ]
    }
  },
  es: {
    locationDisplay: "Orlando, Florida, Estados Unidos",
    header: {
      nav: [
        { label: "Nosotros", href: "#about" },
        { label: "Servicios", href: "#services" },
        { label: "Presencia Global", href: "#global-presence" },
        { label: "Productos", href: "#products" },
        { label: "Por qué UNYRA", href: "#why-unyra" },
        { label: "Contacto", href: "#contact" }
      ],
      cta: "Iniciar Alianza",
      languageLabel: "Selector de idioma",
      openMenu: "Abrir navegación",
      closeMenu: "Cerrar navegación"
    },
    hero: {
      eyebrow: "Orlando, Florida, Estados Unidos | Comercio Global | Abastecimiento de Commodities | Ejecución Internacional",
      title: "Comercio Global. Ejecución Real.",
      description:
        "Conectando proveedores y compradores en mercados internacionales con precisión, confianza y ejecución estratégica.",
      primaryCta: "Iniciar Alianza",
      secondaryCta: "Contáctenos",
      trustLine:
        "Desarrollado para generar confianza con bancos, proveedores globales, grandes compradores y socios estratégicos.",
      highlights: [
        "Credibilidad institucional",
        "Experiencia en commodities",
        "Ejecución internacional"
      ],
      stats: [
        { value: "EE. UU.", label: "Base en Orlando, Florida" },
        { value: "6 polos", label: "Corredores activos de abastecimiento y comercio" },
        { value: "3 idiomas", label: "Inglés, portugués y español" }
      ],
      visualTag: "Operador Estratégico Global",
      visualTitle: "Un puente internacional entre oferta, demanda y expansión comercial.",
      visualDescription:
        "UNYRA opera con la disciplina de un socio estratégico de comercio internacional, alineando abastecimiento, ejecución y relaciones comerciales de largo plazo entre mercados."
    },
    about: {
      eyebrow: "Sobre UNYRA",
      title: "Una empresa global de comercio y desarrollo de negocios construida para contrapartes serias.",
      description:
        "UNYRA GROUP LLC tiene base en Orlando, Florida, y opera internacionalmente en comercio de commodities, abastecimiento global y desarrollo de negocios transfronterizos.",
      paragraphs: [
        "Conectamos proveedores confiables y compradores calificados con foco en claridad comercial, ejecución disciplinada y creación de valor de largo plazo.",
        "Nuestra actuación combina acceso a mercado, inteligencia de abastecimiento y soporte práctico a la transacción para convertir conversaciones en flujo comercial consistente.",
        "UNYRA aporta una sólida experiencia en productos agrícolas, especialmente en cadenas globales de ajo entre Estados Unidos, Brasil, Argentina, China, Europa y Oriente Medio."
      ],
      markers: [
        {
          title: "Base en EE. UU., alcance global",
          description:
            "Operamos desde Orlando con mandato internacional y una red comercial transfronteriza."
        },
        {
          title: "Mentalidad enfocada en comercio",
          description:
            "Nos posicionamos como un socio orientado a la ejecución, no como un intermediario pasivo."
        },
        {
          title: "Profundidad agrícola",
          description:
            "El ajo y el abastecimiento agrícola siguen siendo un núcleo de especialización."
        }
      ]
    },
    services: {
      eyebrow: "Servicios Clave",
      title: "Cinco capacidades premium para crecimiento internacional y ejecución comercial.",
      description:
        "Cada mandato se desarrolla con disciplina comercial, visión estratégica y seguimiento operativo.",
      items: [
        {
          id: "sourcing",
          title: "Abastecimiento Global",
          description:
            "Identificación de socios de suministro confiables en orígenes estratégicos con disciplina de calidad, tiempo y precio."
        },
        {
          id: "expansion",
          title: "Expansión de Mercado",
          description:
            "Apertura de oportunidades transfronterizas calificadas para empresas que buscan crecimiento internacional con credibilidad."
        },
        {
          id: "execution",
          title: "Ejecución Comercial",
          description:
            "Apoyo al proceso comercial desde la alineación de la negociación hasta el avance práctico de la transacción."
        },
        {
          id: "coordination",
          title: "Coordinación de la Cadena de Suministro",
          description:
            "Alineación entre las partes en abastecimiento, logística, documentación y expectativas de entrega."
        },
        {
          id: "partnerships",
          title: "Alianzas Estratégicas",
          description:
            "Construcción de relaciones de largo plazo entre compradores serios, proveedores y operadores globales."
        }
      ]
    },
    global: {
      eyebrow: "Presencia Global",
      title: "Posicionada en los corredores que definen el comercio agrícola.",
      description:
        "UNYRA está conectada con abastecimiento, distribución y rutas estratégicas de comercio entre las Américas, Europa, China y Oriente Medio.",
      metrics: [
        { value: "6 regiones", label: "puntos de abastecimiento y distribución" },
        { value: "Agrícola", label: "experiencia con el ajo en el centro" },
        { value: "Transfronterizo", label: "ejecución en comercio y desarrollo de negocios" }
      ],
      points: [
        { id: "usa", label: "EE. UU.", x: 20, y: 39, kind: "Distribución" },
        { id: "brazil", label: "Brasil", x: 31, y: 69, kind: "Origen" },
        { id: "argentina", label: "Argentina", x: 28, y: 82, kind: "Origen" },
        { id: "europe", label: "Europa", x: 51, y: 29, kind: "Distribución" },
        { id: "middle-east", label: "Oriente Medio", x: 61, y: 40, kind: "Ruta Comercial" },
        { id: "china", label: "China", x: 77, y: 36, kind: "Origen" }
      ],
      cards: [
        {
          eyebrow: "Red de Abastecimiento",
          title: "Abastecimiento agrícola en mercados de origen estratégicos",
          description:
            "Estructurado sobre relaciones confiables de suministro e inteligencia comercial orientada al producto."
        },
        {
          eyebrow: "Alcance de Distribución",
          title: "Flujo comercial que conecta origen y centros de demanda",
          description:
            "Diseñado para compradores serios, importadores y contrapartes estratégicas."
        },
        {
          eyebrow: "Rutas Comerciales",
          title: "Ejecución internacional con visibilidad comercial",
          description:
            "Coordinación clara entre mercados, expectativas y ritmo operativo."
        }
      ]
    },
    products: {
      eyebrow: "Industrias y Productos",
      title: "Enfocados donde la calidad, la continuidad y el conocimiento de mercado importan.",
      description:
        "UNYRA combina posicionamiento comercial con una visión práctica de la realidad de las cadenas agrícolas.",
      items: [
        {
          title: "Productos Frescos",
          description:
            "Relaciones de suministro alineadas con plazo, calidad y continuidad comercial confiable."
        },
        {
          title: "Cadenas Globales de Ajo",
          description:
            "Conocimiento profundo de los flujos internacionales del ajo, la dinámica de abastecimiento y los requisitos del comprador."
        },
        {
          title: "Commodities Agrícolas",
          description:
            "Soporte estratégico para productos agrícolas donde la ejecución y la confianza son decisivas."
        },
        {
          title: "Distribución Global de Alimentos",
          description:
            "Coordinación transfronteriza para movimiento de producto, alineación entre contrapartes y desarrollo de suministro de largo plazo."
        }
      ]
    },
    why: {
      eyebrow: "Por qué UNYRA",
      title: "Construida para reducir fricción, reforzar confianza y hacer avanzar los negocios.",
      description:
        "Nuestro valor no está solo en conectar partes. Está en alinear inteligencia de mercado, disciplina de ejecución y calidad relacional.",
      items: [
        {
          title: "Red Global",
          description:
            "Relaciones en múltiples regiones crean acceso a conversaciones calificadas entre oferta y demanda."
        },
        {
          title: "Ejecución Confiable",
          description:
            "Priorizamos seguimiento disciplinado, respuesta ágil y claridad comercial."
        },
        {
          title: "Inteligencia de Mercado",
          description:
            "El conocimiento de categoría y la perspectiva internacional apoyan mejores decisiones."
        },
        {
          title: "Alianzas de Largo Plazo",
          description:
            "Nos enfocamos en contrapartes que buscan alineación duradera, no transacciones aisladas."
        },
        {
          title: "Eficiencia Operativa",
          description:
            "Una estructura ágil y organizada ayuda a que las oportunidades avancen con menos ruido y mejor coordinación."
        }
      ]
    },
    contact: {
      eyebrow: "Contacto",
      title: "Inicie una conversación de alto valor con UNYRA.",
      description:
        "Comparta su necesidad de abastecimiento, oferta de suministro u objetivo de expansión. Evaluamos oportunidades con discreción y seriedad comercial.",
      trustPoints: [
        "Posicionamiento institucional para bancos, proveedores y contrapartes globales",
        "Comunicación multilingüe en inglés, portugués y español",
        "Base en Orlando, Florida, con alcance comercial internacional"
      ],
      form: {
        labels: {
          name: "Nombre",
          company: "Empresa",
          email: "Correo electrónico",
          message: "Mensaje"
        },
        placeholders: {
          name: "Su nombre",
          company: "Nombre de la empresa",
          email: "nombre@empresa.com",
          message: "Cuéntenos su necesidad de abastecimiento, compra, oferta o expansión de mercado."
        },
        submitLabel: "Contactar a UNYRA",
        disclaimer:
          "Al enviar este formulario, usted acepta ser contactado por UNYRA GROUP LLC respecto a su consulta.",
        successMessage:
          "Su borrador de correo ya está listo. Si no se abre ninguna ventana, escriba directamente a sales@unyragroup.com.",
        fallbackMessage:
          "Actualmente este formulario abre un correo prellenado para que su mensaje llegue de inmediato a UNYRA."
      }
    },
    footer: {
      description:
        "UNYRA GROUP LLC es una empresa global de comercio y desarrollo de negocios que conecta proveedores y compradores mediante inteligencia de abastecimiento, ejecución disciplinada y una visión de alianza de largo plazo.",
      legal: "UNYRA GROUP LLC. Todos los derechos reservados.",
      languageLabel: "Idiomas"
    },
    faq: {
      items: [
        {
          question: "¿Qué hace UNYRA GROUP LLC?",
          answer:
            "UNYRA GROUP LLC opera en comercio de commodities, abastecimiento global y desarrollo de negocios transfronterizos, conectando proveedores y compradores en mercados internacionales."
        },
        {
          question: "¿Dónde está ubicada UNYRA GROUP LLC?",
          answer:
            "UNYRA GROUP LLC tiene base en Orlando, Florida, Estados Unidos, y opera internacionalmente."
        },
        {
          question: "¿Qué productos forman parte de la experiencia de UNYRA?",
          answer:
            "UNYRA cuenta con amplia experiencia en cadenas globales de ajo, productos frescos, commodities agrícolas y distribución internacional de alimentos."
        },
        {
          question: "¿En qué regiones trabaja UNYRA?",
          answer:
            "UNYRA opera en Estados Unidos, Brasil, Argentina, China, Europa y Oriente Medio."
        },
        {
          question: "¿Cómo puedo contactar a UNYRA?",
          answer:
            "Puede contactar a UNYRA por correo en sales@unyragroup.com, por teléfono al +1 888 789 8843 o mediante el formulario del sitio."
        }
      ]
    }
  }
};

export const organizationStructuredData = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: siteSettings.name,
  url: siteSettings.url,
  logo: `${siteSettings.url}/brand/unyra-group-logo.png`,
  email: siteSettings.email,
  telephone: siteSettings.phoneDisplay,
  description: siteSettings.seoDescription,
  areaServed: [
    "United States",
    "Brazil",
    "Argentina",
    "China",
    "Europe",
    "Middle East"
  ],
  knowsAbout: [
    "global trade",
    "commodity trading",
    "global sourcing",
    "garlic supply chains",
    "agricultural commodities",
    "cross-border business development"
  ],
  sameAs: [siteSettings.url]
};

export const localBusinessStructuredData = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  name: siteSettings.name,
  image: `${siteSettings.url}/opengraph-image`,
  url: siteSettings.url,
  telephone: siteSettings.phoneDisplay,
  email: siteSettings.email,
  address: {
    "@type": "PostalAddress",
    addressLocality: "Orlando",
    addressRegion: "FL",
    addressCountry: "US"
  },
  areaServed: [
    "United States",
    "Brazil",
    "Argentina",
    "China",
    "Europe",
    "Middle East"
  ],
  description:
    "International trading, global sourcing, and cross-border business development with expertise in garlic and agricultural supply chains."
};

export const faqStructuredData = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: siteContent.en.faq.items.map((item) => ({
    "@type": "Question",
    name: item.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: item.answer
    }
  }))
};
