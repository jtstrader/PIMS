USE [PIMS]
GO

-- create all tables if they have yet to be created
IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='Population')
CREATE TABLE [Population] (
	ssn varchar(11) NOT NULL PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='Location')
CREATE TABLE [Location] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [Population],
	address_1 varchar(255),
	address_2 varchar(255),
	city varchar(255),
	state varchar(2),
	zip int
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='MaritalStatus')
CREATE TABLE [MaritalStatus] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [Population],
	partner_ssn varchar(11) FOREIGN KEY REFERENCES [Population]
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='Health')
CREATE TABLE [Health] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [Population],
	sex char(1) NULL,
	date_of_birth date NOT NULL,
	date_of_death date
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='Business')
CREATE TABLE [Business] (
	business_id int NOT NULL PRIMARY KEY,
	name varchar(255) NOT NULL,
	worth bigint,
	founding_year int NOT NULL
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='BusinessLocation')
CREATE TABLE [BusinessLocation] (
	business_id int NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [Business],
	address varchar(255),
	city varchar(255),
	state varchar(255),
	zip int
);

IF NOT EXISTS (SELECT * FROM [sys].[tables] WHERE [name]='Occupation')
CREATE TABLE [Occupation] (
	ssn varchar(11) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES [Population],
	business_id int FOREIGN KEY REFERENCES [Business],
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
('Population'), ('Business'), ('Health'), ('Location'), ('MaritalStatus'), ('BusinessLocation'), ('Occupation')
SET NOCOUNT OFF

-- first clear rows from tables, must delete rows of dependent tables first to maintain
-- referential integrity, so Population and Business will be deleted last
SET NOCOUNT ON
DELETE FROM [MaritalStatus]
DELETE FROM [Location]
DELETE FROM [Health]
DELETE FROM [BusinessLocation]
DELETE FROM [Population]
DELETE FROM [Business]
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