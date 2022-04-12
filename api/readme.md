### Instructions to connect to localhost:

* set spring.datasource.url=jdbc:sqlserver://localhost;databaseName=PIMS
* set spring.datasource.username={your username}
* set spring.datasource.password={your password}
* add these:
  * spring.datasource.driverClassName=com.microsoft.sqlserver.jdbc.SQLServerDriver
  * spring.jpa.show-sql=true
  * spring.jpa.hibernate.dialect=org.hibernate.dialect.SQLServer2012Dialect
  * spring.jpa.hibernate.ddl-auto = none

### where to find username and password
* connect to localhost
* Security->Logins->administrator
* Once you click on that you should be able to set a user and pass and that's what you'll use in the resources file.