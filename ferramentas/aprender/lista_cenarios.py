#!/usr/bin/env python3
"""Gera a Lista de Verificação – Cenários (PDF para o Aprender e página Markdown do site).

Uso: python3 lista_cenarios.py --slides DIR_COM_slideNN.jpg [--matricula 000000000]
Saídas: ./saida/<nome>.pdf e ./saida/lista-cenarios.md (+ imagens)
"""
import argparse, html, os, shutil, asyncio

AUTOR = "Henrique Schneider Fernandes da Rosa"
NOME_ARQ = "Grupo03HenriqueSchneiderVerifacaçãoListaCenários.pdf"
FONTE = "Barbosa e Silva (2010), cap. 6, seç. 6.3, slides do cap. 6"

# (pergunta, slide, complemento da fonte, caixa de recorte em frações ou None)
ITENS = [
 ("O cenário é apresentado como uma narrativa, textual ou pictórica, concreta e rica em detalhes contextuais, de uma situação de uso da aplicação (e não como uma lista de funcionalidades ou de requisitos)?", 9, "", None),
 ("O cenário é uma história sobre pessoas realizando uma atividade, isto é, envolve usuários, processos e dados reais ou potenciais?", 10, "seç. 6.3", (0, 0.2, 1, 0.56)),
 ("O artefato deixa claro para que o cenário foi elaborado: descrever uma história num domínio de atividade (para capturar requisitos e auxiliar no entendimento da atividade), levantar questões sobre a introdução de tecnologia, explorar diferentes soluções de design ou avaliar se um produto satisfaz a necessidade dos seus usuários?", 10, "seç. 6.3", (0, 0.2, 1, 0.74)),
 ("O cenário descreve o ambiente ou contexto, isto é, os detalhes da situação que motivam ou explicam os objetivos, as ações e as reações dos atores?", 11, "", (0.1, 0.24, 1, 0.36)),
 ("O cenário identifica os atores, isto é, as pessoas que interagem com o computador ou com outros elementos do ambiente, com as características pessoais relevantes ao cenário?", 11, "", (0.1, 0.34, 1, 0.5)),
 ("O cenário declara os objetivos dos atores, isto é, os efeitos desejados na situação que motivam as ações realizadas por eles?", 11, "", (0.1, 0.49, 1, 0.6)),
 ("O cenário registra o planejamento, isto é, a atividade mental dirigida para transformar um objetivo em um comportamento ou conjunto de ações?", 11, "", (0.1, 0.6, 1, 0.71)),
 ("O cenário descreve as ações (comportamento observável dos atores) e os eventos (ações externas ou reações produzidas pelo computador ou por outras características do ambiente)?", 11, "", (0.1, 0.7, 1, 0.87)),
 ("O cenário registra a avaliação, isto é, a atividade mental dirigida para interpretar a situação?", 11, "", (0.1, 0.86, 1, 0.96)),
 ("Depois da narrativa, há uma análise do cenário que lista os pontos que podem ser considerados problemáticos e que devem ser considerados em um reprojeto de IHC (por exemplo, transcrição manual de dados, falta de integração com outras informações, impossibilidade de realizar uma ação pelo próprio sistema)?", 13, "slide com a “Análise dos cenários”", None),
 ("O cenário foi refinado pelo questionamento sistemático (Carroll et al., 1994), segmentando-o em proposições e fazendo as perguntas “Por quê?”, “Como?” e “O que é?”, cujas respostas trazem, respectivamente, as condições, as consequências e os estados anteriores ou posteriores da atividade; os detalhes da sequência de ações; e os objetos e seus atributos?", 14, "Tabela 6.1", None),
 ("O cenário foi verificado com perguntas de resposta sim ou não — “<X> pode ser feito da maneira <Y>?” e “<X> faz parte de <Y>?” — para avaliar se uma ação ou atributo está bem definido e localizado no nível certo da hierarquia?", 14, "Tabela 6.1", (0, 0.6, 1, 1)),
 ("Para cada elemento do cenário (objetivo, ambiente, atores e planejamento) foram feitas as perguntas da Tabela 6.2 (por exemplo, para o objetivo: por que os atores querem ou precisam alcançá-lo e quais as precondições; para o ambiente: em que situações o cenário ocorre, quando, onde e por quê)?", 15, "Tabela 6.2", None),
]

REFS = [
 "BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador*. Rio de Janeiro: Elsevier, 2010.",
 "CARROLL, John M. et al. Scenario-based design: envisioning work and technology in system development. In: *Proceedings of the ACM Conference on Human Factors in Computing Systems*. 1994. Consulta indireta (Carroll et al., 1994 apud Barbosa; Silva, 2010).",
 "SALES, André Barros de. *Plano de Ensino: Interação Humano Computador (FGA0173), 02/2026, Turma 01, v1*. Brasília: Universidade de Brasília, 2026.",
]
# a referência de Carroll et al. só é conferida pela citação indireta; ver nota na página
REFS = [REFS[0], REFS[2]]

def recorta(src, dst, box):
    from PIL import Image
    im = Image.open(src).convert('RGB'); w,h = im.size
    if box: im = im.crop((int(box[0]*w), int(box[1]*h), int(box[2]*w), int(box[3]*h)))
    im.save(dst, quality=85, optimize=True)

def fonte(slide, comp):
    return f"{FONTE}, slide {slide}" + (f", {comp}" if comp else "")

def build(slides_dir, out_dir, matricula=None, data="10/11/2026"):
    os.makedirs(out_dir, exist_ok=True); img_dir = os.path.join(out_dir, "imagens"); os.makedirs(img_dir, exist_ok=True)
    esc = html.escape
    cab = f"""<table class="cab"><tr><td><b>Disciplina:</b> Interação Humano Computador (FGA0173), 2026.2, Turma 01<br><b>Professor:</b> Prof. Dr. André Barros de Sales<br><b>Atividade:</b> Atividade Avaliativa (Individual) – Elaborar uma lista de verificação – Cenários</td>
    <td><b>Estudante:</b> {AUTOR}<br>{('<b>Matrícula:</b> '+esc(matricula)+'<br>') if matricula else ''}<b>Grupo:</b> 03 (Detran-DF)<br><b>Data:</b> {data}</td></tr></table>"""
    h = [f"""<html><head><meta charset="utf-8"><style>
    @page {{ size:A4; margin:16mm 15mm 16mm 15mm }}
    body {{ font-family: Arial, Helvetica, sans-serif; font-size:10.5pt; line-height:1.38; color:#111 }}
    h1 {{ font-size:17pt; margin:0 0 6px; color:#0b3d6e }} h2 {{ font-size:13pt; color:#0b3d6e; border-bottom:1px solid #9bb; padding-bottom:2px; margin-top:16px }}
    table {{ border-collapse:collapse; width:100% }} th,td {{ border:1px solid #888; padding:4px 6px; vertical-align:top; font-size:9.5pt }} th {{ background:#e6eef6 }}
    .cab td {{ border:1px solid #444; width:50%; font-size:10pt }}
    .item {{ page-break-inside:avoid; margin:10px 0 14px }} .q {{ font-weight:bold }} .res {{ margin:4px 0; font-size:10pt }}
    figure {{ margin:6px 0 0 }} figcaption.t {{ font-size:9pt; font-weight:bold; margin-bottom:3px }} figcaption.f {{ font-size:8.5pt; color:#333; margin-top:2px }}
    img {{ max-width:70%; max-height:105mm; border:1px solid #999 }} .nota {{ font-size:9pt; color:#333 }}
    </style></head><body>
    <h1>Lista de Verificação – Cenários</h1>{cab}
    <h2>Histórico de versões</h2>
    <p class="nota"><b>Tabela 1 – Histórico de versões do artefato Lista de Verificação – Cenários</b></p>
    <table><tr><th>Data</th><th>Versão</th><th>Descrição</th><th>Autor(es)</th><th>Revisor(es)</th></tr>
    <tr><td>{data}</td><td>1.0</td><td>Criação da lista de verificação (13 itens)</td><td>{AUTOR}</td><td>—</td></tr></table>
    <p class="nota">Fonte: elaborado pelo autor (2026).</p>
    <h2>1. Introdução</h2>
    <p>Esta lista de verificação serve para inspecionar o artefato <b>Cenários</b> de um projeto de IHC. Tem {len(ITENS)} itens, todos fundamentados em Barbosa e Silva (2010), capítulo 6, seção 6.3, conforme os slides do capítulo 6, que reproduzem as páginas do livro. Cada item é uma pergunta completa, que traz os elementos a serem aferidos no artefato e se responde com <b>Conforme</b>, <b>Não conforme</b> ou <b>Não se aplica</b>. Abaixo de cada item estão a fonte e a foto do texto que o fundamenta (SALES, 2026).</p>
    <h2>2. Itens da lista</h2>"""]
    for i,(q,s,comp,box) in enumerate(ITENS,1):
        recorta(os.path.join(slides_dir,f"slide{s:02d}.jpg"), os.path.join(img_dir,f"{i:02d}.jpg"), box)
        h.append(f"""<div class="item"><div class="q">Item {i}. {esc(q)}</div>
        <div class="res">Resposta: ( ) Conforme &nbsp; ( ) Não conforme &nbsp; ( ) Não se aplica</div>
        <div class="res"><b>Fonte:</b> {esc(fonte(s,comp))}.</div>
        <figure><figcaption class="t">Figura {i} – Foto do trecho que fundamenta o item {i}</figcaption>
        <img src="imagens/{i:02d}.jpg" alt="Slide {s} do capítulo 6 de Barbosa e Silva (2010) com o trecho que fundamenta o item {i}">
        <figcaption class="f">Fonte: {esc(fonte(s,comp))}.</figcaption></figure></div>""")
    h.append("""<h2>Referências bibliográficas</h2>
    <p>BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. <i>Interação Humano-Computador</i>. Rio de Janeiro: Elsevier, 2010.</p>
    <p>SALES, André Barros de. <i>Plano de Ensino: Interação Humano Computador (FGA0173), 02/2026, Turma 01, v1</i>. Brasília: Universidade de Brasília, 2026.</p>
    <h2>Agradecimentos e uso de IA generativa</h2>
    <p>Conforme o Código de Conduta da SBC adotado no Plano de Ensino (SALES, 2026, p. 3), declaro o uso de IA generativa: a ferramenta <b>Claude (Anthropic)</b> foi usada a meu pedido para localizar nos slides do capítulo 6 os trechos sobre cenários, redigir a primeira versão dos itens como perguntas completas, recortar as imagens dos slides e formatar este documento. O conteúdo foi conferido por mim com os slides, e sou o responsável por ele. A ferramenta não é autora do artefato.</p></body></html>""")
    open(os.path.join(out_dir,"lista-cenarios.html"),"w",encoding="utf-8").write("\n".join(h))

    # página Markdown para o site
    md = [f"""# Lista de Verificação – Cenários

**Autoria:** Henrique Schneider Fernandes da Rosa · **Entrega 7** (atividade individual do Moodle, prazo 10/11/2026, 23:30)

## Tabela de contribuição

**Tabela 1 – Contribuições no trabalho "Lista de Verificação – Cenários"**

| Integrante | Contribuição | Atividade (link) | Gravação (link) |
| --- | --- | --- | --- |
| Alexandre Vilar Valadares Fonsêca | Não se aplica (atividade individual) | — | — |
| Gabriel Robson Nunes Neiva da Silva | Não se aplica (atividade individual) | — | — |
| Henrique Schneider Fernandes da Rosa | Autoria do trabalho (atividade individual) | Esta página | — |
| João Vitor Tavares de Sá Lima | Não se aplica (atividade individual) | — | — |

Fonte: elaborado pelos autores (2026).

## Histórico de versões

**Tabela 2 – Histórico de versões do trabalho "Lista de Verificação – Cenários"**

| Data | Versão | Descrição | Autor(es) | Revisor(es) |
| --- | --- | --- | --- | --- |
| {data} | 1.0 | Elaboração do trabalho (13 itens) e publicação no site | Henrique Schneider | — |

Fonte: elaborado pelos autores (2026).

## 1. Introdução

Atividade individual do Moodle "Elaborar uma lista de verificação – Cenários", com no mínimo 8 itens (SALES, [2026]). Esta lista tem {len(ITENS)} itens, fundamentados em Barbosa e Silva (2010), capítulo 6, seção 6.3, conforme os slides do capítulo 6, que reproduzem páginas do livro.

Cada item é uma pergunta completa, respondida com **Conforme**, **Não conforme** ou **Não se aplica**. Abaixo de cada item estão a fonte e a foto do trecho que o fundamenta. Clique no título de cada figura para abrir a foto.

## 2. Itens da lista
"""]
    for i,(q,s,comp,box) in enumerate(ITENS,1):
        md.append(f"""### Item {i}

{q}

**Fonte:** {fonte(s,comp)}.

??? quote "Figura {i} – Foto do trecho que fundamenta o item {i}"

    ![Slide {s} do capítulo 6 de Barbosa e Silva (2010) com o trecho que fundamenta o item {i}](imagens/lista-cenarios/{i:02d}.jpg)

    Fonte: {fonte(s,comp)}.
""")
    md.append("""## Referências bibliográficas

BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador*. Rio de Janeiro: Elsevier, 2010.

SALES, André Barros de. *Plano de Ensino: Interação Humano Computador (FGA0173), 02/2026, Turma 01, v1*. Brasília: Universidade de Brasília, 2026.

## Agradecimentos e uso de IA generativa

**Uso de IA generativa neste trabalho.** O Claude (Anthropic) foi utilizado, a pedido de Henrique Schneider, para localizar nos slides do capítulo 6 os trechos sobre cenários, redigir a primeira versão dos itens como perguntas completas, recortar as imagens dos slides e formatar o documento e esta página. O conteúdo foi conferido pelo autor com os slides, e a ferramenta não é autora do trabalho (SALES, 2026, p. 3).
""")
    open(os.path.join(out_dir,"lista-cenarios.md"),"w",encoding="utf-8").write("\n".join(md))

    async def pdf():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
            pg = await b.new_page(); await pg.goto("file://"+os.path.abspath(os.path.join(out_dir,"lista-cenarios.html")))
            await pg.pdf(path=os.path.join(out_dir,NOME_ARQ), format="A4", print_background=True, margin={"top":"16mm","bottom":"16mm","left":"15mm","right":"15mm"},
                         display_header_footer=True, header_template="<span></span>",
                         footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#555">Interação Humano Computador – André Barros de Sales – 2026.2 · Grupo 03 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
            await b.close()
    asyncio.run(pdf())

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--slides", required=True); ap.add_argument("--out", default="saida"); ap.add_argument("--matricula")
    a = ap.parse_args(); build(a.slides, a.out, a.matricula)
