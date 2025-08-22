# Manual testing guide


This document describes manual test cases to validate the functionality of the dual model SOAR .
1. **Prediction** Classifies a URL as MALICIOUS or BENIGN.  
2. **Attribution** If MALICIOUS, attributes it to one of three threat actor:  
   - State-Sponsored  
   - Organized Cybercrime  
   - Hacktivist  

---

# Malicious URL

From the 'URL Feature Input sidebar, select:

**URL length:** long
**SSL Certificate Status:** Suspicious
**Sub-domain Complexity:** one

**URL has a Prefix/Suffix** checked 
**URL uses an IP Address**  checked
**Is it a shortened URL**   unchecked
**URL contains '@' symbol** unchecked
**Is it an abnormal URL**   checked
**URL has political keyword**  unchecked

## Malicious URL testing expected result
   prediction: Malicious Phishing URL
   Malicious Confidence Score: 96.00% 

## Malicious URL testing expected attribution
   This phishing attempt is likely linked to Organized Crime

-------------
# Benign URL

From the 'URL Feature Input sidebar, select:

**URL length:** normal
**SSL Certificate Status:** trusted
**Sub-domain Complexity:** one

**URL has a Prefix/Suffix** unchecked 
**URL uses an IP Address**  unchecked
**Is it a shortened URL**   checked
**URL contains '@' symbol** unchecked
**Is it an abnormal URL**   unchecked
**URL has political keyword**  unchecked

## Malicious URL testing expected result
   Prediction: Benign URL
   Malicious Confidence Score: 15.00% 
