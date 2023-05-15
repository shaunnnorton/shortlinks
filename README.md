# Shortlinks

This is a webserver to run to create shortlinks ah la bit.ly. 

## Enviornmental Variables

* ADMIN_USERNAME
  * This will be the default username used to manage shortlinks created. 
* ADMIN_PASSWORD
  * This will be the default Password used to manage shortlinks created.
* DATABASE_URL
  * The URI of the database to store the shortlinks (LocalFile: sqlite:///database.db)
* POSTGRES_PASSWORD
  * The password for the database. 
* SECRET_KEY
  * The secret key to be used. 
