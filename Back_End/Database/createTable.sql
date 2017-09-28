create table convertor
(
	brand varchar(100) not null,
	type varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_height real not null,
	actual_weight real,
	CONSTRAINT basic_info PRIMARY KEY(brand, type, brand_size, actual_height)
);

create table boy_top_long
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_chest varchar(100),
	actual_chest real,
	brand_sleeve varchar(100),
	actual_sleeve real,
	price real,
	organic char,
	made_in_usa char,
);

create table boy_top_short
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_chest varchar(100),
	actual_chest real,
	brand_sleeve varchar(100),
	actual_sleeve real,
	price real,
	organic char,
	made_in_usa char,
);

create table boy_bottom_pants
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	crotch varchar(100),
	brand_waist varchar(100),
	actual_waist real,
	brand_hip varchar(100),
	actual_hip real,
	brand_instream varchar(100),
	actual_instream real,
	ajustable char,
	price real,
	organic char,
	made_in_usa char,
);

create table boy_bottom_short
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_waist varchar(100),
	actual_waist real,
	brand_hip varchar(100),
	actual_hip real,
	brand_instream varchar(100),
	actual_instream real,
	ajustable char,
	price real,
	organic char,
	made_in_usa char,	
);

create table girl_top_long
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_chest varchar(100),
	actual_chest real,
	brand_sleeve varchar(100),
	actual_sleeve real,
	brand_sweep varchar(100),
	actual_sweep real,
	price real,
	organic char,
	made_in_usa char,
);

create table girl_top_short
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_chest varchar(100),
	actual_chest real,
	brand_sleeve varchar(100),
	actual_sleeve real,
	brand_sweep varchar(100),
	actual_sweep real,
	price real,
	organic char,
	made_in_usa char,	
);

create table girl_bottom_long
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_waist varchar(100),
	actual_waist real,
	brand_hip varchar(100),
	actual_hip real,
	brand_instream varchar(100),
	actual_instream real,
	ajustable char,
	price real,
	organic char,
	made_in_usa char,
);

create table gir_bottom_short
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	brand_waist varchar(100),
	actual_waist real,
	brand_hip varchar(100),
	actual_hip real,
	brand_instream varchar(100),
	actual_instream real,
	ajustable char,
	price real,
	organic char,
	made_in_usa char,
);

create table girl_dress
(
	brand varchar(100) not null,
	actual_height varchar(100) not null,
	brand_size varchar(100) not null,
	brand_weight varchar(100),
	actual_weight real,
	hollow_to_floor char,
	brand_waist varchar(100),
	actual_waist real,
	brand_hip varchar(100),
	actual_hip real,
	brand_sleeve varchar(100),
	actual_sleeve real,
	brand_instream varchar(100),
	actual_instream real,
	price real,
	organic char,
	made_in_usa char,
);