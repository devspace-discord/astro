CREATE TABLE IF NOT EXISTS tags (
  tag_id serial,
  tag text,
  owner_id bigint,
  timestamp bigint
)
