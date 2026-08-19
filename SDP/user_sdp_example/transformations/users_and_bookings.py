from pyspark import pipelines as dp
from pyspark.sql.functions import col, count, desc


# Please edit the sample below

@dp.materialized_view
def users_and_bookings():
    return (spark.read.table("user_cleaned")
            .join(spark.read.table("samples.wanderbricks.bookings"), "user_id")
            .groupBy(col("name"))
            .agg(count("booking_id").alias("bookings_count"))
            .orderBy(desc("bookings_count"))
            .limit(100)
            #.select("user_id", "user_name", "booking_id", "booking_date")

    )