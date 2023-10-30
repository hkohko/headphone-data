from db_main import connect


def unpack(to_unpack: tuple):
    return to_unpack[0]


def main(search: str):
    search_term = {"search": f"%{search.replace(' ', '%')}%"}
    Q_USER_QUERY = "SELECT id FROM headphone WHERE name LIKE :search"
    Q_GET_IMAGE = "SELECT img_url FROM imglink WHERE id=:product"
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(Q_USER_QUERY, search_term)
        product_id = next(query for query in cursor)
        cursor.execute(Q_GET_IMAGE, {"product": unpack(product_id)})
        result = cursor.fetchone()
    return unpack(result)


if __name__ == "__main__":
    product_search = main("tin t2")
    print(product_search)
