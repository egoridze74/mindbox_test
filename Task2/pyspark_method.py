from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def get_products_with_categories(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_links_df: DataFrame
) -> DataFrame:
    products_with_categories = (
        products_df.join(
            product_category_links_df,
            on="product_id",
            how="left"
        )
        .join(
            categories_df,
            on="category_id",
            how="left"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )
    
    return products_with_categories