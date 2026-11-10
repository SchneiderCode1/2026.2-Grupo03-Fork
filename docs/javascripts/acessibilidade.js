/*
 * Barra de acessibilidade do site do Grupo 03 (IHC 2026.2).
 * Oferece: aumentar/diminuir o tamanho do texto, restaurar o tamanho padrão
 * e ativar/desativar o alto contraste. As escolhas ficam salvas no navegador
 * (localStorage) e são reaplicadas a cada página, inclusive com a navegação
 * instantânea do Material for MkDocs (document$).
 */
(function () {
  "use strict";

  var CHAVE_FONTE = "g03-tamanho-fonte";
  var CHAVE_CONTRASTE = "g03-alto-contraste";
  var PADRAO = 100;
  var MIN = 80;
  var MAX = 160;
  var PASSO = 10;

  function ler(chave, valorPadrao) {
    try {
      var v = window.localStorage.getItem(chave);
      return v === null ? valorPadrao : v;
    } catch (e) {
      return valorPadrao;
    }
  }

  function gravar(chave, valor) {
    try {
      window.localStorage.setItem(chave, String(valor));
    } catch (e) {
      /* navegação privada ou armazenamento bloqueado: segue sem salvar */
    }
  }

  function tamanhoAtual() {
    var n = parseInt(ler(CHAVE_FONTE, PADRAO), 10);
    return isNaN(n) ? PADRAO : Math.min(MAX, Math.max(MIN, n));
  }

  function aplicarFonte(tamanho) {
    document.documentElement.style.setProperty("--g03-fator-fonte", String(tamanho / 100));
    gravar(CHAVE_FONTE, tamanho);
    var rotulo = document.querySelector(".g03-a11y__valor");
    if (rotulo) {
      rotulo.textContent = tamanho + "%";
    }
  }

  function contrasteAtivo() {
    var v = ler(CHAVE_CONTRASTE, null);
    if (v === "1") return true;
    if (v === "0") return false;
    return !!(window.matchMedia && window.matchMedia("(prefers-contrast: more)").matches);
  }

  function aplicarContraste(ativo) {
    document.documentElement.classList.toggle("g03-alto-contraste", ativo);
    gravar(CHAVE_CONTRASTE, ativo ? "1" : "0");
    var botao = document.querySelector("[data-g03-contraste]");
    if (botao) {
      botao.setAttribute("aria-pressed", ativo ? "true" : "false");
    }
  }

  function criarBotao(rotulo, titulo, acao, extra) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "g03-a11y__botao";
    b.textContent = rotulo;
    b.title = titulo;
    b.setAttribute("aria-label", titulo);
    if (extra) {
      b.setAttribute(extra, "");
    }
    b.addEventListener("click", acao);
    return b;
  }

  function montar() {
    var cabecalho = document.querySelector(".md-header__inner");
    if (cabecalho && !cabecalho.querySelector(".g03-a11y")) {
      var grupo = document.createElement("div");
      grupo.className = "g03-a11y";
      grupo.setAttribute("role", "group");
      grupo.setAttribute("aria-label", "Opções de acessibilidade");

      grupo.appendChild(criarBotao("A−", "Diminuir o tamanho do texto", function () {
        aplicarFonte(Math.max(MIN, tamanhoAtual() - PASSO));
      }));

      var valor = document.createElement("span");
      valor.className = "g03-a11y__valor";
      valor.setAttribute("aria-live", "polite");
      grupo.appendChild(valor);

      grupo.appendChild(criarBotao("A+", "Aumentar o tamanho do texto", function () {
        aplicarFonte(Math.min(MAX, tamanhoAtual() + PASSO));
      }));

      grupo.appendChild(criarBotao("A", "Restaurar o tamanho padrão do texto", function () {
        aplicarFonte(PADRAO);
      }));

      grupo.appendChild(criarBotao("AC", "Ativar ou desativar o alto contraste", function () {
        aplicarContraste(!document.documentElement.classList.contains("g03-alto-contraste"));
      }, "data-g03-contraste"));

      var busca = cabecalho.querySelector(".md-search");
      cabecalho.insertBefore(grupo, busca || null);
    }
    aplicarFonte(tamanhoAtual());
    aplicarContraste(contrasteAtivo());
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(montar);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", montar);
  } else {
    montar();
  }
})();
