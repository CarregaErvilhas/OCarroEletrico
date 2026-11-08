# O Carro Elétrico

O site https://ocarroeletrico.com: a mobilidade elétrica em Portugal explicada a quem conduz. Carregar
em casa e na rua, condomínio, instalação, apoios e impostos, com a lei e a fonte de cada facto.

O conhecimento vem do [Voltaria](https://github.com/CarregaErvilhas/voltaria) (submodule em
`voltaria/`), o mesmo que o [ohmigo](https://ohmigo.ocarroeletrico.com/) serve aos assistentes. Aqui é
reescrito para pessoas, em português e em inglês.

```sh
scripts/build.py      # gera _site/
scripts/check.py      # o que o CI corre
```

Como funciona e como se reescrevem as páginas: [CLAUDE.md](CLAUDE.md). A voz do site:
[agent/TOM.md](agent/TOM.md).

## Licença

- **Conteúdo** (`content/`, `agent/` e o resto do texto): [CC-BY-4.0](LICENSE). É uma adaptação do
  Voltaria, que tem a mesma licença.
- **Código** (`scripts/`, `.github/`, o HTML, CSS e JavaScript do `site/`): [MIT](LICENSE-CODE).

Podes usar, adaptar e redistribuir, incluindo para fins comerciais, desde que credites as duas
origens e digas se alteraste:

> Conteúdo d'O Carro Elétrico (https://ocarroeletrico.com), adaptado do Voltaria
> (https://github.com/CarregaErvilhas/voltaria), CC-BY-4.0.

### O nome e a imagem ficam de fora

As licenças cobrem o conteúdo e o código, não a marca. Não estão licenciados o nome **O Carro
Elétrico**, o domínio, a mascote (o carrinho repórter, laranja), o ícone e as imagens feitas com eles (os
desenhos em `site/base.html` e os ficheiros em `site/static/`, menos a fonte). Podes usar o nome para
dizer de onde vem o conteúdo. Um fork precisa de nome e de imagem próprios.

A fonte Nunito tem a sua licença: [SIL OFL 1.1](site/static/fonts/OFL-Nunito.txt).

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md). Em resumo: erros de conteúdo corrigem-se no Voltaria; aqui,
código, design e a voz do site. Cada commit assinado com `git commit -s` (DCO), sem CLA.
