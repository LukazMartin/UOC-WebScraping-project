from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, url, pagination_index):
        self.url = url
        self.pagination_index = pagination_index
        self.current_index = 0
        self.index_parameter = 'startIndex'
        self.page = None
        self.soup = None
        self.links = None
        self.linksToExplore = []
        self.next_url = None
        self.explore = True

    def __get_page(self, user_agent=None):

        # Some pages don't work without headers. See robots.txt
        if not self.next_url:
            page_ = requests.get(self.url, headers={"User-Agent": user_agent})
        else:
            page_ = requests.get(self.next_url, headers={"User-Agent": user_agent})

        if not page_.ok:  # Only requests 2XX are valid
            raise Exception(f"Could not get page {self.url}")

        self.page = page_

    def __get_soup(self):
        soup_ = BeautifulSoup(self.page.content)
        self.soup = soup_

    def __get_links(self):
        self.links = self.soup.find_all('a')

    def __filter_links(self):

        explorer_links = []
        for link in self.links:
            str_link = link.get('href')  # Sometimes it's None
            if str_link and '/propiedad/' in link.get('href'):
                explorer_links.append(link.get('href'))
        self.linksToExplore = self.linksToExplore + explorer_links

        if len(explorer_links) == 0:  # No more links to explore
            self.explore = False

    def __get_next_link(self):
        index = self.url.index(self.index_parameter)
        self.current_index += self.pagination_index

        if self.next_url is None:  # Hay 2 anuncios en lugar de casas en la primera pagina
            self.current_index -= 2

        self.next_url = self.url[:index + len(self.index_parameter) + 1] + str(self.current_index)
        self.next_url += self.url[index + len(self.index_parameter) + 2:]

    def scrape(self):
        while self.explore:
            self.__get_page()
            self.__get_soup()
            self.__get_links()
            self.__filter_links()
            self.__get_next_link()

        #  TODO: Hasta aquí he recorrido todas las paginas guardando los links importantes en self.linksToExplore
        # Lo que deberíamos hacer ahora es:
        # 1. Recorrer todos los links guardados e buscar en cada uno la información más relevante
        #   - Titulo, Descripcion, numero dormitorios, numero baños, superficie, precio, calle..
        # 2. Guardar esta información como una nueva fila en un CSV que guardaremos en /dataset


if __name__ == '__main__':

    scrapper = Scraper("https://www.engelvoelkers.com/es/search/?q=&startIndex=0&businessArea=residential&sortOrder=DESC&sortField=newestProfileCreationTimestamp&pageSize=18&facets=bsnssr%3Aresidential%3Bcntry%3Aspain%3Bobjcttyp%3Acondo%3Brgn%3Abarcelona%3Btyp%3Abuy%3B", 18)
    scrapper.scrape()



# Paginas para documentar en el pdf:
# page = get_page("https://www.engelvoelkers.com/es-es/propiedades/comprar-vivienda/barcelona/")  # review robots.txt -> This is the main page
# https://www.engelvoelkers.com/dp-sitemap/sitemap_index.xml
# https://www.engelvoelkers.com/sitemap_index.xml
