CREATE TABLE IF NOT EXISTS tags (
  tag_id serial,
  tag varchar(55),
  content text,
  author bigint
);

CREATE TABLE IF NOT EXISTS staff (
  user_id bigint
);

CREATE TABLE IF NOT EXISTS reaction_roles (
  reaction_role_id serial,
  message_id bigint,
  emoji text,
  role_id bigint
)
