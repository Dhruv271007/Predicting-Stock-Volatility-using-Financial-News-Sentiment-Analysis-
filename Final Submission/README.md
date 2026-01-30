# 📰 Financial News Parsing & Sentiment Analysis Pipeline

This repository contains an end-to-end pipeline for collecting, cleaning, and analyzing financial news, and studying its relationship with stock price volatility.

## 🚀 Project Overview

### **1. News Data Collection**
- Parses financial news from multiple RSS feeds:
  - Wall Street Journal  
  - Bloomberg  
  - CNBC  
- Uses Python libraries:
  - `requests`
  - `beautifulsoup4`

### **2. Data Cleaning & Integration**
- Cleans and preprocesses raw news headlines.
- Merges processed news data with historical stock price data sourced from **Yahoo Finance**.

### **3. Sentiment Analysis with FinBERT**
- Utilizes **FinBERT**, a finance-specific transformer model, to perform sentiment analysis on each news headline.
- Generates sentiment labels and continuous sentiment scores.

### **4. Volatility Computation**
- Computes rolling volatility for **GOOG (Google)** using NumPy.
- Aligns volatility measures with sentiment scores over time.

### **5. Correlation & Visualization**
- Calculates the correlation between:
  - News sentiment  
  - Stock volatility  
- Visualizes the relationship using `matplotlib` through line plots and comparative graphs.

---

## 📈 Key Highlights
- Shows how financial news sentiment can be linked to market volatility.
- Demonstrates practical integration of NLP (FinBERT) into quantitative finance workflows.
- Fully modular pipeline—extendable to additional tickers or news sources.
- A useful starting point for sentiment-driven trading models or event-driven market analysis.

---

## 📦 Technologies Used
- Python  
- requests  
- beautifulsoup4  
- pandas  
- numpy  
- matplotlib  
- yfinance  
- FinBERT (HuggingFace)
