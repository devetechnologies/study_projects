from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
  name = "customers_history_agg",
  comment = "Aggregated customer history"
)
def customers_history_agg():
  return (
    spark.read.table("customers_history")
      .groupBy("id")
      .agg(
          count_distinct("address").alias("address_count"),
          count_distinct("email").alias("email_count"),
          count_distinct("firstname").alias("firstname_count"),
          count_distinct("lastname").alias("lastname_count")
      )
  )