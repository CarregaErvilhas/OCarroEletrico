# Contribuir para O Carro Elétrico

Obrigado. Não há papelada: não assinas nenhum acordo nem cedes direitos.

## Primeiro: o conteúdo corrige-se no Voltaria

As páginas deste site são reescritas a partir do [Voltaria](https://github.com/CarregaErvilhas/voltaria).
Viste um erro numa regra, num artigo da lei, num apoio ou numa data? A correção vai para a skill ou
para os factos do Voltaria, por PR lá. Na reescrita seguinte, chega aqui sozinha.

Neste repo entram PRs de:

- código do site (`scripts/`, `site/`, `.github/`);
- design, textos do próprio site (`site/strings.json`) e a mascote;
- a voz do site (`agent/TOM.md`) e as regras do agente (`agent/SYSTEM.md`);
- uma página que leia mal, quando o problema é a forma e não o facto.

## Assinar os commits (DCO)

Cada commit leva uma linha `Signed-off-by`, que o git acrescenta com `-s`:

```sh
git commit -s -m "site: o índice da página fica fixo ao rolar"
```

Com ela certificas o [Developer Certificate of Origin](DCO): que o contributo é teu, ou que tens o
direito de o enviar, sob a licença do projeto. O nome e o email têm de ser reais e iguais aos do
autor do commit. Esqueceste-te? `git commit --amend -s` no último commit, ou
`git rebase --signoff main` para todos os do branch.

Uma verificação automática (`dco.yml`) recusa PRs com commits sem assinatura. Localmente:
`scripts/check-dco.sh origin/main..HEAD`.

## Licença dos contributos

O que envias fica com a licença do resto do repo: [CC-BY-4.0](LICENSE) para o conteúdo, [MIT](LICENSE-CODE)
para o código. As duas são irrevogáveis: o projeto e quem o usa podem continuar a usar o teu
contributo, e tu continuas a ser o autor. O crédito fica no histórico do git.

O nome, a mascote e os ícones não estão em nenhuma das licenças (ver o README). Um contributo para a
mascote ou para os ícones entra na marca do site.

## Verificações

Antes de abrir um PR, na raiz do repo (só precisam de `python3`):

```sh
scripts/check.py      # as páginas contra o Voltaria, o tom e o build completo
scripts/build.py      # gera _site/ para veres no browser
```

A Action `checks.yml` corre o `check.py` em cada PR.

## Revisão

Tudo entra por PR, revisto pelos CODEOWNERS. Só merges squash ou rebase.
