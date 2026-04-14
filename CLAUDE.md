# Recycle Intel - 回收產業供應鏈情報追蹤

## 專案狀態：建置中

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **股價抓取** | 13 檔股票，Yahoo Finance | 待建置 |
| **新聞爬蟲** | 涵蓋 13 家公司 | 待建置 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | 待客製化 |
| **報告生成** | 每日報告、7 日報告 | 待建置 |
| **前端** | D3.js Dashboard、供應鏈圖、事件時間軸 | 待建置 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 待建置 |

---

## 追蹤範圍

### 公司 (13 家)

**上游 - 設備/貿易** (2 家)
- TOMRA Systems 陶朗 (TOM.OL Oslo NOK) - 分選設備
- Glencore 嘉能可 (GLEN.L London GBP) - 原物料貿易

**中游 - 回收/處理** (11 家)
- Waste Management 廢管 (WM NYSE) - 廢棄物管理
- Republic Services 共和 (RSG NYSE) - 廢棄物管理
- Waste Connections (WCN NYSE) - 廢棄物管理
- Umicore 優美科 (UMI.BR Euronext EUR) - 貴金屬回收
- Veolia 威立雅 (VIE.PA Euronext EUR) - 環保服務
- Aurubis 奧魯比斯 (NDA.DE XETRA EUR) - 銅回收
- Boliden 博利登 (BOL.ST Stockholm SEK) - 金屬回收
- Sims Limited 西姆斯 (SGM.AX ASX AUD) - 金屬回收
- Renewi 瑞紐威 (RWI.AS Amsterdam EUR) - 廢棄物轉化
- 崑鼎投資控股 (6803.TWO TPEx TWD) - 廢棄物處理
- American Battery Technology 美國電池 (ABAT NASDAQ) - 電池回收

### 主題 (configs/topics.yml)

- 電池回收 (battery_recycling)
- 塑膠回收 (plastic_recycling)
- 電子廢棄物 (ewaste)
- 循環經濟政策 (circular_economy_policy)
- 碳權 (carbon_credit)
- 財報 / 展望
- 原物料價格

---

## 標準流程

```
fetch_news → enrich_event → generate_metrics → detect_anomalies →
generate_daily → generate_7d_report → update_baselines → deploy
```

## 資料夾結構

```
recycle-intel/
├── lib/                        # 規則引擎
├── scripts/                    # 執行腳本
├── configs/                    # 設定檔
│   ├── companies.yml           # 13 家公司 + 上下游關係
│   ├── topics.yml              # 主題 + 關鍵字
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   └── anomaly_rules.yml       # 異常偵測規則
├── fetchers/                   # 公司新聞爬蟲
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件 (JSONL)
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務資料
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
├── site/
│   ├── index.html              # D3.js Dashboard
│   └── data/                   # 前端資料
└── CLAUDE.md
```

---

## 產出報告（Claude CLI）

當用戶說「產出報告」時，執行以下流程：

### 1. 拉取最新資料
```bash
git pull origin main
```

### 2. 讀取事件資料
- 讀取近 7 天的 `data/events/{date}.jsonl`
- 識別重要事件、主題趨勢、供應鏈動態

### 3. 產出分析並寫入 JSON
讀取現有的 Actions 報告 JSON，追加 `llm_analysis` 和 `financials` 欄位。

### 4. Commit 並 Push
```bash
git add site/data/reports/
git commit -m "Weekly report: {date}"
git push
```

---

## 快速啟動

```bash
cd repos/recycle-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 6231 -d site

# 瀏覽器開啟
open http://localhost:6231
```
