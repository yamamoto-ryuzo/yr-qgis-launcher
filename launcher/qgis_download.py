import os
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import subprocess

def get_version(msi_name):
    match = re.search(r'(\d+\.\d+\.\d+-\d+)', msi_name)
    return match.group(1) if match else None

def download_latest_msi(download_url):
    response = requests.get(download_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    msi_links = {link.get('href') for link in links if link.get('href') and link.get('href').endswith('.msi')}

    if not msi_links:
        print('MSIファイルが見つかりませんでした。')
    else:
        latest_msi = max(msi_links, key=get_version)
        version = get_version(latest_msi)
        folder_name = f"QGIS{version}"
        os.makedirs(folder_name, exist_ok=True)
        save_path = os.path.join(folder_name, latest_msi)
        
        if os.path.exists(save_path):
            print(f'{save_path} は既に存在します。ダウンロードをスキップします。')
        else:
            msi_url = download_url + latest_msi
            msi_response = requests.get(msi_url, stream=True)
            msi_response.raise_for_status()
            total_size = int(msi_response.headers.get('content-length', 0))
            with open(save_path, 'wb') as file, tqdm(
                desc=save_path,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in msi_response.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            print(f'最新のMSIファイルを {save_path} にダウンロードしました。')

        # MSIファイルを起動してインストールを開始
        print(f'{save_path} を起動してインストールを開始します。')
        subprocess.run(['msiexec', '/i', save_path])

if __name__ == '__main__':
    download_url = 'https://ftp.osuosl.org/pub/osgeo/download/qgis/windows/'
    download_latest_msi(download_url)