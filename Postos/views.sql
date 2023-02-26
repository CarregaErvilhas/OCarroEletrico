ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T1kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/kWh ") > 0 
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T2kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 2", "/kWh ") > 0 
             THEN replace(substr("TARIFA 2", 2, instr("TARIFA 2", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T3kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 3", "/kWh ") > 0 
             THEN replace(substr("TARIFA 3", 2, instr("TARIFA 3", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;



ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T1min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/min ") > 0 
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T2min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 2", "/min ") > 0 
             THEN replace(substr("TARIFA 2", 2, instr("TARIFA 2", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN T3min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 3", "/min ") > 0 
             THEN replace(substr("TARIFA 3", 2, instr("TARIFA 3", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;


       
ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN ACTIVAÇÃO NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/charge ") > 0 
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/charge ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN €kWh NUMERIC GENERATED ALWAYS AS
	(T1kWh + T2kWh + T3kWh)
  VIRTUAL;
 
ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN €min NUMERIC GENERATED ALWAYS AS
	(T1min + T2min + T3min)
  VIRTUAL;

 
ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN "CCS2-Custo-€" NUMERIC GENERATED ALWAYS AS
	(
	"ACTIVAÇÃO" + 
	"€kWh" * (45*.6) +
	"€min" * 32
	)
  VIRTUAL;

 
ALTER TABLE "MOBIe_Lista_de_postos.csv"
ADD COLUMN "TYPE2-Custo-€" NUMERIC GENERATED ALWAYS AS
	(
	"ACTIVAÇÃO" + 
	"€kWh" * (45) +
	"€min" * 255
	)
  VIRTUAL;


DROP VIEW IF EXISTS [Todos_Os_Postos];
CREATE VIEW Todos_Os_Postos
AS 
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "CCS2-Custo-€") AS "CCS2-Custo-€",
	format("%.3f", "TYPE2-Custo-€") AS "TYPE2-Custo-€",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"TIPO DE TOMADA",
	"POTÊNCIA DA TOMADA (kW)",
	"FORMATO DA TOMADA",
	"ESTADO DO POSTO",
	"ESTADO DA TOMADA"
FROM
	"MOBIe_Lista_de_postos.csv"
ORDER BY
	cast("CCS2-Custo-€" as NUMERIC) ASC;


DROP VIEW IF EXISTS [CCS];
CREATE VIEW "CCS 20-80%"
AS 
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "CCS2-Custo-€") AS "CCS2-Custo-€",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"POTÊNCIA DA TOMADA (kW)",
	"FORMATO DA TOMADA",
	"ESTADO DA TOMADA"
FROM
	"MOBIe_Lista_de_postos.csv"
WHERE
	"TIPO DE TOMADA" LIKE 'CCS' AND "ESTADO DO POSTO" NOT LIKE 'Offline'
ORDER BY
	cast("CCS2-Custo-€" as NUMERIC) ASC;


DROP VIEW IF EXISTS [TYPE2];
CREATE VIEW "TYPE2 0-100%"
AS 
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "TYPE2-Custo-€") AS "TYPE2-Custo-€",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"POTÊNCIA DA TOMADA (kW)",
	"FORMATO DA TOMADA",
	"ESTADO DA TOMADA"
FROM
	"MOBIe_Lista_de_postos.csv"
WHERE
	"TIPO DE TOMADA" like 'Mennekes' AND "ESTADO DO POSTO" NOT LIKE 'Offline'
ORDER BY
	cast("TYPE2-Custo-€" as NUMERIC) ASC;
