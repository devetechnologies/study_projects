from pyspark import pipelines as dp


# Please edit the sample below
@dp.materialized_view
@dp.expect_or_drop("no null emails", "email IS NOT NULL")
def user_cleaned():
    return spark.read.table("sample_users_user_sdp_example")