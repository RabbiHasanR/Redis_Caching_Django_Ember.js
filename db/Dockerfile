FROM postgres:16.2-alpine

# Environment variables
ENV POSTGRES_USER=testuser
ENV POSTGRES_PASSWORD=12345
ENV POSTGRES_DB=mydb

# Copy SQL initialization scripts
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432

# CMD [ "postgres", "-p", "5432" ]


# for above dockerfile container bash 
# psql -U <postgres_user> -d <postgres_db>