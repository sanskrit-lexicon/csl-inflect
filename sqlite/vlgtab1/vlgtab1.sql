CREATE TABLE vlgtab1 (
 model VARCHAR(100)  NOT NULL,
 stem VARCHAR(100)  NOT NULL,
 refs VARCHAR(100)  NOT NULL,
 data TEXT NOT NULL
);
.separator "\t"
.import temp_input.txt vlgtab1
#create index datum on vlgtab1(key);
pragma table_info (vlgtab1);
select count(*) from vlgtab1;
.exit
