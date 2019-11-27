CREATE TABLE vlgtab2 (
 key VARCHAR(100)  NOT NULL,
 model VARCHAR(100)  NOT NULL,
 stem VARCHAR(100)  NOT NULL
);
.separator "\t"
.import temp_input.txt vlgtab2
# create index datum on vlgtab2(key);
pragma table_info (vlgtab2);
select count(*) from vlgtab2;
.exit
