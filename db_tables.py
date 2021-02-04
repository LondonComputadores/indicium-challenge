#!/usr/bin/python

SCHEMA="public"
DB="northwind"
PGDATABASE="northwind"
PGUSER="northwind_user"


psql -Atc "select tablename from pg_tables where schemaname='$SCHEMA'" $DB |\
    while read SCHEMA; do
    if [[ "$SCHEMA" != "pg_catalog" && "$SCHEMA" != "information_schema" ]]; then
        psql -Atc "select tablename from pg_tables where schemaname='$SCHEMA'" |\
            while read TBL; do
                psql -c "COPY $SCHEMA.$TBL TO STDOUT WITH CSV DELIMITER ';' HEADER ENCODING 'UTF-8'" > $SCHEMA.$TBL.csv
            done
fi
done