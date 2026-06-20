# Database Errors

## Connection Errors

### "Connection refused" / "Cannot connect to database"
- Verify the database host, port, username, and password in your configuration.
- Ensure the database server is running.
- Check firewall rules to allow connections on the DB port (default: 5432 for PostgreSQL, 3306 for MySQL).

### "Too many connections"
- Your app has exceeded the max connection limit.
- Implement a connection pool (e.g., PgBouncer, HikariCP).
- Increase `max_connections` in the database config if resources allow.

## Query Errors

### "Deadlock detected"
- Two transactions are blocking each other.
- Implement retry logic with exponential backoff.
- Review transaction ordering to ensure consistent lock acquisition.

### "Duplicate key value violates unique constraint"
- A record with the same unique field already exists.
- Check for existing records before insert or use `INSERT ... ON CONFLICT`.

### "Relation does not exist"
- The table or view referenced does not exist.
- Verify the schema name and run pending migrations.

## Performance Issues

### Slow Queries
- Use `EXPLAIN ANALYZE` to identify bottlenecks.
- Add appropriate indexes on frequently queried columns.
- Avoid `SELECT *`; specify only required columns.

### High Disk Usage
- Run `VACUUM` and `ANALYZE` (PostgreSQL) to reclaim storage.
- Archive or delete old data using scheduled jobs.

## Backup & Recovery
- Automated backups run daily and are retained for 30 days.
- To restore, go to Admin Panel > Database > Restore from Backup.
- Point-in-time recovery (PITR) is available on Enterprise plans.
