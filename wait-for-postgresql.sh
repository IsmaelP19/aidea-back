#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

export PGUSER="${POSTGRES_USER:-postgres}"
export PGPASSWORD="${POSTGRES_PASSWORD:-docker}"

until psql -h "$host" -U "$PGUSER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"
exec $cmd