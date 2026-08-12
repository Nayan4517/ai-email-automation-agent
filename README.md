# ai-email-automation-agent
AI-powered email automation using n8n, Python, Gmail API and LLMs
# AI Email Automation Agent

An AI-powered email automation project designed to classify, prioritize, summarize, and process emails automatically.

## Project Overview

The system analyzes incoming emails and identifies their category and priority. It can be extended to use Large Language Models such as OpenAI or Gemini for intelligent email understanding and response generation.

## Key Features

- Email classification
- Email priority detection
- Email summarization
- AI-assisted response generation
- Automated workflow processing
- Gmail API integration
- Google Sheets integration for tracking

## Architecture

Gmail
   ↓
n8n Workflow
   ↓
Email Processing
   ↓
AI Analysis
   ↓
Classification + Priority + Summary
   ↓
Automated Action / Response

## Technologies Used

- Python
- n8n
- OpenAI / Gemini API
- Gmail API
- Google Sheets
- JavaScript
- REST APIs

## Project Structure

```text
ai-email-automation-agent/
│
├── workflow/
│   └── email_automation_workflow.json
│
├── python/
│   └── email_processor.py
│
├── README.md
└── .gitignore
