CREATE TABLE IF NOT EXISTS tags (
  tag_id serial,
  tag varchar(55),
  content text,
  author bigint
);

CREATE TABLE IF NOT EXISTS staff (
  user_id bigint
);
