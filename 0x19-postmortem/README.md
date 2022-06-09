![alt text]([http://url/to/img.png](https://drive.google.com/file/d/1RqTEu3CiyYkcrYHFc08UUGUZDS-oKXRi/view?usp=sharing))
# Project 0x19-Postmortem

This is an incident report based on the Holberton School project Web stack debugging #1
## Issue Summary:

After installing Nginx as our web server, we ran into issues when attempting to connect to port 80. This issue causes problems for our user base as it means they will not be able to connect using HTTP.

## Timeline:

* When was the issue detected: 2022-04-25 00:00 (GMT-04:00)
* How was the issue detected: An Automated test failed during deployment
* Actions taken: Researched default installation files for enabled and available sites
* Which team/individuals was the incident escalated to: Luis Manuel Rivera Sanchez
* How the incident was resolved: Changing the default file for enabled sites so it would listen to port 80 instead of port 8080

## Root cause and resolution

NGINX automatically closes port 80 as its default setting. We only needed to look at the default files for enabled sites to see that the server was listening on port 8080 instead of port 80.

<br /> <br />
Because we noticed this issue right after we had installed the Nginx web server, we figured Nginx closes port 80 by default. We decided to look into the default files that come with Nginx. and noticed this was indeed where the issue was. The default file for enabled sites was listening in on port 8080 instead of port 80.

<br /> <br />
Removing that file and instead replacing it with the default file for available sites was enough to fix the issue. The default file for available sites is identical, only that it listened in on port 80.

<br /> <br />
The team was able to confirm the solution after the server was restarted and a curl command was run on port 80.

## Corrective and preventative measures:

Ensuring that all servers are created using a pre-approved script, instead of changing the settings manually should be enough to prevent this type of issue from happening in the future. Continuing to create automated tests that check the configuration files against the acceptance criteria of the team should also ensure that this sort of issue is caught and doesn't occur on production environments.
