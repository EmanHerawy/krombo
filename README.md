# Krombo Crew
# **🛡️ Krombo: Blockchain Scam Detection & Risk Assessment**  
![alt text](image.png)
## **🔍 Overview**  
Krombo is an **AI-powered blockchain security analysis tool** designed to **detect scams, fraudulent wallets, and high-risk transactions** in various blockchain networks.  

By analyzing **on-chain behavior, blacklist databases, and social sentiment**, Krombo helps users determine the **trustworthiness of a wallet, token, or asset** before interacting with it.  

---

## **🛠️ Features**  
✅ **Wallet & Token Security Investigation**  
- Queries **blockchain explorers, forensic databases, and security audits**.  
- Extracts **transaction history, blacklist status, and scam links**.  

✅ **Real-Time Risk Assessment**  
- Detects **suspicious behavior** (flash loans, rug pulls, rapid fund movements).  
- Identifies **wallet connections to flagged entities**.  

✅ **Blacklist & Scam Detection**  
- Checks if a wallet or token appears in **known scam databases**.  
- Allows users to **flag new scams**.  

✅ **Social Sentiment & Reputation Analysis**  
- Scrapes **forums, Twitter, and crypto communities** for warnings.  
- Identifies red flags from **public discussions**.  

✅ **Final Risk Score & Report**  
- Aggregates data into a **scam likelihood score (0-100)**.  
- Provides a **detailed report** with risk levels and explanations.  

---

## **🛠️ How It Works**  

Krombo utilizes **CrewAI** to coordinate multiple agents, each specializing in **different aspects of blockchain security analysis**.  

### **🔹 Agents & Their Roles**  

| Agent | Role | Function |  
|--------|-----------------------------|------------------------------------------------|  
| 📖 `researcher` | Blockchain Security Data Researcher | Gathers and analyzes **wallet or asset data** from blockchain forensic and security databases. |  
| 🚨 `wallet_blacklist_checker` | Wallet Blacklist Investigator | Checks if a **wallet or asset** is flagged in **scam or blacklist databases**. |  
| 🔍 `transaction_behavior_analyst` | On-Chain Behavior Analyst | Detects **suspicious transaction patterns** (flash loans, wash trading, rug pulls). |  
| 📢 `sentiment_reputation_analyst` | Reputation & Sentiment Investigator | Scrapes **social media and forums** for warnings or scam reports. |  
| ⚠️ `risk_assessment_expert` | Risk Score & Report Analyst | Aggregates findings and generates a **scam likelihood score** with a risk report. |  

---

## Demo 
check the demo in the `output.logs` file and the screenshot in the `screenshots` folder.
- (Presentation)[https://www.loom.com/share/e593fd836f5e4970856a823b428c02de?sid=285b902c-e38d-4e16-8862-31d9b6431183] 


## **🛠️ CrewAI Workflow**  

1️⃣ **Research & Data Gathering**: Scrapes blockchain explorers, forensic databases, and security audits.  
2️⃣ **Blacklist Check**: Scans known scam and blacklist databases for flagged entities.  
3️⃣ **Transaction Behavior Analysis**: Identifies unusual activities like flash loans and rug pulls.  
4️⃣ **Sentiment Analysis**: Extracts warnings from social media, crypto forums, and communities.  
5️⃣ **Final Risk Assessment**: Aggregates data into a **risk score** with an **explanation report**.  

---

## **🚀 Future Enhancements**  
🔹 **Real-time monitoring & alerts** for scam activities.  
🔹 **AI-powered fraud pattern detection** for emerging threats.  
🔹 **User-submitted scam reporting** for community-driven security.  

---


## **🙌 Contributing**  
Pull requests are welcome! Please open an issue for feature requests or bug reports.  



## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the krombo Crew, assembling the agents and assigning them tasks as defined in your configuration.


## Understanding Your Crew

The krombo Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Krombo Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
