FROM postgres:16.2-alpine

ENV POSTGRES_USER testuser
ENV POSTGRES_PASSWORD 12345
ENV POSTGRES_DB testdb

# COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD [ "postgres", "-p", "5432" ]


# for above dockerfile container bash 
# psql -U <postgres_user> -d <postgres_db>