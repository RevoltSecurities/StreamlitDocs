import streamlit as st

# Page Configuration
st.set_page_config(page_title="Subdominator Documentation", layout="wide")

# Sidebar Navigation
st.sidebar.title("📘 Subdominator Documentation")
page = st.sidebar.radio("Go to", [
    "Overview",
    "Installation",
    "Post Installation (API Key Configuration)",
    "Usage",
    "Running Subdominator",
    "Shell Tutorial & Documentation"
])

# ============================
# 📌 OVERVIEW
# ============================
if page == "Overview":
    st.title("Subdominator - An Advanced Subdomain Enumeration Tool")
    st.markdown(
    f'<div style="text-align: center;"><img src="https://raw.githubusercontent.com/RevoltSecurities/Subdominator/refs/heads/main/img/subdominator-v2.png" width="500", height=500></div>',
    unsafe_allow_html=True
)
    st.markdown("""
   ### **Overview:**  

Subdominator is a **high-performance passive subdomain enumeration tool** designed for **security researchers and bug hunters**. Built with **asynchronous execution**, it efficiently leverages **50+ passive sources**, integrating both **free and paid APIs** to maximize discovery coverage.  
With its **lightweight and optimized architecture**, Subdominator ensures **fast enumeration** while seamlessly handling large-scale reconnaissance. It features **real-time notifications** via **Slack and Pushbullet**, enabling instant updates on discovered assets.  

A key advantage of Subdominator is its **local database support**, which automatically stores **enumeration results** on the user’s machine. This allows for **historical subdomain tracking**, enabling users to **reference and analyze past discoveries**, improving efficiency in continuous security monitoring and reconnaissance workflows. 🚀

### **Key Features**  
- **50+ Passive Sources** – Retrieves subdomains from multiple APIs and online databases.  
- **Multi-API Support** – Integrates both free and paid API sources for comprehensive enumeration.  
- **Real-Time Notifications** – Supports Slack,Pushbullter alerts.  
- **Customizable Configuration** – Allows users to include/exclude specific sources.  
- **Multiple Output Formats** – Supports JSON and text-based output.  
- **Stdin/Stdout Support** – Can be used with other tools in automated workflows.  
- **Asynchronous Requests** – Ensures high-speed enumeration with **httpx.AsyncClient**.  
- **Lightweight & Fast** – Designed for efficient and scalable reconnaissance.
    """)

# ============================
# 📌 INSTALLATION
# ============================
elif page == "Installation":
    st.title("⚙️ Installation")
    st.markdown("""
### 🔹 **Installation Guide**  

Ensure you have **Python 3.12 or later** installed before proceeding with the installation. You can verify your Python version using:  

```bash
python3 --version
```  

#### ✅ **Install Subdominator from PyPI** (Recommended)  
The easiest way to install Subdominator is via PyPI:  

```bash
pip install --upgrade subdominator
```  

#### ✅ **Install the Latest Version from GitHub**  
To install the latest development version directly from GitHub:  

```bash
pip install --upgrade git+https://github.com/RevoltSecurities/Subdominator
```  

#### ✅ **Install Using PIPX** (For Isolated Environments)  
To avoid dependency conflicts, you can install Subdominator using `pipx`:  

```bash
pipx install subdominator
```  

To install the latest version from GitHub with `pipx`:  

```bash
pipx install git+https://github.com/RevoltSecurities/Subdominator
```  

#### ✅ **Install from Git Source** (For Development)  
For users who want to contribute or modify the tool, clone and install directly from source:  

```bash
git clone https://github.com/RevoltSecurities/Subdominator.git
cd Subdominator
pip install --upgrade pip
pip install -r requirements.txt
```  

After installation, you can verify if Subdominator is installed correctly by running:  

```bash
subdominator --help
```
    """)

# ============================
# 📌 POST INSTALLATION (API KEYS)
# ============================
elif page == "Post Installation (API Key Configuration)":
    st.title("🔑 API Key Configuration")
    st.markdown("""
## 🔹 **Post-Installation Configuration**  

Subdominator is ready to use immediately after installation. However, to utilize **API-based passive sources**, you need to configure API keys for the following services.  

---

**The following API services used by subdominator**:  

- **AbuseIPDB** → [abuseipdb.com](https://abuseipdb.com)  
- **AlienVault** → [otx.alienvault.com](https://otx.alienvault.com)  
- **Anubis** → [jldc.me/anubis](https://jldc.me/anubis)  
- **ARP Syndicate** → [arpsyndicate.io](https://www.arpsyndicate.io/pricing.html)  
- **BeVigil** → [bevigil.com](https://bevigil.com/login)  
- **BinaryEdge** → [binaryedge.io](https://binaryedge.io)  
- **BufferOver** → [tls.bufferover.run](https://tls.bufferover.run/)  
- **BuiltWith** → [api.builtwith.com](https://api.builtwith.com/domain-api)  
- **C99** → [subdomainfinder.c99.nl](https://subdomainfinder.c99.nl/)  
- **Censys** → [censys.com](https://censys.com/)  
- **CertSpotter** → [sslmate.com/certspotter](https://sslmate.com/certspotter/)  
- **Chaos** → [chaos.projectdiscovery.io](https://chaos.projectdiscovery.io/)  
- **CodeRog** → [rapidapi.com/coderog](https://rapidapi.com/coderog-coderog-default/api/subdomain-finder5/pricing)  
- **CommonCrawl** → [index.commoncrawl.org](https://index.commoncrawl.org/)  
- **crt.sh** → [crt.sh](https://crt.sh)  
- **Cyfare** → [cyfare.net](https://cyfare.net)  
- **Digitorus** → [digitorus.com](https://www.digitorus.com/)  
- **DigitalYama** → [digitalyama.com](https://digitalyama.com/)  
- **DNSDumpster** → [dnsdumpster.com](https://dnsdumpster.com/)  
- **DNSRepo** → [dnsarchive.net](https://dnsarchive.net/)  
- **Fofa** → [en.fofa.info](https://en.fofa.info/)  
- **Facebook** → [developers.facebook.com](https://developers.facebook.com/)  
- **FullHunt** → [fullhunt.io](https://fullhunt.io/)  
- **Google** → [programmablesearchengine.google.com](https://programmablesearchengine.google.com/controlpanel/create)  
- **HackerTarget** → [hackertarget.com](https://hackertarget.com/)  
- **HudsonRock** → [cavalier.hudsonrock.com](https://cavalier.hudsonrock.com)  
- **HunterMap** → [hunter.how](https://hunter.how/)  
- **IntelX** → [intelx.io](https://intelx.io/)  
- **LeakIX** → [leakix.net](https://leakix.net/)  
- **MerkleMap** → [merklemap.com](https://www.merklemap.com)  
- **MySSL** → [myssl.com](https://myssl.com)  
- **Netlas** → [netlas.io](https://netlas.io/)  
- **Odin** → [odin.io](https://odin.io/)  
- **Quake** → [quake.360.cn](https://quake.360.cn/)  
- **Racent** → [face.racent.com](https://face.racent.com)  
- **RapidAPI** → [rapidapi.com/hub](https://rapidapi.com/hub)  
- **RapidDNS** → [rapiddns.io](https://rapiddns.io/)  
- **RedHuntLabs** → [devportal.redhuntlabs.com](https://devportal.redhuntlabs.com/)  
- **RSECloud** → [rsecloud.com/search](https://rsecloud.com/search)  
- **SecurityTrails** → [securitytrails.com](http://securitytrails.com/)  
- **Shodan** → [shodan.io](https://shodan.io)  
- **ShodanX** → [github.com/RevoltSecurities/Shodanx](https://github.com/RevoltSecurities/Shodanx)  
- **ShrewdEye** → [shrewdeye.app](https://shrewdeye.app/api)  
- **SiteDossier** → [sitedossier.com](https://sitedossier.com/)  
- **ThreatCrowd** → [ci-www.threatcrowd.org](http://ci-www.threatcrowd.org/)  
- **Trickest** → [trickest.io](https://trickest.io/)  
- **URLScan** → [urlscan.io](https://urlscan.io/)  
- **VirusTotal** → [virustotal.com](https://virustotal.com/)  
- **WaybackArchive** → [archive.org/wayback](https://archive.org/wayback)  
- **WhoisXML** → [whoisxmlapi.com](https://whoisxmlapi.com)  
- **ZoomEyeAPI** → [www.zoomeye.hk](https://www.zoomeye.hk/)  

---

## **🔧 Google Setup**  

1. **Login to your Google account** in your browser.  
2. Visit [Google Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/create) and create a search engine.  
   - Select **"All Web"** as the search option.  
   - The configuration should look like this:  

   <h1 align="center">
   <img src="https://github.com/RevoltSecurities/GoogleDorker/assets/119435129/7b871906-a08b-4473-bc47-31f797ae88f6" width="700px">
   <br>
   </h1>

3. After successfully creating the search engine, **copy your CX ID**.  
4. Now, grab your **Google API key** from [here](https://developers.google.com/custom-search/v1/introduction).  
5. Click **"Get Key"**, create a new project with any name, and click **Next**.  
6. After generating the API key, click **"Show Key"** and **copy it**.  
7. Add your Google **CX ID and API Key** to the YAML configuration file:  

```yaml
google:
  - 23892479:AIdjhakbkdiudgiao
```

---

## **🔧 RedHunt Labs Attack Surface Recon API**  

- RedHunt Labs provides **different API endpoints** based on the user's subscription.  
- Ensure you **add the correct endpoint** before running any scans.  

Example YAML configuration:  

```yaml
redhuntlabs:
  - ENDPOINT:API_TOKEN
  - https://reconapi.redhuntlabs.com/community/v1/domains/subdomains:joEPzJJp2AuOCw7teAj63HYrPGnsxuPQ
```

---

## **🔧 ZoomEye API Configuration**  

ZoomEye has **geographical access restrictions**:  

- **`api.zoomeye.org`** → **For users inside China**  
- **`api.zoomeye.hk`** → **For users outside China**  

Example YAML configuration:  

```yaml
zoomeyeapi:
  - zoomeye.hk:4f73021d-ff95-4f53-937f-83d6db719eec
```

---

## **📂 Configuration File**  

API keys are stored in the configuration file located at:  

```sh
$HOME/.config/Subdominator/provider-config.yaml
```  

This file is **automatically generated** when you run the tool for the first time.  
It follows the **YAML format**, allowing **multiple API keys** for each service. One key will be **randomly selected** during enumeration.  

```yaml
censys: 
  - API-SECRET:API-KEY
  - 9f5a-be11-4b9e-9564-9596e78:Va92kyMYPS7ANKpI8CjV
facebook:
  - APPID:APPSECRET
  - 1550699734936481:3b2eff7304659559380ad88d8c4b82f
google:
  - CX-ID:API-KEY
  - 34992b4aee9494e7b:AIzaSyCcEqqOERofbkudEY_iVC2_Wfv0A
intelx:
  - HOST:API-KEY
  - 2.intelx.io:1995e804-3c71-4938042-8042802-efa29ae2964d
redhuntlabs: 
  - API-URL:API-KEY
  - https://reconapi.redhuntlabs.com/community/v1/domains/subdomains:VRp7HK3jWiRSnpPfois7979spn4tvDVi0vM
dnsdumpster:
  - z4gi42ifs9asdjbopakwbhorhao0du42po92jkbnkjbsdug082sjbkdhohabdaoiuboadhg
securitytrails:
  - dauobheiuabhougbouUBDOowbdoaobo
shodan:
  - AAAAClP1bJJSRMEYJazgwhJKrggRwKA
zoomeyeapi:
  - API-HOST:API-key
  - api.zoomeye.hk:4f73021d-ff95-4f53-937f-83d6db719eec
dnrepo:
  - ACCESS-TOKEN:API-KEY
  - DIHIdfiuobfoaubobosbdo:3090420DBIUBDOBFO

```

---

## **✅ Final Notes**  

- Ensure your **API keys are valid** and in **valid format** before running the tool.  
- You can **update the config file** anytime to add new keys or services.  

By properly setting up Subdominator, you unlock the full power of comprehensive subdomain reconnaissance using multiple high-quality passive sources. 🚀
    """, unsafe_allow_html=True)

# ============================
# 📌 USAGE
# ============================
elif page == "Usage":
    st.title("🚀 Usage")
    st.markdown("""
Learn Subdominator usage, including input options, resource selection, output customization, and debugging flags.

---

## **Access Help**  
Use `subdominator -h` to display all available options.  

```bash
subdominator -h
```

```console
             _          _                    _                _                
            | |        | |                  (_)              | |               
 ___  _   _ | |__    __| |  ___   _ __ ___   _  _ __    __ _ | |_   ___   _ __ 
/ __|| | | || '_ \  / _` | / _ \ | '_ ` _ \ | || '_ \  / _` || __| / _ \ | '__|
\__ \| |_| || |_) || (_| || (_) || | | | | || || | | || (_| || |_ | (_) || |   
|___/ \__,_||_.__/  \__,_| \___/ |_| |_| |_||_||_| |_| \__,_| \__| \___/ |_|   
                                                                               
                                                                               

                     - RevoltSecurities


[DESCRIPTION]: 

    Subdominator is a passive subdomain enumeration tool that discovers subdomains for your targets using passive and open-source resources.

[USAGE]: 

    subdominator [flags]

[FLAGS]:

    [INPUT]:
    
        -d,   --domain                :  Target domain name for subdomain enumeration.
        -dL,  --domain-list           :  File containing multiple domains for bulk enumeration.
        stdin/stdout                  :  Supports input/output redirection.

    [OUTPUT]:
    
        -o,   --output                :  Save results to a file.
        -oD,  --output-directory      :  Directory to save results (useful when -dL is specified).
        -json, --json                 :  Output results in JSON format.
        
    [MODE]:
    
        -shell, --shell               :  Enable interactive shell mode to work with subdominator Database,generate report and etc.

    [OPTIMIZATION]:
    
        -t,   --timeout               :  Set timeout value for API requests (default: 30s).
        -fw,  --filter-wildcards      :  Filter out wildcard subdomains.

    [CONFIGURATION]:
    
        -cp,  --config-path           :  Custom config file path for API keys (default: $HOME/.config/Subdominator/provider-config.yaml).
        -cdp, --config-db-path        :  Custom database config path (default: $HOME/.cache/SubdominatorDB/subdominator.db).
        -nt,  --notify                :  Send notifications for found subdomains via Slack, Pushbullet.
        -px,  --proxy                 :  Use an HTTP proxy for debugging requests.
        -dork, --dork                 :  Use a custom google dork for google resource (ex: -ir google --dork 'site:target.com -www -dev intext:secrets')

    [RESOURCE CONFIGURATION]:
    
        -ir,  --include-resources     :  Specify sources to include (comma-separated).
        -er,  --exclude-resources     :  Specify sources to exclude (comma-separated).
        -all, --all                   :  Use all available sources for enumeration.

    [UPDATE]:
    
        -up,  --update                :  Update Subdominator to the latest version (manual YAML update required).
        -duc, --disable-update-check  :  Disable automatic update checks.
        -sup, --show-updates          :  Show the latest update details.

    [DEBUGGING]:
    
        -h,   --help                  :  Show this help message and exit.
        -v,   --version               :  Show the current version and check for updates.
        -s,   --silent                :  Show only subdomains in output.
        -ski, --show-key-info         :  Show API key errors (e.g., out of credits).
        -sti, --show-timeout-info     :  Show timeout errors for sources.
        -nc,  --no-color              :  Disable colorized output.
        -ls,  --list-source           :  List available subdomain enumeration sources.
        -V,   --verbose               :  Enable verbose output.

```
    """)

# ============================
# 📌 RUNNING SUBDOMINATOR
# ============================
elif page == "Running Subdominator":
    st.title("🚀 Running Subdominator")
    st.markdown("""
## **1. Basic Execution**  

To start a basic subdomain enumeration, you need to specify a target domain using the `-d` flag:  

```console
subdominator -d hackerone.com

             _          _                    _                _                
            | |        | |                  (_)              | |               
 ___  _   _ | |__    __| |  ___   _ __ ___   _  _ __    __ _ | |_   ___   _ __ 
/ __|| | | || '_ \  / _` | / _ \ | '_ ` _ \ | || '_ \  / _` || __| / _ \ | '__|
\__ \| |_| || |_) || (_| || (_) || | | | | || || | | || (_| || |_ | (_) || |   
|___/ \__,_||_.__/  \__,_| \___/ |_| |_| |_||_||_| |_| \__,_| \__| \___/ |_|   

                     - RevoltSecurities

[version]: subdominator current version v2.1.0 (latest)
[INFO]: Loading provider configuration file from $HOME/.config/Subdominator/provider-config.yaml
[INFO]: Enumerating subdomain for hackerone.com
mta-sts.hackerone.com
info.hackerone.com
go.hackerone.com
o3.email.hackerone.com
resources.hackerone.com
api.hackerone.com
ns.hackerone.com
*.hackerone.com
o1.email.hackerone.com
mta-sts.forwarding.hackerone.com
3d.hackerone.com
www.hackerone.com
a.ns.hackerone.com
design.hackerone.com
links.hackerone.com
gslink.hackerone.com
o2.email.hackerone.com
apis.hackerone.com
events.hackerone.com
docs.hackerone.com
email.hackerone.com
support.hackerone.com
mta-sts.managed.hackerone.com
b.ns.hackerone.com
[INFO]: Total 24 subdomains found for hackerone.com in 6.27 seconds
[INFO]: Happy Hacking th3sanjai ☠️ 🔥 🚀

```
This command will query multiple passive data sources and return a list of discovered subdomains.

To perform enumeration on multiple domains, use the `--domain-list (-dL)` flag:  

```bash
subdominator -dL domains.txt
```
This allows you to run enumeration on a batch of domains provided in a text file.

Alternatively, you can use input redirection:  
```bash
cat domains.txt | subdominator
```
This method is useful when chaining commands or processing results dynamically.

---

## **2. Pipe Results to Other Tools**

Subdominator's output can be seamlessly integrated with other tools for further analysis. For example, you can pipe the discovered subdomains to **SubProber**, which will check for running HTTP services on the identified hosts.  

### **Example: Enumerate Subdomains and Probe HTTP Services**  
```console
subdominator -d hackerone.com -s | subprober --silent -sc -tl

https://mta-sts.managed.hackerone.com [404][Page not found · GitHub Pages]
https://mta-sts.hackerone.com [404][Page not found · GitHub Pages]
http://mta-sts.hackerone.com [404][Page not found · GitHub Pages]
http://mta-sts.managed.hackerone.com [404][Page not found · GitHub Pages]
https://gslink.hackerone.com [404][404 Not Found]
https://api.hackerone.com [200][HackerOne API]
http://resources.hackerone.com [404][Sorry, no Folders found.]
http://api.hackerone.com [200][HackerOne API]
http://gslink.hackerone.com [404][404 Not Found]
https://docs.hackerone.com [200][HackerOne Help Center]
http://docs.hackerone.com [200][HackerOne Help Center]
https://resources.hackerone.com [404][Sorry, no Folders found.]
https://mta-sts.forwarding.hackerone.com [404][Page not found · GitHub Pages]
http://mta-sts.forwarding.hackerone.com [404][Page not found · GitHub Pages]
https://www.hackerone.com [200][HackerOne | #1 Trusted Security Platform and Hacker Program]
http://www.hackerone.com [200][HackerOne | #1 Trusted Security Platform and Hacker Program]
http://support.hackerone.com [200][ Sign into : HackerOne Support Portal ]
https://support.hackerone.com [200][ Sign into : HackerOne Support Portal ]
```

By piping results to other tools, you can streamline reconnaissance and automate advanced enumeration workflows.

---

## **3. Controlling Enumeration Sources**  

Subdominator allows you to customize the enumeration process by selecting or excluding specific sources.

### **Include Specific Sources**  

If you want to use only specific sources, use the `--include-resources (-ir)` flag:  
```bash
subdominator -d example.com -ir crtsh,bevigil,virustotal
```
This will restrict the enumeration to only the specified sources.

### **Exclude Certain Sources**  

To exclude specific sources, use the `--exclude-resources (-er)` flag:  
```bash
subdominator -d example.com -er hackertarget,dnsdumpster
```
This command ensures that the excluded sources are not used during enumeration.

### **Use All Sources**  

To run enumeration using all available sources, use the `--all` flag:  
```bash
subdominator -d example.com --all
```
This enables exhaustive subdomain discovery, though it may take longer to complete.

To list all available sources, use:  
```bash
subdominator --list-source
```
```console

             _          _                    _                _                
            | |        | |                  (_)              | |               
 ___  _   _ | |__    __| |  ___   _ __ ___   _  _ __    __ _ | |_   ___   _ __ 
/ __|| | | || '_ \  / _` | / _ \ | '_ ` _ \ | || '_ \  / _` || __| / _ \ | '__|
\__ \| |_| || |_) || (_| || (_) || | | | | || || | | || (_| || |_ | (_) || |   
|___/ \__,_||_.__/  \__,_| \___/ |_| |_| |_||_||_| |_| \__,_| \__| \___/ |_|   
                                                                               
                     - RevoltSecurities

[version]: subdominator current version v2.1.0 (latest)
[INFO]: Current Available passive resources: [53]
[INFO]: Sources marked with an * needs API key(s) or token(s) configuration to works
[INFO]: Hey sanjai you can config your api keys or token here /home/sanjai/.config/Subdominator/provider-config.yaml to work
abuseipDB                                                                                                                                                                                                                                     
alienvault                                                                                                                                                                                                                                    
anubis                                                                                                                                                                                                                                        
arpsyndicate*                                                                                                                                                                                                                                 
bevigil*                                                                                                                                                                                                                                      
binaryedge*                                                                                                                                                                                                                                   
bufferover*                                                                                                                                                                                                                                   
builtwith*                                                                                                                                                                                                                                    
c99*                                                                                                                                                                                                                                          
censys*                                                                                                                                                                                                                                       
certspotter*                                                                                                                                                                                                                                  
chaos*                                                                                                                                                                                                                                        
coderog*                                                                                                                                                                                                                                      
commoncrawl                                                                                                                                                                                                                                   
crtsh                                                                                                                                                                                                                                         
cyfare                                                                                                                                                                                                                                        
digitorus                                                                                                                                                                                                                                     
digitalyama*                                                                                                                                                                                                                                  
dnsdumpster*                                                                                                                                                                                                                                  
dnsrepo*                                                                                                                                                                                                                                      
fofa*                                                                                                                                                                                                                                         
facebook*                                                                                                                                                                                                                                     
fullhunt*                                                                                                                                                                                                                                     
google*                                                                                                                                                                                                                                       
hackertarget                                                                                                                                                                                                                                  
hudsonrock                                                                                                                                                                                                                                    
huntermap*                                                                                                                                                                                                                                    
intelx*                                                                                                                                                                                                                                       
leakix*                                                                                                                                                                                                                                       
merklemap*                                                                                                                                                                                                                                    
myssl                                                                                                                                                                                                                                         
netlas*                                                                                                                                                                                                                                       
odin*                                                                                                                                                                                                                                         
quake*                                                                                                                                                                                                                                        
racent                                                                                                                                                                                                                                        
rapidapi*                                                                                                                                                                                                                                     
rapiddns                                                                                                                                                                                                                                      
redhuntlabs*                                                                                                                                                                                                                                  
rsecloud*                                                                                                                                                                                                                                     
securitytrails*                                                                                                                                                                                                                               
shodan*                                                                                                                                                                                                                                       
shodanx                                                                                                                                                                                                                                       
shrewdeye                                                                                                                                                                                                                                     
sitedossier                                                                                                                                                                                                                                   
threatcrowd                                                                                                                                                                                                                                   
trickest*                                                                                                                                                                                                                                     
urlscan                                                                                                                                                                                                                                       
virustotal*                                                                                                                                                                                                                                   
waybackarchive                                                                                                                                                                                                                                
whoisxml*                                                                                                                                                                                                                                     
zoomeyeapi*                                                                                                                                                                                                                                   
rapidfinder*                                                                                                                                                                                                                                  
rapidscan* 
```
---

## **4. Saving and Formatting Output**  

### **Save Results to a File**  
To save discovered subdomains to a file, use the `--output (-o)` flag:  
```bash
subdominator -d example.com -o results.txt
```

### **Save Results in a Directory (for bulk enumeration)**  
When running bulk enumeration (`-dL`), you can store results in a directory:  
```bash
subdominator -dL domains.txt -oD ./output/
```
This will create separate files for each domain inside the specified directory.

### **JSON Output**  
To store the results in JSON format, use the `--json` flag:  
```bash
subdominator -d example.com --json -o results.json
```

---

## **5. Handling Wildcards and Performance Optimization**  

### **Filtering Wildcard Subdomains**  
Many domains use wildcard DNS records, which may result in false positives. To filter them out, use:  
```bash
subdominator -d example.com -fw
```

### **Setting API Request Timeout**  
To control request timeout (default: 30s), use:  
```bash
subdominator -d example.com -t 15
```
This reduces the timeout to 15 seconds per request, which may speed up the enumeration.

---

## **6. Using a Proxy for Debugging**  

If you need to debug requests using a proxy (such as Burp Suite or an HTTP proxy), you can enable it using:  
```bash
subdominator -d example.com -px http://127.0.0.1:8080
```

---

## **7. Google Dorking Integration**  

Subdominator supports Google Dorking to find additional subdomains via Google Search. You can provide a custom dork using:  
```bash
subdominator -ir google --dork "site:example.com -www -dev intext:secrets"
```
This allows advanced search queries to find hidden subdomains.

---

## **8. Updating Subdominator**  

To check for new updates and upgrade to the latest version:  
```bash
subdominator --update
```
To disable automatic update checks:  
```bash
subdominator --disable-update-check
```
To display the latest update details:  
```bash
subdominator --show-updates
```

---

## **9. Debugging and Verbose Logging**  

### **Enable Verbose Output**  
To view detailed logs of the enumeration process:  
```bash
subdominator -d example.com -V
```

### **Silent Mode (Only Subdomains Output)**  
To get clean output containing only subdomains (useful for automation):  
```bash
subdominator -d example.com -s
```

### **Show API Key Errors**  
To identify API key issues (e.g., expired or out of credits):  
```bash
subdominator -d example.com --show-key-info
```

### **Show Timeout Issues**  
To display sources that encountered timeouts:  
```bash
subdominator -d example.com --show-timeout-info
```

### **Disable Colored Output**  
If needed, you can disable color formatting in the terminal:  
```bash
subdominator -d example.com --no-color
```

---

    """)

# ============================
# 📌 SHELL DOCUMENTATION
# ============================
elif page == "Shell Tutorial & Documentation":
    st.title("💻 Shell Tutorial & Documentation")
    st.markdown("""
# **SubDominator Shell Mode - Documentation & Tutorial**  

## **Introduction**  
The **SubDominator Shell Mode** is an interactive command-line interface that allows users to manage, query, and export domain and subdomain data stored in a database. This shell provides a streamlined approach to handling subdomain enumeration data efficiently with built-in commands for database operations, reporting, and exporting results.

## **Starting the SubDominator Shell**  
To start the SubDominator interactive shell mode, use the following command:  

```bash
subdominator -shell
```

This command launches the shell, allowing you to execute various database operations interactively.

---

## **Available Commands & Usage**  
The shell provides the following commands for interacting with the database:

### **1. Connect to the Database**
```bash
connect db
```
- Establishes a connection to the SubDominator database.  
- This command must be executed before using any database-related commands.  
- If the database is not connected, attempting to run other commands will result in an error.  

**Example:**  
```bash
[subdominator]$ connect db
[✔] Connected to SubDominator Database.
```

---

### **2. Show All Domains in the Database**
```bash
show domains
```
- Displays a list of all stored domains.  

**Example:**  
```bash
[subdominator]$ show domains
┌──────────────────────┐
│       Domain         │
├──────────────────────┤
│ example.com          │
│ testsite.com         │
└──────────────────────┘
```

---

### **3. Show Subdomains of a Specific Domain**
```bash
show subdomain <domain>
```
- Lists all stored subdomains of the given domain.  

**Example:**  
```bash
[subdominator]$ show subdomain example.com
┌────────────────────────┐
│       Subdomain        │
├────────────────────────┤
│ sub1.example.com       │
│ sub2.example.com       │
└────────────────────────┘
```

---

### **4. Add a Domain with Subdomains from a File**
```bash
add domain <domain> <subdomains_file>
```
- Adds a domain and its subdomains to the database from a file.  
- The file should contain one subdomain per line.  

**Example:**  
```bash
[subdominator]$ add domain example.com subdomains.txt
[✔] Domain example.com added successfully!
```

---

### **5. Update an Existing Domain’s Subdomains**
```bash
update <domain> <subdomains_file>
```
- Updates the subdomains of an existing domain with new entries from a file.  
- If the domain does not exist in the database, an error is displayed.  

**Example:**  
```bash
[subdominator]$ update example.com updated_subdomains.txt
[✔] Domain example.com updated successfully!
```

---

### **6. Delete a Domain and Its Subdomains**
```bash
delete <domain>
```
- Removes a domain and all associated subdomains from the database.  

**Example:**  
```bash
[subdominator]$ delete example.com
[✖] Domain example.com and all its records deleted successfully!
```

---

### **7. Export Domain Data**
```bash
export <domain> <filename> <format>
```
- Exports the subdomains of a given domain into a file.  
- The format can be `txt` or `json`.  

**Examples:**  
```bash
[subdominator]$ export example.com subdomains.txt txt
[✔] Data exported to subdomains.txt successfully!

[subdominator]$ export example.com subdomains.json json
[✔] Data exported to subdomains.json successfully!
```

---

### **8. Generate a Report**
```bash
report <domain> <filename> <format>
```
- Generates a detailed report for the specified domain in either `HTML` or `PDF` format.  
- The report includes a list of all subdomains associated with the domain.  

**Examples:**  
```bash
[subdominator]$ report example.com report.html html
[✔] HTML report saved as report.html

[subdominator]$ report example.com report.pdf pdf
[✔] PDF report saved as report.pdf
```

---

### **9. Exit the Shell**
```bash
exit
```
- Exits the SubDominator interactive shell.  

**Example:**  
```bash
[subdominator]$ exit
[✖] Exiting SubDominator Shell...
```

---

### **10. View Help Menu**
```bash
help
```
- Displays the available commands and their usage.  

**Example Output:**  
```bash
[subdominator]$ help

Available Commands:
  connect db                            - Connect to SubDominator DataBase
  show domains                          - Show all domains
  show subdomain <domain>               - Show subdomains of a domain
  add domain <domain> <subdomains_file> - Add a domain
  update <domain> <subdomains_file>     - Update an existing domain
  delete <domain>                       - Delete a domain and all subdomains
  export <domain> <file> <format>       - Export data to txt/json
  report <domain> <file> <format>       - Generate subdomains report in html/pdf format
  exit                                  - Exit the interactive shell
  help                                  - Show this help menu
  System Commands                       - ls, clear, pwd, cd, cat, echo, mkdir, rm, cp, mv
```

---

    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Team [RevoltSecurities](https://github.com/RevoltSecurities)")
