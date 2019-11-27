DROP TABLE lgtab1;
CREATE TABLE lgtab1 (
 key VARCHAR(100)  NOT NULL,
 data TEXT NOT NULL
);
.separator "\t"
.import lgtab1_input.txt lgtab1
create index datum on lgtab1(key);
pragma table_info (lgtab1);
select count(*) from lgtab1;
.exit
