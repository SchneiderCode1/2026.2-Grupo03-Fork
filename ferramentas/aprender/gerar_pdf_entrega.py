#!/usr/bin/env python3
"""Gera o PDF para o Aprender: capa com o link do vídeo e o link do GitHub Pages + páginas do site impressas.

Uso (na raiz do repositório, depois de `mkdocs build -d site`):
  python3 ferramentas/aprender/gerar_pdf_entrega.py --site site --titulo "Relato dos Resultados da Avaliação do Protótipo de Alta Fidelidade" \
      --entrega 7 --video https://youtu.be/XXXX --link https://interacao-humano-computador.github.io/2026.2-Grupo03/entrega-7/ \
      --paginas entrega-7/relatorio-do-grupo entrega-7/contribuicoes --saida RelatoProtAltaFideDetran-DF.pdf

Nomes de arquivo exigidos pelo Aprender (Entregas futuras.md):
  Entrega 7: RelatoProtAltaFideNomedoSite.pdf  ->  RelatoProtAltaFideDetran-DF.pdf
  Inspeção do Grupo +1 (Entrega 7): InspRelatoProtAltaFideNomedoSite.pdf  ->  InspRelatoProtAltaFideDetran-DF.pdf
Só roda se o vídeo e o link forem informados: o script não inventa endereços.
"""
import argparse, asyncio, html, os, subprocess, sys, tempfile

MEMBROS = ["Alexandre Vilar Valadares Fonsêca","Gabriel Robson Nunes Neiva da Silva","Henrique Schneider Fernandes da Rosa","João Vitor Tavares de Sá Lima"]

def capa(a):
    li = "".join(f"<li>{html.escape(m)}</li>" for m in MEMBROS)
    return f"""<html><head><meta charset="utf-8"><style>
    body{{font-family:Arial,Helvetica,sans-serif;color:#111;margin:0}} .c{{padding:40px 10px}}
    h1{{font-size:22pt;color:#0b3d6e;margin:0 0 6px}} h2{{font-size:13pt;font-weight:normal;margin:0 0 30px}}
    td{{padding:6px 10px;border:1px solid #888;font-size:11pt;vertical-align:top}} td:first-child{{background:#e6eef6;font-weight:bold;width:28%}} table{{border-collapse:collapse;width:100%}}
    </style></head><body><div class="c">
    <p style="font-size:10pt">PROJETO DA DISCIPLINA DE INTERAÇÃO HUMANO-COMPUTADOR (2026.2)<br>Campus Darcy Ribeiro / Faculdade de Ciências da Tecnologia (FCTE) · Turma 01 · Prof. Dr. André Barros de Sales</p>
    <h1>{html.escape(a.titulo)}</h1><h2>Entrega {a.entrega} · Grupo 03 · Detran-DF</h2>
    <table><tr><td>Vídeo da apresentação</td><td>{html.escape(a.video)}</td></tr>
    <tr><td>GitHub Pages da entrega</td><td>{html.escape(a.link)}</td></tr>
    <tr><td>Integrantes</td><td><ul style="margin:0;padding-left:18px">{li}</ul></td></tr></table>
    </div></body></html>"""

async def main(a):
    from playwright.async_api import async_playwright
    tmp = tempfile.mkdtemp(); pdfs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox","--allow-file-access-from-files"])
        pg = await b.new_page()
        open(f"{tmp}/capa.html","w",encoding="utf-8").write(capa(a))
        await pg.goto(f"file://{tmp}/capa.html"); await pg.pdf(path=f"{tmp}/00.pdf", format="A4", print_background=True); pdfs.append(f"{tmp}/00.pdf")
        for i,pag in enumerate(a.paginas,1):
            f = os.path.abspath(os.path.join(a.site, pag.strip("/"), "index.html"))
            if not os.path.exists(f): sys.exit(f"Página não encontrada no site compilado: {f}")
            await pg.emulate_media(media="print"); await pg.goto("file://"+f); await pg.wait_for_timeout(800)
            await pg.add_style_tag(content=".md-sidebar,.md-header,.md-tabs,.md-footer,.g03-a11y{display:none!important}.md-main__inner{margin:0}.md-content{margin:0!important}details>*{display:block!important}")
            await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            await pg.pdf(path=f"{tmp}/{i:02d}.pdf", format="A4", print_background=True, margin={"top":"14mm","bottom":"14mm","left":"12mm","right":"12mm"},
                         display_header_footer=True, header_template="<span></span>",
                         footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#555">Interação Humano Computador – André Barros de Sales – 2026.2 · Grupo 03 · <span class="pageNumber"></span></div>')
            pdfs.append(f"{tmp}/{i:02d}.pdf")
        await b.close()
    subprocess.run(["pdfunite",*pdfs,a.saida], check=True); print("gerado:", a.saida)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    for k in ("titulo","entrega","video","link","saida"): ap.add_argument("--"+k, required=True)
    ap.add_argument("--site", default="site"); ap.add_argument("--paginas", nargs="+", required=True)
    a = ap.parse_args()
    asyncio.run(main(a))
