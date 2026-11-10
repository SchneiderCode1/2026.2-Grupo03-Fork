# Aprender (Moodle): envios da disciplina

Scripts e instruções para preparar os arquivos que vão para o Aprender. Nada daqui aparece no site. O que o Claude gerou é rascunho: **leia antes de enviar**, porque você responde pelo conteúdo (SALES, 2026, p. 3).

## Prazos e nomes de arquivo (Entregas futuras.md)

| Atividade | Prazo | Nome do arquivo | Como gerar |
| --- | --- | --- | --- |
| Lista de verificação individual – Cenários | 10/11/2026, 23:30 | `GrupoNroNomedoAlunoVerifacaçãoListaCenários.pdf` (feito: `Grupo03HenriqueSchneiderVerifacaçãoListaCenários.pdf`) | `lista_cenarios.py` (precisa dos slides do cap. 6 recortados em `slideNN.jpg`) |
| Relato dos resultados da avaliação do protótipo de alta fidelidade | 15/11/2026, 23:59 | `RelatoProtAltaFideNomedoSite.pdf` → `RelatoProtAltaFideDetran-DF.pdf` | `gerar_pdf_entrega.py` |
| Inspeção do Grupo +1 – Relato do protótipo de alta fidelidade | 16/11/2026, 23:59 | `InspRelatoProtAltaFideNomedoSite.pdf` → `InspRelatoProtAltaFideDetran-DF.pdf` | `gerar_pdf_entrega.py` |

O arquivo da entrega deve conter a **URL do vídeo da apresentação** e o **link do GitHub Pages** (Entregas futuras.md). O Aprender cobra esses dois endereços; o script se recusa a rodar sem eles, para não inventar nenhum.

## Gerar o PDF do relato (15/11) depois que as páginas estiverem publicadas

```bash
mkdocs build -d site          # com o plugin redirects instalado (pip install -r requirements.txt)
python3 ferramentas/aprender/gerar_pdf_entrega.py --site site \
  --titulo "Relato dos Resultados da Avaliação do Protótipo de Alta Fidelidade" --entrega 7 \
  --video https://youtu.be/<ID-DO-VIDEO> \
  --link https://interacao-humano-computador.github.io/2026.2-Grupo03/entrega-7/ \
  --paginas entrega-7/relatorio-do-grupo entrega-7/contribuicoes \
  --saida RelatoProtAltaFideDetran-DF.pdf
```

Para a inspeção, use `--paginas entrega-7/verificacao/inspecao-grupo-XX`, `--link` com o endereço dessa página e `--saida InspRelatoProtAltaFideDetran-DF.pdf`. O vídeo da apresentação precisa estar no YouTube como "não listado" (D9).

## Listas de verificação antigas (sem arquivo no repositório)

`pendencias/integrantes-e-trabalhos-individuais.md` (seção 3, Quadro 1) lista as atividades individuais de Henrique Schneider cujo PDF não está no repositório (DECIDE, Métodos de Avaliação, Perfil de Usuário, Personas, Elenco de Personas, HTA, CTT e Storyboard). Se o Aprender ainda aceitar envio atrasado, o `lista_cenarios.py` serve de modelo para gerar cada uma, a partir dos slides ou das páginas do livro.
