DROP TABLE lgtab2;
CREATE TABLE lgtab2 (
 key VARCHAR(100)  NOT NULL,
 model VARCHAR(100)  NOT NULL,
 lgtab2id TEXT NOT NULL
);
.separator "\t"
.import lgtab2_input.txt lgtab2
create index datum on lgtab2(key);
pragma table_info (lgtab2);
select count(*) from lgtab2;
.exit
