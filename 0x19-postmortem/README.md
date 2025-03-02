**# Postmortem: Apache Server Outage on Web Application**

## **Issue Summary**
On **March 2, 2025**, from **01:22 AM UTC to 01:45 AM UTC** (23 minutes), my Apache web server experienced an outage that resulted in me not being unable to access the web application. On attempting to reach the application I encountered **HTTP 500 errors or blank pages**. The root cause was a misconfigured Apache configuration file, which was inadvertently moved while debugging a different issue.

## **Timeline**
- **01:22 AM UTC** - Monitoring system alerts that the web application is unresponsive.
- **01:23 AM UTC** - Manual testing via `curl -sI 127.0.0.1` confirms Apache is down.
- **01:25 AM UTC** - Investigates Apache logs (`/var/log/apache2/error.log`) and notices configuration errors.
- **01:28 AM UTC** - Attempted `systemctl restart apache2`, which fails with a missing configuration file error.
- **01:30 AM UTC** - Assumption: The issue is due to a permission problem; checked `/etc/apache2/` permissions but found no issues.
- **01:35 AM UTC** - Further investigation shows `/etc/apache2/apache2.conf` is missing.
- **01:40 AM UTC** - Decided to reinstall Apache to restore the missing configuration.
- **01:43 AM UTC** - Apache reinstalled, configuration restored, and the service restarted successfully.
- **01:45 AM UTC** - Application confirmed operational, and monitoring reports normal response times.

## **Root Cause and Resolution**
### **Root Cause:**
While troubleshooting an unrelated issue and attempting to simulate an HTTP 500 error, the Apache configuration file (`/etc/apache2/apache2.conf`) was mistakenly moved, causing Apache to fail on restart. Without this critical file, Apache could not properly initialize, resulting in the downtime.

### **Resolution:**
1. Identified the missing configuration file by reviewing Apache logs.
2. Verified the issue by running `apachectl configtest`, which confirmed the missing file.
3. Reinstalled Apache to restore default configurations.
4. Restarted Apache using `sudo systemctl restart apache2`, successfully bringing the service back online.
5. Verified application functionality by testing the site manually and using `curl`.
6. Monitored logs for any residual issues.

## **Corrective and Preventative Measures**
### **Improvements/Fixes:**
- Implement safeguards against accidental file deletion/movement.
- Improve monitoring to detect missing configuration files before service failure.

### **To-Do List:**
- [ ] Implement automated backups for `/etc/apache2/` configuration files.
- [ ] Enable version control (e.g., Git) for critical configuration files.
- [ ] Set up alerts for `systemctl status apache2` failures.
- [ ] Document best practices for handling configuration changes.

By implementing these changes, I aim to prevent similar incidents and enhance system reliability.


