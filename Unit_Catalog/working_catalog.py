# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS study_catalog
# MAGIC MANAGED LOCATION 'abfss://metastore@mmstudystorage.dfs.core.windows.net/';
# MAGIC --
# MAGIC create database if not exists study_catalog.study_schema;
# MAGIC create table if not exists study_catalog.study_schema.study_table (id int, name string);
# MAGIC insert into study_catalog.study_schema.study_table values (1, 'a'), (2, 'b'), (3, 'c');
# MAGIC --
# MAGIC select * from study_catalog.study_schema.study_table;
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS study_catalog.study_schema.study_table;

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists ext_catalog 
# MAGIC managed location 'abfss://metastore@mmstudystorage.dfs.core.windows.net/external';
# MAGIC
# MAGIC create schema if not exists ext_catalog.ext_schema;
# MAGIC create table if not exists ext_catalog.ext_schema.ext_table (id int, name string);
# MAGIC insert into ext_catalog.ext_schema.ext_table values (1, 'a'), (2, 'b'), (3, 'c');
# MAGIC
# MAGIC select * from ext_catalog.ext_schema.ext_table;
# MAGIC     
# MAGIC --DROP TABLE IF EXISTS ext_catalog.ext_schema.ext_table;
# MAGIC
# MAGIC