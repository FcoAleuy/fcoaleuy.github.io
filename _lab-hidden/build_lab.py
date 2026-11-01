# -*- coding: utf-8 -*-
"""Generates the Product Lab (index + case pages) in EN / ES / FR.

Run from anywhere:   python -X utf8 -I _lab-hidden/build_lab.py

PUBLISHED decides what goes live. Anything not listed there is written to
_lab-hidden/<lang>/<slug>/ instead. GitHub Pages runs Jekyll on this repo (no
.nojekyll), and Jekyll skips folders that start with "_", so hidden pages are NOT
served on franciscoaleuy.ca. The repository itself is public, so the source is
still visible on GitHub.

To publish a project: add its slug to PUBLISHED, run this script, commit.
SoyManada is rebuilt from the original page in git history (work/soymanada at
the commit in SOY_SRC_REV), so the script can be re-run safely.
"""
import io, os, re, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")).replace("\\", "/")
ROOT = os.path.dirname(ROOT) + "/"
SOY_SRC_REV = "89d6e8c"          # last commit that still has the original work/soymanada pages

PUBLISHED = ["content-loop", "soymanada", "resumonkey", "craft-beer-qa"]   # order = order on the index
HIDDEN = ["field-service-ops", "tour-sales-b2b", "design-studio-launch"]

PRE = {"en": "", "es": "/es", "fr": "/fr"}

def wr(path, s):
    full = ROOT + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, "w", encoding="utf-8", newline="").write(s)

def esc(s): return s.replace("&", "&amp;")

def git_show(path):
    return subprocess.run(["git", "show", "%s:%s" % (SOY_SRC_REV, path)], capture_output=True, text=True,
                          encoding="utf-8", cwd=ROOT).stdout

# ------------------------------------------------------------------ UI strings
UI = {
 "en": dict(prev="&larr; Previous case", next="Next case &rarr;", lab="Product Lab", back="&larr; Back to Product Lab",
   fig="Figures as of November 2026", read="Read the case &rarr;", discuss="Discuss this project",
   status={"live": "Live", "pilot": "Pilot", "mvp": "MVP", "prog": "In progress", "concept": "Concept"},
   h=dict(problem="The problem", discovery="Discovery", decisions="Key decisions", built="What I built", status="Status and results", next="What&rsquo;s next"),
   f=dict(role="Role", timeline="Timeline", stack="Stack", cost="Cost", note="Note"), chip="Stack", cardtags="Tags",
   idx_eyebrow="Francisco Aleuy &middot; Product Lab",
   idx_tldr="Products I build on my own: discovery, decisions, build and testing. Every case follows the same order: the problem, discovery, key decisions, what I built, status and results, what&rsquo;s next."),
 "es": dict(prev="&larr; Caso anterior", next="Siguiente caso &rarr;", lab="Product Lab", back="&larr; Volver al Product Lab",
   fig="Cifras a noviembre de 2026", read="Leer el caso &rarr;", discuss="Conversar sobre este proyecto",
   status={"live": "En vivo", "pilot": "Piloto", "mvp": "MVP", "prog": "En curso", "concept": "Concepto"},
   h=dict(problem="El problema", discovery="Descubrimiento", decisions="Decisiones clave", built="Qué construí", status="Estado y resultados", next="Qué sigue"),
   f=dict(role="Rol", timeline="Período", stack="Stack", cost="Costo", note="Nota"), chip="Stack", cardtags="Etiquetas",
   idx_eyebrow="Francisco Aleuy &middot; Product Lab",
   idx_tldr="Productos que construyo por mi cuenta: descubrimiento, decisiones, construcción y pruebas. Cada caso sigue el mismo orden: el problema, descubrimiento, decisiones clave, qué construí, estado y resultados, qué sigue."),
 "fr": dict(prev="&larr; Cas précédent", next="Cas suivant &rarr;", lab="Product Lab", back="&larr; Retour au Product Lab",
   fig="Chiffres au mois de novembre 2026", read="Lire le cas &rarr;", discuss="Discuter de ce projet",
   status={"live": "En ligne", "pilot": "Pilote", "mvp": "MVP", "prog": "En cours", "concept": "Concept"},
   h=dict(problem="Le problème", discovery="Découverte", decisions="Décisions clés", built="Ce que j&rsquo;ai construit", status="Statut et résultats", next="Suite"),
   f=dict(role="Rôle", timeline="Période", stack="Stack", cost="Coût", note="Note"), chip="Stack", cardtags="Étiquettes",
   idx_eyebrow="Francisco Aleuy &middot; Product Lab",
   idx_tldr="Produits que je construis moi-même : découverte, décisions, construction et tests. Chaque cas suit le même ordre : le problème, la découverte, les décisions clés, ce que j&rsquo;ai construit, le statut et les résultats, la suite."),
}
STATUS_CLS = {"live": "st-live", "pilot": "st-pilot", "mvp": "st-mvp", "prog": "st-prog", "concept": "st-concept"}

# ------------------------------------------------------------------ project content (plain text; esc() is applied on render)
P = {}

# ---------- 1. ODAC Content Loop (status live) ----------
P["content-loop"] = dict(status="live", en=dict(
  title="Content Loop, Osoyoos & District Arts Council",
  summary="A content portal for an arts council with 18 member groups, designed to keep running after I hand it off.",
  tags=["Product discovery", "Nonprofit", "Supabase", "Handoff design"],
  facts=[("role", "Volunteer Board Director, product lead and builder"), ("timeline", "June 2026 to present"),
         ("stack", "GitHub Pages, Supabase (Postgres, Auth, Storage), Resend"), ("cost", "$0 (free tiers)")],
  problem=["The Osoyoos & District Arts Council is an umbrella organization for 18 member arts groups. Member groups sent content to promote through informal emails, nobody could track what had been received or published, the council's goal of publishing within 48 hours was never measured, and member groups never heard how their content performed with the public."],
  discovery=["I interviewed the president and other directors, then cross-checked what they told me against meeting minutes, financial documents and email history. I only treated a problem as real once I had direct evidence for it. The three validated pain points: untraceable intake, an unmeasured 48-hour publishing goal, and no feedback loop to member groups."],
  decisions=[("Assist, not automate.", "I chose not to connect the portal directly to Facebook and Instagram through the Meta API. Access tokens expire and need ongoing technical maintenance, and after my handoff nobody at the council would be able to do it. Instead, the portal prepares the text, image and preview for each channel, and the administrator publishes with copy and paste. Less automation, but a system that keeps working."),
             ("Design for the real operator.", "The admin side was designed for a non-technical administrator, kept as simple as a spreadsheet, rather than for me."),
             ("$0 running cost.", "Every component runs on a free tier, so the council carries no software bills.")],
  built=["A public intake form for member groups, with automatic email confirmations, verified end to end with a real submission.",
         "An admin dashboard with a traffic-light indicator for the 48-hour publishing goal, per-channel publishing (Facebook, Instagram, website), editable social media previews with copy buttons, and admin invitations.",
         "Alongside the portal: moved the council's email to a domain-based Google Workspace for Nonprofits setup, recommended role-based addresses (president@, treasurer@) so correspondence stays with the role when volunteers rotate, recommended email authentication (SPF, DKIM, DMARC), helped hire the council's Executive Administrator and designed the handoff around her."],
  status_text=["Live. The intake form was verified end to end with a real submission, and the admin dashboard makes every piece of content traceable and the 48-hour publishing goal visible for the first time. The system was designed to be operated by the council's administrator, not by me."],
  next="Track the 48-hour goal over time and tackle the third pain point: giving member groups feedback on how their content performed."),
 es=dict(
  title="Content Loop, Osoyoos & District Arts Council",
  summary="Un portal de contenidos para un consejo de artes con 18 grupos miembros, diseñado para seguir funcionando después de mi traspaso.",
  tags=["Descubrimiento de producto", "Organización sin fines de lucro", "Supabase", "Diseño del traspaso"],
  facts=[("role", "Director voluntario del directorio, líder de producto y constructor"), ("timeline", "Junio de 2026 a la fecha"),
         ("stack", "GitHub Pages, Supabase (Postgres, Auth, Storage), Resend"), ("cost", "$0 (planes gratuitos)")],
  problem=["El Osoyoos & District Arts Council es una organización paraguas de 18 grupos artísticos miembros. Los grupos enviaban el contenido a promocionar por correos informales, nadie podía rastrear qué se había recibido o publicado, la meta del consejo de publicar en 48 horas nunca se medía y los grupos nunca sabían cómo le había ido a su contenido con el público."],
  discovery=["Entrevisté a la presidencia y a otros miembros del directorio, y luego contrasté lo que me dijeron con actas de reuniones, documentos financieros e historial de correos. Solo consideré real un problema cuando tuve evidencia directa. Los tres problemas validados: una recepción sin trazabilidad, una meta de publicación en 48 horas sin medir y ningún circuito de retroalimentación hacia los grupos miembros."],
  decisions=[("Asistir, no automatizar.", "Decidí no conectar el portal directamente a Facebook e Instagram mediante la API de Meta. Los tokens de acceso expiran y requieren mantenimiento técnico continuo, y tras mi traspaso nadie en el consejo podría hacerlo. En cambio, el portal prepara el texto, la imagen y la vista previa de cada canal, y quien administra publica con copiar y pegar. Menos automatización, pero un sistema que sigue funcionando."),
             ("Diseñar para el operador real.", "La parte de administración se diseñó para una persona administradora no técnica, tan simple como una planilla, y no para mí."),
             ("Costo de operación de $0.", "Cada componente corre en un plan gratuito, así que el consejo no carga con cuentas de software.")],
  built=["Un formulario público de recepción para los grupos miembros, con confirmaciones automáticas por correo, verificado de punta a punta con un envío real.",
         "Un panel de administración con un semáforo para la meta de publicación en 48 horas, publicación por canal (Facebook, Instagram, sitio web), vistas previas editables para redes sociales con botones de copiar e invitaciones para administradores.",
         "Junto al portal: moví el correo del consejo a una configuración con dominio propio de Google Workspace for Nonprofits, recomendé direcciones por rol (president@, treasurer@) para que la correspondencia se quede con el cargo cuando roten los voluntarios, recomendé autenticación de correo (SPF, DKIM, DMARC), ayudé a contratar a la administradora ejecutiva del consejo y diseñé el traspaso en torno a ella."],
  status_text=["En vivo. El formulario de recepción se verificó de punta a punta con un envío real, y el panel de administración hace que cada contenido sea rastreable y que la meta de 48 horas sea visible por primera vez. El sistema se diseñó para que lo opere la administradora del consejo, no yo."],
  next="Hacer seguimiento de la meta de 48 horas en el tiempo y abordar el tercer problema: dar a los grupos miembros retroalimentación sobre el desempeño de su contenido."),
 fr=dict(
  title="Content Loop, Osoyoos & District Arts Council",
  summary="Un portail de contenu pour un conseil des arts de 18 groupes membres, conçu pour continuer à fonctionner après ma passation.",
  tags=["Découverte produit", "Organisme sans but lucratif", "Supabase", "Conception de la passation"],
  facts=[("role", "Membre bénévole du conseil d’administration, responsable produit et concepteur"), ("timeline", "Juin 2026 à aujourd’hui"),
         ("stack", "GitHub Pages, Supabase (Postgres, Auth, Storage), Resend"), ("cost", "0 $ (forfaits gratuits)")],
  problem=["L’Osoyoos & District Arts Council est un organisme parapluie de 18 groupes artistiques membres. Les groupes envoyaient le contenu à promouvoir par des courriels informels, personne ne pouvait suivre ce qui avait été reçu ou publié, l’objectif du conseil de publier en 48 heures n’était jamais mesuré et les groupes ne savaient jamais comment leur contenu avait été reçu par le public."],
  discovery=["J’ai interviewé la présidence et d’autres membres du conseil, puis recoupé leurs propos avec les procès-verbaux, les documents financiers et l’historique des courriels. Je n’ai considéré un problème comme réel qu’avec une preuve directe. Les trois points de douleur validés : une réception sans traçabilité, un objectif de 48 heures non mesuré et aucune boucle de rétroaction vers les groupes membres."],
  decisions=[("Assister, pas automatiser.", "J’ai choisi de ne pas connecter le portail directement à Facebook et Instagram par l’API de Meta. Les jetons d’accès expirent et demandent un entretien technique continu, et après ma passation personne au conseil ne pourrait s’en charger. À la place, le portail prépare le texte, l’image et l’aperçu pour chaque canal, et la personne administratrice publie par copier-coller. Moins d’automatisation, mais un système qui continue de fonctionner."),
             ("Concevoir pour l’opérateur réel.", "L’interface d’administration a été conçue pour une personne administratrice non technique, aussi simple qu’un tableur, et non pour moi."),
             ("Coût d’exploitation de 0 $.", "Chaque composant tourne sur un forfait gratuit, le conseil n’a donc aucune facture de logiciel.")],
  built=["Un formulaire public de réception pour les groupes membres, avec confirmations automatiques par courriel, vérifié de bout en bout avec une vraie soumission.",
         "Un tableau de bord d’administration avec un feu tricolore pour l’objectif de publication en 48 heures, la publication par canal (Facebook, Instagram, site web), des aperçus modifiables pour les réseaux sociaux avec boutons de copie et des invitations d’administrateurs.",
         "En parallèle du portail : migration du courriel du conseil vers une configuration Google Workspace for Nonprofits sur un domaine propre, recommandation d’adresses par rôle (president@, treasurer@) pour que la correspondance reste avec le poste quand les bénévoles se succèdent, recommandation d’authentification des courriels (SPF, DKIM, DMARC), aide à l’embauche de l’administratrice exécutive du conseil et conception de la passation autour d’elle."],
  status_text=["En ligne. Le formulaire de réception a été vérifié de bout en bout avec une vraie soumission, et le tableau de bord rend chaque contenu traçable et l’objectif de 48 heures visible pour la première fois. Le système a été conçu pour être exploité par l’administratrice du conseil, pas par moi."],
  next="Suivre l’objectif de 48 heures dans le temps et s’attaquer au troisième point de douleur : donner aux groupes membres une rétroaction sur la performance de leur contenu."))

# ---------- 2. Operations digitization (hidden until the owner's feedback session) ----------
P["field-service-ops"] = dict(status="mvp", en=dict(
  title="Operations digitization for a field service business",
  summary="Mapped how a Vancouver espresso equipment repair company runs, found where revenue was leaking, and built the first tool to fix it.",
  tags=["Discovery", "Field service", "Revenue leakage", "Mobile-first"],
  facts=[("role", "Embedded product owner and builder (volunteer; also my Industrial Engineering capstone)"), ("timeline", "October 2026 to present"),
         ("stack", "HTML, CSS, JavaScript, GitHub Pages (MVP); shared backend planned (Supabase or Google Sheets)")],
  problem=["A small company repairs commercial espresso machines for a major coffee chain. Jobs arrive through the client's dispatch platform and an intermediary, parts are ordered by eye, labels are handwritten, and every technician report goes through a WhatsApp group before the owner approves it and the accountant invoices it. The owner is the bottleneck, and some work never gets billed."],
  discovery=["I worked inside the business as a technician in training, which let me see the process from the floor. I mapped every system involved (the client's dispatch platform, an intermediary portal, an invoicing app, QuickBooks, parts suppliers and the WhatsApp group) and ranked 7 pain points by their impact on the owner and on cash collection. Evidence I found:"],
  discovery_bullets=["Invoices older than 90 days that could no longer be collected, because the client cancels them after 90 days.", "5 to 6 invoices a week missed during manual review.", "Early-morning calls from the intermediary because technicians had no way to share an ETA."],
  decisions=[("Inventory first.", "Parts are the base of everything else: a reliable catalogue makes reports, ordering and invoicing possible. So the first MVP is the parts inventory, not the reporting flow."),
             ("Ship a demo before building a backend.", "The first version stores data in the browser so the owner can react to something real before we invest in a shared database."),
             ("Reuse what already works.", "One technician already writes excellent reports with an AI assistant; those reports will be the examples for the new report flow.")],
  built=["A catalogue of 403 Thermoplan Mastrena II parts, built by cross-checking the manufacturer's manuals against the physical parts in the shop, including corrections to parts that had been catalogued with the wrong SKU.",
         "MVP v0.1, a mobile-first inventory app: catalogue by SKU and machine module, stock per warehouse and per technician truck, stock adjustments with a movement log, low-stock alerts with a suggested reorder list, total inventory value for accounting, printable barcode labels and CSV export."],
  status_text=["MVP v0.1 working as a demo, in review with the owner (feedback session in November 2026)."],
  next="Add a shared backend so the whole team uses the same data, then build the second tool: a digital technician report that pulls parts from the catalogue and goes straight to the owner for approval and to the accountant for invoicing, with no copy and paste."),
 es=dict(
  title="Digitalización de operaciones para un negocio de servicio en terreno",
  summary="Mapeé cómo funciona una empresa de reparación de equipos de espresso en Vancouver, encontré dónde se filtraban ingresos y construí la primera herramienta para corregirlo.",
  tags=["Descubrimiento", "Servicio en terreno", "Fuga de ingresos", "Mobile-first"],
  facts=[("role", "Product owner y constructor integrado en el equipo (voluntario; también mi proyecto de título de Ingeniería Industrial)"), ("timeline", "Octubre de 2026 a la fecha"),
         ("stack", "HTML, CSS, JavaScript, GitHub Pages (MVP); backend compartido planificado (Supabase o Google Sheets)")],
  problem=["Una pequeña empresa repara máquinas de espresso comerciales para una gran cadena de café. Los trabajos llegan por la plataforma de despacho del cliente y por un intermediario, los repuestos se piden a ojo, las etiquetas se escriben a mano y cada informe de técnico pasa por un grupo de WhatsApp antes de que el dueño lo apruebe y la contadora lo facture. El dueño es el cuello de botella y parte del trabajo nunca se factura."],
  discovery=["Trabajé dentro del negocio como técnico en formación, lo que me permitió ver el proceso desde el piso. Mapeé todos los sistemas involucrados (la plataforma de despacho del cliente, un portal del intermediario, una app de facturación, QuickBooks, proveedores de repuestos y el grupo de WhatsApp) y ordené 7 problemas según su impacto en el dueño y en el cobro. Evidencia que encontré:"],
  discovery_bullets=["Facturas con más de 90 días que ya no se podían cobrar, porque el cliente las anula a los 90 días.", "Entre 5 y 6 facturas por semana que se escapaban en la revisión manual.", "Llamadas temprano en la mañana del intermediario porque los técnicos no tenían cómo compartir una hora estimada de llegada."],
  decisions=[("Primero el inventario.", "Los repuestos son la base de todo lo demás: un catálogo confiable hace posibles los informes, los pedidos y la facturación. Por eso el primer MVP es el inventario de repuestos y no el flujo de informes."),
             ("Entregar una demo antes de construir un backend.", "La primera versión guarda los datos en el navegador para que el dueño reaccione a algo real antes de invertir en una base de datos compartida."),
             ("Reutilizar lo que ya funciona.", "Un técnico ya escribe excelentes informes con un asistente de IA; esos informes serán los ejemplos para el nuevo flujo de informes.")],
  built=["Un catálogo de 403 repuestos Thermoplan Mastrena II, construido cruzando los manuales del fabricante con los repuestos físicos del taller, incluidas correcciones de repuestos que estaban catalogados con el SKU equivocado.",
         "MVP v0.1, una app de inventario mobile-first: catálogo por SKU y módulo de la máquina, stock por bodega y por camioneta de cada técnico, ajustes de stock con registro de movimientos, alertas de stock bajo con lista sugerida de reposición, valor total del inventario para contabilidad, etiquetas con código de barras imprimibles y exportación CSV."],
  status_text=["MVP v0.1 funcionando como demo, en revisión con el dueño (sesión de retroalimentación en noviembre de 2026)."],
  next="Agregar un backend compartido para que todo el equipo use los mismos datos y luego construir la segunda herramienta: un informe digital del técnico que toma los repuestos del catálogo y va directo al dueño para su aprobación y a la contadora para facturar, sin copiar y pegar."),
 fr=dict(
  title="Numérisation des opérations d’une entreprise de service sur le terrain",
  summary="J’ai cartographié le fonctionnement d’une entreprise de réparation d’équipements à espresso à Vancouver, trouvé où les revenus fuyaient et construit le premier outil pour y remédier.",
  tags=["Découverte", "Service sur le terrain", "Fuite de revenus", "Mobile-first"],
  facts=[("role", "Product owner et concepteur intégré à l’équipe (bénévole ; aussi mon projet de fin d’études en génie industriel)"), ("timeline", "Octobre 2026 à aujourd’hui"),
         ("stack", "HTML, CSS, JavaScript, GitHub Pages (MVP) ; backend partagé prévu (Supabase ou Google Sheets)")],
  problem=["Une petite entreprise répare des machines à espresso commerciales pour une grande chaîne de café. Les travaux arrivent par la plateforme de répartition du client et par un intermédiaire, les pièces sont commandées à l’œil, les étiquettes sont écrites à la main et chaque rapport de technicien passe par un groupe WhatsApp avant que le propriétaire l’approuve et que la comptable le facture. Le propriétaire est le goulot d’étranglement et une partie du travail n’est jamais facturée."],
  discovery=["J’ai travaillé dans l’entreprise comme technicien en formation, ce qui m’a permis de voir le processus depuis le terrain. J’ai cartographié tous les systèmes en jeu (la plateforme de répartition du client, un portail d’intermédiaire, une application de facturation, QuickBooks, les fournisseurs de pièces et le groupe WhatsApp) et classé 7 points de douleur selon leur effet sur le propriétaire et sur l’encaissement. Preuves relevées :"],
  discovery_bullets=["Des factures de plus de 90 jours qui ne pouvaient plus être encaissées, parce que le client les annule après 90 jours.", "De 5 à 6 factures par semaine oubliées lors de la révision manuelle.", "Des appels tôt le matin de l’intermédiaire, parce que les techniciens n’avaient aucun moyen de communiquer une heure d’arrivée estimée."],
  decisions=[("L’inventaire d’abord.", "Les pièces sont la base de tout le reste : un catalogue fiable rend possibles les rapports, les commandes et la facturation. Le premier MVP est donc l’inventaire des pièces, pas le flux de rapports."),
             ("Livrer une démo avant de construire un backend.", "La première version stocke les données dans le navigateur pour que le propriétaire réagisse à quelque chose de concret avant d’investir dans une base de données partagée."),
             ("Réutiliser ce qui fonctionne déjà.", "Un technicien rédige déjà d’excellents rapports avec un assistant d’IA ; ces rapports serviront d’exemples pour le nouveau flux de rapports.")],
  built=["Un catalogue de 403 pièces Thermoplan Mastrena II, construit en recoupant les manuels du fabricant avec les pièces physiques de l’atelier, y compris des corrections de pièces cataloguées avec un mauvais SKU.",
         "MVP v0.1, une application d’inventaire mobile-first : catalogue par SKU et par module de machine, stock par entrepôt et par camion de technicien, ajustements de stock avec journal des mouvements, alertes de stock bas avec liste de réapprovisionnement suggérée, valeur totale de l’inventaire pour la comptabilité, étiquettes à code-barres imprimables et export CSV."],
  status_text=["MVP v0.1 fonctionnel en démo, en révision avec le propriétaire (séance de rétroaction en novembre 2026)."],
  next="Ajouter un backend partagé pour que toute l’équipe utilise les mêmes données, puis construire le deuxième outil : un rapport numérique de technicien qui puise les pièces dans le catalogue et va directement au propriétaire pour approbation et à la comptable pour facturation, sans copier-coller."))

# ---------- 3. Craft beer platform (published, anonymized name) ----------
P["craft-beer-qa"] = dict(status="prog", en=dict(
  title="Chilean craft beer discovery platform, product and quality",
  summary="Co-founder covering product management and quality on a 3-person team, from risk-based test planning to a new end-to-end automation base.",
  tags=["Risk-based testing", "ISTQB", "Playwright", "AI-assisted QA", "Product management"],
  facts=[("role", "Co-founder, Product Owner and QA Lead"), ("timeline", "2026 to present"), ("stack", "Next.js 15, TypeScript, MongoDB, Better Auth, Playwright"),
         ("note", "The application code was built by my partners; my work was product management, testing and tool decisions.")],
  metrics=[("77%", "Account & authentication: 69 of about 90 test cases"), ("68%", "Age & role permissions: 75 of about 110 test cases"), ("144", "test cases executed, of an estimated 670 to 850 across 12 areas")],
  problem=["A web platform to discover Chilean craft beers, bars and breweries on an interactive map was heading to launch with no formal testing, no analytics and no official email. Nobody on the team owned product or quality."],
  discovery=["I reviewed the state of the project against the plan: I analyzed a recorded team meeting of almost two hours together with the brand brief and the project board, and listed what the team believed was ready versus what was actually built. The main gaps: no tests, no analytics and no email on the project's own domain."],
  decisions=[("Test the riskiest areas first.", "Accounts and role-based permissions carry the highest risk, so they came first."),
             ("AI executes, a human verifies.", "AI agents ran test sessions in parallel; I designed the plan, reviewed the test cases, verified every defect manually and wrote the reports. Manual verification caught a defect the automated runs missed: a dialog hidden behind the map."),
             ("Simple tools with clear limits.", "For analytics I recommended a free tool with a documented limit (Umami) over a more complex one, to reduce setup work and privacy risk before launch.")],
  built=["A risk-based test plan. Full-site scope is estimated at 670 to 850 test cases across 12 areas.",
         "Two test cycles: 144 test cases executed (156 executions including 12 re-tests) and 24 defects reported (1 high, 10 medium, 13 low) in ISTQB-style reports.",
         "Coverage of the highest-risk areas: account and authentication 69 of about 90 cases; age and role permissions 75 of about 110.",
         "An end-to-end automation base with Playwright, set up from scratch: Chilean locale and time zone, integration with the development server, first tests passing. Of the full scope, 281 scenarios are selected for automation and being implemented now.",
         "A tool decision document for analytics and domain email, plus the team's meeting minutes with owners and next steps."],
  status_text=["Pre-launch. Testing campaign ongoing and automation of the 281 selected scenarios in progress. Security findings are shared privately with the team."],
  next="Finish automating the selected scenarios, cover the remaining areas (brewery dashboard, discovery and map, moderation) and run a regression cycle before launch."),
 es=dict(
  title="Plataforma chilena de descubrimiento de cerveza artesanal, producto y calidad",
  summary="Cofundador a cargo de la gestión de producto y la calidad en un equipo de 3 personas, desde la planificación de pruebas basada en riesgo hasta una nueva base de automatización de punta a punta.",
  tags=["Testing basado en riesgo", "ISTQB", "Playwright", "QA asistido por IA", "Gestión de producto"],
  facts=[("role", "Cofundador, Product Owner y Líder de QA"), ("timeline", "2026 a la fecha"), ("stack", "Next.js 15, TypeScript, MongoDB, Better Auth, Playwright"),
         ("note", "El código de la aplicación lo construyeron mis socios; mi trabajo fue la gestión de producto, las pruebas y las decisiones de herramientas.")],
  metrics=[("77%", "Cuenta y autenticación: 69 de unos 90 casos de prueba"), ("68%", "Permisos por edad y rol: 75 de unos 110 casos de prueba"), ("144", "casos de prueba ejecutados, de un estimado de 670 a 850 en 12 áreas")],
  problem=["Una plataforma web para descubrir cervezas artesanales chilenas, bares y cervecerías en un mapa interactivo iba camino al lanzamiento sin pruebas formales, sin analítica y sin correo oficial. Nadie en el equipo era responsable del producto ni de la calidad."],
  discovery=["Revisé el estado del proyecto frente al plan: analicé una reunión grabada del equipo de casi dos horas junto con el brief de marca y el tablero del proyecto, y listé lo que el equipo creía listo frente a lo que realmente estaba construido. Las brechas principales: sin pruebas, sin analítica y sin correo en el dominio propio del proyecto."],
  decisions=[("Probar primero las áreas de mayor riesgo.", "Las cuentas y los permisos por rol son lo más riesgoso, así que fueron lo primero."),
             ("La IA ejecuta, una persona verifica.", "Agentes de IA ejecutaron sesiones de prueba en paralelo; yo diseñé el plan, revisé los casos de prueba, verifiqué cada defecto manualmente y escribí los informes. La verificación manual detectó un defecto que las ejecuciones automáticas no vieron: un diálogo tapado por el mapa."),
             ("Herramientas simples con límites claros.", "Para la analítica recomendé una herramienta gratuita con un límite documentado (Umami) en lugar de una más compleja, para reducir el trabajo de configuración y el riesgo de privacidad antes del lanzamiento.")],
  built=["Un plan de pruebas basado en riesgo. Se estima que el alcance de todo el sitio es de 670 a 850 casos de prueba en 12 áreas.",
         "Dos ciclos de prueba: 144 casos de prueba ejecutados (156 ejecuciones incluidos 12 re-tests) y 24 defectos reportados (1 alto, 10 medios, 13 bajos) en informes de estilo ISTQB.",
         "Cobertura de las áreas de mayor riesgo: cuenta y autenticación 69 de unos 90 casos; permisos por edad y rol 75 de unos 110.",
         "Una base de automatización de punta a punta con Playwright, armada desde cero: configuración regional y zona horaria de Chile, integración con el servidor de desarrollo y primeras pruebas pasando. Del alcance total, 281 escenarios están seleccionados para automatizar y se están implementando ahora.",
         "Un documento de decisión de herramientas para analítica y correo del dominio, además de las actas de reunión del equipo con responsables y próximos pasos."],
  status_text=["Pre-lanzamiento. Campaña de pruebas en marcha y automatización de los 281 escenarios seleccionados en curso. Los hallazgos de seguridad se comparten en privado con el equipo."],
  next="Terminar de automatizar los escenarios seleccionados, cubrir las áreas restantes (panel de cervecerías, descubrimiento y mapa, moderación) y ejecutar un ciclo de regresión antes del lanzamiento."),
 fr=dict(
  title="Plateforme chilienne de découverte de bières artisanales, produit et qualité",
  summary="Cofondateur responsable de la gestion de produit et de la qualité au sein d’une équipe de 3 personnes, de la planification de tests fondée sur le risque à une nouvelle base d’automatisation de bout en bout.",
  tags=["Tests fondés sur le risque", "ISTQB", "Playwright", "AQ assistée par IA", "Gestion de produit"],
  facts=[("role", "Cofondateur, Product Owner et responsable AQ"), ("timeline", "2026 à aujourd’hui"), ("stack", "Next.js 15, TypeScript, MongoDB, Better Auth, Playwright"),
         ("note", "Le code de l’application a été écrit par mes associés ; mon travail a porté sur la gestion de produit, les tests et le choix des outils.")],
  metrics=[("77 %", "Compte et authentification : 69 cas de test sur environ 90"), ("68 %", "Permissions selon l’âge et le rôle : 75 cas de test sur environ 110"), ("144", "cas de test exécutés, sur une estimation de 670 à 850 dans 12 zones")],
  problem=["Une plateforme web pour découvrir des bières artisanales chiliennes, des bars et des brasseries sur une carte interactive allait vers le lancement sans tests formels, sans analytique et sans courriel officiel. Personne dans l’équipe n’était responsable du produit ni de la qualité."],
  discovery=["J’ai examiné l’état du projet par rapport au plan : j’ai analysé une réunion d’équipe enregistrée de près de deux heures, avec le brief de marque et le tableau du projet, et listé ce que l’équipe croyait prêt par rapport à ce qui était réellement construit. Les principaux écarts : pas de tests, pas d’analytique et pas de courriel sur le domaine propre du projet."],
  decisions=[("Tester d’abord les zones les plus à risque.", "Les comptes et les permissions par rôle sont ce qui présente le plus de risque, ils sont donc passés en premier."),
             ("L’IA exécute, un humain vérifie.", "Des agents d’IA ont exécuté des sessions de test en parallèle ; j’ai conçu le plan, révisé les cas de test, vérifié chaque défaut manuellement et rédigé les rapports. La vérification manuelle a trouvé un défaut que les exécutions automatiques avaient manqué : une boîte de dialogue cachée derrière la carte."),
             ("Des outils simples aux limites claires.", "Pour l’analytique, j’ai recommandé un outil gratuit à la limite documentée (Umami) plutôt qu’un outil plus complexe, afin de réduire le travail de configuration et le risque pour la vie privée avant le lancement.")],
  built=["Un plan de test fondé sur le risque. La portée de tout le site est estimée à 670 à 850 cas de test dans 12 zones.",
         "Deux cycles de test : 144 cas de test exécutés (156 exécutions, dont 12 retests) et 24 défauts signalés (1 élevé, 10 moyens, 13 faibles) dans des rapports de style ISTQB.",
         "Couverture des zones les plus à risque : compte et authentification 69 cas sur environ 90 ; permissions selon l’âge et le rôle 75 sur environ 110.",
         "Une base d’automatisation de bout en bout avec Playwright, montée de zéro : paramètres régionaux et fuseau horaire du Chili, intégration au serveur de développement, premiers tests réussis. Sur la portée totale, 281 scénarios sont retenus pour l’automatisation et en cours d’implémentation.",
         "Un document de décision d’outils pour l’analytique et le courriel du domaine, ainsi que les comptes rendus de réunion de l’équipe avec responsables et prochaines étapes."],
  status_text=["Pré-lancement. Campagne de tests en cours et automatisation des 281 scénarios retenus en cours. Les constats de sécurité sont partagés en privé avec l’équipe."],
  next="Terminer l’automatisation des scénarios retenus, couvrir les zones restantes (tableau de bord des brasseries, découverte et carte, modération) et exécuter un cycle de régression avant le lancement."))

# ---------- 4. New Frontier (hidden) ----------
P["tour-sales-b2b"] = dict(status="concept", en=dict(
  title="New Frontier, tour sales for Patagonia hotels",
  summary="Validated a tour-sales tool with real data and pivoted from a tourist app to a B2B tool before writing any code.",
  tags=["Discovery", "Pivot", "B2B", "Multi-tenant platform"],
  facts=[("role", "Product Owner (with a partner who works in tourism in Patagonia)"), ("timeline", "2026"), ("stack", "To be defined with the developer")],
  problem=["Hotels and agencies near Torres del Paine sell tours through WhatsApp, paper and spreadsheets. Commissions are calculated by hand, mistakes happen and there is no record of who sold what."],
  discovery=["The first idea was an app for tourists to book tours directly. Interviews with agencies showed that hotels are the main booking channel, so cutting them out was not realistic. We pivoted to a tool for the hotels and agencies themselves. I validated the commission structure with six months of real sales data from a partner in the industry and benchmarked market commissions (typically 15 to 20%). Before defining the MVP, I sent the domain expert a structured set of questions on workflow, pain points, master data, commission rules, pilot and confidentiality."],
  decisions=[("Pivot on evidence, not preference.", "The B2C idea was dropped because the data said so."),
             ("Build once, reuse many times.", "The tool will be the first template of a multi-tenant platform, Bizmonkey, so other small businesses (a second one is already interested) can run their own site on the same base, with admin and collaborator roles."),
             ("Name checked before committing.", "Platform names were checked for availability before choosing one.")],
  built=["A validated problem and commission model, an approved design direction, and a product brief with MVP scope, out-of-scope items and roles, ready for a developer."],
  status_text=["Concept, ready for development."],
  next="Build the MVP (sales log, extras, automatic commission calculation, KPI dashboard, roles) and confirm a pilot hotel."),
 es=dict(
  title="New Frontier, venta de tours para hoteles de la Patagonia",
  summary="Validé una herramienta de venta de tours con datos reales y pasé de una app para turistas a una herramienta B2B antes de escribir una sola línea de código.",
  tags=["Descubrimiento", "Pivote", "B2B", "Plataforma multi-tenant"],
  facts=[("role", "Product Owner (con un socio que trabaja en turismo en la Patagonia)"), ("timeline", "2026"), ("stack", "Por definir con el desarrollador")],
  problem=["Los hoteles y agencias cerca de Torres del Paine venden tours por WhatsApp, papel y planillas. Las comisiones se calculan a mano, ocurren errores y no queda registro de quién vendió qué."],
  discovery=["La primera idea fue una app para que los turistas reservaran tours directamente. Las entrevistas con agencias mostraron que los hoteles son el principal canal de reserva, así que dejarlos fuera no era realista. Pivotamos hacia una herramienta para los propios hoteles y agencias. Validé la estructura de comisiones con seis meses de ventas reales de un socio de la industria y comparé las comisiones del mercado (típicamente de 15 a 20%). Antes de definir el MVP, envié a la persona experta del rubro un conjunto estructurado de preguntas sobre flujo de trabajo, problemas, datos maestros, reglas de comisión, piloto y confidencialidad."],
  decisions=[("Pivotar por evidencia, no por preferencia.", "La idea B2C se descartó porque los datos así lo indicaron."),
             ("Construir una vez, reutilizar muchas.", "La herramienta será la primera plantilla de una plataforma multi-tenant, Bizmonkey, para que otros negocios pequeños (ya hay un segundo interesado) operen su propio sitio sobre la misma base, con roles de administrador y colaborador."),
             ("Verificar el nombre antes de comprometerse.", "Se revisó la disponibilidad de los nombres de plataforma antes de elegir uno.")],
  built=["Un problema y un modelo de comisiones validados, una dirección de diseño aprobada y un brief de producto con alcance del MVP, elementos fuera de alcance y roles, listo para un desarrollador."],
  status_text=["Concepto, listo para desarrollo."],
  next="Construir el MVP (registro de ventas, extras, cálculo automático de comisiones, panel de KPIs, roles) y confirmar un hotel piloto."),
 fr=dict(
  title="New Frontier, vente de excursions pour les hôtels de Patagonie",
  summary="J’ai validé un outil de vente d’excursions avec des données réelles et basculé d’une application pour touristes vers un outil B2B avant d’écrire la moindre ligne de code.",
  tags=["Découverte", "Pivot", "B2B", "Plateforme multi-tenant"],
  facts=[("role", "Product Owner (avec un associé qui travaille dans le tourisme en Patagonie)"), ("timeline", "2026"), ("stack", "À définir avec le développeur")],
  problem=["Les hôtels et agences près de Torres del Paine vendent des excursions par WhatsApp, sur papier et dans des tableurs. Les commissions sont calculées à la main, des erreurs surviennent et il n’existe aucune trace de qui a vendu quoi."],
  discovery=["La première idée était une application permettant aux touristes de réserver directement. Les entretiens avec les agences ont montré que les hôtels sont le principal canal de réservation, les écarter n’était donc pas réaliste. Nous avons pivoté vers un outil pour les hôtels et agences eux-mêmes. J’ai validé la structure des commissions avec six mois de ventes réelles d’un partenaire du secteur et comparé les commissions du marché (typiquement de 15 à 20 %). Avant de définir le MVP, j’ai envoyé à l’expert du domaine une série structurée de questions sur le flux de travail, les points de douleur, les données de référence, les règles de commission, le pilote et la confidentialité."],
  decisions=[("Pivoter sur les preuves, pas sur la préférence.", "L’idée B2C a été abandonnée parce que les données l’indiquaient."),
             ("Construire une fois, réutiliser souvent.", "L’outil sera le premier modèle d’une plateforme multi-tenant, Bizmonkey, pour que d’autres petites entreprises (une deuxième est déjà intéressée) gèrent leur propre site sur la même base, avec des rôles d’administrateur et de collaborateur."),
             ("Nom vérifié avant de s’engager.", "La disponibilité des noms de plateforme a été vérifiée avant d’en choisir un.")],
  built=["Un problème et un modèle de commissions validés, une direction de design approuvée et un brief produit avec la portée du MVP, les éléments hors portée et les rôles, prêt pour un développeur."],
  status_text=["Concept, prêt pour le développement."],
  next="Construire le MVP (journal des ventes, extras, calcul automatique des commissions, tableau de bord d’indicateurs, rôles) et confirmer un hôtel pilote."))

# ---------- 5. Interior design studio (hidden) ----------
P["design-studio-launch"] = dict(status="concept", en=dict(
  title="Digital launch for an independent design studio",
  summary="Pro bono discovery and digital roadmap for an architect launching an interior design studio in Vancouver.",
  tags=["Discovery", "Early-stage business", "Digital presence"],
  facts=[("role", "Product Owner, pro bono"), ("timeline", "October 2026 to present")],
  problem=["An architect is launching an interior design studio in Vancouver. He found his first client by offering free AI-generated before-and-after visuals to homeowners, but that channel depended on a previous job. He has no website, no professional email and a small social media audience, and he will be away from the city for several months."],
  discovery=["I ran a one-hour discovery session with a prepared question set covering the business, capacity, channels and expectations. Key findings: capacity of about 2 projects a month, 2 to 3 weeks per space, a deliberately low entry price, and a 3-month goal of booking 2 projects for spring."],
  decisions=[("Remote-first acquisition.", "Since he will be away, acquisition has to work without him in the city: website, social media and online marketplaces, not flyers."),
             ("Professional basics first.", "A domain and professional email build trust in a business where the client lets someone into their home."),
             ("Buffer every estimate.", "Add time to each project estimate; delivering early builds reputation, delivering late loses it.")],
  built=["A prioritized digital roadmap: domain and professional email, a portfolio website hosted at no cost, and a content plan based on documenting the first project."],
  status_text=["In discovery. Goal: 2 projects booked for spring 2027."],
  next="Launch the domain, email and portfolio site, then evaluate a client and project management tool if demand grows."),
 es=dict(
  title="Lanzamiento digital de un estudio de diseño independiente",
  summary="Descubrimiento y hoja de ruta digital pro bono para un arquitecto que lanza un estudio de diseño de interiores en Vancouver.",
  tags=["Descubrimiento", "Negocio en etapa temprana", "Presencia digital"],
  facts=[("role", "Product Owner, pro bono"), ("timeline", "Octubre de 2026 a la fecha")],
  problem=["Un arquitecto está lanzando un estudio de diseño de interiores en Vancouver. Consiguió su primer cliente ofreciendo a propietarios visuales gratuitos de antes y después generados con IA, pero ese canal dependía de un trabajo anterior. No tiene sitio web ni correo profesional, tiene una audiencia pequeña en redes sociales y estará fuera de la ciudad varios meses."],
  discovery=["Realicé una sesión de descubrimiento de una hora con un set de preguntas preparado sobre el negocio, la capacidad, los canales y las expectativas. Hallazgos clave: capacidad de unos 2 proyectos al mes, de 2 a 3 semanas por espacio, un precio de entrada deliberadamente bajo y una meta a 3 meses de cerrar 2 proyectos para la primavera."],
  decisions=[("Captación remota primero.", "Como estará fuera, la captación tiene que funcionar sin él en la ciudad: sitio web, redes sociales y marketplaces en línea, no volantes."),
             ("Primero lo básico profesional.", "Un dominio y un correo profesional generan confianza en un negocio donde el cliente deja entrar a alguien a su casa."),
             ("Holgura en cada estimación.", "Agregar tiempo a la estimación de cada proyecto; entregar antes construye reputación, entregar tarde la pierde.")],
  built=["Una hoja de ruta digital priorizada: dominio y correo profesional, un sitio de portafolio alojado sin costo y un plan de contenidos basado en documentar el primer proyecto."],
  status_text=["En descubrimiento. Meta: 2 proyectos cerrados para la primavera de 2027."],
  next="Lanzar el dominio, el correo y el sitio de portafolio, y luego evaluar una herramienta de gestión de clientes y proyectos si la demanda crece."),
 fr=dict(
  title="Lancement numérique d’un studio de design indépendant",
  summary="Découverte et feuille de route numérique à titre bénévole pour un architecte qui lance un studio de design d’intérieur à Vancouver.",
  tags=["Découverte", "Entreprise en démarrage", "Présence numérique"],
  facts=[("role", "Product Owner, à titre bénévole"), ("timeline", "Octobre 2026 à aujourd’hui")],
  problem=["Un architecte lance un studio de design d’intérieur à Vancouver. Il a trouvé son premier client en offrant à des propriétaires des visuels avant-après générés par IA, mais ce canal dépendait d’un contrat précédent. Il n’a ni site web ni courriel professionnel, son audience sur les réseaux sociaux est petite et il sera absent de la ville pendant plusieurs mois."],
  discovery=["J’ai mené une séance de découverte d’une heure avec une série de questions préparées sur l’entreprise, la capacité, les canaux et les attentes. Constats clés : une capacité d’environ 2 projets par mois, de 2 à 3 semaines par espace, un prix d’entrée volontairement bas et un objectif à 3 mois de réserver 2 projets pour le printemps."],
  decisions=[("Acquisition à distance d’abord.", "Comme il sera absent, l’acquisition doit fonctionner sans lui en ville : site web, réseaux sociaux et places de marché en ligne, pas de prospectus."),
             ("Les bases professionnelles d’abord.", "Un domaine et un courriel professionnel inspirent confiance dans un métier où le client laisse entrer quelqu’un chez lui."),
             ("Une marge sur chaque estimation.", "Ajouter du temps à l’estimation de chaque projet ; livrer tôt bâtit la réputation, livrer tard la fait perdre.")],
  built=["Une feuille de route numérique priorisée : domaine et courriel professionnel, un site de portfolio hébergé sans frais et un plan de contenu fondé sur la documentation du premier projet."],
  status_text=["En découverte. Objectif : 2 projets réservés pour le printemps 2027."],
  next="Lancer le domaine, le courriel et le site de portfolio, puis évaluer un outil de gestion des clients et des projets si la demande augmente."))

# ---------- 6. Resumonkey (published; previous brief) ----------
P["resumonkey"] = dict(status="pilot", en=dict(
  title="Resumonkey",
  summary="A daily job digest that searches three markets, scores each listing 0 to 10 and explains the score.",
  tags=["Python/FastAPI", "Next.js", "Supabase", "Render (cron)", "Resend", "GitHub"],
  facts=[("role", "Solo product and build"), ("stack", "Python/FastAPI, Next.js, Supabase, Render (cron), Resend, GitHub")],
  metrics=[("3", "markets searched: Canada, Chile and remote"), ("8", "known calibration cases that must pass before every real send"), ("8.3 → 3.2 min", "run time after splitting the work across language models")],
  problem=["Searching across several markets means reading the same noisy listings every day. Many are in the wrong country, require a language the search excludes, or are already stale. A ranking that cannot explain itself is hard to trust and hard to fix.",
           "I built it first for my own search across Canada, Chile and remote roles. It runs as a pilot, so every design choice is judged against real daily use before anything else is added."],
  discovery=["Three questions shaped the product. What must never reach the digest? Hard filters on country, required language and listing age. How does a listing earn its score? A rubric of components, with the reasoning shown, rather than a single opinion. How do I know the scoring still behaves after a change? A set of known cases that has to pass first."],
  decisions=[("Hard filters before scoring.", "Country, required language and age are rules, not model judgement. The cost is that a filter is only as good as its rule."),
             ("A 0 to 10 score built from components, with an explanation.", "More to maintain than one number, but every score can be challenged and corrected."),
             ("A calibration suite of 8 known cases before every real send.", "Slower to ship a change, in return for catching a drifting score before it reaches the digest."),
             ("Work split across language models.", "More moving parts to coordinate, in return for a run time that fell from 8.3 to 3.2 minutes."),
             ("Full listing text stored in Supabase.", "Scores can be audited and re-run later against exactly what was scored.")],
  built=["Filtering and scoring service: Python/FastAPI.", "Web interface: Next.js.", "Storage: Supabase, including the full text of every listing.", "Daily run: a cron job on Render.", "Delivery: the digest is sent through Resend.", "Code: GitHub."],
  status_text=["Pilot. Run time went from 8.3 minutes to 3.2. Eight known calibration cases must pass before each real send. The digest covers three markets: Canada, Chile and remote."],
  next="The pilot decides. Where a score is challenged, the rubric is tightened; where the digest surprises me, that case joins the calibration suite."),
 es=dict(
  title="Resumonkey",
  summary="Un digest diario de empleos que busca en tres mercados, puntúa cada oferta de 0 a 10 y explica el puntaje.",
  tags=["Python/FastAPI", "Next.js", "Supabase", "Render (cron)", "Resend", "GitHub"],
  facts=[("role", "Producto y construcción en solitario"), ("stack", "Python/FastAPI, Next.js, Supabase, Render (cron), Resend, GitHub")],
  metrics=[("3", "mercados: Canadá, Chile y remoto"), ("8", "casos de calibración conocidos que deben pasar antes de cada envío real"), ("8,3 → 3,2 min", "tiempo de ejecución tras repartir el trabajo entre modelos de lenguaje")],
  problem=["Buscar en varios mercados significa leer cada día las mismas ofertas con ruido. Muchas son del país equivocado, exigen un idioma que la búsqueda excluye o ya están vencidas. Un ranking que no puede explicarse es difícil de creer y difícil de corregir.",
           "Lo construí primero para mi propia búsqueda en Canadá, Chile y roles remotos. Funciona como piloto, así que cada decisión de diseño se juzga con uso diario real antes de agregar nada más."],
  discovery=["Tres preguntas dieron forma al producto. ¿Qué no debe llegar nunca al digest? Filtros duros por país, idioma requerido y antigüedad de la oferta. ¿Cómo gana su puntaje una oferta? Con una rúbrica por componentes y el razonamiento a la vista, no una sola opinión. ¿Cómo sé que el puntaje sigue comportándose bien tras un cambio? Con un conjunto de casos conocidos que debe pasar primero."],
  decisions=[("Filtros duros antes de puntuar.", "País, idioma requerido y antigüedad son reglas, no criterio del modelo. El costo es que un filtro vale lo que vale su regla."),
             ("Un puntaje de 0 a 10 construido por componentes, con explicación.", "Hay más que mantener que con un solo número, pero cada puntaje se puede cuestionar y corregir."),
             ("Una suite de calibración de 8 casos conocidos antes de cada envío real.", "Cambiar algo toma más tiempo, a cambio de detectar un puntaje que se desvía antes de que llegue al digest."),
             ("Trabajo repartido entre modelos de lenguaje.", "Más piezas que coordinar, a cambio de un tiempo de ejecución que bajó de 8,3 a 3,2 minutos."),
             ("Texto completo de cada oferta guardado en Supabase.", "Los puntajes se pueden auditar y volver a ejecutar sobre exactamente lo que se puntuó.")],
  built=["Servicio de filtrado y puntaje: Python/FastAPI.", "Interfaz web: Next.js.", "Almacenamiento: Supabase, con el texto completo de cada oferta.", "Ejecución diaria: una tarea programada (cron) en Render.", "Envío: el digest se despacha con Resend.", "Código: GitHub."],
  status_text=["Piloto. El tiempo de ejecución bajó de 8,3 minutos a 3,2. Ocho casos de calibración conocidos deben pasar antes de cada envío real. El digest cubre tres mercados: Canadá, Chile y remoto."],
  next="El piloto decide. Donde un puntaje se cuestiona, se ajusta la rúbrica; donde el digest me sorprende, ese caso entra a la suite de calibración."),
 fr=dict(
  title="Resumonkey",
  summary="Un digest quotidien d’emplois qui parcourt trois marchés, note chaque offre de 0 à 10 et explique la note.",
  tags=["Python/FastAPI", "Next.js", "Supabase", "Render (cron)", "Resend", "GitHub"],
  facts=[("role", "Produit et développement en solo"), ("stack", "Python/FastAPI, Next.js, Supabase, Render (cron), Resend, GitHub")],
  metrics=[("3", "marchés : Canada, Chili et télétravail"), ("8", "cas de calibration connus qui doivent passer avant chaque envoi réel"), ("8,3 → 3,2 min", "durée d’exécution après répartition du travail entre des modèles de langage")],
  problem=["Chercher sur plusieurs marchés, c’est relire chaque jour les mêmes offres bruitées. Beaucoup sont dans le mauvais pays, exigent une langue que la recherche exclut ou sont déjà périmées. Un classement qui ne sait pas s’expliquer est difficile à croire et difficile à corriger.",
           "Je l’ai d’abord conçu pour ma propre recherche au Canada, au Chili et en télétravail. Il fonctionne en pilote : chaque choix de conception est jugé à l’usage quotidien réel avant d’ajouter quoi que ce soit."],
  discovery=["Trois questions ont façonné le produit. Que ne doit jamais contenir le digest ? Des filtres stricts sur le pays, la langue exigée et l’ancienneté de l’offre. Comment une offre gagne-t-elle sa note ? Par une grille de composantes, avec le raisonnement visible, plutôt qu’un avis unique. Comment savoir que la notation se comporte encore bien après un changement ? Avec un ensemble de cas connus qui doit passer d’abord."],
  decisions=[("Filtres stricts avant la notation.", "Pays, langue exigée et ancienneté sont des règles, pas un jugement du modèle. Le coût : un filtre vaut ce que vaut sa règle."),
             ("Une note de 0 à 10 construite par composantes, avec explication.", "Plus à maintenir qu’un chiffre unique, mais chaque note peut être contestée et corrigée."),
             ("Une suite de calibration de 8 cas connus avant chaque envoi réel.", "Un changement prend plus de temps, en échange de repérer une note qui dérive avant qu’elle n’atteigne le digest."),
             ("Travail réparti entre des modèles de langage.", "Plus d’éléments à coordonner, en échange d’une durée d’exécution passée de 8,3 à 3,2 minutes."),
             ("Texte complet de chaque offre stocké dans Supabase.", "Les notes peuvent être vérifiées et relancées sur exactement ce qui a été noté.")],
  built=["Service de filtrage et de notation : Python/FastAPI.", "Interface web : Next.js.", "Stockage : Supabase, avec le texte complet de chaque offre.", "Exécution quotidienne : une tâche planifiée (cron) sur Render.", "Envoi : le digest est expédié via Resend.", "Code : GitHub."],
  status_text=["Pilote. La durée d’exécution est passée de 8,3 minutes à 3,2. Huit cas de calibration connus doivent passer avant chaque envoi réel. Le digest couvre trois marchés : Canada, Chili et télétravail."],
  next="Le pilote tranche. Quand une note est contestée, la grille est resserrée ; quand le digest me surprend, ce cas rejoint la suite de calibration."))

# ---------- SoyManada: moved page, card data only ----------
P["soymanada"] = dict(status="live", en=dict(
  title="SoyManada", summary="A trilingual, manually verified directory of services for Spanish-speaking newcomers to Canada.",
  tags=["React + Vite", "Supabase", "i18next", "GitHub Actions"]),
 es=dict(title="SoyManada", summary="Un directorio trilingüe y verificado manualmente de servicios para hispanohablantes recién llegados a Canadá.",
  tags=["React + Vite", "Supabase", "i18next", "GitHub Actions"]),
 fr=dict(title="SoyManada", summary="Un répertoire trilingue, vérifié manuellement, de services pour les nouveaux arrivants hispanophones au Canada.",
  tags=["React + Vite", "Supabase", "i18next", "GitHub Actions"]))

# ------------------------------------------------------------------ CSS + HTML helpers
LAB_EXTRA_CSS = """
.lab-card{display:block;background:rgba(56,189,248,.04);border:1px solid rgba(56,189,248,.16);border-radius:14px;padding:1.5rem 1.6rem;margin-bottom:1.1rem;transition:border-color .25s,transform .25s,box-shadow .25s}
.lab-card:hover{border-color:rgba(56,189,248,.45);transform:translateY(-3px);box-shadow:0 10px 36px rgba(56,189,248,.1)}
.lab-card h2{font-size:1.3rem;margin:0 0 .35rem;color:#f8fafc;line-height:1.3}
.lab-card p{margin:.2rem 0 .9rem;color:#cbd5e1;line-height:1.6}
.lab-card .lc-top{display:flex;align-items:flex-start;gap:.7rem;justify-content:space-between;flex-wrap:wrap}
.lab-card .lc-go{font-size:.85rem;color:#38bdf8;font-weight:600}
.status-badge{font-size:.62rem;font-weight:700;padding:.16rem .6rem;border-radius:99px;letter-spacing:.06em;text-transform:uppercase;vertical-align:middle;border:1px solid;white-space:nowrap}
.st-live{color:#0f172a;background:#38bdf8;border-color:#38bdf8}
.st-pilot{color:#f59e0b;border-color:rgba(245,158,11,.5);background:rgba(245,158,11,.08)}
.st-mvp{color:#38bdf8;border-color:rgba(56,189,248,.55);background:rgba(56,189,248,.08)}
.st-prog{color:#a78bfa;border-color:rgba(167,139,250,.5);background:rgba(167,139,250,.08)}
.st-concept{color:#94a3b8;border-color:rgba(148,163,184,.4);background:rgba(148,163,184,.06)}
.hdr-status{display:flex;align-items:center;gap:.8rem;flex-wrap:wrap;margin:.2rem 0 1rem}
.fig-note{font-size:.78rem;color:#64748b;font-style:italic;margin:0}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.1rem 2rem;margin:1.8rem 0 0;padding:1.3rem 0 0;border-top:1px solid rgba(56,189,248,.14)}
.facts dt{font-size:.64rem;letter-spacing:.16em;text-transform:uppercase;color:#64748b;font-weight:700}
.facts dd{margin:.3rem 0 0;color:#e2e8f0;font-size:.95rem;line-height:1.55}
.facts .wide{grid-column:1/-1}
"""
H2S = "color:#f8fafc;font-size:1.5rem;margin-bottom:1.5rem;border-left:4px solid #38bdf8;padding-left:1rem"
def sec(title, inner): return '  <div style="margin-bottom:4rem"><h2 style="%s">%s</h2>%s</div>\n' % (H2S, title, inner)
def para(t): return '<p style="font-size:1.05rem;color:#cbd5e1;line-height:1.7;margin-bottom:1rem">%s</p>' % esc(t)
def blt(items, bold_heads=True):
    out = '<ul style="list-style:none;padding:0;color:#cbd5e1">'
    for it in items:
        body = ("<strong>%s</strong> %s" % (esc(it[0]), esc(it[1]))) if isinstance(it, tuple) else esc(it)
        out += '<li style="margin-bottom:1rem;padding-left:1.5rem;position:relative"><span style="position:absolute;left:0;color:#38bdf8">&#9657;</span>%s</li>' % body
    return out + "</ul>"
def metrics_html(m):
    return '<div class="case-metrics">' + "".join('<div class="case-metric"><div class="num">%s</div><div class="lbl">%s</div></div>' % (esc(a), esc(b)) for a, b in m) + "</div>"
def chips_html(label, items):
    return '<div class="stack-chips"><span class="chip-label">%s</span>%s</div>' % (label, "".join('<span class="chip">%s</span>' % esc(i) for i in items))
def case_nav(prev, nxt, ui):
    a = '<a href="%s"><span>%s</span><strong>%s</strong></a>' % (prev[0], ui["prev"], esc(prev[1])) if prev else ""
    b = '<a href="%s" class="next"><span>%s</span><strong>%s</strong></a>' % (nxt[0], ui["next"], esc(nxt[1])) if nxt else ""
    return '  <nav class="case-nav" aria-label="Case study navigation">%s%s</nav>\n' % (a, b)
def back(href, text):
    return '  <a href="%s" style="display:inline-flex;align-items:center;gap:0.5rem;color:#94a3b8;text-decoration:none;margin-bottom:3rem;font-size:0.9rem;transition:color 0.2s">%s</a>\n\n' % (href, text)
def wrap_main(inner):
    return ('<main style="max-width: 800px; margin: 0 auto; padding: 0 1.5rem;">\n<div style="max-width:800px;margin:0 auto;padding:4rem 1rem">\n\n'
            + inner + '\n</div>\n</main>')
def cta(label):
    return ('  <div style="margin-top:3rem;text-align:center"><a href="mailto:contact@franciscoaleuy.ca" style="display:inline-block;padding:1rem 2rem;'
            'border:1px solid rgba(56,189,248,0.4);color:#38bdf8;border-radius:100px;font-weight:600;text-decoration:none;font-size:1rem">%s</a></div>\n') % label

def shell_for(lg):
    path = (PRE[lg].lstrip("/") + "/" if PRE[lg] else "") + "work/soymanada/index.html"
    src = git_show(path)
    i = src.index("<main"); j = src.index("</main>") + len("</main>")
    return src[:i], src[i:j], src[j:]

def finish(lg, slug, head, mainhtml, tail, title, hidden=False):
    pre = PRE[lg]
    head = re.sub(r"<title>.*?</title>", lambda m: "<title>%s</title>" % esc(title), head, count=1, flags=re.S)
    if hidden:
        head = head.replace("<meta charset=\"UTF-8\">", "<meta charset=\"UTF-8\"><meta name=\"robots\" content=\"noindex,nofollow\">", 1)
    head = head.replace("</style>", CASE_BASE_CSS + LAB_EXTRA_CSS + "</style>", 1)
    head, n = re.subn(r'(\s*)(<a href="[^"]*#contact" class="nav-link highlight">)',
                      lambda m: '%s<a href="%s/lab/" class="nav-link">Product Lab</a>%s%s' % (m.group(1), pre, m.group(1), m.group(2)), head, count=1)
    assert n == 1, "nav insert failed for " + lg
    for l2, p2 in PRE.items():
        tgt = ("%s/lab/%s/" % (p2, slug)) if slug else ("%s/lab/" % p2)
        tail = tail.replace('href="%s/work/soymanada/"' % p2, 'href="%s"' % tgt)
    return head + mainhtml + tail

CASE_BASE_CSS = ""   # filled from the original English SoyManada stylesheet below
_orig = git_show("work/soymanada/index.html")
_a = _orig.index("@keyframes caseUp"); _e = ".case-nav a.next{text-align:right;margin-left:auto}"
CASE_BASE_CSS = _orig[_a:_orig.index(_e) + len(_e)]

def case_page(lg, slug):
    ui = UI[lg]; d = P[slug][lg]; st = P[slug]["status"]; pre = PRE[lg]
    body = back(pre + "/lab/", ui["back"])
    facts = ""
    for key, val in d["facts"]:
        wide = ' class="wide"' if key == "note" else ""
        facts += "<div%s><dt>%s</dt><dd>%s</dd></div>" % (wide, ui["f"][key], esc(val))
    body += ('  <header style="margin-bottom:4rem">\n    <span class="eyebrow">Product Lab</span>\n'
             '    <h1 style="font-size:2.3rem;line-height:1.2;color:#f8fafc;margin-bottom:.8rem">%s</h1>\n'
             '    <div class="hdr-status"><span class="status-badge %s">%s</span><p class="fig-note">%s</p></div>\n'
             '    <p class="case-tldr">%s</p>\n    <dl class="facts">%s</dl>\n    %s\n  </header>\n') % (
             esc(d["title"]), STATUS_CLS[st], ui["status"][st], ui["fig"], esc(d["summary"]), facts,
             metrics_html(d["metrics"]) if d.get("metrics") else "")
    body += sec(ui["h"]["problem"], "".join(para(x) for x in d["problem"]))
    disc = "".join(para(x) for x in d["discovery"])
    if d.get("discovery_bullets"): disc += blt(d["discovery_bullets"])
    body += sec(ui["h"]["discovery"], disc)
    body += sec(ui["h"]["decisions"], blt(d["decisions"]))
    body += sec(ui["h"]["built"], blt(d["built"]) + "<!-- screenshot slot: add captures here -->")
    body += sec(ui["h"]["status"], "".join(para(x) for x in d["status_text"]))
    body += sec(ui["h"]["next"], para(d["next"]))
    body += cta(ui["discuss"])
    published = [s for s in PUBLISHED if s != slug]
    if slug in PUBLISHED:
        ix = PUBLISHED.index(slug)
        prv = PUBLISHED[ix - 1] if ix > 0 else None
        nxt = PUBLISHED[ix + 1] if ix + 1 < len(PUBLISHED) else None
        pv = (pre + "/lab/%s/" % prv, P[prv][lg]["title"]) if prv else (pre + "/lab/", ui["lab"])
        nx = (pre + "/lab/%s/" % nxt, P[nxt][lg]["title"]) if nxt else (pre + "/lab/", ui["lab"])
        body += case_nav(pv, nx, ui)
    else:
        body += case_nav(None, (pre + "/lab/", ui["lab"]), ui)
    return body

def index_page(lg):
    ui = UI[lg]; pre = PRE[lg]
    cards = ""
    for slug in PUBLISHED:
        d = P[slug][lg]; st = P[slug]["status"]
        cards += ('  <a class="lab-card" href="%s/lab/%s/"><div class="lc-top"><h2>%s</h2><span class="status-badge %s">%s</span></div>'
                  '<p>%s</p><div class="stack-chips" style="margin:0 0 1rem">%s</div><span class="lc-go">%s</span></a>\n') % (
                  pre, slug, esc(d["title"]), STATUS_CLS[st], ui["status"][st], esc(d["summary"]),
                  "".join('<span class="chip">%s</span>' % esc(t) for t in d["tags"]), ui["read"])
    return ('  <header style="margin-bottom:3rem"><span class="eyebrow">%s</span>'
            '<h1 style="font-size:2.5rem;line-height:1.2;color:#f8fafc;margin-bottom:1rem">Product Lab</h1>'
            '<p class="case-tldr">%s</p></header>\n%s  <p class="fig-note">%s</p>\n') % (ui["idx_eyebrow"], ui["idx_tldr"], cards, ui["fig"])

SOY_H = {"en": ["Context &amp; Problem", "The Solution", "Technical Architecture", "Strategic Impact"],
         "es": ["Contexto y Problema", "La Solución", "Arquitectura Técnica", "Impacto Estratégico"],
         "fr": ["Contexte et Problème", "La Solution", "Architecture Technique", "Impact Stratégique"]}
SOY_PARITY = {
 "es": dict(eb="SaaS &middot; Tecnología migratoria", live="En vivo",
   tl="Los recién llegados hispanohablantes a Canadá no encontraban servicios verificados en su idioma, así que diseñé, construí y lancé un directorio trilingüe verificado. En solitario, de cero a producción.",
   m=[("3", "idiomas: enrutamiento completo ES / EN / FR-CA"), ("100%", "de los proveedores verificados manualmente antes de publicarse"), ("0 → 1", "fundador y desarrollador: de la estrategia al despliegue")],
   pi="Alineado con PIPEDA"),
 "fr": dict(eb="SaaS &middot; Technologie de l&rsquo;immigration", live="En ligne",
   tl="Les nouveaux arrivants hispanophones au Canada ne trouvaient pas de services vérifiés dans leur langue ; j&rsquo;ai donc conçu, construit et lancé un répertoire trilingue vérifié. En solo, de zéro à la mise en ligne.",
   m=[("3", "langues : routage complet ES / EN / FR-CA"), ("100 %", "des fournisseurs vérifiés manuellement avant la mise en ligne"), ("0 → 1", "fondateur et développeur : de la stratégie au déploiement")],
   pi="Conforme à PIPEDA")}

def soy_page(lg):
    ui = UI[lg]; pre = PRE[lg]
    head, m, tail = shell_for(lg)
    m, n1 = re.subn(r'<a href="[^"]*#(?:work|projects)"([^>]*)>[^<]*</a>', lambda x: '<a href="%s/lab/"%s>%s</a>' % (pre, x.group(1), ui["back"]), m, count=1)
    assert n1 == 1, ("soy back link", lg)
    new_h = [ui["h"]["problem"], ui["h"]["decisions"], ui["h"]["built"], ui["h"]["status"]]
    for old, new in zip(SOY_H[lg], new_h):
        assert m.count(">%s<" % old) == 1, (lg, old)
        m = m.replace(">%s<" % old, ">%s<" % new, 1)
    soy_chips = ""
    if lg != "en":
        X = SOY_PARITY[lg]
        hm = re.search(r'(<header[^>]*>\s*)(<h1[^>]*>)(.*?)(</h1>)(.*?)(</header>)', m, flags=re.S)
        assert hm, ("soy header", lg)
        m = (m[:hm.start()] + hm.group(1) + '<span class="eyebrow">%s</span>\n    ' % X["eb"] + hm.group(2) + hm.group(3)
             + '<span class="live-badge">%s</span>' % X["live"] + hm.group(4) + hm.group(5)
             + '<p class="case-tldr">%s</p>\n    %s\n  ' % (X["tl"], metrics_html(X["m"])) + hm.group(6) + m[hm.end():])
        soy_chips = "  " + chips_html(ui["chip"], ["React + Vite", "Supabase (PostgreSQL + RLS + Auth)", "i18next", "GitHub Actions CI/CD", X["pi"], "Multi-LLM pipeline"]) + "\n\n"
    m = m.replace("</h1>", "</h1>\n    <p class=\"fig-note\" style=\"margin:0 0 1rem\">%s</p>" % ui["fig"], 1)
    ix = PUBLISHED.index("soymanada")
    prv, nxt = PUBLISHED[ix - 1] if ix > 0 else None, PUBLISHED[ix + 1] if ix + 1 < len(PUBLISHED) else None
    cn = case_nav((pre + "/lab/%s/" % prv, P[prv][lg]["title"]) if prv else (pre + "/lab/", ui["lab"]),
                  (pre + "/lab/%s/" % nxt, P[nxt][lg]["title"]) if nxt else (pre + "/lab/", ui["lab"]), ui)
    m, n2 = re.subn(r'  ?<nav class="case-nav".*?</nav>\n?', lambda x: cn, m, count=1, flags=re.S)
    if n2 == 1: m = m.replace(cn, soy_chips + cn, 1)
    else:
        k = m.rindex("</div>\n</main>")
        m = m[:k] + soy_chips + cn + m[k:]
    return finish(lg, "soymanada", head, m, tail, "SoyManada — Francisco Aleuy")

# ------------------------------------------------------------------ build
def out_dir(lg, slug, hidden):
    if hidden: return "_lab-hidden/%s/%s/" % (lg, slug)
    return (PRE[lg].lstrip("/") + "/" if PRE[lg] else "") + "lab/" + (slug + "/" if slug else "")

for lg in ("en", "es", "fr"):
    head, _, tail = shell_for(lg)
    wr(out_dir(lg, "", False) + "index.html", finish(lg, "", head, wrap_main(index_page(lg)), tail, "Product Lab — Francisco Aleuy"))
    for slug in PUBLISHED + HIDDEN:
        hidden = slug not in PUBLISHED
        if slug == "soymanada":
            wr(out_dir(lg, slug, hidden) + "index.html", soy_page(lg)); continue
        wr(out_dir(lg, slug, hidden) + "index.html",
           finish(lg, slug, head, wrap_main(case_page(lg, slug)), tail, "%s — Francisco Aleuy" % P[slug][lg]["title"], hidden=hidden))
    # redirect stub at the old SoyManada URL
    old = (PRE[lg].lstrip("/") + "/" if PRE[lg] else "") + "work/soymanada/index.html"
    new_url = "%s/lab/soymanada/" % PRE[lg]
    wr(old, ('<!DOCTYPE html><html lang="%s"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">'
             '<title>SoyManada — Francisco Aleuy</title><link rel="canonical" href="https://franciscoaleuy.ca%s">'
             '<meta http-equiv="refresh" content="0; url=%s"><script>location.replace(%r);</script></head>'
             '<body style="background:#0f172a;color:#f8fafc;font-family:Inter,sans-serif;padding:3rem 1.5rem">'
             '<p>SoyManada moved to the Product Lab: <a href="%s" style="color:#38bdf8">%s</a></p></body></html>\n') % (lg, new_url, new_url, new_url, new_url, new_url))
    print("built", lg)
print("published:", PUBLISHED, "| hidden:", HIDDEN)
