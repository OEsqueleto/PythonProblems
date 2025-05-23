from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ----- CONFIGURAÇÃO -----
# Lista de SKUs a serem testados
sku_list = [
    "377857043C",
    # ... adicione quantos SKUs quiser
]

# Inicializa o driver (Chrome). Ajuste se for usar Firefox ou outro.
driver = webdriver.Chrome()

try:
    for sku in sku_list:
        url = f"https://lista.mercadolivre.com.br/{sku}"
        print(f"Abrindo SKU {sku}: {url}")
        driver.get(url)
        time.sleep(2)  # espera a página carregar

        # Tenta encontrar a mensagem de "sem anúncios"
        try:
            aviso = driver.find_element(
                By.CSS_SELECTOR,
                "h3.ui-search-rescue__title"
            )
            if "Não há anúncios que correspondam à sua busca" in aviso.text:
                print(f"  → SKU {sku}: sem anúncios. Pulando.\n")
                continue  # pula para o próximo SKU
        except:
            # Se não encontrar o elemento, segue adiante
            pass

        # Se chegou aqui, há pelo menos um anúncio
        print(f"  → SKU {sku}: anúncios encontrados! Aguardando 4 s e scroll...")
        time.sleep(4)

        # Executa scroll de 800px vertical
        driver.execute_script("window.scrollBy(0, 800);")
        print("  → Scroll realizado. Seguindo para o próximo.\n")

finally:
    driver.quit()
    print("Concluído. Navegador fechado.")
