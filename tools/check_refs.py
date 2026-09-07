#!/usr/bin/env python3
"""引用一致性自检（每周更新完成后运行）——《AI 客户经营》中英双语。

检查三件事：
1. 附录 A 编号 vs 正文上标编号的差集（附录有条目但正文未引用 = 可能漏标）
2. 正文上标链接格式（必须是 <sup><a href="12-附录A-案例索引与资料出处.md#X-Y">[X-Y]</a></sup> 中英相对链接形式，不能是纯文本 sup 或绝对路径）
3. 正文引用的编号在附录 A 必须存在（悬空引用）

用法：
    python3 tools/check_refs.py
退出码：0 = 全部通过；1 = 有问题（输出明细）
"""
import re, sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPENDIX_ZH = os.path.join(BASE, "book", "12-附录A-案例索引与资料出处.md")
APPENDIX_EN = os.path.join(BASE, "book-en", "12-appendix-a-sources.md")
ZH_BODY = ["01-第1章-AI客户经营元年.md","02-第2章-客户全生命周期与AI引擎.md",
           "03-第3章-开拓-AI把获客变成产能.md","04-第4章-转化-AI个性化定价与对话式成交.md",
           "05-第5章-服务-AI客服与人工兜底.md","06-第6章-留存与扩展-客户成功AI化.md",
           "07-第7章-底座-AI-CRM与客户数据.md","08-第8章-组织-人技能与变革.md",
           "09-第9章-行业篇-十一个行业的AI客户经营.md","10-第10章-反面与边界-反噬幻觉合规与责任.md",
           "11-第11章-未来-当客户变成AI.md"]
EN_BODY = ["01-ch1-year-one-ai-customer-operations.md","02-ch2-the-customer-lifecycle-and-the-ai-engine.md",
           "03-ch3-acquisition-turning-prospecting-into-capacity.md","04-ch4-conversion-personalization-pricing-conversational-commerce.md",
           "05-ch5-service-ai-support-and-human-backup.md","06-ch6-retention-and-expansion-ai-driven-customer-success.md",
           "07-ch7-the-foundation-ai-crm-and-customer-data.md","08-ch8-organization-people-skills-and-change.md",
           "09-ch9-industry-playbook-eleven-industries.md","10-ch10-the-dark-side-backlash-hallucination-compliance.md",
           "11-ch11-the-future-when-the-customer-is-an-ai.md"]

def read(path):
    return open(path, encoding="utf-8").read()

def main():
    errors = []      # 硬错误
    warnings = []    # 建议人工确认

    appendix_zh = read(APPENDIX_ZH)
    appendix_refs = set(re.findall(r'<a id="([\d-]+)"', appendix_zh))

    zh_body = "".join(read(os.path.join(BASE, "book", f)) for f in ZH_BODY)
    en_body = ""
    if os.path.exists(APPENDIX_EN):
        en_body = "".join(read(os.path.join(BASE, "book-en", f)) for f in EN_BODY)

    # 1. 上标链接格式（硬错误）
    for lang, body in [("中文", zh_body)] + ([("英文", en_body)] if en_body else []):
        plain = re.findall(r'<sup>\[([\d-]+)\]</sup>(?!<a)', body)
        if plain:
            errors.append(f"[{lang}] 纯文本上标（缺链接）: {sorted(set(plain))[:5]}")
        abslink = re.findall(r'<sup><a href="/12-[^"]*#([\d-]+)">', body)
        if abslink:
            errors.append(f"[{lang}] 绝对路径链接（GitHub 会坏）: {sorted(set(abslink))[:5]}")
        bad_href = re.findall(r'<sup><a href="([^"]*)"', body)
        ok_zh = re.findall(r'<sup><a href="12-附录A-案例索引与资料出处\.md#[\d-]+">', body)
        ok_en = re.findall(r'<sup><a href="12-appendix-a-sources\.md#[\d-]+">', body)
        if lang == "中文" and len(ok_zh) != len(bad_href):
            errors.append(f"[中文] 存在非标准 href（应为 12-附录A-案例索引与资料出处.md#X-Y）: {len(bad_href)-len(ok_zh)} 处")
        if lang == "英文" and len(ok_en) != len(bad_href):
            errors.append(f"[英文] 存在非标准 href（应为 12-appendix-a-sources.md#X-Y）: {len(bad_href)-len(ok_en)} 处")

    # 2. 悬空引用（硬错误）
    zh_refs = set(re.findall(r'<sup><a href="12-附录A-案例索引与资料出处\.md#([\d-]+)">', zh_body)) | set(re.findall(r'<sup>\[([\d-]+)\]</sup>', zh_body))
    en_refs = set()
    if en_body:
        en_refs = set(re.findall(r'<sup><a href="12-appendix-a-sources\.md#([\d-]+)">', en_body)) | set(re.findall(r'<sup>\[([\d-]+)\]</sup>', en_body))
    for lang, refs in [("中文", zh_refs), ("英文", en_refs)]:
        missing = sorted(r for r in refs if r not in appendix_refs)
        if missing:
            errors.append(f"[{lang}] 悬空引用（附录A无此编号）: {missing[:10]}")

    # 3. 附录有条目正文未引用（警告）
    used = zh_refs | en_refs
    unused = sorted(appendix_refs - used)
    if unused:
        warnings.append(f"附录 A 有条目正文未标注 ({len(unused)} 条): {unused[:15]}{'...' if len(unused) > 15 else ''}")

    print("=" * 60)
    print("引用一致性自检（AI 客户经营，中英双语）")
    print(f"附录 A 条目: {len(appendix_refs)} | 中文正文引用: {len(zh_refs)} | 英文正文引用: {len(en_refs)}")
    print("=" * 60)
    if errors:
        for e in errors:
            print(f"❌ {e}")
    if warnings:
        for w in warnings:
            print(f"⚠️ {w}")
    if not errors and not warnings:
        print("✅ 全部通过")
    print()
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
