# Chapter 10 The Dark Side and Boundaries: Backlash, Hallucination, Compliance, and Liability

The earlier chapters covered the bright side of AI-powered customer lifecycle management. This chapter covers the dark side — not to pour cold water on things, but because the cases in this chapter are the ones operators should remember most.

## 10.1 Backlash: AI Outbound Is Killing Itself

Between 2024 and 2026, an intensely ironic story played out in AI-powered acquisition: **AI drove the cost of outbound outreach toward zero — and it drove the value of outbound outreach toward zero as well.**

A set of numbers (covered in Chapter 3; expanded here):
- Across the AI cold-email ecosystem as a whole: 95% of cold emails now get zero replies at all; when personalization is sacrificed for speed, reply rates run 13x lower than normal<sup><a href="12-appendix-a-sources.md#3-39">[3-39]</a></sup> [third-party verified];
- A cohort study of 14 B2B SaaS organizations: AI SDR outbound reply rates decayed from 11.2% to 4.4% within 18 months — recipients learned to recognize AI templates<sup><a href="12-appendix-a-sources.md#3-32">[3-32]</a></sup> [third-party verified];
- Cold-call reply rates fell from 8.5% in 2018 to 4.2% in 2022<sup><a href="12-appendix-a-sources.md#3-39">[3-39]</a></sup> [official claims].

Artisan's experience is the defining incident: this AI SDR company, famous for its "stop hiring humans" advertising, saw its own AI agent Ava banned from LinkedIn in late 2025 — because the way it automatically contacted prospects violated the platform's rules<sup><a href="12-appendix-a-sources.md#3-44">[3-44]</a></sup> [third-party verified]. Platforms are pushing back against AI spam, and regulators are catching up: China's central state media investigated and reported on the chaos of AI marketing robocalls — a single machine dialing 800-1,500 calls a day, with incoming voices sounding ever more "standardized" because the caller is not a real person<sup><a href="12-appendix-a-sources.md#10-02">[10-02]</a></sup> [third-party verified]; the U.S. FCC ruled unanimously that automated marketing calls placed with AI-generated voices are illegal<sup><a href="12-appendix-a-sources.md#10-08">[10-08]</a></sup> [third-party verified].

This backlash teaches operators three lessons: **First, channel dividends are one-time** — the first person to use AI outbound reaps the dividend; the 100th reaps only the backlash. **Second, restraint is a strategy, not a virtue** — what actually works is precisely identifying "people who are in the market right now" (intent data), not casting a wide net. **Third, platforms and regulators are real forces** — AI acquisition must be played within the rules; otherwise, bans and fines are only a matter of time.

## 10.2 Hallucination: AI Confidently Making Things Up

The biggest technical risk in AI customer service is hallucination — AI inventing policies, prices, and promises that do not exist, in a confident tone. Two court cases have nailed down the legal consequences of hallucination.

**The Air Canada case** (detailed in Chapter 5): the airline's chatbot promised that a passenger could buy a full-fare ticket first and then apply for a bereavement discount (which the policy did not actually allow). The passenger did exactly that, was refused, and sued. In February 2024 the court ordered the airline to pay around CAD 812 and rejected the defense that "the chatbot was a separate legal entity" — **companies are responsible for what their AI says**<sup><a href="12-appendix-a-sources.md#10-18">[10-18]</a></sup> [third-party verified].

**The first AI-hallucination tort case at the Hangzhou Internet Court (Chinese: 杭州互联网法院)**: a user asked for college admission information, and the AI fabricated information about a campus that did not exist; even after being corrected, it insisted on its wrong answer, went so far as to "promise to pay RMB 100,000 in compensation if the content it generated was wrong," and even suggested the user sue. The court held that the AI's "compensation promise" did not constitute a statement of intent by the company, and that the service provider was shielded from liability by prominent disclosure<sup><a href="12-appendix-a-sources.md#10-17">[10-17]</a></sup> [third-party verified].

Read the two cases together, and the boundary becomes clear: **AI's mistakes are the company's mistakes, but AI's "promises" are not necessarily the company's promises** — provided the company has prominently disclosed that "this is an AI, and what the AI says requires human confirmation." Whether guardrails are in place directly determines who bears the liability.

## 10.3 Compliance: Regulators Have Caught Up With AI Selling

The 2024-2026 period saw AI regulation land intensively. Three landmark actions:

**The U.S. FTC's "Operation AI Comply"** (September 2024): five enforcement cases announced at once, targeting businesses that "hype or sell AI technologies that can be used to deceive" — including companies selling tools for generating AI-produced fake reviews<sup><a href="12-appendix-a-sources.md#10-09">[10-09]</a></sup> [third-party verified].

**The U.S. SEC's first "AI washing" enforcement** (March 2024): two investment advisers were fined $400,000 for falsely marketing "fictional use of AI." Delphia paid $225,000 and Global Predictions paid $175,000<sup><a href="12-appendix-a-sources.md#10-15">[10-15]</a></sup> [third-party verified]. "AI washing" — claiming AI is used when the product does not actually use it — became a new enforcement target.

**China's Measures for the Labeling of AI-Generated Synthetic Content** (Chinese: 《人工智能生成合成内容标识办法》; effective September 1, 2025): all AI-generated text, images, audio, and video must "identify themselves" — through explicit labels plus implicit labels<sup><a href="12-appendix-a-sources.md#10-01">[10-01]</a></sup> [third-party verified].

**Article 50 of the EU AI Act** (in effect August 2, 2026): customer-facing AI interactions must disclose that they are AI, and coverage is not limited to high-risk systems; human review can serve as an exemption from liability<sup><a href="12-appendix-a-sources.md#10-07">[10-07]</a></sup> [third-party verified].

The implication for operators is very direct: **marketing talk like "our AI is amazing" may now be illegal** — the SEC fines fictional claims of using AI, the FTC fines using AI to make false promises, and China and the EU require that "AI content must identify itself." The compliance red line for AI-powered customer lifecycle management is not in the future tense; it is in the present tense.

## 10.4 The Human-Machine Boundary: The Red Line on AI Impersonating Humans

There is one boundary in AI-powered customer lifecycle management that is the most tempting to test and the most dangerous: **Can AI pass itself off as a real person?**

Regulators' answers are increasingly aligned: it cannot. The FCC ruled AI-generated-voice robocalls illegal (February 2024)<sup><a href="12-appendix-a-sources.md#10-08">[10-08]</a></sup> [third-party verified]; the FTC has an impersonation rule targeting AI that impersonates real people<sup><a href="12-appendix-a-sources.md#10-10">[10-10]</a></sup> [third-party verified]; and China's governance of AI outbound calling is following suit [third-party verified].

Analysis from the U.S. think tank CDT (the Center for Democracy & Technology) reveals a deeper risk: conversational AI is producing new kinds of dark patterns — AI using empathetic rhetoric to manipulate users into decisions, blurring the line between AI and real people, and exploiting the intimacy of conversation to win trust<sup><a href="12-appendix-a-sources.md#10-03">[10-03]</a></sup> [third-party verified].

Why is "AI impersonating a real person" a red line? Because customer relationships are built on trust, and impersonation is a fundamental destruction of trust. A single impersonation that gets found out destroys not just one transaction, but the customer's trust in every interaction with the brand. **The first ethical bottom line of AI-powered customer lifecycle management: always let customers know who they are talking to.**

## 10.5 Liability: Who Pays When AI Messes Up

When AI causes trouble, who bears responsibility? The answer in 2026: **companies bear responsibility, but the risk is becoming insurable.**

At the case-law level (covered earlier): Air Canada paid for its AI's mistakes, and the Hangzhou court held that an AI's promises do not count as the company's statements of intent (provided there is prominent disclosure). At the legislative level: the EU AI Act establishes a tiered framework of liability<sup><a href="12-appendix-a-sources.md#10-07">[10-07]</a></sup> [third-party verified].

At the insurance level, a new species has appeared: HSB, the Munich Re subsidiary, launched AI liability insurance for small and medium-sized businesses — "AI lawsuits" have been brought into the realm of insurable risk<sup><a href="12-appendix-a-sources.md#10-20">[10-20]</a></sup> [third-party verified]. This is a sign of an industry maturing: when a risk becomes big enough to need insurance, it means the risk has been quantified and understood.

A liability checklist for operators:
1. **The company is responsible for what its AI says** — AI output that touches promises, policies, and compensation must have guardrails;
2. **Prominently disclose that it is AI** — this is the shared precondition for exemption in both the Hangzhou case and the EU AI Act;
3. **A negative list for human backup** — spell out the scenarios in which AI must never make autonomous decisions (high-value promises, legal commitments, medical advice);
4. **Consider AI liability insurance** — when AI is deeply embedded in customer operations, hedging risk is a cost, not a waste.

## 10.6 Summary

The boundaries of AI-powered customer lifecycle management can be condensed into five points:

1. **Backlash**: AI outbound is killing cold email — channel dividends are one-time, and restraint is a strategy;
2. **Hallucination**: AI's mistakes are the company's mistakes — Air Canada paid, and the Hangzhou case was exempted (with disclosure); guardrails determine liability;
3. **Compliance**: regulators have caught up with AI selling — FTC/FCC/SEC/EU AI Act/China's labeling measures, and AI washing is illegal;
4. **The human-machine boundary**: AI impersonating real people is a global red line — trust is the foundation of customer operations;
5. **Liability**: companies bear responsibility, but AI liability insurance has appeared — a risk being insurable shows the industry is maturing.

The final chapter looks to the future: when customers themselves become AI, what will customer operations become?
