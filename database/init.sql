USE [PIMS]
GO

-- create all tables if they have yet to be created
IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='population')
CREATE TABLE [population] (
	ssn varchar(11) NOT NULL PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='location')
CREATE TABLE [location] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [population],
	address_1 varchar(255),
	address_2 varchar(255),
	city varchar(255),
	state varchar(2),
	zip int
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='marital_status')
CREATE TABLE [marital_status] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [population],
	partner_ssn varchar(11) FOREIGN KEY REFERENCES [population]
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='health')
CREATE TABLE [health] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [population],
	sex char(1) NULL,
	date_of_birth date NOT NULL,
	date_of_death date
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='business')
CREATE TABLE [business] (
	business_id int NOT NULL PRIMARY KEY,
	name varchar(255) NOT NULL,
	worth bigint,
	founding_year int NOT NULL
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='business_location')
CREATE TABLE [business_location] (
	business_id int NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [business],
	address varchar(255),
	city varchar(255),
	state varchar(255),
	zip int
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='occupation')
CREATE TABLE [occupation] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [population],
	business_id int FOREIGN KEY REFERENCES [business],
	position varchar(255),
	wage bigint,
	salary bigint
);


-- declare variables, one for path appending and one for iterating through table
-- insert your path to your csv directory here, make sure all are present before running SQL script!
DECLARE @Path VARCHAR(255) = 'YOUR PATH HERE'
DECLARE @NewPath VARCHAR(255)
DECLARE @Tables TABLE ([Table] VARCHAR(255))
DECLARE @CurrTable VARCHAR(255)

-- dynamic SQL 
DECLARE @SQL NVARCHAR(MAX)

-- load table
SET NOCOUNT ON
INSERT INTO @Tables VALUES
('population'), ('business'), ('health'), ('location'), ('marital_status'), ('business_location'), ('occupation')
SET NOCOUNT OFF

-- first clear rows from tables, must delete rows of dependent tables first to maintain
-- referential integrity, so population and business will be deleted last
SET NOCOUNT ON
DELETE FROM [occupation]
DELETE FROM [marital_status]
DELETE FROM [location]
DELETE FROM [health]
DELETE FROM [business_location]
DELETE FROM [population]
DELETE FROM [business]
SET NOCOUNT OFF

-- loop and pop from the table
WHILE EXISTS (SELECT [Table] FROM @Tables)
BEGIN
	-- get first table
	SET NOCOUNT ON
	SELECT TOP 1 @CurrTable = [Table] FROM @Tables
	SET NOCOUNT OFF

	SET @NewPath = @Path + @CurrTable + '.csv'
	
	-- perform insertions
	SET @SQL =
	'
	USE [PIMS]
	BULK INSERT [' + @CurrTable + ']
	FROM ''' + @NewPath + ''' 
	WITH (
		DATAFILETYPE = ''char'',
		FIRSTROW = 2,
		CHECK_CONSTRAINTS,
		ROWTERMINATOR = ''0x0A'',
		FIELDTERMINATOR = '','',
		KEEPNULLS
	);
	SELECT @Count = COUNT(*) FROM [' + @CurrTable + ']
	'
	DECLARE @ROWRESULTS INT
	
	SET NOCOUNT ON
	EXEC sp_executesql @SQL, N'@Count INT OUTPUT', @Count = @ROWRESULTS OUTPUT
	SET NOCOUNT OFF

	PRINT CONCAT('Table [' + @CurrTable + '] established with ', @ROWRESULTS, ' rows.')

	SET NOCOUNT ON
	DELETE FROM @Tables WHERE [Table] = @CurrTable
	SET NOCOUNT OFF
END