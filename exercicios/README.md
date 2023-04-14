<details>
<summary><strong>Orientações</strong></summary><br />

**Criar e ativar ambiente virtual**

  ```bash
  $ python3 -m venv .venv && source .venv/bin/activate
  ```

**Instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r requirements.txt
  ```

**Rodar container com Selenium**

  ```bash
  $ docker-compose up
  ```  
</details>

Exercício 1
-----------

Com o Selenium, faça uma requisição para o endpoint “[https://quotes.toscrape.com/“](https://quotes.toscrape.com/%22) e imprima a primeira citação que aparece na página.

Exercício 2
-----------

Imprima todos os parágrafos da página “[https://www.wikimetal.com.br/iron-maiden-scorpions-kiss-veja-melhores-albuns-1982/“](https://www.wikimetal.com.br/iron-maiden-scorpions-kiss-veja-melhores-albuns-1982/%22).

Exercício 3
-----------

Utilizando a ferramenta Selenium, no site “[https://diolinux.com.br/“](https://diolinux.com.br/%22), faça a extração dos campos título, link para o post, trecho exibido de cada post da página inicial.

Exercício 4
-----------

Com o Beautiful Soup, faça a extração de todos os links da página “[https://pt.wikipedia.org/wiki/Rock\_in\_Rio”](https://pt.wikipedia.org/wiki/Rock_in_Rio%22)

> ✨ Dica: Dê uma espiada na seção sobre **atributos** [na documentação](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/#atributos) da ferramenta.
