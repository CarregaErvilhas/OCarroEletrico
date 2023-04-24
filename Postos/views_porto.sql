ALTER TABLE "Porto"
ADD COLUMN "POTÊNCIA DA TOMADA (kW) NUMERIC" NUMERIC GENERATED ALWAYS AS
	(REPLACE("POTÊNCIA DA TOMADA (kW)", ',', '.'))
  VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN T1kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/kWh ") > 0
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN T2kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 2", "/kWh ") > 0
             THEN replace(substr("TARIFA 2", 2, instr("TARIFA 2", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN T3kWh NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 3", "/kWh ") > 0
             THEN replace(substr("TARIFA 3", 2, instr("TARIFA 3", "/kWh ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;



ALTER TABLE "Porto"
ADD COLUMN T1min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/min ") > 0
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN T2min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 2", "/min ") > 0
             THEN replace(substr("TARIFA 2", 2, instr("TARIFA 2", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN T3min NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 3", "/min ") > 0
             THEN replace(substr("TARIFA 3", 2, instr("TARIFA 3", "/min ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;



ALTER TABLE "Porto"
ADD COLUMN ACTIVAÇÃO NUMERIC GENERATED ALWAYS AS
  (CASE WHEN instr("TARIFA 1", "/charge ") > 0
             THEN replace(substr("TARIFA 1", 2, instr("TARIFA 1", "/charge ")-2), ',', '.')
             ELSE "0"
        END) VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN €kWh NUMERIC GENERATED ALWAYS AS
	(T1kWh + T2kWh + T3kWh)
  VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN €min NUMERIC GENERATED ALWAYS AS
	(T1min + T2min + T3min)
  VIRTUAL;


/* Determina a duração para carregar de 0-100% para um veiculo com bateria de 60kWh a 7.4kW ou 22kW */
 ALTER TABLE "Porto"
ADD COLUMN "Duração (minutos) até 7kW" NUMERIC GENERATED ALWAYS AS
	(
		60
		/
		MIN
		(
			"POTÊNCIA DA TOMADA (kW) NUMERIC"
			,
			7.4
		)
		*60*1.2
	)
  VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN "Duração (minutos) até 22kW" NUMERIC GENERATED ALWAYS AS
	(
		60
		/
		MIN
		(
			"POTÊNCIA DA TOMADA (kW) NUMERIC"
			,
			22
		)
		*60*1.2
	)
  VIRTUAL;


/* Determina a duração para carregar de 20-80% para um veiculo com bateria de 60kWh a té 130kW */
ALTER TABLE "Porto"
ADD COLUMN "Duração (minutos) até 130kW" NUMERIC GENERATED ALWAYS AS
	(
		MAX
		(
			(
				60*.6
				/
				(
					MIN
					(
						"POTÊNCIA DA TOMADA (kW) NUMERIC"
						,
						127
					)
				)
				*60*1.3
			)
			,35
		)
	) /* factor cagaço */
  VIRTUAL;


ALTER TABLE "Porto"
ADD COLUMN "CCS2 Custo €" NUMERIC GENERATED ALWAYS AS
	(
	"ACTIVAÇÃO"
	+
	"€kWh" * (60*.6)
	+
	"€min" * "Duração (minutos) até 130kW"
	)
  VIRTUAL;


ALTER TABLE "Porto"
ADD COLUMN "TYPE2 7kW Custo €" NUMERIC GENERATED ALWAYS AS
	(
	"ACTIVAÇÃO"
	+
	"€kWh" * (60)
	+
	"€min" * "Duração (minutos) até 7kW"
	)
  VIRTUAL;

ALTER TABLE "Porto"
ADD COLUMN "TYPE2 22kW Custo €" NUMERIC GENERATED ALWAYS AS
	(
	"ACTIVAÇÃO"
	+
	"€kWh" * (60)
	+
	"€min" * "Duração (minutos) até 22kW"
	)
  VIRTUAL;


DROP VIEW IF EXISTS [Porto_Todos_Os_Postos];
CREATE VIEW Porto_Todos_Os_Postos
AS
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "CCS2 Custo €") AS "CCS2 Custo €",
	format("%.3f", "TYPE2 7kW Custo €") AS "TYPE2 7kW Custo €",
	format("%.3f", "TYPE2 22kW Custo €") AS "TYPE2 22kW Custo €",
	format("%i", "Duração (minutos) até 130kW") AS "Duração (minutos) até 130kW",
	format("%i", "Duração (minutos) até 7kW") AS "Duração (minutos) até 7kW",
	format("%i", "Duração (minutos) até 22kW") AS "Duração (minutos) até 22kW",
	"POTÊNCIA DA TOMADA (kW)",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"TIPO DE TOMADA",
	"FORMATO DA TOMADA",
	"ESTADO DO POSTO",
	"ESTADO DA TOMADA"
FROM
	"Porto"
ORDER BY
	cast("CCS2 Custo €" as NUMERIC) ASC,
	cast("Duração (minutos) até 130kW" as NUMERIC) ASC;


DROP VIEW IF EXISTS [Porto_CCS2_20_80_percent];
CREATE VIEW Porto_CCS2_20_80_percent
AS
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "CCS2 Custo €") AS "CCS2 Custo €",
	format("%i", "Duração (minutos) até 130kW") AS "Duração (minutos) até 130kW",
	"POTÊNCIA DA TOMADA (kW)",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"FORMATO DA TOMADA",
	"ESTADO DA TOMADA"
FROM
	"Porto"
WHERE
	"TIPO DE TOMADA" LIKE 'CCS' AND "ESTADO DO POSTO" NOT LIKE 'Offline'
ORDER BY
	cast("CCS2 Custo €" as NUMERIC) ASC,
	cast("Duração (minutos) até 130kW" as NUMERIC) ASC;


DROP VIEW IF EXISTS [Porto_TYPE2_7kW_0_100_percent];
CREATE VIEW Porto_TYPE2_7kW_0_100_percent
AS
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "TYPE2 7kW Custo €") AS "TYPE2 7kW Custo €",
	format("%i", "Duração (minutos) até 7kW") AS "Duração (minutos) até 7kW",
	"POTÊNCIA DA TOMADA (kW)",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"FORMATO DA TOMADA",
	"ESTADO DA TOMADA"
FROM
	"Porto"
WHERE
	"TIPO DE TOMADA" like 'Mennekes' AND "ESTADO DO POSTO" NOT LIKE 'Offline'
ORDER BY
	cast("TYPE2 7kW Custo €" as NUMERIC) ASC,
	cast("Duração (minutos) até 7kW" as NUMERIC) ASC;

DROP VIEW IF EXISTS [Porto_TYPE2_22kW_0_100_percent];
CREATE VIEW Porto_TYPE2_22kW_0_100_percent
AS
SELECT
	"UID DA TOMADA",
	CIDADE,
	MORADA,
	OPERADOR,
	format("%.3f", "TYPE2 22kW Custo €") AS "TYPE2 22kW Custo €",
	format("%i", "Duração (minutos) até 22kW") AS "Duração (minutos) até 22kW",
	"POTÊNCIA DA TOMADA (kW)",
	"TARIFA 1",
	"TARIFA 2",
	"TARIFA 3",
	"FORMATO DA TOMADA",
	"ESTADO DA TOMADA"
FROM
	"Porto"
WHERE
	"TIPO DE TOMADA" like 'Mennekes' AND "ESTADO DO POSTO" NOT LIKE 'Offline'
ORDER BY
	cast("TYPE2 22kW Custo €" as NUMERIC) ASC,
	cast("Duração (minutos) até 22kW" as NUMERIC) ASC;
