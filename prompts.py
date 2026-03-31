# prompts.py

GLOBAL_NEWS_PROMPT = """
You are a global macro strategist.

Give top 5 global events (last 7 days) impacting Indian markets.

Output:
- 5 bullet points
- Very short
"""

INDIA_NEWS_PROMPT = """
You are an Indian market analyst.

Give top 5 Indian events (last 7 days) impacting markets.

Output:
- 5 bullet points
- Very short
"""

SECTOR_PROMPT = """
Based on this news:

GLOBAL:
{global_news}

INDIA:
{india_news}

Give top sectors impacted in India + direction.

Output:
- sector: direction (1 line reason)
"""

STOCK_PROMPT = """
Based on sectors:

{sectors}

Give NSE/BSE stocks being discussed by experts.

Output:
- sector → stock names
(max 3 per sector)
"""

MOMENTUM_PROMPT = """
From these stocks:

{stocks}

Which stocks show early uptrend?

Output:
- stock → reason
"""

PORTFOLIO_PROMPT = """
From these momentum stocks:

{momentum}

Give 5–8 stocks portfolio.

Include:
- weight %
- reason

Keep short.
"""
