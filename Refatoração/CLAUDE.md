# CLAUDE.md — Refatoração do GitHub Pages do Grupo 03 (IHC 2026.2 · Detran-DF)

Estas instruções valem para toda sessão do Claude Code neste repositório. O objetivo é **refatorar o site do grupo para que cumpra, da forma mais fiel possível, as regras da disciplina** de Interação Humano-Computador (FGA0173, UnB/FCTE, Prof. Dr. André Barros de Sales). Cada regra abaixo indica a fonte e a página de onde saiu. Quando houver dúvida sobre uma regra, vale o texto da fonte, não esta paráfrase.

---

## 0. Contexto

- **Site:** https://interacao-humano-computador.github.io/2026.2-Grupo03/ — MkDocs + Material for MkDocs. A navegação fica em `mkdocs.yml` e as páginas em `docs/`.
- **Objeto do projeto:** Portal do Detran-DF. O processo de design é a Engenharia de Usabilidade de Mayhew, e o planejamento das avaliações segue o framework DECIDE.
- **Equipe atual:** Alexandre Vilar Valadares Fonsêca, Gabriel Robson Nunes Neiva da Silva, Henrique Schneider Fernandes da Rosa e João Vitor Tavares de Sá Lima. Ex-integrantes: Camile Barbosa Gonzaga de Oliveira (só Entrega 1) e Eduardo Ribeiro Gomes da Silva (Entregas 1 e 2). **Pergunte** antes de alterar qualquer menção aos ex-integrantes.
- **Material de referência (fora do repositório):** a pasta local `IHC/` do Henrique tem o Plano de Ensino, os livros e os modelos citados aqui. Ver `IHC/LEIA-ME - Estrutura de Arquivos.md`. Se a pasta não estiver acessível, **não** invente o conteúdo dela: marque `[VERIFICAR]`.
- **Estado das entregas em 10/11/2026:** Entregas 1–6 entregues. A Entrega 7 (relato dos resultados do protótipo de alta fidelidade) vence em 15/11, com inspeção do Grupo +1 em 16/11 e apresentação em 17/11; a 8 vence em 22/11 e o Projeto Final em 30/11 (Plano de Ensino, pp. 4–6).
- **Branch e repositório:** o site é publicado da `main` do repositório `Interacao-Humano-Computador/2026.2-Grupo03`. O Henrique também tem o fork `SchneiderCode1/2026.2-Grupo03-Fork`.

---

## 1. Regras invioláveis

1. **Não invente conteúdo acadêmico.** Isso inclui citações, números de página, trechos “literais”, dados de avaliação, participantes, resultados, datas de reunião, links de vídeo, nomes de revisores e contribuições. Quando faltar informação, deixe um marcador visível e um comentário:
   `**[VERIFICAR: descrever o que falta]**` e `<!-- TODO(VERIFICAR): detalhe -->`.
   Motivo: “Qualquer atividade plagiada, será atribuída a nota zero ao estudante e/ou grupo” (Plano de Ensino, p. 2).
2. **Não altere autoria.** Não mude quem é autor ou revisor de um artefato, não apague linhas de histórico de versão nem de tabelas de contribuição. O histórico é só de acréscimo. “Cada artefato produzido pelo grupo e postado na Wiki deve ser identificado pelo(s) autor(es)” (Plano de Ensino, p. 2).
3. **Não reescreva o texto dos integrantes.** Você pode mudar formatação, estrutura, legendas, citações e referências, e corrigir ortografia. Mudança de conteúdo, argumento ou conclusão vai como sugestão no relatório (seção 9), não como edição.
4. **Declare o uso de IA.** Esta é a única forma de registro do uso do Claude: na página e no relatório, nunca como autor no histórico de versões nem no Git. Toda página que você editar ganha (ou atualiza) a seção “Agradecimentos e uso de IA generativa”, dizendo **o que** foi feito com o Claude e **onde**. A disciplina adota o Código de Conduta da SBC: a utilização de ferramentas de IA generativa “deve ser declarada explicitamente no trabalho” e a declaração “deve listar as ferramentas e descrever onde foram empregadas” (Plano de Ensino, p. 3).
5. **Não exponha a matrícula** de nenhum integrante. A página da equipe deve ter foto e nome, “sem matrícula” (Plano de Ensino, p. 8, item 1).
6. **Não quebre URLs publicadas.** Os links do site já estão em PDFs entregues no Moodle e em inspeções de outros grupos. Para renomear ou mover uma página, use o plugin `mkdocs-redirects` com o caminho antigo → novo, e **peça aprovação** antes.
7. **Git.** Trabalhe na branch `refatoracao/padrao-disciplina`, nunca direto na `main`, e não use `push --force`. Faça um commit por seção ou página, com mensagem em português (ex.: `docs(guia-estilo): padroniza legendas e referências ABNT`). **Os commits ficam na conta do Henrique**: autor e committer `Henrique Schneider Fernandes da Rosa <165057013+SchneiderCode1@users.noreply.github.com>` (e-mail *noreply* do GitHub, para não expor o e-mail pessoal num repositório público). **Não inclua o Claude como autor nem como coautor**: nada de `Co-Authored-By`, `Claude-Session` ou assinatura "Generated with Claude Code" em commits e PRs. Pela regra da SBC adotada no Plano de Ensino (p. 3), a ferramenta não é autora; o uso dela é declarado no conteúdo (regra 4) e no `REFATORACAO-RELATORIO.md`, não no Git. Faça os commits só depois de terminar o lote pedido e validar o build.
8. **Peça confirmação antes de:** criar ou remover páginas da navegação, mudar `mkdocs.yml`, mexer em mais de ~10 arquivos de uma vez, ou fazer qualquer coisa que dependa de uma decisão do grupo (por exemplo, a situação da Camile ou qual processo de design fica oficial).

---

## 2. Fluxo de trabalho

1. **Inventário.** Leia `mkdocs.yml` e liste todas as páginas de `docs/`, indicando para cada uma: entrega, autor(es) e quais elementos da seção 3 ela tem.
2. **Auditoria antes de editar.** Gere `REFATORACAO-RELATORIO.md` na raiz do repositório, **fora** de `docs/` e da navegação. Ele deve ter a matriz *item da lista de verificação × página × situação*, usando as respostas que a disciplina pede: **Conforme / Não conforme / Não se aplica** (enunciados das listas de verificação no Moodle). Mostre o relatório ao usuário e espere o “ok”.
3. **Correções mecânicas, página a página:** estrutura, histórico, legendas, citações, referências, seção de IA, links e imagens quebrados.
4. **Lacunas de conteúdo:** não preencha. **Desde 17/10/2026 o site publicado não mostra marcadores `[VERIFICAR]`:** o que falta sai da página (célula vazia vira "—") e é registrado em `pendencias/<entrega>.md`, com página, o que falta e responsável sugerido (seção 7). Os marcadores só aparecem nos modelos de `modelos/` e nos rascunhos de `pendencias/paginas-fora-do-site/`.
5. **Validação:** rode `mkdocs build --strict` (sem nenhum aviso), verifique links internos e imagens, e confira o tema claro/escuro.
6. **Fechamento:** atualize o relatório com o que mudou, o que falta e quem precisa agir. Abra um PR com esse resumo.

---

## 3. Modelo obrigatório de página de artefato

Baseado nos 11 “Itens do Desenvolvimento do projeto”, que valem para todas as entregas (Plano de Ensino, pp. 8–9, itens D1–D11).

```markdown
# <Título do artefato>

## Tabela de contribuição
<!-- D10: “Tabela de contribuição no início do artefato com o nome de todos os integrantes com a contribuição de cada integrante com hiperligação atividade e da gravação, se houver.” (Plano, p. 9) -->

**Tabela N – Contribuições no artefato <nome>**

| Integrante | Contribuição | Atividade (link) | Gravação (link) |
|---|---|---|---|
| Alexandre Vilar Valadares Fonsêca | … | … | … |
| Eduardo Ribeiro Gomes da Silva | … | … | … |
| Gabriel Robson | … | … | … |
| Henrique Schneider Fernandes da Rosa | … | … | … |
| João Vitor Tavares de Sá Lima | … | … | … |

Fonte: elaborado pelos autores (2026).

## Histórico de versões
<!-- D1 “histórico de versão padronizado” e D2 “autor(es) e revisor(es) para cada artefato” (Plano, p. 8) -->

**Tabela N – Histórico de versões do artefato <nome>**

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|

Fonte: elaborado pelos autores (2026).

## 1. Introdução
<!-- D5: “Um texto fazendo uma introdução dos artefatos” (Plano, p. 8) -->

## 2…n. <Conteúdo>
<!-- Cada item de conteúdo da disciplina: referência + foto do texto + autor do item (seção 5.4) -->

## Referências bibliográficas
<!-- D3: referências em todos os artefatos (Plano, p. 8); formato NBR 6023 (seção 5.5) -->

## Agradecimentos e uso de IA generativa
<!-- D11 (Plano, p. 9) + Código de Conduta SBC (Plano, p. 3) -->
```

Regras do modelo:
- **Todo integrante aparece na tabela de contribuição.** Quem não contribuiu fica com `[VERIFICAR: contribuição]`; não apague a linha. Pelo Plano de Ensino (p. 2), o integrante que não participa de uma entrega recebe nota zero nela, por isso a ausência precisa ficar visível para o grupo resolver.
- O título da tabela de histórico tem de corresponder ao artefato da página. Exemplo de erro já encontrado: a página de storyboard do Henrique usa a legenda “Documento de Análise de Tarefas”.

---

## 4. Padrão do histórico de versões

Adaptado dos itens “Geral” da lista de verificação de qualidade de artefatos (`Modelo - Lista de Verificação da Qualidade de Artefatos.xls`, aba “Estória de Usuário”, itens 3 e 6).

- Colunas fixas, nesta ordem: `Data | Versão | Descrição | Autor(es) | Revisor(es)`.
- Data no formato `DD/MM/AAAA`. Versão `X.Y`: `1.0` na criação, `+0.1` para ajustes e `+1.0` para revisão ou reestruturação ampla.
- A versão deve ser incrementada e a alteração registrada no histórico (item 3). A versão mais recente do histórico corresponde ao estado atual da página (item 6).
- A descrição começa com verbo no particípio ou substantivo de ação (“Criação…”, “Inclusão…”, “Padronização…”).
- **Revisor com nome próprio**, nunca “Integrantes do grupo”, “-” ou “A definir”. Se ainda não existe revisor, use `[VERIFICAR: revisor]`. O revisor não pode ser o autor da mesma versão. Esse foi um item da própria lista do grupo na inspeção da Entrega 3: “nenhum integrante seja revisor do próprio trabalho no mesmo ciclo” (Relatório de Inspeção Entrega 3, item 12).
- Toda edição sua acrescenta uma linha. Exemplo:
  `| 16/10/2026 | 2.1 | Padronização de legendas, citações e referências (ABNT) e inclusão da seção de uso de IA | Henrique Schneider | — |`
  O autor da linha é o integrante que pediu a mudança (a IA não é autora; Plano de Ensino, p. 3). Revisor ainda não definido fica "—" no site e vai para `pendencias/`.

---

## 5. Citações, ilustrações e referências (ABNT)

Fonte das normas: PUC MINAS. *Orientações para elaboração de projetos de pesquisa, trabalhos acadêmicos, relatórios técnicos e/ou científicos e artigos científicos: conforme a ABNT*. Belo Horizonte, 2025 (`Guia - ABNT - …pdf`). As páginas citadas são as impressas no guia.

### 5.1 Citação indireta (paráfrase)
É “a apresentação das ideias de um autor consultado. Não se transcreve o texto, apenas utilizam-se as ideias que constam nele” (PUC Minas, 2025, p. 177). Indique autor e ano. **Regra extra do grupo:** inclua sempre capítulo, seção, página e, quando possível, o parágrafo, para garantir a rastreabilidade.
Formato padrão: `(Barbosa; Silva, 2010, cap. 9, seç. 9.8, p. 313)` ou, na narrativa, `Barbosa e Silva (2010, p. 313)`.

### 5.2 Citação direta curta (até 3 linhas)
Vai entre aspas duplas e precisa da página: “A citação direta curta, de até três linhas, é inserida na sequência normal do texto entre aspas duplas” (PUC Minas, 2025, p. 178).

### 5.3 Citação direta longa (mais de 3 linhas) e citação de citação
- A citação longa “é recuada a 4 cm da margem esquerda, tamanho da fonte 10, espaço entre linhas simples e sem aspas” (PUC Minas, 2025, p. 179). No MkDocs, use bloco de citação (`>`) **sem aspas**, com a referência no fim.
- Para fonte original não consultada, use `apud` (PUC Minas, 2025, p. 185). Exemplo: `(Mayhew, 1999 apud Barbosa; Silva, 2010, p. 110)`.
- Só use citação direta copiando **literalmente** do material. Se não conseguir conferir o texto original, transforme em paráfrase ou marque `[VERIFICAR: conferir trecho e página]`.

### 5.4 Itens de conteúdo da disciplina: referência + foto + autor
O Plano de Ensino exige, item por item, “referência bibliográfica da fonte e foto do texto da referência” e o “Autor” do item (pp. 9–13). Também afirma que “Todos os integrantes da equipe devem elaborar itens de conteúdo da disciplina” (p. 9) e que cada um deve fazer “ao menos um 1 item de conteúdo da disciplina” por entrega (pp. 11–13). Cada item segue este padrão:

```markdown
### <Nome do item>
**Autor do item:** <Integrante>

<texto com citação (Autor, ano, cap., p.)>

**Figura N – Trecho de Barbosa e Silva (2010, cap. 9, p. 313) sobre o framework DECIDE**

![Fotografia da página 313 de Barbosa e Silva (2010) com a descrição das atividades do DECIDE](../assets/referencias/barbosa-silva-2010-p313.png)

Fonte: Barbosa e Silva (2010, p. 313).
```

- Salve as fotos em `docs/assets/referencias/` com o nome `<autor>-<ano>-p<página>.png`, em minúsculas e sem acento.
- **Você não tira fotos.** Se a imagem não existir, deixe o bloco com `[VERIFICAR: foto da p. X]` e liste a pendência no relatório.
- Corrija placeholders e divergências que já existem. Exemplo encontrado na página de Perfis e Personas: `caminho_imagem_p136_p175.png` e uma legenda que diz “p. 136” com link para `p135`.

### 5.5 Ilustrações e tabelas
Segundo o guia (PUC Minas, 2025, p. 17):
- A identificação vai **acima**: “Indique o nome da ilustração (… quadro, figura, imagem, tabelas …) na parte superior … seguido por uma indicação numérica sequencial em algarismos arábicos, separado por hífen e o título”. No site: `**Tabela 3 – Metas de usabilidade selecionadas**`.
- A fonte vai **abaixo**: “Na parte inferior da ilustração, indique a fonte consultada”. Material próprio usa `Fonte: elaborado pelos autores (2026).`
- “Não citar endereços eletrônicos como fonte”: a URL aparece só nas referências.
- A ilustração deve ficar “o mais próximo possível da informação a que se referem”, e o texto deve chamá-la (“conforme a Tabela 3”). Isso atende ao D4: “As tabelas e imagens possuem legenda e fonte e elas chamadas dentro do texto?” (Plano de Ensino, p. 8).
- A numeração é sequencial **dentro de cada página**, com séries separadas para Tabela, Figura e Quadro.
- Toda imagem tem texto alternativo (`![descrição]`), que é requisito básico de acessibilidade e coerente com o tema da disciplina.

### 5.6 Referências (NBR 6023)
Use o sobrenome em maiúsculas e o título em itálico (`*…*`). A lista vem em ordem alfabética e só inclui obras citadas na página. Formas de referência já conferidas nos arquivos:

```
BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador*. Rio de Janeiro: Elsevier, 2010.
BARBOSA, Simone Diniz Junqueira et al. *Interação Humano-Computador e Experiência do Usuário*. Rio de Janeiro: Simone Diniz Junqueira Barbosa, 2021. E-book.
SALES, André Barros de. *Plano de Ensino: Interação Humano Computador (FGA0173), 02/2026, Turma 01, v1*. Brasília: Universidade de Brasília, 2026.
PONTIFÍCIA UNIVERSIDADE CATÓLICA DE MINAS GERAIS. Sistema Integrado de Bibliotecas. *Orientações para elaboração de projetos de pesquisa, trabalhos acadêmicos, relatórios técnicos e/ou científicos e artigos científicos: conforme a Associação Brasileira de Normas Técnicas (ABNT)*. Belo Horizonte: PUC Minas, 2025.
DEPARTAMENTO DE TRÂNSITO DO DISTRITO FEDERAL. *Portal do Detran-DF*. Brasília, DF, 2026. Disponível em: https://www.detran.df.gov.br/. Acesso em: <dd mmm. aaaa>.
```

- Para Preece, Rogers e Sharp (*Design de Interação*), confira a edição, a editora e o ano na folha de rosto antes de padronizar. O grupo usa a 1ª ed. (2005) e a 3ª ed. Marque `[VERIFICAR]` se não for possível conferir.
- Vídeos (Klemmer, YouTube) usam a forma de documento audiovisual online: `TÍTULO. Local: Produtor, ano. 1 vídeo (min). Disponível em: … Acesso em: …`.
- **Unifique** as formas divergentes: “Barbosa & Silva”, “BARBOSA e SILVA” e “Simone Diniz” passam todas para o formato acima.

---

## 6. Requisitos por seção do site

Para cada requisito, verifique se a página atende e registre o resultado no relatório. Entre parênteses está o item da lista de verificação e a página do Plano de Ensino.

### 6.1 Início / Equipe / Geral (Entrega 1, itens do Planejamento Geral, p. 8)
- Página dos integrantes **com foto**, com nome e sem matrícula (item 1). Gabriel deve estar incluído.
- Cronograma com **todas as atividades de todas as etapas para cada integrante**, com datas de início e fim e com o período de revisão (item 2). Também precisa do **período de gravação** de cada etapa (item 3) e de um **período de revisão/ajustes** após as considerações dos monitores e do professor (item 4).
- Motivação e critérios da escolha do site (item 5). Planejamento e avaliação dos sites selecionados (item 6).
- **Opção de contraste de cores** (item 7). No Material for MkDocs, configure `theme.palette` com os esquemas `default` e `slate` e um `toggle` de alternância, e confira o contraste dos dois.
- Página de **atas com acesso à gravação** (item 9). Ver seção 6.7.
- **Cronograma executado** com quem realizou cada artefato e as datas reais (D6, p. 8). Mantenha-o separado do planejado.
- **Processo de design:** precisa ter justificativa (Itens do conteúdo, p. 9). O relatório da Entrega 1 chama de “Processo de Design Selecionado” tanto o DECIDE quanto a Engenharia de Usabilidade de Mayhew. Proponha ao usuário, **sem aplicar sozinho**, este texto: Mayhew é o *processo de design* (Barbosa; Silva, 2010, cap. 4, Fig. 4.7, p. 110) e o DECIDE é o *framework de planejamento das avaliações* (Barbosa; Silva, 2010, seç. 9.8, pp. 312–313).

### 6.2 Perfil de Usuário, Personas, Cenários, Análise de Tarefas e Aspectos Éticos (Entrega 2, pp. 9–11)
- Perfil definido por **mais de uma técnica** de elicitação ou ferramenta (item 1).
- Atributos do perfil (item 2) e os **4 grupos de atributos**: idade, experiência, atitudes (tecnófilos/tecnófobos) e tarefas primárias (item 3). Fonte: Barbosa e Silva (2010, cap. 6, p. 175).
- Aspectos éticos (item 4) e os **4 princípios**: autonomia, beneficência, não maleficência e justiça/equidade (item 5). Fonte: Barbosa e Silva (2010, seç. 5.4, pp. 138–139).
- Pedido de permissão antes de gravar (item 6) e **TCLE** (item 7). Fonte: Barbosa e Silva (2010, p. 140).
- No mínimo **duas técnicas de coleta de dados** (item 8). O site tem páginas de entrevistas e questionários: confira se trazem dados reais e não modelos vazios.
- **Cenários** (item 9). Um cenário é “uma história sobre pessoas realizando uma atividade” (Barbosa; Silva, 2010, seç. 6.3, p. 183).
- **Análise de tarefas** (item 10), com **uma atividade por integrante modelada em pelo menos duas técnicas**: HTA (diagrama, legenda e tabela) e GOMS ou CTT (item 11). Fonte: Barbosa e Silva (2010, seç. 6.4, pp. 192–203).
- Personas, incluindo a persona primária (Barbosa; Silva, 2010, seç. 6.2, pp. 176–180).

### 6.3 Princípios Gerais, Metas de Usabilidade e Guia de Estilo (Entrega 3, pp. 11–12)
- **Características da plataforma** (item 10).
- Os **tópicos dos princípios gerais**, na ordem (item 12). O Plano numera 8 itens e agrupa “consistência e padronização” com “promoção da eficiência do usuário” no item 4: correspondência com as expectativas dos usuários; simplicidade nas estruturas das tarefas; equilíbrio entre controle e liberdade do usuário; consistência e padronização; promoção da eficiência do usuário; antecipação das necessidades do usuário; visibilidade e reconhecimento; conteúdo relevante e expressão adequada; projeto para erros. Fonte: Barbosa e Silva (2010, cap. 8, p. 265).
- **Metas de usabilidade** com referência (item 13) e com a **razão da seleção** (item 14). Fatores de usabilidade: Barbosa e Silva (2010, cap. 2, pp. 28–29).
- **Guia de estilo** com a estrutura de 6 partes do Plano (item 16): introdução; resultados de análise; elementos de interface; elementos de interação; elementos de ação; vocabulário e padrões. Fonte: Barbosa e Silva (2010, cap. 8, p. 283), a partir de Marcus (1992) e Mayhew (1999).
- O guia de estilo deve **corresponder ao site avaliado** (item 17).

### 6.4 Planejamento da Avaliação do Storyboard e da Análise de Tarefas (Entrega 4, pp. 12–13)
- Seguir o **DECIDE** (item 2), com as atividades D-E-C-I-D-E (Barbosa; Silva, 2010, seç. 9.8, pp. 312–313).
- Objetivos (item 3), métodos com referência (item 4), questões práticas como recrutamento, quantidade e justificativa, local, equipamentos, prazos, orçamento e pessoal (item 5), e questões éticas (item 6).
- **Estrutura do relatório de resultados** (item 7), conforme Barbosa e Silva (2010, seç. 9.7.5, pp. 311–312): objetivos e escopo; método; número e perfil de usuários e avaliadores; sumário dos dados com tabelas e gráficos; interpretação; lista de problemas; planejamento do reprojeto.
- **Cronograma com data, horário e local** da avaliação (item 8).
- **Cada quadro do storyboard ligado a uma especificação da análise de tarefas** (item 9).
- **Número de storyboards igual ao número de integrantes** (item 10). ⚠ O site tem páginas para Alexandre, Gabriel, Henrique e João Vitor; **falta a do Eduardo**. Crie só o esqueleto com `[VERIFICAR]` e avise.
- **Teste piloto definido e com data** (item 11), com referência a Barbosa e Silva (2010, p. 307), e **sem** os resultados do piloto entrando nos resultados da avaliação (item 12).
- Itens que o avaliador deve anotar durante a sessão (item 13).
- Uniformize as quatro ou cinco páginas individuais: mesma estrutura de seções, mesmas legendas e mesmo histórico.
- Encurte o título da navegação “Planejamento de Storyboard, Análise de Tarefas e Planejamento de Relatos, Análise de Tarefas”. Sugestão: “Planejamento da Avaliação (Storyboard e Análise de Tarefas)”. **Peça aprovação** e use redirect se o slug mudar.

### 6.5 Entregas 5 a 8 e Projeto Final (estrutura apenas)
- Pode criar **esqueletos** de página com o modelo da seção 3 e marcadores `[VERIFICAR]`, **sem conteúdo inventado**.
- **Entrega 5:** relato dos resultados do storyboard e da análise de tarefas, seguindo a estrutura de p. 312, e planejamento da avaliação do protótipo de papel (Barbosa; Silva, 2010, seç. 10.2.3, p. 358).
- **Entregas 6 e 7:** relato do protótipo de papel, planejamento e relato do protótipo de alta fidelidade.
- **Entrega 8:** verificação de todos os artefatos. Use o relatório da seção 9 como base.
- **Projeto Final:** a página precisa cobrir os **14 tópicos** do Plano de Ensino (p. 7), entre eles: tabelas de ferramentas, técnicas, artefatos por integrante, avaliações, vídeos com participantes, facilidades e dificuldades por integrante, e IA generativa com vantagens e desvantagens. A apresentação dura de 20 a 30 minutos (p. 8).

### 6.6 Verificação / Inspeções
- Cada página de inspeção traz os itens do Plano de Ensino com **Resposta (Sim/Não/Incompleto)**, **evidência** (minuto do vídeo ou link) e **versão, data e hora da avaliação**, como nas tabelas do Plano (pp. 8–13).
- Os itens extras criados pelo grupo trazem **fonte com página** e **autor do item**.

### 6.7 Atas (`docs/atas/`)
Siga o modelo de ata do MCTIC (`SiglaProjeto_AtaReuniao_AAAAMMDD_XX`) e o item D7 do Plano (p. 9: “data, horário de início e do final, participantes, objetivo, atividades definidas etc”):
1. **Identificação:** data; início e término (previsto e realizado); local; redator; convocados e presentes; link da gravação (D8).
2. **Objetivo.**
3. **Pauta:** nº e descrição.
4. **Pendências anteriores:** pendência, responsável e data.
5. **Assuntos tratados:** nº, descrição e tipo (Apresentação / Decisão / Definição / Solicitação / Pendência).
6. **Compromissos / atividades definidas:** compromisso, responsável e data.
7. **Próxima reunião.**

As duas atas existentes (27/09 e 14/10) não seguem todos esses campos: a Reunião 01 não tem objetivo nem atividades definidas. Complete a estrutura e marque `[VERIFICAR]` no que faltar. Não invente horários nem decisões.

### 6.8 Apresentações
- Os vídeos devem estar no YouTube como **“não listado”** (D9, p. 9). Liste os links por entrega, com os integrantes que aparecem em cada vídeo; o Projeto Final pede essa tabela (Plano, p. 7). Não presuma a visibilidade do vídeo: marque `[VERIFICAR: não listado?]`.

---

## 7. Responsáveis sugeridos para as pendências (apenas para o relatório)

Use o cronograma do grupo (Relatório Entrega 1, §4) e `IHC/Tarefas por Integrante.md` para sugerir quem resolve cada pendência. Por exemplo: o storyboard do Eduardo fica com Eduardo; revisores ausentes ficam com o autor da página, que indica um revisor. **Não** escreva esses nomes nas páginas do site.

---

## 8. Padrões técnicos do repositório

- `mkdocs build --strict` deve passar sem avisos. Nenhum link interno ou imagem pode estar quebrado.
- Use caminhos relativos para imagens e links. Assets ficam em `docs/assets/` (fotos de referência em `docs/assets/referencias/`).
- Páginas novas usam slug em minúsculas, com hífen e sem acento. Páginas existentes mantêm o slug (seção 1, item 6).
- Títulos seguem a hierarquia `#` → `##` → `###`, sem pular níveis, e só há um `#` por página.
- Idioma `pt-BR` (`theme.language: pt-BR`).
- Os itens “Geral” da checklist de qualidade de artefatos (aba “Estória de Usuário”, itens 1–12) valem como *definition of done* de cada página:
  - formatação conforme o modelo;
  - versão incrementada e coerente com o histórico;
  - sem erros de pontuação ou gramática;
  - **sem textos auxiliares ou de exemplo esquecidos** (como “A preencher”, “Lorem”, `caminho_imagem…`);
  - itens não usados marcados como **“Não se aplica”**.

---

## 9. Relatório de refatoração (`REFATORACAO-RELATORIO.md`)

Fica na raiz, fora da navegação do site, e tem quatro partes:
1. **Resumo:** páginas auditadas, páginas alteradas e número de pendências por tipo.
2. **Matriz de conformidade:** item da lista (D1–D11 e os itens de conteúdo de cada entrega) × página → Conforme / Não conforme / Não se aplica, com evidência (arquivo e linha).
3. **Pendências humanas:** fotos de referência, revisores, links de vídeo, conteúdo faltante, decisões do grupo. Cada uma com página, o que falta e o responsável sugerido.
4. **Sugestões de conteúdo** que não foram aplicadas (seção 1, item 3).

---

## 10. Problemas já identificados em 15/10/2026 (confirmar antes de corrigir)

Lista feita por leitura automática do site publicado. Pode estar desatualizada.

- Revisores genéricos ou vazios nos históricos (“Integrantes do grupo”, “-”, “A definir”, “A preencher”).
- Páginas sem introdução e sem a seção de uso de IA (por exemplo, `storyboard/planejamento/Henrique_Schneider/`).
- Tabelas de cronograma sem legenda nem numeração. Legenda da Tabela 1 que não corresponde à página de storyboard.
- Perfis e Personas: imagens de referência que não aparecem, um placeholder `caminho_imagem_p136_p175.png` e a divergência p. 136 × arquivo `p135`.
- Falta a página de planejamento do storyboard do Eduardo.
- Título longo e repetido na navegação da Entrega 4.
- Página `apresentacoes/` fora da navegação lateral.
- Ata da Reunião 01 sem objetivo e sem atividades definidas.
- Inconsistência DECIDE × Mayhew como “processo de design” no material da Entrega 1.

---

## 11. Padrões adotados dos sites de outros grupos (10/11/2026)

O Henrique pediu para basear o site nos pontos positivos dos Grupos 05, 06 e 07 (https://interacao-humano-computador.github.io/2026.2-Grupo05/, .../2026.2-Grupo06/ e .../2026.2-Grupo07/). Mantenha estes padrões em todas as páginas novas. Não copie código nem texto desses grupos: reimplemente.

1. **Acessibilidade no cabeçalho** (Grupos 05 e 06): barra própria em `docs/javascripts/acessibilidade.js` (A−, A+, A, AC), estilos no fim de `docs/stylesheets/extra.css`. Toda página nova deve continuar legível com alto contraste ligado: confira com Playwright.
2. **Visão geral por entrega** (Grupo 06): cada aba começa em `docs/entrega-N/index.md` (`navigation.indexes`), com tabela de contribuição, histórico, introdução com o escopo literal do Plano, datas, tabela das páginas do grupo e tabela do material de cada integrante. Ao publicar páginas novas, atualize a tabela da visão geral.
3. **Mesma estrutura e mesmos nomes de arquivo para todos os integrantes** (Grupo 06): `docs/entrega-N/integrantes/<slug>/` com `index.md` e os artefatos com o mesmo nome em todos (ex.: `prototipo-papel.md`, `planejamento-alta-fidelidade.md`, `video-avaliacao.md`). No menu, "Material dos integrantes" sempre em ordem alfabética: Alexandre Vilar, Gabriel Robson, Henrique Schneider, João Vitor.
4. **Páginas do grupo em todas as entregas**, na ordem: Visão geral, Relatório da entrega (resumo), Relatório do grupo (transcrição do Google Docs), Contribuições, Verificação (lista e inspeção do Grupo +1), Material dos integrantes.
5. **Vídeos** (Grupos 05 e 06): toda gravação vai para a Tabela 3, 4 ou 5 de `docs/apresentacoes.md` e as apresentações também para a seção 5, em bloco recolhível com `youtube-nocookie` (classe `g03-video`).
6. **Introdução em toda página:** se a primeira seção já for de contexto, objetivo ou escopo, use "1. Introdução: <título original>" e acrescente uma frase de apresentação; caso contrário, inclua "## Introdução" antes das seções numeradas. Não renumere seções nem tabelas existentes (há remissões a "seção N" e "Tabela N" dentro e fora das páginas).

## 12. Organização da próxima entrega

Ao terminar uma entrega, prepare a seguinte, sem inventar conteúdo:

1. Crie `docs/entrega-N/index.md` (visão geral) com escopo literal e datas do Plano de Ensino, cronograma de cada integrante transcrito dos planejamentos da entrega anterior (sem alterar datas), estrutura exigida do artefato com a fonte e o roteiro de publicação. Inclua só essa página no menu.
2. Crie `modelos/entrega-N/` (fora de `docs/`) com os modelos da seção 3 para as páginas do grupo, a inspeção do Grupo +1 e as páginas de cada integrante, com `[VERIFICAR]` em tudo que depende de dado real, e um `README.md` com o destino de cada modelo e o trecho do `mkdocs.yml`.
3. Crie `pendencias/entrega-N.md` com prazos (Moodle, inspeção, apresentação, atividades individuais) e responsáveis sugeridos.
4. Quando um integrante publicar a página, ela entra no menu e na tabela da visão geral; os marcadores saem e o que faltar vai para `pendencias/`.
5. Feche a entrega anterior: publique a página-resumo, o relatório do grupo (transcrito do Google Docs, sem reescrever) e as contribuições; passe o normalizador de formato nas páginas individuais (seção 11) e registre tudo no `REFATORACAO-RELATORIO.md`.

Estado em 10/11/2026: a Entrega 7 está organizada (`docs/entrega-7/index.md`, `modelos/entrega-7/`, `pendencias/entrega-7.md`); a Entrega 8 (verificação dos artefatos, 22/11) ainda não.

## Histórico de versões

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 15/10/2026 | 1.0 | Criação das instruções a partir do Plano de Ensino, de Barbosa e Silva (2010), do guia ABNT da PUC Minas (2025), do modelo de ata do MCTIC, da checklist de qualidade de artefatos e de uma leitura do site publicado | Claude (IA generativa, Anthropic), a pedido de Henrique Schneider | [VERIFICAR: revisor] |
| 10/11/2026 | 2.0 | Equipe e estado das entregas atualizados; commits na conta do Henrique sem coautoria do Claude (regra 7); autoria das linhas de histórico (seção 4); marcadores fora do site (seção 2); seções 11 (padrões dos Grupos 05, 06 e 07) e 12 (organização da próxima entrega) | Henrique Schneider | — |
