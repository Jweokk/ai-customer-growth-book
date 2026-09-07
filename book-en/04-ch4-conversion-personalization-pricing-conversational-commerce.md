# Chapter 4 Conversion: Personalization, Pricing, and Conversational Commerce

The customer has arrived — how do you get them to pay? This chapter is about how AI changes "conversion." Four battlegrounds: personalized recommendations, pricing, conversational commerce, and sales forecasting.

## 4.1 Personalization: From "Guess You Like" to "Generative Understanding"

Personalization is already the default expectation: 71% of consumers expect companies to deliver personalized interactions, and 76% are disappointed when they don't get them<sup><a href="12-appendix-a-sources.md#4-17">[4-17]</a></sup>[third-party verified]. But traditional personalization (collaborative filtering, rule-based recommendations) hit its ceiling long ago — e-commerce has been stuck at a 2–3% conversion-rate bottleneck for more than a decade.

AI upgrades personalization from "guessing what you like" to "generative understanding." Two cases in point:

**Netflix**: More than 80% of viewing time comes from AI recommendations. A 2024 causal study (Zielnicki et al.) found that swapping the recommender for random picks would cut engagement by 16%<sup><a href="12-appendix-a-sources.md#4-08">[4-08]</a></sup>[third-party verified]. In March 2025 Netflix went a step further, starting to rebuild its recommendation system with LLM foundation models — from "predicting which tile you click" to "understanding why you watch."

**Taobao (Chinese: 淘宝)**: In 2025 it launched RecGPT, its in-house recommendation LLM with 10 billion parameters, upgrading the entire "Guess You Like" feed to generative recommendations. Official figures: clicks grew by double digits, and add-to-cart counts and time spent both rose by more than 5%<sup><a href="12-appendix-a-sources.md#4-14">[4-14]</a></sup>[official claims].

McKinsey frames the next frontier in terms of two levers: AI-driven precision promotions (offers that fit "micro-communities" more closely) and generative AI producing personalized content in a distinctive voice at scale<sup><a href="12-appendix-a-sources.md#4-17">[4-17]</a></sup>[third-party verified]. Bloomreach's benchmarks claim AI personalization can lift conversion rates by up to 25% relative to traditional CRO and raise revenue per visitor by an average of more than 20%<sup><a href="12-appendix-a-sources.md#4-15">[4-15]</a></sup>[official claims] — vendor claims, so discount them when reading, but the direction is consistent: **personalization is moving from "segments" to "each individual."**

## 4.2 Pricing: The Era of Charging for Outcomes Is Here

AI's impact on pricing runs deeper than its impact on personalization. It changes two things at once: **how to price** and **what to price**.

**What to price**: The pricing unit of software is shifting from per-seat to per-outcome. Traditional SaaS sells the right to use software, which customers put to work themselves; in the AI-agent era, software companies can take responsibility for the work actually delivered — work previously performed by employees in sales, support, and customer success<sup><a href="12-appendix-a-sources.md#1-11">[1-11]</a></sup>[third-party verified]. Salesforce is the flagship case: Agentforce's ARR has passed $1.5 billion, up more than 240% year over year<sup><a href="12-appendix-a-sources.md#7-07">[7-07]</a></sup>[third-party verified]. HubSpot's Breeze AI agents have moved straight to pay-per-result<sup><a href="12-appendix-a-sources.md#7-15">[7-15]</a></sup>[third-party verified]. No Jitter offers a vivid analogy: customers no longer "buy software" — they "buy work"<sup><a href="12-appendix-a-sources.md#1-11">[1-11]</a></sup>[third-party verified].

**How to price**: The cost structure of AI products has changed. Traditional SaaS enjoyed "near-zero marginal cost to serve one more customer"; every query to an AI product incurs inference and compute costs (the return of COGS). Bessemer Venture Partners' AI pricing playbook is built specifically around charging frameworks for "a world where every token costs money"<sup><a href="12-appendix-a-sources.md#4-01">[4-01]</a></sup>[official claims]. Dynamic pricing, usage-based pricing, and outcome-based pricing have become the new normal.

The controversy around dynamic pricing is also worth recording. Delta Air Lines used AI for personalized pricing, drawing a joint inquiry from about 24 members of the US House of Representatives demanding it disclose whether it was using "surveillance-based personalized price discrimination" to push fares higher<sup><a href="12-appendix-a-sources.md#4-16">[4-16]</a></sup>[third-party verified]. Airlines used dynamic pricing to raise load factors from 72% in the early 2000s to above 80%, while average fares actually fell — yet consumers' acceptance of "the same seat at different prices for different people" is far lower than vendors expected<sup><a href="12-appendix-a-sources.md#4-19">[4-19]</a></sup>[third-party verified]. When pricing goes AI, technology is not the obstacle — trust is.

## 4.3 Conversational Commerce: The Conversation Is the Shelf

The third change is that the "shelf" itself has disappeared. In the past, customers browsed websites and scrolled through product listings; now a customer simply tells an AI, "I want a waterproof jacket under €200," and the AI system interprets, compares, and recommends across retailers<sup><a href="12-appendix-a-sources.md#4-03">[4-03]</a></sup>[third-party verified]. Shopping shifts from "browsing" to "describing what you need," with AI agents executing on the shopper's behalf.

The scale figures are already striking:

- **Amazon Rufus**: more than 300 million users in 2025, monthly actives up 149% year over year, total interactions up 210%<sup><a href="12-appendix-a-sources.md#4-02">[4-02]</a></sup>[third-party verified];
- **McKinsey's forecast**: agentic commerce could generate $1 trillion in US retail revenue by 2030; Morgan Stanley expects nearly half of US consumers to use AI agents by 2030, which could add as much as $115 billion in new spending to US e-commerce<sup><a href="12-appendix-a-sources.md#4-11">[4-11]</a></sup>[third-party verified];
- **Meta WhatsApp Business AI Agent**: opened to businesses worldwide in June 2026 — it can answer questions, recommend products, book appointments, and qualify leads, handing off to a human when it gets stuck<sup><a href="12-appendix-a-sources.md#4-07">[4-07]</a></sup>[third-party verified].

BCG's report put it most bluntly: **a retailer's most valuable customers may no longer be human** — AI agents (embedded in Perplexity, ChatGPT, Google Gemini, and other platforms) are taking over the discover–compare–decide–order sequence<sup><a href="12-appendix-a-sources.md#4-03">[4-03]</a></sup>[third-party verified].

The implications for operators cut both ways. The good news: AI agents are tireless 24/7 buyers that close deals more efficiently. The bad news: AI agents recognize only data, not brands — when the buyer is an AI, human emotional assets such as "brand affinity" carry no weight, and what determines whether a product is chosen is its product data (how structured it is, inventory truthfulness, price transparency, interoperable protocols)<sup><a href="12-appendix-a-sources.md#11-25">[11-25]</a></sup>[third-party verified]. Chapter 11 will go deeper into this theme.

## 4.4 Sales Forecasting and the Funnel: Gong versus Clari

The fourth battleground is the AI-ification of the sales funnel itself. In the past, sales forecasting depended on sales managers' gut calls: how much the quarter would close was a matter of feel. AI has turned it into a data problem.

**Gong** entered through conversation intelligence: AI analyzes every sales call, email, and meeting to extract insights — which talk tracks work, which signals point to a win or a loss. In 2025 Gong's ARR broke through $300 million, pointing toward an IPO path<sup><a href="12-appendix-a-sources.md#4-13">[4-13]</a></sup>[third-party verified].

**Clari** entered through forecasting and pipeline governance: it takes point-in-time snapshots of every change to every opportunity, and AI forecasts revenue on that basis<sup><a href="12-appendix-a-sources.md#4-04">[4-04]</a></sup>[third-party verified].

By the end of 2025, the boundary between the two had blurred — both do conversation analytics, both do forecasting, both sell "Revenue Intelligence"<sup><a href="12-appendix-a-sources.md#4-04">[4-04]</a></sup>[third-party verified]. The very existence of this category says something: **sales management is moving from "experience-driven" to "AI-driven"** — not replacing sales managers, but backing their judgment with data.

The Chinese example is Neocrm (Chinese: 销售易). In 2026 it released NeoAgent 2.0, and its president, Deng Yongfu (Chinese: 邓永富), drew a clear distinction: "AI CRM 1.0 is a CRM with AI added on; 2.0 is a CRM born for AI" — shifting from a process tool to one built around a business semantic model<sup><a href="12-appendix-a-sources.md#4-18">[4-18]</a></sup>[third-party verified]. The AI CRM research report co-published by CAICT (Chinese: 信通院) and Fenxiangxiaoke (Chinese: 纷享销客) sets out a technical roadmap: large models drive CRM interaction from "forms and menus" to "conversational interaction," and the system shifts from "humans driving the system" to "the system driving humans"<sup><a href="12-appendix-a-sources.md#4-10">[4-10]</a></sup>[official claims].

## 4.5 Summary

The AI-ification of the conversion stage comes down to four things happening at once:

1. **Personalization from segments to individuals** — LLMs make "a tailored experience for every customer" possible (Netflix's 80% of viewing coming from recommendations, Taobao's RecGPT);
2. **Pricing from seats to outcomes** — customers begin paying for "completed work" (Agentforce's $1.5 billion ARR, HubSpot's pay-per-result), while the trust problem of dynamic pricing surfaces at the same time (the Delta inquiry);
3. **The shelf from webpages to conversations** — AI agents compare prices and place orders on people's behalf, and brand equity gives way to data assets (Rufus's 300 million users, the $1 trillion forecast for 2030);
4. **The funnel from experience to data** — revenue intelligence turns sales forecasting into an algorithm (Gong's $300 million ARR, Neocrm's NeoAgent 2.0).

Conversion ends in the close; what follows the close is service. The next chapter covers the most crowded — and most misunderstood — stage of the customer lifecycle: customer service.
