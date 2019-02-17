#!/usr/bin/python3
# coding: utf-8

import asyncio
import time
import aiohttp
from aiohttp import web

url_list = ['https://images.livrariasaraiva.com.br/imagemnet/imagem.aspx/?pro_id=10285303&qld=90&l=430&a=-1',
            'https://images-na.ssl-images-amazon.com/images/I/51aRceSWyHL.jpg',
            'https://imgc.allpostersimages.com/img/print/posters/rick-and-morty_a-G-15352576-0.jpg',
            'https://images.tcdn.com.br/img/img_prod/604201/rick_and_morty_ii_1042_1_20180314090538.png',
            'https://cdn.shopify.com/s/files/1/0191/7850/products/RICKMORTY_39_-_COVER_A_FNL_WEB_1024x1024.jpg?v=1530034748',
            'https://jovemnerd.com.br/wp-content/uploads/2017/04/rick-morty-760x428.jpeg'
]

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status >= 200 and response.status < 300:
                image = await response.read()
            else:
                raise aiohttp.HttpProcessingError(
                        code = response.status,
                        message = response.reason,
                        headers = response.headers
                        )
    return image


async def downloader(url_list):
    counter = 0
    downloads = [download_image(url) for url in url_list]
    for download in asyncio.as_completed(downloads):
        image = await download
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_image, image, str(counter) + '.jpeg')
        counter += 1

def save_image(image, name):
    with open('downloads/{}'.format(name), 'wb') as fp:
        fp.write(image)


if __name__ == '__main__':
    t0 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(downloader(url_list))
    elapsed = time.time() - t0
    print("Executado em {:.2f}s".format(elapsed))
    #loop.close()
