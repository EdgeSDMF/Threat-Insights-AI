resource "aws_s3_bucket" "log_bucket" {
  bucket = "threatinsightsai-logs"
  acl    = "private"
}

resource "aws_glue_catalog_database" "logs_db" {
  name = "security_logs"
}

resource "aws_glue_catalog_table" "cloudtrail" {
  name          = "cloudtrail_logs"
  database_name = aws_glue_catalog_database.logs_db.name
  table_type    = "EXTERNAL_TABLE"
}
