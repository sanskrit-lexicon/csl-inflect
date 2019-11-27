CREATE TABLE lgtab1 (
 model VARCHAR(100)  NOT NULL,
 stem VARCHAR(100)  NOT NULL,
 refs VARCHAR(100)  NOT NULL,
 data TEXT NOT NULL
);
.separator "\t"
.import ../../nominals/pysanskritv2/tables/calc_tables.txt lgtab1
#create index datum on lgtab1(key);
pragma table_info (lgtab1);
select count(*) from lgtab1;
.exit
