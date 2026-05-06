import streamlit as st
import pandas as pd
import plotly.express as px
import re

# ==================================================
# Page setup
# ==================================================
st.set_page_config(
    page_title="AI Technology Intelligence Scout",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Technology Intelligence Scout")
st.caption(
    "Search journals, news, industry signals, vendors, patents, and technology trends to detect the right technology."
)

st.markdown("""
This app works as an **AI technology scouting and horizon scanning tool**.

It helps users:
- Search technology options
- Compare technologies
- Detect best-fit solutions
- Score investment readiness
- Review related references
- Navigate to external reference sources
- Recommend whether to **Explore, Pilot, Scale, or Avoid**
""")

# ==================================================
# Technology Intelligence Database
# ==================================================
technology_database = [
    {
        "Technology": "AI Clinical Decision Support System",
        "Category": "Artificial Intelligence",
        "Industry": "Healthcare",
        "Use Cases": "clinical decision support diagnosis triage treatment recommendation hospital workflow patient safety",
        "Journal Signals": "machine learning clinical decision support predictive analytics diagnostic accuracy AI healthcare",
        "News Signals": "AI hospitals digital health clinical automation healthcare AI adoption",
        "Industry Signals": "electronic health records hospital automation patient safety value based care",
        "Vendor Signals": "EHR vendors AI healthtech clinical AI platforms",
        "Patent Signals": "AI diagnosis predictive model clinical workflow optimization",
        "Lifecycle": "Growth",
        "TRL": 7,
        "Strategic Fit": 9,
        "Integration Cost": 6,
        "Vendor Stability": 8,
        "Security Risk": 6,
        "Regulatory Risk": 8,
        "Pilot Evidence": 7,
        "Description": "Uses AI and machine learning to support clinical diagnosis, triage, treatment recommendations, and hospital decision-making.",
        "Journal References": [
            "AI-based clinical decision support systems for improving diagnostic accuracy.",
            "Machine learning models for clinical prediction and decision support.",
            "Evaluation of AI-enabled clinical decision support in hospital workflows."
        ],
        "News References": [
            "Hospitals are increasingly adopting AI tools to support clinicians and improve workflow efficiency.",
            "Digital health companies are expanding clinical AI tools for diagnosis and triage support."
        ],
        "Industry References": [
            "Electronic Health Record integration with clinical decision support.",
            "Hospital digital transformation and AI-enabled patient safety systems.",
            "Healthcare AI governance and clinical validation frameworks."
        ],
        "Vendor References": [
            "Epic clinical decision support solutions.",
            "Oracle Health clinical intelligence tools.",
            "Microsoft Cloud for Healthcare AI services."
        ],
        "Patent Regulatory References": [
            "AI-assisted diagnostic decision support patents.",
            "Medical software as a medical device regulatory guidance.",
            "Clinical AI risk management and validation requirements."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: AI clinical decision support",
                    "URL": "https://scholar.google.com/scholar?q=AI+clinical+decision+support+systems",
                    "Description": "Search academic papers about AI-based clinical decision support systems."
                },
                {
                    "Title": "PubMed: Clinical decision support artificial intelligence",
                    "URL": "https://pubmed.ncbi.nlm.nih.gov/?term=clinical+decision+support+artificial+intelligence",
                    "Description": "Search biomedical research on clinical AI and decision support."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: AI clinical decision support healthcare",
                    "URL": "https://news.google.com/search?q=AI+clinical+decision+support+healthcare",
                    "Description": "Explore recent market and hospital adoption news."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Microsoft Cloud for Healthcare",
                    "URL": "https://www.microsoft.com/en-us/industry/health/microsoft-cloud-for-healthcare",
                    "Description": "Explore Microsoft healthcare cloud and AI services."
                },
                {
                    "Title": "Search: Healthcare AI decision support vendors",
                    "URL": "https://www.google.com/search?q=healthcare+AI+clinical+decision+support+vendors",
                    "Description": "Search for companies offering clinical decision support solutions."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: AI clinical decision support",
                    "URL": "https://patents.google.com/?q=AI+clinical+decision+support",
                    "Description": "Explore patents related to AI-based clinical decision systems."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "FDA Software as a Medical Device",
                    "URL": "https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd",
                    "Description": "Review guidance related to medical software and digital health."
                },
                {
                    "Title": "WHO Digital Health",
                    "URL": "https://www.who.int/health-topics/digital-health",
                    "Description": "Review global digital health guidance and resources."
                }
            ]
        }
    },

    {
        "Technology": "IoMT Remote Patient Monitoring",
        "Category": "Internet of Medical Things",
        "Industry": "Healthcare",
        "Use Cases": "remote patient monitoring chronic disease wearable sensors home care telemedicine physiological monitoring",
        "Journal Signals": "wearable sensors physiological monitoring telemedicine remote care IoMT",
        "News Signals": "remote monitoring virtual care digital health connected devices",
        "Industry Signals": "IoMT home healthcare chronic disease management hospital at home",
        "Vendor Signals": "medical device companies wearable health platforms cloud monitoring",
        "Patent Signals": "sensor monitoring wireless medical device physiological data",
        "Lifecycle": "Growth",
        "TRL": 8,
        "Strategic Fit": 8,
        "Integration Cost": 7,
        "Vendor Stability": 7,
        "Security Risk": 7,
        "Regulatory Risk": 7,
        "Pilot Evidence": 8,
        "Description": "Uses connected medical devices and wearable sensors to monitor patient health remotely.",
        "Journal References": [
            "IoMT-enabled remote patient monitoring for chronic disease management.",
            "Wearable sensors for physiological signal monitoring.",
            "Telemedicine and remote care technologies in modern healthcare."
        ],
        "News References": [
            "Remote patient monitoring adoption increased after the expansion of virtual care.",
            "Hospitals and home-care providers are investing in connected medical devices."
        ],
        "Industry References": [
            "Hospital-at-home models using connected devices.",
            "Cloud-based patient monitoring platforms.",
            "IoMT cybersecurity and interoperability frameworks."
        ],
        "Vendor References": [
            "Philips remote patient monitoring solutions.",
            "Medtronic connected care technologies.",
            "GE HealthCare monitoring platforms."
        ],
        "Patent Regulatory References": [
            "Wireless physiological monitoring device patents.",
            "Medical device data privacy requirements.",
            "Remote monitoring reimbursement and regulatory policies."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: IoMT remote patient monitoring",
                    "URL": "https://scholar.google.com/scholar?q=IoMT+remote+patient+monitoring",
                    "Description": "Find research papers about IoMT and remote monitoring."
                },
                {
                    "Title": "PubMed: wearable sensors remote patient monitoring",
                    "URL": "https://pubmed.ncbi.nlm.nih.gov/?term=wearable+sensors+remote+patient+monitoring",
                    "Description": "Search biomedical research on wearable monitoring and remote care."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: Remote patient monitoring digital health",
                    "URL": "https://news.google.com/search?q=remote+patient+monitoring+digital+health",
                    "Description": "Review recent news about RPM and connected health."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Philips Healthcare",
                    "URL": "https://www.philips.com/healthcare",
                    "Description": "Explore monitoring and connected care solutions."
                },
                {
                    "Title": "Search: IoMT vendors",
                    "URL": "https://www.google.com/search?q=IoMT+remote+patient+monitoring+vendors",
                    "Description": "Search for IoMT and remote monitoring vendors."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Remote patient monitoring wearable sensors",
                    "URL": "https://patents.google.com/?q=remote+patient+monitoring+wearable+sensors",
                    "Description": "Explore patents related to wearable sensors and remote monitoring."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "FDA Digital Health Center of Excellence",
                    "URL": "https://www.fda.gov/medical-devices/digital-health-center-excellence",
                    "Description": "Review digital health and connected medical device guidance."
                },
                {
                    "Title": "WHO Medical Devices",
                    "URL": "https://www.who.int/health-topics/medical-devices",
                    "Description": "Review global guidance on medical devices."
                }
            ]
        }
    },

    {
        "Technology": "Robotic Process Automation",
        "Category": "Automation",
        "Industry": "Healthcare",
        "Use Cases": "claims processing appointment scheduling billing data entry administrative automation hospital workflow",
        "Journal Signals": "workflow automation hospital administration operational efficiency RPA healthcare",
        "News Signals": "RPA healthcare automation back office digital transformation",
        "Industry Signals": "cost reduction administrative efficiency process automation",
        "Vendor Signals": "UiPath Automation Anywhere Microsoft Power Automate",
        "Patent Signals": "workflow automation robotic process automation data extraction",
        "Lifecycle": "Maturity",
        "TRL": 9,
        "Strategic Fit": 8,
        "Integration Cost": 4,
        "Vendor Stability": 9,
        "Security Risk": 4,
        "Regulatory Risk": 3,
        "Pilot Evidence": 9,
        "Description": "Automates repetitive administrative and operational workflows in hospitals and healthcare organizations.",
        "Journal References": [
            "Robotic process automation in healthcare administration.",
            "Workflow automation for improving hospital operational efficiency.",
            "Digital transformation of administrative healthcare processes."
        ],
        "News References": [
            "Healthcare providers are using RPA to reduce administrative burden.",
            "RPA adoption is growing in billing, claims, and scheduling workflows."
        ],
        "Industry References": [
            "Back-office automation in hospitals.",
            "Revenue cycle automation.",
            "Administrative workflow optimization."
        ],
        "Vendor References": [
            "UiPath healthcare automation.",
            "Automation Anywhere healthcare solutions.",
            "Microsoft Power Automate."
        ],
        "Patent Regulatory References": [
            "Workflow automation and document processing patents.",
            "Data privacy requirements for automated healthcare workflows.",
            "Healthcare administrative automation governance."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: RPA in healthcare",
                    "URL": "https://scholar.google.com/scholar?q=robotic+process+automation+in+healthcare",
                    "Description": "Search research on robotic process automation in healthcare."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: RPA healthcare automation",
                    "URL": "https://news.google.com/search?q=RPA+healthcare+automation",
                    "Description": "Review news about healthcare RPA adoption."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "UiPath Healthcare Automation",
                    "URL": "https://www.uipath.com/solutions/industry/healthcare",
                    "Description": "Explore RPA solutions for healthcare."
                },
                {
                    "Title": "Microsoft Power Automate",
                    "URL": "https://powerautomate.microsoft.com/",
                    "Description": "Explore Microsoft workflow automation platform."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: RPA healthcare",
                    "URL": "https://patents.google.com/?q=robotic+process+automation+healthcare",
                    "Description": "Search patents related to healthcare workflow automation."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "HIPAA Information",
                    "URL": "https://www.hhs.gov/hipaa/index.html",
                    "Description": "Review US healthcare privacy rules relevant to automated workflows."
                }
            ]
        }
    },

    {
        "Technology": "Generative AI Chatbot",
        "Category": "Generative AI",
        "Industry": "Healthcare",
        "Use Cases": "patient support staff support medical education administrative assistance chatbot knowledge assistant",
        "Journal Signals": "large language models healthcare chatbot patient communication medical education generative AI",
        "News Signals": "ChatGPT healthcare generative AI hospital assistant digital front door",
        "Industry Signals": "customer experience patient engagement automation knowledge assistant",
        "Vendor Signals": "OpenAI Microsoft Google Anthropic healthcare chatbot vendors",
        "Patent Signals": "conversational AI medical chatbot natural language processing",
        "Lifecycle": "Growth",
        "TRL": 7,
        "Strategic Fit": 8,
        "Integration Cost": 5,
        "Vendor Stability": 7,
        "Security Risk": 7,
        "Regulatory Risk": 6,
        "Pilot Evidence": 7,
        "Description": "Supports patients, staff, and administrators through conversational AI and knowledge assistance.",
        "Journal References": [
            "Large language models in healthcare communication.",
            "Generative AI for medical education and patient engagement.",
            "Evaluation of chatbot safety and accuracy in healthcare settings."
        ],
        "News References": [
            "Hospitals are testing generative AI assistants for patient communication.",
            "Healthcare organizations are exploring AI chatbots for administrative support."
        ],
        "Industry References": [
            "Digital front door platforms.",
            "Patient engagement automation.",
            "Knowledge management and staff support systems."
        ],
        "Vendor References": [
            "OpenAI API.",
            "Microsoft Azure OpenAI Service.",
            "Google Cloud healthcare AI tools."
        ],
        "Patent Regulatory References": [
            "Conversational AI patents for healthcare support.",
            "Privacy and safety considerations for AI chatbots.",
            "Clinical governance requirements for generative AI tools."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Large language models healthcare chatbot",
                    "URL": "https://scholar.google.com/scholar?q=large+language+models+healthcare+chatbot",
                    "Description": "Search academic literature on healthcare chatbots and LLMs."
                },
                {
                    "Title": "PubMed: Generative AI healthcare chatbot",
                    "URL": "https://pubmed.ncbi.nlm.nih.gov/?term=generative+AI+healthcare+chatbot",
                    "Description": "Search biomedical research on generative AI chatbots."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: Generative AI healthcare chatbot",
                    "URL": "https://news.google.com/search?q=generative+AI+healthcare+chatbot",
                    "Description": "Review recent news about healthcare AI chatbots."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Azure OpenAI Service",
                    "URL": "https://azure.microsoft.com/en-us/products/ai-services/openai-service",
                    "Description": "Explore enterprise generative AI deployment options."
                },
                {
                    "Title": "OpenAI API",
                    "URL": "https://openai.com/api/",
                    "Description": "Explore OpenAI API options for chatbot development."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Conversational AI healthcare chatbot",
                    "URL": "https://patents.google.com/?q=conversational+AI+healthcare+chatbot",
                    "Description": "Explore patents related to conversational AI in healthcare."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "FDA Digital Health",
                    "URL": "https://www.fda.gov/medical-devices/digital-health-center-excellence",
                    "Description": "Review digital health regulatory guidance."
                },
                {
                    "Title": "NIST AI Risk Management Framework",
                    "URL": "https://www.nist.gov/itl/ai-risk-management-framework",
                    "Description": "Review AI governance and risk management guidance."
                }
            ]
        }
    },

    {
        "Technology": "Predictive Maintenance for Medical Equipment",
        "Category": "AI and IoT",
        "Industry": "Healthcare",
        "Use Cases": "medical equipment maintenance downtime prediction biomedical engineering asset management hospital equipment reliability",
        "Journal Signals": "predictive maintenance medical devices equipment failure machine learning biomedical engineering",
        "News Signals": "AI maintenance healthcare equipment uptime hospital engineering",
        "Industry Signals": "asset management biomedical engineering cost reduction equipment reliability",
        "Vendor Signals": "CMMS vendors IoT platforms predictive maintenance vendors IBM Maximo Siemens GE HealthCare",
        "Patent Signals": "equipment failure prediction sensor maintenance medical device",
        "Lifecycle": "Growth",
        "TRL": 8,
        "Strategic Fit": 9,
        "Integration Cost": 6,
        "Vendor Stability": 8,
        "Security Risk": 5,
        "Regulatory Risk": 5,
        "Pilot Evidence": 8,
        "Description": "Uses AI and IoT data to predict medical equipment failure, reduce downtime, and improve biomedical engineering maintenance.",
        "Journal References": [
            "Predictive maintenance using machine learning for healthcare equipment reliability.",
            "IoT-enabled condition monitoring for medical device maintenance.",
            "Artificial intelligence for biomedical equipment management and failure prediction."
        ],
        "News References": [
            "Healthcare organizations are increasingly adopting AI-enabled asset monitoring to reduce equipment downtime.",
            "Hospitals are using predictive analytics to improve operational efficiency and equipment availability."
        ],
        "Industry References": [
            "Computerized Maintenance Management Systems integrated with IoT sensors.",
            "Healthcare asset management platforms for biomedical engineering departments.",
            "Smart hospital infrastructure and connected equipment monitoring."
        ],
        "Vendor References": [
            "IBM Maximo Application Suite.",
            "Siemens Healthineers digital service solutions.",
            "GE HealthCare asset performance management solutions."
        ],
        "Patent Regulatory References": [
            "Patents related to sensor-based equipment failure prediction.",
            "Medical device cybersecurity and maintenance documentation requirements.",
            "Healthcare technology management standards and risk-based maintenance guidance."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Predictive maintenance healthcare equipment",
                    "URL": "https://scholar.google.com/scholar?q=predictive+maintenance+healthcare+equipment+machine+learning",
                    "Description": "Find academic papers about predictive maintenance for healthcare equipment."
                },
                {
                    "Title": "Google Scholar: IoT condition monitoring medical equipment",
                    "URL": "https://scholar.google.com/scholar?q=IoT+condition+monitoring+medical+equipment",
                    "Description": "Find research about IoT-based medical equipment monitoring."
                },
                {
                    "Title": "PubMed: Predictive maintenance medical equipment",
                    "URL": "https://pubmed.ncbi.nlm.nih.gov/?term=predictive+maintenance+medical+equipment",
                    "Description": "Search biomedical research related to medical equipment maintenance."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: AI healthcare equipment predictive maintenance",
                    "URL": "https://news.google.com/search?q=AI+healthcare+equipment+predictive+maintenance",
                    "Description": "Review recent news about AI-based healthcare equipment maintenance."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "IBM Maximo",
                    "URL": "https://www.ibm.com/products/maximo",
                    "Description": "Explore enterprise asset management and predictive maintenance solutions."
                },
                {
                    "Title": "Search: Healthcare CMMS predictive maintenance",
                    "URL": "https://www.google.com/search?q=healthcare+CMMS+predictive+maintenance",
                    "Description": "Search for computerized maintenance management systems used in healthcare."
                },
                {
                    "Title": "Search: Medical equipment asset management platforms",
                    "URL": "https://www.google.com/search?q=medical+equipment+asset+management+platforms",
                    "Description": "Explore platforms for biomedical engineering asset management."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Medical equipment predictive maintenance",
                    "URL": "https://patents.google.com/?q=medical+equipment+predictive+maintenance",
                    "Description": "Explore patents related to medical equipment failure prediction and maintenance."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "FDA Medical Device Software Guidance",
                    "URL": "https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd",
                    "Description": "Review regulatory guidance for software used in medical device contexts."
                },
                {
                    "Title": "WHO Medical Devices",
                    "URL": "https://www.who.int/health-topics/medical-devices",
                    "Description": "Review global information about medical device management and safety."
                },
                {
                    "Title": "Search: ISO 14971 medical device risk management",
                    "URL": "https://www.google.com/search?q=ISO+14971+medical+device+risk+management",
                    "Description": "Search for medical device risk management guidance."
                }
            ]
        }
    },

    {
        "Technology": "Digital Twin for Hospitals",
        "Category": "Simulation and Digital Twin",
        "Industry": "Healthcare",
        "Use Cases": "hospital operations bed management patient flow facility planning equipment utilization simulation",
        "Journal Signals": "digital twin hospital operations simulation patient flow optimization",
        "News Signals": "digital twin healthcare smart hospital operational simulation",
        "Industry Signals": "smart hospitals predictive operations asset optimization",
        "Vendor Signals": "Siemens Dassault Microsoft Azure digital twin platforms",
        "Patent Signals": "digital twin simulation hospital workflow asset monitoring",
        "Lifecycle": "Growth",
        "TRL": 6,
        "Strategic Fit": 9,
        "Integration Cost": 8,
        "Vendor Stability": 7,
        "Security Risk": 6,
        "Regulatory Risk": 5,
        "Pilot Evidence": 6,
        "Description": "Creates a virtual model of hospital operations to simulate and optimize resources, workflows, equipment, and patient flow.",
        "Journal References": [
            "Digital twin applications for hospital operations.",
            "Simulation-based patient flow optimization.",
            "Smart hospital planning using digital twin technology."
        ],
        "News References": [
            "Healthcare systems are exploring digital twins for operational planning.",
            "Smart hospitals are adopting simulation tools to improve efficiency."
        ],
        "Industry References": [
            "Smart hospital operations.",
            "Predictive facility planning.",
            "Asset optimization and hospital command centers."
        ],
        "Vendor References": [
            "Siemens digital twin solutions.",
            "Dassault Systèmes healthcare simulation.",
            "Microsoft Azure Digital Twins."
        ],
        "Patent Regulatory References": [
            "Digital twin simulation patents.",
            "Hospital facility planning and data governance requirements.",
            "Operational simulation and privacy considerations."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Digital twin hospital operations",
                    "URL": "https://scholar.google.com/scholar?q=digital+twin+hospital+operations",
                    "Description": "Search papers on digital twins for hospital operations."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: Digital twin healthcare smart hospital",
                    "URL": "https://news.google.com/search?q=digital+twin+healthcare+smart+hospital",
                    "Description": "Review news about smart hospitals and digital twins."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Microsoft Azure Digital Twins",
                    "URL": "https://azure.microsoft.com/en-us/products/digital-twins",
                    "Description": "Explore Azure digital twin platform."
                },
                {
                    "Title": "Search: Hospital digital twin vendors",
                    "URL": "https://www.google.com/search?q=hospital+digital+twin+vendors",
                    "Description": "Search vendors offering hospital digital twin solutions."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Digital twin hospital",
                    "URL": "https://patents.google.com/?q=digital+twin+hospital",
                    "Description": "Explore patents related to hospital digital twin technologies."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "NIST Cybersecurity Framework",
                    "URL": "https://www.nist.gov/cyberframework",
                    "Description": "Review cybersecurity guidance for connected digital platforms."
                }
            ]
        }
    },

    {
        "Technology": "Computer Vision Quality Inspection",
        "Category": "Computer Vision",
        "Industry": "Manufacturing",
        "Use Cases": "defect detection visual inspection quality control production line manufacturing automation",
        "Journal Signals": "computer vision defect detection deep learning quality inspection",
        "News Signals": "AI quality inspection smart manufacturing industrial vision",
        "Industry Signals": "Industry 4.0 factory automation quality control",
        "Vendor Signals": "industrial camera vendors machine vision platforms",
        "Patent Signals": "visual defect detection automated inspection computer vision",
        "Lifecycle": "Growth",
        "TRL": 8,
        "Strategic Fit": 8,
        "Integration Cost": 6,
        "Vendor Stability": 8,
        "Security Risk": 4,
        "Regulatory Risk": 3,
        "Pilot Evidence": 8,
        "Description": "Uses computer vision to detect production defects and improve quality control.",
        "Journal References": [
            "Deep learning for industrial defect detection.",
            "Computer vision quality inspection in smart manufacturing.",
            "Automated visual inspection for production systems."
        ],
        "News References": [
            "Manufacturers are adopting AI-based visual inspection to improve quality.",
            "Computer vision is becoming a major Industry 4.0 application."
        ],
        "Industry References": [
            "Smart manufacturing and Industry 4.0.",
            "Machine vision quality control.",
            "Automated production-line inspection."
        ],
        "Vendor References": [
            "Cognex machine vision.",
            "Keyence vision systems.",
            "Industrial camera and inspection platform vendors."
        ],
        "Patent Regulatory References": [
            "Visual defect detection patents.",
            "Industrial automation safety requirements.",
            "Quality assurance documentation standards."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Computer vision defect detection manufacturing",
                    "URL": "https://scholar.google.com/scholar?q=computer+vision+defect+detection+manufacturing",
                    "Description": "Search research about computer vision in quality inspection."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: AI quality inspection manufacturing",
                    "URL": "https://news.google.com/search?q=AI+quality+inspection+manufacturing",
                    "Description": "Review news about AI quality inspection."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Cognex Machine Vision",
                    "URL": "https://www.cognex.com/",
                    "Description": "Explore industrial machine vision systems."
                },
                {
                    "Title": "Search: Computer vision quality inspection vendors",
                    "URL": "https://www.google.com/search?q=computer+vision+quality+inspection+vendors",
                    "Description": "Search vendors offering AI visual inspection solutions."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Computer vision defect detection",
                    "URL": "https://patents.google.com/?q=computer+vision+defect+detection",
                    "Description": "Explore patents related to visual defect detection."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "ISO Quality Management",
                    "URL": "https://www.iso.org/iso-9001-quality-management.html",
                    "Description": "Review ISO 9001 quality management information."
                }
            ]
        }
    },

    {
        "Technology": "AI Energy Forecasting",
        "Category": "AI Forecasting",
        "Industry": "Energy",
        "Use Cases": "energy demand forecasting grid optimization renewable energy planning smart grid load prediction",
        "Journal Signals": "load forecasting renewable energy prediction smart grid machine learning",
        "News Signals": "AI energy grid forecasting renewable optimization",
        "Industry Signals": "smart grid energy transition power management demand planning",
        "Vendor Signals": "energy analytics vendors grid software AI forecasting platforms",
        "Patent Signals": "load forecasting power grid machine learning optimization",
        "Lifecycle": "Growth",
        "TRL": 8,
        "Strategic Fit": 8,
        "Integration Cost": 6,
        "Vendor Stability": 8,
        "Security Risk": 5,
        "Regulatory Risk": 5,
        "Pilot Evidence": 8,
        "Description": "Uses AI models to forecast energy demand and improve grid planning, renewable integration, and power management.",
        "Journal References": [
            "Machine learning for energy demand forecasting.",
            "AI-based smart grid optimization.",
            "Renewable energy forecasting using predictive models."
        ],
        "News References": [
            "Utilities are investing in AI forecasting for grid reliability.",
            "AI is increasingly used to manage renewable energy variability."
        ],
        "Industry References": [
            "Smart grid analytics.",
            "Demand response optimization.",
            "Renewable energy planning tools."
        ],
        "Vendor References": [
            "Energy analytics vendors.",
            "Grid optimization platforms.",
            "AI forecasting providers."
        ],
        "Patent Regulatory References": [
            "Power load forecasting patents.",
            "Smart grid regulatory requirements.",
            "Energy data governance and cybersecurity standards."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: AI energy demand forecasting smart grid",
                    "URL": "https://scholar.google.com/scholar?q=AI+energy+demand+forecasting+smart+grid",
                    "Description": "Search research about AI load forecasting and smart grids."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: AI energy forecasting smart grid",
                    "URL": "https://news.google.com/search?q=AI+energy+forecasting+smart+grid",
                    "Description": "Review recent news about AI energy forecasting."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Search: AI energy forecasting platforms",
                    "URL": "https://www.google.com/search?q=AI+energy+forecasting+platforms",
                    "Description": "Search vendors and platforms for energy forecasting."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: AI load forecasting smart grid",
                    "URL": "https://patents.google.com/?q=AI+load+forecasting+smart+grid",
                    "Description": "Explore patents related to AI load forecasting."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "International Energy Agency",
                    "URL": "https://www.iea.org/",
                    "Description": "Review global energy transition and grid analysis."
                }
            ]
        }
    },

    {
        "Technology": "Blockchain Medical Records",
        "Category": "Blockchain",
        "Industry": "Healthcare",
        "Use Cases": "medical records consent management health data exchange traceability patient data sharing",
        "Journal Signals": "blockchain electronic health records data sharing privacy consent",
        "News Signals": "blockchain health records decentralized healthcare data",
        "Industry Signals": "interoperability patient data ownership secure data exchange",
        "Vendor Signals": "blockchain health startups digital identity vendors",
        "Patent Signals": "distributed ledger medical records patient consent blockchain",
        "Lifecycle": "Emergence",
        "TRL": 5,
        "Strategic Fit": 6,
        "Integration Cost": 8,
        "Vendor Stability": 5,
        "Security Risk": 5,
        "Regulatory Risk": 8,
        "Pilot Evidence": 4,
        "Description": "Uses distributed ledger technology to support secure medical record sharing, consent management, and traceability.",
        "Journal References": [
            "Blockchain for electronic health record sharing.",
            "Patient consent management using distributed ledger technology.",
            "Privacy-preserving healthcare data exchange."
        ],
        "News References": [
            "Blockchain healthcare pilots continue to focus on interoperability and patient data control.",
            "Health data exchange remains a major area of blockchain experimentation."
        ],
        "Industry References": [
            "Patient identity and consent platforms.",
            "Interoperability and secure data sharing systems.",
            "Healthcare data governance platforms."
        ],
        "Vendor References": [
            "Blockchain health startups.",
            "Digital identity providers.",
            "Distributed ledger technology vendors."
        ],
        "Patent Regulatory References": [
            "Distributed ledger medical record patents.",
            "Patient consent and data-sharing regulatory requirements.",
            "Healthcare interoperability standards."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Blockchain electronic health records",
                    "URL": "https://scholar.google.com/scholar?q=blockchain+electronic+health+records",
                    "Description": "Search research on blockchain and health records."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: Blockchain medical records",
                    "URL": "https://news.google.com/search?q=blockchain+medical+records",
                    "Description": "Review market news about blockchain healthcare records."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Search: Healthcare blockchain interoperability",
                    "URL": "https://www.google.com/search?q=healthcare+blockchain+interoperability",
                    "Description": "Search industry information on blockchain interoperability."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Blockchain medical records",
                    "URL": "https://patents.google.com/?q=blockchain+medical+records",
                    "Description": "Explore patents related to blockchain health records."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "HL7 FHIR",
                    "URL": "https://www.hl7.org/fhir/",
                    "Description": "Review healthcare data interoperability standards."
                }
            ]
        }
    },

    {
        "Technology": "Legacy On-Premise Hospital System",
        "Category": "Legacy IT",
        "Industry": "Healthcare",
        "Use Cases": "legacy hospital information system old infrastructure limited integration outdated software",
        "Journal Signals": "legacy system interoperability limitation hospital information system modernization",
        "News Signals": "legacy IT modernization cybersecurity risk hospital systems",
        "Industry Signals": "digital transformation cloud migration system replacement",
        "Vendor Signals": "legacy vendors old hospital software",
        "Patent Signals": "legacy information system migration interoperability",
        "Lifecycle": "Decline",
        "TRL": 9,
        "Strategic Fit": 4,
        "Integration Cost": 9,
        "Vendor Stability": 4,
        "Security Risk": 8,
        "Regulatory Risk": 7,
        "Pilot Evidence": 5,
        "Description": "Traditional on-premise hospital system with limited interoperability, modernization capacity, and higher security risk.",
        "Journal References": [
            "Legacy system limitations in healthcare interoperability.",
            "Modernization of hospital information systems.",
            "Security risks in outdated healthcare IT infrastructure."
        ],
        "News References": [
            "Hospitals are replacing legacy IT systems due to cybersecurity and interoperability concerns.",
            "Cloud migration is becoming part of healthcare digital transformation."
        ],
        "Industry References": [
            "Healthcare cloud migration.",
            "Legacy system replacement strategies.",
            "Hospital IT modernization."
        ],
        "Vendor References": [
            "Cloud healthcare platforms.",
            "EHR modernization vendors.",
            "Healthcare interoperability platforms."
        ],
        "Patent Regulatory References": [
            "Healthcare system migration technologies.",
            "Cybersecurity requirements for healthcare systems.",
            "Data migration and interoperability standards."
        ],
        "Reference Links": {
            "Journal Databases": [
                {
                    "Title": "Google Scholar: Legacy hospital information system modernization",
                    "URL": "https://scholar.google.com/scholar?q=legacy+hospital+information+system+modernization",
                    "Description": "Search research on legacy healthcare IT modernization."
                }
            ],
            "News and Market Signals": [
                {
                    "Title": "Google News: Legacy healthcare IT modernization",
                    "URL": "https://news.google.com/search?q=legacy+healthcare+IT+modernization",
                    "Description": "Review news on replacing legacy healthcare systems."
                }
            ],
            "Industry and Vendor Sources": [
                {
                    "Title": "Search: Healthcare cloud migration legacy systems",
                    "URL": "https://www.google.com/search?q=healthcare+cloud+migration+legacy+systems",
                    "Description": "Search industry guidance on cloud migration and modernization."
                }
            ],
            "Patent Databases": [
                {
                    "Title": "Google Patents: Healthcare legacy system migration",
                    "URL": "https://patents.google.com/?q=healthcare+legacy+system+migration",
                    "Description": "Explore patents related to legacy system migration."
                }
            ],
            "Regulatory and Standards Guidance": [
                {
                    "Title": "NIST Cybersecurity Framework",
                    "URL": "https://www.nist.gov/cyberframework",
                    "Description": "Review cybersecurity framework for IT modernization."
                }
            ]
        }
    }
]

df = pd.DataFrame(technology_database)

# ==================================================
# Sidebar inputs
# ==================================================
st.sidebar.header("🔍 AI Search Inputs")

search_query = st.sidebar.text_area(
    "Describe what you are looking for",
    value="I need a technology to reduce hospital equipment downtime and improve biomedical engineering maintenance."
)

industry_filter = st.sidebar.selectbox(
    "Select Industry",
    [
        "Any",
        "Healthcare",
        "Manufacturing",
        "Energy",
        "Education",
        "Finance",
        "Government",
        "Transportation"
    ]
)

source_focus = st.sidebar.multiselect(
    "Search Signal Sources",
    [
        "Use Cases",
        "Journal Signals",
        "News Signals",
        "Industry Signals",
        "Vendor Signals",
        "Patent Signals"
    ],
    default=[
        "Use Cases",
        "Journal Signals",
        "News Signals",
        "Industry Signals",
        "Vendor Signals",
        "Patent Signals"
    ]
)

risk_tolerance = st.sidebar.selectbox(
    "Risk Tolerance",
    ["Low", "Medium", "High"]
)

budget_level = st.sidebar.selectbox(
    "Budget Level",
    ["Low", "Medium", "High"]
)

minimum_match = st.sidebar.slider(
    "Minimum Search Match Score",
    min_value=0,
    max_value=100,
    value=5
)

# ==================================================
# Helper functions
# ==================================================
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def keyword_match_score(query, row, selected_sources):
    query_words = set(clean_text(query).split())

    combined_text = ""
    for source in selected_sources:
        combined_text += " " + str(row[source])

    combined_words = set(clean_text(combined_text).split())

    if not query_words:
        return 0

    matched_words = query_words.intersection(combined_words)
    score = len(matched_words) / len(query_words)

    return round(score * 100, 1)


def matched_keywords(query, row, selected_sources):
    query_words = set(clean_text(query).split())

    combined_text = ""
    for source in selected_sources:
        combined_text += " " + str(row[source])

    combined_words = set(clean_text(combined_text).split())
    matched = sorted(list(query_words.intersection(combined_words)))

    return ", ".join(matched) if matched else "No direct keyword match"


def calculate_investment_score(row, risk_tolerance, budget_level):
    positive_score = (
        row["TRL"] * 1.2 +
        row["Strategic Fit"] * 1.8 +
        row["Vendor Stability"] * 1.2 +
        row["Pilot Evidence"] * 1.5
    )

    risk_score = (
        row["Integration Cost"] * 1.2 +
        row["Security Risk"] * 1.4 +
        row["Regulatory Risk"] * 1.2
    )

    lifecycle_weight = {
        "Emergence": 0.85,
        "Growth": 1.15,
        "Maturity": 0.95,
        "Decline": 0.55
    }

    risk_adjustment = {
        "Low": 0.85,
        "Medium": 1.00,
        "High": 1.10
    }

    budget_adjustment = {
        "Low": 0.85 if row["Integration Cost"] > 6 else 1.00,
        "Medium": 1.00,
        "High": 1.10
    }

    raw_score = (
        positive_score - risk_score
    ) * lifecycle_weight[row["Lifecycle"]]

    final_score = raw_score * risk_adjustment[risk_tolerance] * budget_adjustment[budget_level]

    normalized_score = max(0, min(100, round(final_score * 3, 1)))

    return normalized_score


def recommend_action(score, lifecycle, pilot_evidence):
    if lifecycle == "Decline":
        return "Avoid / Replace"

    if score >= 75 and pilot_evidence >= 7:
        return "Scale"

    elif score >= 55:
        return "Pilot"

    elif score >= 35:
        return "Explore"

    else:
        return "Avoid / Reassess"


def decision_explanation(row):
    recommendation = row["Recommendation"]

    if recommendation == "Scale":
        return (
            "This technology shows strong readiness, strategic fit, vendor stability, "
            "and pilot evidence. It may be suitable for scaling after governance review."
        )

    elif recommendation == "Pilot":
        return (
            "This technology is promising but should be tested through a bounded pilot "
            "before full capital investment."
        )

    elif recommendation == "Explore":
        return (
            "This technology has potential but requires more horizon scanning, "
            "evidence collection, and technical evaluation."
        )

    elif recommendation == "Avoid / Replace":
        return (
            "This technology is in decline or has weak strategic value. "
            "Avoid major new investment and consider replacement options."
        )

    else:
        return (
            "This technology currently has high uncertainty or risk. "
            "Reassess before investment."
        )


def display_reference_list(title, references):
    st.markdown(f"### {title}")

    if references:
        for ref in references:
            st.write(f"- {ref}")
    else:
        st.write("No references added yet.")


def display_external_reference_navigation(reference_links):
    """
    Display clickable external links grouped by reference category.
    """

    if not reference_links:
        st.info("No external reference links are available for this technology.")
        return

    st.markdown("""
    Use the links below to explore the evidence behind the selected technology.
    These links help you review research papers, market news, patents, vendor information,
    industry context, and regulatory guidance.
    """)

    for category, links in reference_links.items():
        with st.expander(f"🔗 {category}", expanded=True):
            for item in links:
                title = item.get("Title", "Open reference")
                url = item.get("URL", "#")
                description = item.get("Description", "")

                st.markdown(f"**[{title}]({url})**")

                if description:
                    st.caption(description)


# ==================================================
# Main app logic
# ==================================================
if st.sidebar.button("Search and Detect Technology"):

    search_df = df.copy()

    if industry_filter != "Any":
        search_df = search_df[search_df["Industry"] == industry_filter]

    search_df["Search Match Score"] = search_df.apply(
        lambda row: keyword_match_score(search_query, row, source_focus),
        axis=1
    )

    search_df["Matched Keywords"] = search_df.apply(
        lambda row: matched_keywords(search_query, row, source_focus),
        axis=1
    )

    search_df["Investment Score"] = search_df.apply(
        lambda row: calculate_investment_score(row, risk_tolerance, budget_level),
        axis=1
    )

    search_df["Final AI Score"] = (
        search_df["Search Match Score"] * 0.45 +
        search_df["Investment Score"] * 0.55
    ).round(1)

    search_df["Recommendation"] = search_df.apply(
        lambda row: recommend_action(
            row["Final AI Score"],
            row["Lifecycle"],
            row["Pilot Evidence"]
        ),
        axis=1
    )

    search_df["Decision Explanation"] = search_df.apply(decision_explanation, axis=1)

    search_df = search_df[search_df["Search Match Score"] >= minimum_match]
    search_df = search_df.sort_values(by="Final AI Score", ascending=False)

    if search_df.empty:
        st.warning(
            "No strong match found. Try broader search words such as AI, hospital, "
            "maintenance, automation, monitoring, diagnosis, digital twin, or remote care."
        )

    else:
        best = search_df.iloc[0]

        # --------------------------------------------------
        # Best technology result
        # --------------------------------------------------
        st.subheader("🏆 Best Technology Detected")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Technology", best["Technology"])

        with col2:
            st.metric("Search Match", f"{best['Search Match Score']}%")

        with col3:
            st.metric("Final AI Score", f"{best['Final AI Score']}/100")

        with col4:
            st.metric("Decision", best["Recommendation"])

        st.success(best["Description"])

        st.markdown(f"""
        ### 🧠 Why this technology was selected

        **{best['Technology']}** was selected because it matched your search need
        and showed relevant investment potential.

        **Matched keywords:** {best['Matched Keywords']}

        **Decision explanation:** {best['Decision Explanation']}
        """)

        # --------------------------------------------------
        # Evidence and investment profile
        # --------------------------------------------------
        st.subheader("📊 Evidence and Investment Profile")

        profile_df = pd.DataFrame({
            "Evaluation Factor": [
                "Category",
                "Industry",
                "Lifecycle",
                "Technology Readiness Level",
                "Strategic Fit",
                "Integration Cost",
                "Vendor Stability",
                "Security Risk",
                "Regulatory Risk",
                "Pilot Evidence",
                "Search Match Score",
                "Investment Score",
                "Final AI Score",
                "Recommendation"
            ],
            "Value": [
                best["Category"],
                best["Industry"],
                best["Lifecycle"],
                f"{best['TRL']} / 9",
                f"{best['Strategic Fit']} / 10",
                f"{best['Integration Cost']} / 10",
                f"{best['Vendor Stability']} / 10",
                f"{best['Security Risk']} / 10",
                f"{best['Regulatory Risk']} / 10",
                f"{best['Pilot Evidence']} / 10",
                f"{best['Search Match Score']}%",
                f"{best['Investment Score']} / 100",
                f"{best['Final AI Score']} / 100",
                best["Recommendation"]
            ]
        })

        st.dataframe(profile_df, use_container_width=True)

        # --------------------------------------------------
        # Matched intelligence signals
        # --------------------------------------------------
        st.subheader("📡 Matched Intelligence Signals")

        signal_df = pd.DataFrame({
            "Source": [
                "Use Cases",
                "Journal Signals",
                "News Signals",
                "Industry Signals",
                "Vendor Signals",
                "Patent Signals"
            ],
            "Extracted Signals": [
                best["Use Cases"],
                best["Journal Signals"],
                best["News Signals"],
                best["Industry Signals"],
                best["Vendor Signals"],
                best["Patent Signals"]
            ]
        })

        st.dataframe(signal_df, use_container_width=True)

        # --------------------------------------------------
        # References and external navigation
        # --------------------------------------------------
        st.subheader("📚 References and External Navigation")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Journal / Research",
            "News / Market",
            "Industry",
            "Vendor",
            "Patent / Regulatory",
            "External Links"
        ])

        with tab1:
            display_reference_list(
                "Journal / Research References",
                best["Journal References"]
            )

        with tab2:
            display_reference_list(
                "News / Market References",
                best["News References"]
            )

        with tab3:
            display_reference_list(
                "Industry References",
                best["Industry References"]
            )

        with tab4:
            display_reference_list(
                "Vendor References",
                best["Vendor References"]
            )

        with tab5:
            display_reference_list(
                "Patent / Regulatory References",
                best["Patent Regulatory References"]
            )

        with tab6:
            st.markdown("### 🌐 External Reference Navigation")
            display_external_reference_navigation(best["Reference Links"])

            st.warning("""
            Important: External links open live search or source pages.
            Always review the quality, date, credibility, and relevance of each source
            before making investment decisions.
            """)

        # --------------------------------------------------
        # Full comparison table
        # --------------------------------------------------
        st.subheader("📋 Technology Comparison Database")

        display_columns = [
            "Technology",
            "Category",
            "Industry",
            "Lifecycle",
            "TRL",
            "Strategic Fit",
            "Integration Cost",
            "Vendor Stability",
            "Security Risk",
            "Regulatory Risk",
            "Pilot Evidence",
            "Search Match Score",
            "Investment Score",
            "Final AI Score",
            "Recommendation",
            "Matched Keywords",
            "Decision Explanation"
        ]

        st.dataframe(search_df[display_columns], use_container_width=True)

        # --------------------------------------------------
        # Chart
        # --------------------------------------------------
        st.subheader("📈 Final AI Score Comparison")

        fig = px.bar(
            search_df,
            x="Technology",
            y="Final AI Score",
            color="Recommendation",
            hover_data=[
                "Lifecycle",
                "TRL",
                "Search Match Score",
                "Investment Score",
                "Matched Keywords"
            ],
            title="AI-Based Technology Search and Investment Score"
        )

        fig.update_layout(
            xaxis_title="Technology",
            yaxis_title="Final AI Score",
            xaxis_tickangle=-35
        )

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------------------------------
        # Decision framework
        # --------------------------------------------------
        st.subheader("🧭 Decision Framework: From Signal to Capital Commitment")

        framework = pd.DataFrame({
            "Stage": ["Sense", "Interpret", "Evaluate", "Commit"],
            "Meaning": [
                "Collect signals from journals, patents, startups, news, vendors, and regulation.",
                "Connect the signals to business strategy and future market direction.",
                "Score technology readiness, integration cost, risk, vendor stability, and strategic fit.",
                "Run a bounded pilot before full-scale capital investment."
            ]
        })

        st.table(framework)

else:
    st.info(
        "Enter your technology need in the sidebar, then click "
        "**Search and Detect Technology**."
    )

# ==================================================
# Footer
# ==================================================
st.divider()

st.caption("""
Prototype note: This app uses a structured sample database.
Later, it can be connected to PubMed, Semantic Scholar, Google News,
patent databases, startup databases, vendor websites, and industry reports.
""")