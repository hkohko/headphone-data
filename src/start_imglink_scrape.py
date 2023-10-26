import asyncio

from tqdm import tqdm

from frequency_graph_scraper import create_link_to_product_page, task


async def main(func, img_size):
    id_and_links = await create_link_to_product_page()
    for content in tqdm(id_and_links):
        db_id = content[0]
        link = content[1]
        await func(link, db_id, img_size)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main(task, "medium"))
