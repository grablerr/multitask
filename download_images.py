import os
import argparse
import requests
from multiprocessing import Pool

def download_image(url, output_dir):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.basename(url)
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Загружено: {filename}")
        else:
            print(f"Ошибка при загрузке изображения: {url}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Загрузка изображений из списка URL")
    parser.add_argument("urls", nargs='*', help="Список URL-адресов для загрузки изображений")
    args = parser.parse_args()

    if not args.urls:
        print("Введите URL-адреса для загрузки изображений (разделите запятой):")
        input_urls = input().split(',')
    else:
        input_urls = args.urls

    output_dir = "Загруженные изображения"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    num_processes = os.cpu_count()
    pool = Pool(processes=num_processes)

    pool.starmap(download_image, [(url, output_dir) for url in input_urls])

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
