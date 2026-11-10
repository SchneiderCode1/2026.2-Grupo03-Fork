# Modelos da Entrega 7

Modelos de página para o **Relato dos resultados do protótipo de alta fidelidade** (entrega em 15/11/2026, inspeção em 16/11 e apresentação em 17/11). Esta pasta fica fora de `docs/`, então nada daqui aparece no site.

## Como usar

1. Copie o modelo para o caminho indicado na tabela abaixo (troque `<nome>` pelo slug do integrante: `alexandre-vilar`, `gabriel-robson`, `henrique-schneider` ou `joao-vitor`).
2. Substitua todos os marcadores `[VERIFICAR: ...]` por dados reais. O que não tiver dado sai da página e vai para `pendencias/`.
3. Mantenha a ordem das seções: título, tabela de contribuição, histórico de versões, seções numeradas a partir de "1. Introdução", referências bibliográficas e agradecimentos e uso de IA generativa.
4. Toda tabela e figura tem legenda **acima** (`**Tabela N – Título**`), fonte **abaixo** (`Fonte: ...`) e é chamada no texto ("conforme a Tabela N").
5. Inclua a página na aba "Entrega 7" do `mkdocs.yml` e rode `mkdocs build --strict` antes do commit.

| Modelo | Destino no site |
| --- | --- |
| `relatorio.md` | `docs/entrega-7/relatorio.md` |
| `relatorio-do-grupo.md` | `docs/entrega-7/relatorio-do-grupo.md` |
| `contribuicoes.md` | `docs/entrega-7/contribuicoes.md` |
| `inspecao-grupo-mais-1.md` | `docs/entrega-7/verificacao/inspecao-grupo-XX.md` |
| `integrante/index.md` | `docs/entrega-7/integrantes/<nome>/index.md` |
| `integrante/prototipo-alta-fidelidade.md` | `docs/entrega-7/integrantes/<nome>/prototipo-alta-fidelidade.md` |
| `integrante/relato-teste-usabilidade.md` | `docs/entrega-7/integrantes/<nome>/relato-teste-usabilidade.md` |
| `integrante/video-avaliacao.md` | `docs/entrega-7/integrantes/<nome>/video-avaliacao.md` |

## Planilha de coleta e consolidação

`planilha-coleta-teste-usabilidade.xlsx` (sem nenhum dado de sessão) serve aos testes de cada integrante: a aba "Dados" recebe uma linha por participante e tarefa, a aba "Metas" traz os valores-alvo da Tabela 3 do Planejamento de Henrique (tempos ainda a confirmar após o piloto), a aba "Sumário" calcula sozinha a Tabela 8 (n/N, tempo médio e desvio, erros, ajuda, nota) e a aba "Problemas" é a Tabela 9. Os dados do piloto não entram na planilha (Barbosa; Silva, 2010, p. 307). Quem tiver tarefas ou metas diferentes ajusta as abas "Metas" e "Dados".

Trecho do `mkdocs.yml` para a aba, no mesmo padrão das Entregas 5 e 6:

```yaml
  - Entrega 7:
    - entrega-7/index.md
    - Relatório da entrega: entrega-7/relatorio.md
    - Relatório do grupo: entrega-7/relatorio-do-grupo.md
    - Contribuições: entrega-7/contribuicoes.md
    - Verificação:
      - Inspeção do Grupo XX: entrega-7/verificacao/inspecao-grupo-XX.md
    - Material dos integrantes:
      - Alexandre Vilar:
        - Visão geral: entrega-7/integrantes/alexandre-vilar/index.md
        - Protótipo de alta fidelidade: entrega-7/integrantes/alexandre-vilar/prototipo-alta-fidelidade.md
        - Relato do teste de usabilidade: entrega-7/integrantes/alexandre-vilar/relato-teste-usabilidade.md
        - Vídeos da avaliação: entrega-7/integrantes/alexandre-vilar/video-avaliacao.md
      # repetir para Gabriel Robson, Henrique Schneider e João Vitor, nessa ordem
```

Os modelos foram criados em 10/11/2026 com apoio do Claude (Anthropic), a pedido de Henrique Schneider, a partir do Plano de Ensino, do capítulo 3 do Relatório da Entrega 6 e do modelo de página do grupo (`Refatoração/CLAUDE.md`, seção 3).
