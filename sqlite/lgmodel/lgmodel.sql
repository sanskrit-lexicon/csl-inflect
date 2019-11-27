#DROP TABLE lgmodel;
CREATE TABLE lgmodel (
 model VARCHAR(100)  NOT NULL,
 descr VARCHAR(100)  NOT NULL,
 ref VARCHAR(100)  NOT NULL
);
.separator "\t"
.import lgmodel_input.txt lgmodel
create index datum on lgmodel(model);
pragma table_info (lgmodel);
select count(*) from lgmodel;
.exit
