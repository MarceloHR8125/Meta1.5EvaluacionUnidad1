"""
Usando librerías selenium, Beautiful soup hacer un scrapping de la siguiente pagina:
https://br.investing.com/currencies/usd-mxn-historical-data.
Debe generar en archivos diferentes un reporte por periodo diario, semanal y mensual de los datos históricos de la
moneda USD/MXN. Debe contener las siguientes columnas: Fecha, Último, Abertura, Máximo, Mínima.  El seleccionador del
Período tiene un id  llamado “react-select-3-input”. Recuerde que la etiqueta de la tabla se llama table, que cada
renglón en un <tr> que se componen por celdas cuyas etiquetas se llaman <td>.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
# Usamos las librerias de selenium, pandas y beautifulsoup

def datos_historicos(driver, periodo):
    # Seleccionamos el periodo con react-select-3-input
    periodo_input = driver.find_element_by_id('react-select-3-input')
    periodo_input.send_keys(periodo)
    periodo_input.send_keys(Keys.RETURN)

    # Ponemos un tiempo para que cargue la pagina
    time.sleep(5)

    # Obtener el contenido de los datos historicos
    html = driver.page_source

    # Utilizar BeautifulSoup con el html.parser para analizar el contenido
    soup = BeautifulSoup(html, 'html.parser')

    # Con este codigo ubicamos la parte de los datos historicos
    tabla = soup.find('table', {'id': 'curr_table'})

    # Creamos una lista para almacenar los datos de forma ordenada
    data = []

    # Darle un orden de las filas de la tabla
    for fila in tabla.find_all('tr')[1:]:  # Excluye la primera fila (encabezados)
        celdas = fila.find_all('td')
        fecha = celdas[0].text.strip()
        ultimo = celdas[1].text.strip()
        apertura = celdas[2].text.strip()
        maximo = celdas[3].text.strip()
        minima = celdas[4].text.strip()
        data.append([fecha, ultimo, apertura, maximo, minima])

    # Crear un DataFrame de pandas con los datos solicitados en el ejercicio
    df = pd.DataFrame(data, columns=['Fecha', 'Último', 'Apertura', 'Máximo', 'Mínima'])

    # Guardar los datos en un archivo CSV
    nombre_archivo = f'USD_MXN_Historico_{periodo}.csv'
    df.to_csv(nombre_archivo, index=False)

def investing():
    # Iniciamos el navegador con el driver correcto
    driver = webdriver.Chrome()
    driver.get('https://br.investing.com/currencies/usd-mxn-historical-data')

    # Obtener datos históricos para los períodos diario, semanal y mensual
    periodos = ['Diario', 'Semanal', 'Mensual']
    for periodo in periodos:
        datos_historicos(driver, periodo)


    driver.quit()

if __name__ == "__main__":
    investing()