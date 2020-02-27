#Hunter.io contact harverster for recon-ng


## What does it do?
This is a <a href="https://bitbucket.org/LaNMaSteR53/recon-ng">recon-ng</a> module that allows to import contacts from a <a href="https://www.hunter.io">hunter.io</a>. It takes the all contacts found for a domain and stores them into the contacts tables.

## Installation
Just put it in the `modules/recon/domain-contacts` directory (or any modules subdirectory) of the recon-ng framwork. This is

     ~/.recon-ng/modules/recon/domain-contacts
     
on Kali.

Do 

    modules reload
    
and you should be ready to go.

## Example

```
[recon-ng][default] > workspaces create Telekom
[recon-ng][telekom] > db insert domains
domain (TEXT): telekom.de
notes (TEXT): 
[*] 1 rows affected.
[recon-ng][telekom] > modules load recon/domains-contacts/hunter
[recon-ng][telekom][hunter] > run
...

```
## Help

```
[recon-ng][telekom][hunter] > info

      Name: Hunter.io Contact Harvester
    Author: schwankner
   Version: 1.0
      Keys: emailhunter_key

Description:
  Harvests contacts from hunter.io API V2 using domain.

Options:
  Name    Current Value  Required  Description
  ------  -------------  --------  -----------
  SOURCE  default        yes       source of input (see 'info' for details)

Source Options:
  default        SELECT DISTINCT domain FROM domains WHERE domain IS NOT NULL
  <string>       string representing a single input
  <path>         path to a file containing a list of inputs
  query <sql>    database query returning one column of inputs

```
## Notes
This plugin works by retrieving e-mail addresses from the offical hunter.io V2 api.  

Please note you need a valid api-key to obtain the e-mail addresses

